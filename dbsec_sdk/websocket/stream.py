"""DB증권 실시간 WebSocket 스트리밍.

DB증권 Open API의 실시간 데이터를 WebSocket으로 수신합니다.
정확한 연결/해제, 자동 재연결, graceful shutdown을 보장합니다.

접속 URL:
    운영:   wss://openapi.dbsec.co.kr:7070/websocket
    모의투자: wss://openapi.dbsec.co.kr:17070/websocket

WebSocket 메시지 형식:
    시세 구독:   {"header": {"token": "TOKEN", "tr_type": "1"}, "body": {"tr_cd": "V60", "tr_key": "FNTSLA"}}
    시세 해제:   {"header": {"token": "TOKEN", "tr_type": "2"}, "body": {"tr_cd": "V60", "tr_key": "FNTSLA"}}
    계좌 등록:   {"header": {"token": "TOKEN", "tr_type": "3"}, "body": {"tr_cd": "IS0", "tr_key": ""}}

tr_type (호출 시 직접 지정 — 자동판별하지 않습니다):
    "1" = 일반 시세 TR 구독 등록 (S00, V60, ... — 종목 단위)
    "2" = 일반 시세 TR 구독 해제 (remove_realtime 이 송신)
    "3" = 계좌 단위 TR 등록 (IS0/IS1/IS2/IF0/O/P) — 해제 메시지 없음 (세션 종료가 곧 해제)

주요 실시간 TR코드:
    V60 = 해외주식 체결가 (실시간 시세 신청 필요)
    S00 = 국내주식 체결가
    IS0/IS1: 국내주식 주문접수/주문체결 (계좌)
    IS2:     해외주식 주문체결 (계좌)
    IF0:     국내선물옵션 주문체결 (계좌)
    O:       해외선물옵션 주문체결 (계좌)
    P:       해외선물옵션 잔고 (계좌)

사용법:
    ws = client.create_websocket()
    ws.on_message(my_callback)       # 콜백 등록
    await ws.connect()               # WebSocket 연결
    await ws.add_realtime("V60", "FNTSLA", tr_type="1")        # 일반 시세 구독
    await ws.add_realtime("P", client.config.app_key, tr_type="3")  # 계좌 등록
    await ws.run()                   # 수신 루프 (Ctrl+C로 종료)

tr_type 은 호출자가 직접 지정합니다 (기본값 "1"). 계좌 단위 TR(IS0/IS1/IS2/IF0/O/P)
은 tr_type="3" 으로, 일반 시세 TR 은 tr_type="1" 로 호출하세요. "1"/"2"/"3" 문자열
또는 1/2/3 정수 모두 허용됩니다.
"""

from __future__ import annotations

import asyncio
import json
import logging
from typing import TYPE_CHECKING, Callable

import websockets
from websockets.asyncio.client import ClientConnection

if TYPE_CHECKING:
    from dbsec_sdk.auth import TokenManager
    from dbsec_sdk.config import Config

from dbsec_sdk.exceptions import WebSocketError, RateLimitError, lookup_error
from dbsec_sdk.rate_limiter import AsyncRateLimiter

logger = logging.getLogger(__name__)

# 콜백 시그니처: (tr_cd: str, tr_key: str, data: dict) -> None
MessageCallback = Callable[[str, str, dict], None]

# 참고: 계좌 단위 실시간 TR 목록 — 호출 시 tr_type="3" (계좌등록) 으로 지정해야 합니다.
# 등록만 있고 해제 메시지는 없다 (세션 종료가 곧 해제). tr_key 는 app_key.
# IS0: 국내주식 주문접수, IS1: 국내주식 주문체결, IS2: 해외주식 주문체결,
# IF0: 국내선물옵션 주문체결, O: 해외선물옵션 주문체결, P: 해외선물옵션 잔고.
# 이 목록은 안내용일 뿐, SDK 는 tr_type 을 자동판별하지 않습니다(호출자가 직접 지정).
_ACCOUNT_LEVEL_TR_CDS = frozenset({"IS0", "IS1", "IS2", "IF0", "O", "P"})

# tr_type 별 의미 (호출자가 지정) — 등록(1/3) 후 _subscriptions 에 저장되어
# 재연결 복원·종료 해제 시 동일 tr_type 으로 재현된다.
_TR_TYPE_SUBSCRIBE = "1"    # 일반 시세 구독 등록
_TR_TYPE_UNSUBSCRIBE = "2"  # 일반 시세 구독 해제
_TR_TYPE_ACCOUNT = "3"      # 계좌 단위 등록 (해제 메시지 없음)
_REGISTER_TR_TYPES = frozenset({_TR_TYPE_SUBSCRIBE, _TR_TYPE_ACCOUNT})

# WebSocket 서버 오류코드별 해결 힌트 (코드→원인 메시지는 exceptions.lookup_error 가 제공)
_WS_ERROR_HINTS = {
    "10004": "구독 메시지의 tr_cd 값을 확인하세요 (예: S00 체결가, S01 호가).",
    "10005": "해당 tr_cd 는 현재 모드(운영/모의)에서 허용되지 않습니다 — 모의투자 미지원 TR 인지 확인하세요.",
    "10006": "구독 메시지의 tr_key(종목코드) 값을 확인하세요. 예: 국내주식은 'J ' + 종목코드 (J 뒤 공백으로 2바이트).",
    "10009": "토큰의 계좌정보와 서버 정보가 불일치합니다 — 토큰을 폐기 후 재발급(token_manager.force_refresh())하고 재연결하세요.",
    "10011": "이전 세션이 정리되지 않았을 수 있습니다(앱·계좌당 최대 2세션). "
             "세션 초기화 API 를 호출한 뒤 재연결하세요: "
             "await client.apis.ws_common.ws_session_disconnect() "
             "(examples/ws_common/ws_session_disconnect.py). "
             "연결 자체도 1분당 6회(6 TPM) 제한이 있으니 잠시 후 재시도하세요.",
    "10017": "거래코드(tr_cd)와 종목코드(tr_key) 조합을 확인하세요 — 종목을 찾을 수 없습니다.",
}


class DBSecWebSocket:
    """DB증권 실시간 WebSocket 클라이언트.

    핵심 특성:
    1. 구독 목록 추적: _subscriptions dict에 활성 구독을 관리
    2. 자동 재연결: 연결 끊김 시 exponential backoff로 재연결
    3. 구독 복원: 재연결 성공 시 기존 구독을 자동으로 다시 등록
    4. Graceful shutdown: close() 시 모든 구독 해제 후 연결 종료
    5. 동시성 보호: asyncio.Lock으로 구독/해제 경합 방지

    생명주기:
        connect() → add_realtime() → run() → close()
                     ↑                   |
                     └── 재연결 시 구독 복원 ──┘

    Attributes:
        _url: WebSocket 접속 URL. ws_url 인자로 수동 지정 가능(해외선옵 7071 등),
            미지정 시 config.ws_url(mode에 따라 7070/17070)
        _token_manager: 토큰 관리자 (인증 헤더에 사용)
        _ws: 현재 WebSocket 연결 객체
        _subscriptions: 활성 구독 목록 {(tr_cd, tr_key): tr_type} — 등록 시 사용한
            tr_type("1" 또는 "3")을 보존하여 재연결 복원·종료 해제에 그대로 사용
        _callbacks: 등록된 메시지 콜백 함수 리스트
        _running: 수신 루프 동작 상태
        _reconnect_count: 현재 재연결 시도 횟수
        _lock: 구독/해제 동시성 보호용 Lock
    """

    _MAX_RECONNECT = 5         # 최대 재연결 시도 횟수
    _BACKOFF_BASE = 2          # 재연결 대기 시간 기저 (2, 4, 8, 16, 32초)
    _MAX_SUBSCRIPTIONS = 50    # 세션당 최대 구독 종목 수
    _IO_DELAY = 0.1            # WebSocket 송수신 딜레이 (100ms)
    _CONNECT_TPM = 6          # 연결 자체 유량제어: 1분당 6회 (DB증권 6 TPM 제한)

    def __init__(self, config: Config, token_manager: TokenManager, ws_url: str | None = None):
        # ws_url 을 직접 주면 그 URL 로 접속(해외선옵 7071 등 수동 지정).
        # None 이면 config.ws_url(일반 7070/17070, mode 에 따라 결정).
        self._url = ws_url or config.ws_url
        self._token_manager = token_manager
        self._ws: ClientConnection | None = None
        # (tr_cd, tr_key) → 등록 tr_type ("1"=시세구독 / "3"=계좌등록).
        # 저장된 tr_type 으로 재연결 복원·종료 해제를 동일하게 재현한다.
        self._subscriptions: dict[tuple[str, str], str] = {}
        self._callbacks: list[MessageCallback] = []
        self._running = False
        self._reconnect_count = 0
        self._lock = asyncio.Lock()
        # 연결 유량제어(6 TPM): connect() 와 _reconnect() 가 공유하는 인스턴스 단위 페이서.
        # DB증권은 WebSocket 연결 자체를 1분당 6회로 제한하므로 초과 연결 시도를 선제 차단한다.
        self._connect_limiter = AsyncRateLimiter(self._CONNECT_TPM, 60.0)

    # ──────────────────────────────────────────
    # 연결
    # ──────────────────────────────────────────

    async def connect(self) -> None:
        """WebSocket 서버에 연결합니다.

        mode 설정에 따라 운영(7070) 또는 모의(17070) 서버에 연결됩니다.

        Raises:
            WebSocketError: 연결 실패 시
        """
        try:
            # 연결 유량제어(6 TPM): 직전 연결과 10초(=60/6) 미만이면 자동 대기.
            await self._connect_limiter.acquire()
            self._ws = await websockets.connect(self._url)
            # 연결 후 안정화 딜레이 (100ms)
            await asyncio.sleep(self._IO_DELAY)
            self._running = True
            self._reconnect_count = 0
            logger.info("WebSocket 연결 성공: %s", self._url)
            # 참고: Connect 후 10초 이내에 Send(구독 등록)를 해야 연결이 유지됩니다.
        except Exception as e:
            raise WebSocketError(f"WebSocket 연결 실패: {e}") from e

    # ──────────────────────────────────────────
    # 구독 관리
    # ──────────────────────────────────────────

    async def add_realtime(self, tr_cd: str, tr_key: str = "", tr_type: str | int = "1") -> None:
        """실시간 데이터 구독/계좌 등록 — tr_type 을 호출자가 직접 지정합니다.

        tr_type 은 더 이상 tr_cd 로 자동판별하지 않습니다(호출자가 명시):
        - "1" = 일반 시세 TR 구독 등록 (S00/V60/... — 종목 단위, 기본값)
        - "3" = 계좌 단위 TR 등록 (IS0/IS1/IS2/IF0/O/P). 이 경우 tr_key 는 보통 app_key.
        - "2" = 일반 시세 구독 해제 — remove_realtime 으로 위임합니다.

        서버 송신 후 내부 구독 목록에 등록 tr_type 과 함께 추가합니다.
        재연결 시 동일 tr_type 으로 자동 복원됩니다.

        Args:
            tr_cd: TR 코드 (예: "V60" = 해외주식 체결가, "P" = 해외선물옵션 잔고)
            tr_key: TR 키. 일반 TR 은 종목코드, 계좌 단위 TR 은 app_key.
            tr_type: 등록 종류. "1"(시세구독)/"3"(계좌등록)/"2"(해제). int 1/2/3 도 허용.

        Raises:
            ValueError: tr_type 이 "1"/"2"/"3" (또는 1/2/3) 이 아닐 때
            WebSocketError: WebSocket 미연결 시
            RateLimitError: 세션당 최대 50종목 초과 시
        """
        tr_type = str(tr_type).strip()
        # "2"(해제)는 등록이 아니므로 remove_realtime 으로 위임.
        # 반드시 self._lock 획득 전(락 밖)에서 호출 — remove_realtime 이 같은 Lock 을
        # 다시 잡으므로, 락 안에서 위임하면 self-deadlock 이 난다.
        if tr_type == _TR_TYPE_UNSUBSCRIBE:
            await self.remove_realtime(tr_cd, tr_key)
            return
        if tr_type not in _REGISTER_TR_TYPES:
            raise ValueError(
                f"tr_type 은 '1'(시세구독)/'2'(해제)/'3'(계좌등록) 중 하나여야 합니다 "
                f"(받은 값: {tr_type!r})."
            )
        async with self._lock:
            # 세션당 최대 50종목 제한 확인
            if (tr_cd, tr_key) not in self._subscriptions and \
               len(self._subscriptions) >= self._MAX_SUBSCRIPTIONS:
                raise RateLimitError(
                    f"세션당 최대 {self._MAX_SUBSCRIPTIONS}종목까지 구독 가능합니다. "
                    f"(현재 {len(self._subscriptions)}종목)"
                )
            await self._send_subscribe(tr_cd, tr_key, tr_type=tr_type)
            self._subscriptions[(tr_cd, tr_key)] = tr_type
            kind = "계좌등록" if tr_type == _TR_TYPE_ACCOUNT else "구독 등록"
            logger.info("%s: %s %s (tr_type=%s, 총 %d건)",
                        kind, tr_cd, tr_key, tr_type, len(self._subscriptions))

    async def remove_realtime(self, tr_cd: str, tr_key: str = "") -> None:
        """실시간 데이터 구독을 해제합니다 (tr_type="2").

        등록 시 저장해 둔 tr_type 으로 동작을 분기합니다:
        - 시세구독("1")으로 등록된 건: tr_type="2" 해제 메시지 송신 후 목록 제거
        - 계좌등록("3")으로 등록된 건: 해제 메시지가 정의되지 않은 프로토콜이므로
          송신 없이 내부 목록에서만 제거 (실제 해제는 세션 종료 시점).

        Args:
            tr_cd: TR 코드
            tr_key: TR 키

        Raises:
            WebSocketError: WebSocket 미연결 시
        """
        async with self._lock:
            registered_type = self._subscriptions.get((tr_cd, tr_key))
            if registered_type is not None:
                if registered_type != _TR_TYPE_ACCOUNT:
                    await self._send_subscribe(tr_cd, tr_key, tr_type=_TR_TYPE_UNSUBSCRIBE)
                del self._subscriptions[(tr_cd, tr_key)]
                logger.info("구독 해제: %s %s (등록 tr_type=%s)",
                            tr_cd, tr_key, registered_type)

    # ──────────────────────────────────────────
    # 콜백 관리
    # ──────────────────────────────────────────

    def on_message(self, callback: MessageCallback) -> None:
        """메시지 수신 콜백을 등록합니다.

        콜백 시그니처: callback(tr_cd: str, tr_key: str, data: dict)
        여러 콜백을 등록할 수 있으며, 수신 순서대로 호출됩니다.

        Args:
            callback: 실시간 데이터 수신 시 호출할 함수

        Example::

            def my_handler(tr_cd, tr_key, data):
                print(f"[{tr_cd}] {tr_key}: {data}")

            ws.on_message(my_handler)
        """
        if callback not in self._callbacks:
            self._callbacks.append(callback)

    def off_message(self, callback: MessageCallback) -> None:
        """등록된 콜백을 해제합니다.

        Args:
            callback: 해제할 콜백 함수
        """
        if callback in self._callbacks:
            self._callbacks.remove(callback)

    # ──────────────────────────────────────────
    # 수신 루프
    # ──────────────────────────────────────────

    async def run(self) -> None:
        """메인 수신 루프를 실행합니다.

        WebSocket에서 메시지를 수신하고 등록된 콜백을 호출합니다.

        동작:
        1. websocket.recv()로 메시지 대기
        2. JSON 파싱 후 등록된 콜백에 전달
        3. ConnectionClosed 발생 시 자동 재연결
        4. 재연결 성공 시 기존 구독 자동 복원
        5. KeyboardInterrupt/CancelledError 시 graceful shutdown

        Raises:
            WebSocketError: connect()가 호출되지 않은 경우
            WebSocketError: 재연결 최대 횟수 초과 시
        """
        if not self._ws:
            raise WebSocketError("connect()를 먼저 호출하세요.")

        try:
            while self._running:
                try:
                    # 메시지 수신 대기
                    raw = await self._ws.recv()
                    # JSON 파싱 및 콜백 호출
                    self._handle_message(raw)
                    # 수신 후 처리 딜레이 (100ms)
                    await asyncio.sleep(self._IO_DELAY)
                except websockets.ConnectionClosed:
                    logger.warning("WebSocket 연결 끊김")
                    if not self._running:
                        break
                    # 자동 재연결 시도
                    await self._reconnect()
        except (KeyboardInterrupt, asyncio.CancelledError):
            logger.info("종료 신호 수신")
        finally:
            # 어떤 이유로든 루프 종료 시 정리
            await self.close()

    # ──────────────────────────────────────────
    # 종료
    # ──────────────────────────────────────────

    async def close(self) -> None:
        """WebSocket을 정리하고 종료합니다.

        종료 순서:
        1. 수신 루프 중지 플래그 설정
        2. 모든 활성 구독에 대해 해제 메시지(tr_type="2") 전송
        3. 내부 구독 목록 초기화
        4. WebSocket 연결 close() 호출
        5. WebSocket 객체 None으로 초기화

        연결이 이미 끊긴 상태에서도 안전하게 호출 가능합니다.
        """
        self._running = False

        if self._ws:
            # 1. 활성 구독 모두 해제 (서버에 통보)
            # 계좌등록("3")으로 등록된 건은 해제 메시지가 정의되지 않은 프로토콜이므로
            # 송신하지 않고 내부 목록에서만 제거. 시세구독("1")만 tr_type="2" 송신.
            async with self._lock:
                for (tr_cd, tr_key), registered_type in list(self._subscriptions.items()):
                    if registered_type == _TR_TYPE_ACCOUNT:
                        continue
                    try:
                        await self._send_subscribe(tr_cd, tr_key, tr_type=_TR_TYPE_UNSUBSCRIBE)
                        logger.info("종료 시 구독 해제: %s %s", tr_cd, tr_key)
                    except Exception:
                        pass  # 이미 연결이 끊긴 경우 무시
                self._subscriptions.clear()

            # 2. WebSocket 연결 종료
            try:
                await self._ws.close()
            except Exception:
                pass
            self._ws = None
            logger.info("WebSocket 종료 완료")

    # ──────────────────────────────────────────
    # 내부 메서드
    # ──────────────────────────────────────────

    async def _send_subscribe(self, tr_cd: str, tr_key: str, tr_type: str) -> None:
        """구독/해제 메시지를 WebSocket으로 전송합니다.

        메시지 형식:
            {
                "header": {"token": "ACCESS_TOKEN", "tr_type": "1"},
                "body": {"tr_cd": "V60", "tr_key": "FNTSLA"}
            }

        Args:
            tr_cd: TR 코드
            tr_key: TR 키
            tr_type: "1"=시세구독 등록, "2"=시세구독 해제, "3"=계좌 등록

        Raises:
            WebSocketError: WebSocket이 연결되지 않은 경우
        """
        if not self._ws:
            raise WebSocketError("WebSocket이 연결되지 않음")

        # 요청 경로 — auto_token 정책을 따른다(없으면 발급 or AuthError). 명시 발급은 get_token().
        # 동기 토큰 확보(캐시 미스 시 blocking HTTP)를 to_thread 로 오프로드해 이벤트 루프 정지 방지
        # (구독/재연결 복원 중 다른 태스크가 멈추지 않도록).
        token = await asyncio.to_thread(self._token_manager._token_for_request)
        msg = json.dumps({
            "header": {
                "token": token,
                "tr_type": tr_type,
            },
            "body": {
                "tr_cd": tr_cd,
                "tr_key": tr_key,
            },
        })
        await self._ws.send(msg)
        # 송신 후 안정화 딜레이 (100ms)
        await asyncio.sleep(self._IO_DELAY)

    def _handle_message(self, raw: str | bytes) -> None:
        """수신된 메시지를 파싱하고 등록된 콜백을 호출합니다.

        시세 데이터가 아닌 서버 제어/오류 응답(예: 세션 수 초과 10011, 잘못된 tr_cd 10004)은
        header/body 가 null 이거나 rsp_cd/rsp_msg 만 담겨 온다 — 이 경우 콜백 대신
        원인·해결 힌트를 로그(warning)로 남긴다.

        Args:
            raw: WebSocket에서 수신한 원시 메시지 (JSON 문자열)
        """
        # JSON 파싱
        try:
            data = json.loads(raw)
        except json.JSONDecodeError:
            logger.warning("JSON 파싱 실패: %s", raw[:200])
            return

        if not isinstance(data, dict):
            logger.warning("알 수 없는 메시지 형식: %s", str(data)[:200])
            return

        # 서버가 오류/제어 응답에서 header/body 를 null 로 보내는 경우가 있다 → 빈 dict 정규화
        header = data.get("header") or {}
        body = data.get("body") or {}
        if not isinstance(header, dict):
            header = {}
        if not isinstance(body, dict):
            body = {}

        # 제어/오류 응답 진단 — rsp_cd/rsp_msg 가 있으면 시세 데이터가 아닌 서버 응답
        rsp_cd = str(header.get("rsp_cd") or body.get("rsp_cd") or "")
        rsp_msg = str(header.get("rsp_msg") or body.get("rsp_msg") or "")
        if rsp_cd or rsp_msg:
            known = lookup_error(rsp_cd)        # exceptions.py 의 오류코드표 조회
            hint = _WS_ERROR_HINTS.get(rsp_cd, "")
            msg = f"WebSocket 서버 응답 [rsp_cd={rsp_cd or '-'}] {rsp_msg or known or '(메시지 없음)'}"
            if known and known not in (rsp_msg, ""):
                msg += f" — {known}"
            if hint:
                msg += f"\n  ↳ 해결: {hint}"
            elif rsp_cd not in ("", "0", "00000"):
                msg += ("\n  ↳ 참고: 연결 유량(1분 6회)·세션 한도(계좌당 2세션)·이전 세션 미정리 가능성. "
                        "ws_session_disconnect 호출 후 잠시 뒤 재시도하세요.")
            if rsp_cd in ("", "0", "00000"):
                logger.info(msg)        # 정상 응답(구독 확인 등)
            else:
                logger.warning(msg)     # 오류 응답 — 원인/해결 힌트 노출
            return                      # 제어 응답은 시세 콜백으로 전달하지 않음

        # header/body 모두 비어있으면 (keepalive 등) 콜백을 호출하지 않는다
        if not header and not body:
            logger.debug("빈 메시지 수신(무시): %s", str(raw)[:200])
            return

        # 시세 데이터 — TR 코드/키 추출 (header 또는 body 에 있을 수 있고, 값이 null 일 수 있음)
        tr_cd = header.get("tr_cd") or body.get("tr_cd") or ""
        tr_key = header.get("tr_key") or body.get("tr_key") or ""

        # 등록된 모든 콜백에 데이터 전달
        for callback in self._callbacks:
            try:
                callback(tr_cd, tr_key, body)
            except Exception:
                logger.exception("콜백 실행 오류")

    async def _reconnect(self) -> None:
        """연결이 끊겼을 때 자동으로 재연결을 시도합니다.

        재연결 전략:
        - Exponential backoff: 2초, 4초, 8초, 16초, 32초 간격
        - 최대 5회 시도 후 WebSocketError 발생
        - 재연결 성공 시 기존 구독을 자동으로 다시 등록

        Raises:
            WebSocketError: 최대 재연결 횟수 초과 시
        """
        while self._reconnect_count < self._MAX_RECONNECT:
            self._reconnect_count += 1
            # 대기 시간: 2^1=2, 2^2=4, 2^3=8, 2^4=16, 2^5=32초
            delay = self._BACKOFF_BASE ** self._reconnect_count
            logger.info(
                "재연결 시도 %d/%d (%d초 후)",
                self._reconnect_count, self._MAX_RECONNECT, delay,
            )
            await asyncio.sleep(delay)

            try:
                # 연결 유량제어(6 TPM): backoff 와 별개로 연결 간격(10초)을 보장.
                await self._connect_limiter.acquire()
                # WebSocket 재연결
                self._ws = await websockets.connect(self._url)
                # 연결 후 안정화 딜레이 (100ms)
                await asyncio.sleep(self._IO_DELAY)
                logger.info("재연결 성공")

                # 기존 구독 목록을 순회하며 다시 등록
                # 등록 시 저장해 둔 tr_type("1" 또는 "3") 으로 그대로 재송신.
                async with self._lock:
                    for (tr_cd, tr_key), registered_type in self._subscriptions.items():
                        await self._send_subscribe(tr_cd, tr_key, tr_type=registered_type)
                        logger.info("구독 복원: %s %s (tr_type=%s)", tr_cd, tr_key, registered_type)

                # 재연결 카운터 초기화
                self._reconnect_count = 0
                return
            except Exception as e:
                logger.warning("재연결 실패: %s", e)

        # 최대 횟수 초과 시 연결 종료
        self._running = False
        raise WebSocketError(f"재연결 {self._MAX_RECONNECT}회 실패, 연결 종료")
