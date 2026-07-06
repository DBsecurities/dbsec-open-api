"""DBSecClient - DB증권 Open API 단일 진입점 (비동기).

DB증권 SDK 의 기본(그리고 유일한) 클라이언트는 **비동기**다.
모든 API 호출은 `await` 해야 한다.

사용법:
    import asyncio
    from dbsec_sdk import DBSecClient

    async def main():
        async with DBSecClient("config.yaml") as client:
            # 국내주식 현재가 조회
            resp = await client.apis.kr_stock_quote.kr_stock_inquire_price(
                InputCondMrktDivCode="J", InputIscd1="005930")
            print(resp.to_dataframe())

            # 동시 호출 — 유량제어가 TPS 를 자동 보장
            codes = ["005930", "000660", "035720"]
            results = await asyncio.gather(*[
                client.apis.kr_stock_quote.kr_stock_inquire_price(
                    InputCondMrktDivCode="J", InputIscd1=c)
                for c in codes
            ])

            # WebSocket 실시간 시세 (이미 비동기)
            ws = client.create_websocket()

    asyncio.run(main())

설계:
    공개 클래스 DBSecClient 는 비동기 파사드이고, 실제 요청 로직(2-tier 유량제어,
    auto_token 토큰 자동발급/재발급, 토큰 캐시)은 내부 동기 코어 `_SyncCore` 에 있다.
    비동기 메서드는 코어 메서드를 `asyncio.to_thread` 로 실행한다 — 네트워크 I/O
    구간에서 GIL 을 놓으므로 asyncio.gather 로 실질적 동시성을 얻고, 동시 호출량은
    공유 RateLimitController(스레드 안전)가 TPS 로 자동 제한한다.

    생성된 endpoints.py 메서드는 모두 `return self._client.post(...)` 형태이므로,
    이 비동기 클라이언트를 레지스트리에 주입하면 post() 가 코루틴을 반환해 그대로
    `await` 할 수 있다(메서드 재생성 불필요).
"""

from __future__ import annotations

import asyncio
import logging
import random
import time
from functools import cached_property
from pathlib import Path
from typing import Any, Awaitable, Callable

import requests

from dbsec_sdk.auth import TokenManager
from dbsec_sdk.config import Config
from dbsec_sdk.exceptions import APIError
from dbsec_sdk.rate_limiter import RateLimitController
from dbsec_sdk.response import APIResponse

logger = logging.getLogger("dbsec_sdk.client")

# 토큰 무효/만료 응답코드 — 발생 시 revoke→재발급 후 자동 재시도(영구 복구)
_TOKEN_ERROR_CODES = frozenset({"IGW00121", "IGW00122", "IGW00123"})

# 유량제어 초과(호출 거래건수 초과) 응답코드 — 발생 시 지수백오프+jitter 후 재시도(반응형 안전망).
# 주의: HTTP 상태는 403(토큰발급계열)·500(그 외) 둘 다로 오며, 500 에는 진짜 서버오류(IGW50xxx)도
#       섞이므로, 상태코드가 아니라 반드시 이 rsp_cd 로만 트리거한다.
_RATE_LIMIT_ERROR_CODE = "IGW00201"
_BACKOFF_BASE = 1.0     # 첫 백오프(초). 서버 카운팅 윈도가 1초라 ≥1s 로 시작해 윈도를 확실히 비운다.
_BACKOFF_MAX = 8.0      # 백오프 상한(초). 1→2→4→8 후 8 에서 캡.
_BACKOFF_RETRIES = 4    # 요청당 IGW00201 최대 재시도 횟수(1+2+4+8 ≈ 최악 15s+jitter).

# 연속조회 안전 상한: max_pages 미지정(None)이어도 이 페이지 수에서 강제 중단한다(폭주 방지).
# 서버가 cont_yn='Y' 를 무한 반복하거나 cont_key 가 진행하지 않는 이상 상황 대비.
# 이보다 더 받아야 하면 max_pages 를 명시(예: max_pages=500)하면 그 값이 상한이 된다.
_PAGED_SAFETY_CAP = 100


def _normalize_max_pages(max_pages: Any) -> int | None:
    """연속조회 max_pages 입력 정규화.

    - None / "" (빈 문자열) → None (끝까지)
    - 정수 또는 정수 문자열("2") → int
    - 0 / 음수 / 정수로 못 바꾸는 값 → ValueError (조용한 오작동 대신 명확히 차단)
    """
    if max_pages is None or max_pages == "":
        return None
    try:
        n = int(max_pages)
    except (TypeError, ValueError):
        raise ValueError(
            f"max_pages 는 1 이상의 정수 또는 None 이어야 합니다 (받음: {max_pages!r})."
        )
    if n < 1:
        raise ValueError(
            f"max_pages 는 1 이상이어야 합니다 (받음: {max_pages!r}). 끝까지 받으려면 None/생략."
        )
    return n


class _SyncCore:
    """내부 동기 요청 코어 (직접 사용 금지 — DBSecClient 가 to_thread 로 호출).

    2-tier 유량제어 + auto_token 토큰 자동발급/재발급 + 토큰 캐시 로직을 보유한다.
    """

    def __init__(
        self,
        config_path: str | Path | None = None,
        *,
        rate_limit: bool = True,
        # 안전계수: 실제 사용률 = 서버 TPS × safety. 0.9 = 서버 한도의 90%만 사용(10% 여유).
        # 동시/경계 호출에서 서버 1초 카운팅 윈도 누수를 막는 마진. 0<safety<=1, 작을수록 보수적.
        # (0.9 는 처리율 우선 기본값 — 경계 누수 시 IGW00201 은 rate_limit_backoff 가 흡수.)
        rate_limit_safety: float = 0.9,
        rate_limit_backoff: bool = True,
        auto_token: bool = True,
        token_retry_limit: int = 5,
    ):
        self.config = Config(config_path)
        self.token_manager = TokenManager(self.config, auto_token=auto_token)
        self._auto_token = bool(auto_token)  # 요청 중 토큰거부(IGW0012x) 자동 재발급 여부
        self._rate = RateLimitController(enabled=rate_limit, safety=rate_limit_safety)
        self._rate_limit_backoff = bool(rate_limit_backoff)
        self._token_retry_limit = max(0, int(token_retry_limit))
        # 공유 HTTP 세션(커넥션 풀) — 호출마다 TCP+TLS 핸드셰이크를 없애 동시 처리율을 높인다.
        # (호출당 핸드셰이크가 고동시성에서 GIL 경합을 일으켜 처리율 천장이 됨 — 세션 재사용으로 해소.)
        # requests.Session 은 동시 요청에 thread-safe(urllib3 풀) → asyncio.to_thread 다중스레드에서 안전.
        self._session = requests.Session()
        _adapter = requests.adapters.HTTPAdapter(pool_connections=32, pool_maxsize=32)
        self._session.mount("https://", _adapter)
        self._session.mount("http://", _adapter)

    def request(
        self,
        method: str,
        path: str,
        body: dict | None = None,
        params: dict | None = None,
        extra_headers: dict | None = None,
    ) -> APIResponse:
        """HTTP 요청 전송 → APIResponse. 토큰 인증 헤더 자동 포함.

        호출 직전에 선제 유량제어(2-tier)를 적용한다. 응답 오류는 두 가지를 자동 복구한다:
          · 토큰 무효/만료(IGW00121 등) → auto_token=True 면 revoke→재발급 후 재시도
            (요청당 token_retry_limit 회). auto_token=False 면 즉시 APIError.
          · 유량제어 초과(IGW00201) → rate_limit_backoff=True 면 지수백오프+jitter 재시도
            (요청당 _BACKOFF_RETRIES 회). 두 카운터는 서로 독립이다.

        Raises:
            APIError: 복구 불가 오류이거나 재시도 상한을 초과한 경우.
        """
        url = f"{self.config.base_url}{path if path.startswith('/') else '/' + path}"

        token_attempt = 0   # 토큰 무효/만료 복구 카운터
        rate_attempt = 0    # IGW00201 백오프 재시도 카운터 (토큰 카운터와 독립)
        while True:
            # 1) 선제 유량제어 (앱 글로벌 20TPS + 엔드포인트별 TPS) → IGW00201 사전 차단
            self._rate.acquire(path)

            # 2) 인증 헤더 (재시도 시 새 토큰 반영)
            headers = self.token_manager.get_headers(extra_headers)

            # 3) 전송 (공유 세션 → 커넥션 재사용)
            resp = self._session.request(
                method=method, url=url, json=body, params=params, headers=headers, timeout=30,
            )

            try:
                resp_body = resp.json()
            except Exception:
                resp_body = {"raw": resp.text}

            api_resp = APIResponse(resp.status_code, resp_body, dict(resp.headers))
            if api_resp.is_ok:
                return api_resp

            rsp_cd = resp_body.get("rsp_cd", "") if isinstance(resp_body, dict) else ""

            # 4) 토큰 무효/만료 → auto_token=True 면 재발급 후 재시도 (False 면 그대로 APIError)
            if self._auto_token and rsp_cd in _TOKEN_ERROR_CODES and token_attempt < self._token_retry_limit:
                token_attempt += 1
                # 이 요청에 실제로 사용해 거부당한 토큰을 넘긴다 → 동시 호출 시 다른 스레드가
                # 이미 재발급한 새 토큰을 실수로 revoke 하지 않도록(auth.force_refresh 참고).
                used_token = headers.get("authorization", "").removeprefix("Bearer ").strip() or None
                try:
                    self.token_manager.force_refresh(invalid_token=used_token)
                except Exception:
                    break  # 재발급 실패 → 복구 불가, 원오류 발생
                continue

            # 5) 유량제어 초과(IGW00201) → 지수백오프+jitter 후 재시도 (반응형 안전망).
            #    선제 페이싱(rate_limit)과 독립된 스위치(rate_limit_backoff)로 제어한다.
            #    매트릭스 TPS 가 실제 서버 정책보다 높아 누수되는 경우(드리프트)를 흡수한다.
            if (
                self._rate_limit_backoff
                and rsp_cd == _RATE_LIMIT_ERROR_CODE
                and rate_attempt < _BACKOFF_RETRIES
            ):
                rate_attempt += 1
                delay = min(_BACKOFF_BASE * 2 ** (rate_attempt - 1), _BACKOFF_MAX)
                delay += random.uniform(0, delay * 0.25)  # +0~25% jitter (윈도 클리어 보장 위해 가산만)
                logger.warning(
                    "IGW00201 호출초과 [%s] %d/%d 재시도, %.2fs 백오프 "
                    "(매트릭스 TPS가 실제보다 높을 수 있음 — api_support_matrix.md 점검 권장)",
                    path, rate_attempt, _BACKOFF_RETRIES, delay,
                )
                time.sleep(delay)
                continue

            break  # 그 외 오류이거나 복구 상한 초과

        raise APIError(
            f"API 오류: {resp.status_code} [{rsp_cd}] {api_resp.message}",
            status_code=resp.status_code,
            rsp_cd=rsp_cd,
            body=resp_body,
        )

    def request_paged(
        self,
        method: str,
        path: str,
        body: dict | None = None,
        params: dict | None = None,
        extra_headers: dict | None = None,
        *,
        max_pages: int | None = None,
        cont_key: str = "",
    ) -> list[APIResponse]:
        """연속조회 자동 페이징(동기). 응답 헤더 cont_yn != 'Y' 가 될 때까지 끝까지 반복 호출.

        DB증권 연속조회 프로토콜 (dbsec_helper.call_rest_paged 와 동일):
          · 첫 요청: cont_key='' → cont_yn='N'(처음부터), cont_key 주어지면 cont_yn='Y'(그 키부터 재개)
          · 이후 요청: 직전 응답의 cont_key 를 cont_yn='Y' 로 패스스루
          · 종료: 응답 헤더 cont_yn != 'Y' (서버가 끝을 알림)
        각 페이지는 self.request() 를 거치므로 유량제어(self._rate)가 자동 페이싱한다
        (dbsec_helper.call_rest_paged 의 page_sleep 같은 수동 지연이 필요 없다).

        Args:
            max_pages: 선택적 상한. 기본 None = 서버가 끝을 알릴 때까지 받되, 안전 상한
                100페이지(_PAGED_SAFETY_CAP)에서 강제 중단한다(폭주 방지). 정수를 주면
                그 페이지 수에서 멈춘다(상한에서 멈추면 경고 로그).
            cont_key: 이전 세션 재개용 시작 연속키 (기본 '' = 처음부터).

        Returns:
            list[APIResponse] — 페이지 순서대로. 각 페이지의 .has_more / .cont_key 로 상태 확인 가능.
        """
        max_pages = _normalize_max_pages(max_pages)
        pages: list[APIResponse] = []
        cur_yn, cur_key = ("Y", cont_key) if cont_key else ("N", "")
        while True:
            headers = dict(extra_headers or {})
            headers["cont_yn"] = cur_yn
            headers["cont_key"] = cur_key
            resp = self.request(method, path, body=body, params=params, extra_headers=headers)
            pages.append(resp)
            if not resp.has_more:                 # 서버가 cont_yn != 'Y' → 마지막 페이지
                return pages
            # 무진행 가드: has_more=True 인데 다음 cont_key 가 비었거나 직전과 동일하면
            # 같은 요청이 무한 반복되므로(서버 이상) 경고 후 중단한다.
            next_key = resp.cont_key
            if not next_key or next_key == cur_key:
                logger.warning(
                    "request_paged: 서버가 cont_yn='Y' 이나 cont_key 가 %s [%s] "
                    "— 무진행으로 판단해 %d페이지에서 중단(무한루프 방지).",
                    "비어 있음" if not next_key else f"직전과 동일({cur_key!r})", path, len(pages),
                )
                return pages
            if max_pages is not None and len(pages) >= max_pages:
                logger.warning(
                    "request_paged: max_pages=%d 상한에서 중단 [%s] (cont_key=%r 부터 데이터 남음)",
                    max_pages, path, resp.cont_key,
                )
                return pages
            # 안전 상한: max_pages 미지정이어도 폭주 방지(더 받으려면 max_pages 명시).
            if max_pages is None and len(pages) >= _PAGED_SAFETY_CAP:
                logger.warning(
                    "request_paged: 안전 상한 %d페이지 도달 [%s] — 중단(cont_key=%r 부터 더 있음). "
                    "더 받으려면 max_pages 를 명시하세요.", _PAGED_SAFETY_CAP, path, resp.cont_key,
                )
                return pages
            cur_yn, cur_key = "Y", next_key

    def post(self, path: str, body: dict | None = None, **kwargs: Any) -> APIResponse:
        return self.request("POST", path, body=body, **kwargs)

    def get(self, path: str, params: dict | None = None, **kwargs: Any) -> APIResponse:
        return self.request("GET", path, params=params, **kwargs)

    def create_websocket(self, ws_url: str | None = None):
        from dbsec_sdk.websocket import DBSecWebSocket
        return DBSecWebSocket(self.config, self.token_manager, ws_url=ws_url)


class DBSecClient:
    """DB증권 Open API 비동기 클라이언트 (기본/유일 진입점).

    모든 API 호출은 `await` 한다.

    Args:
        config_path: config.yaml 파일 경로. None이면 환경변수로 설정.
        rate_limit: 선제(proactive) 유량제어(2-tier 페이싱) 사용 여부. 기본 True.
            호출 '전'에 TPS 간격을 맞춰 IGW00201 을 예방한다.
        rate_limit_safety: 유량제어 안전계수(0<safety<=1). 실제 사용률 = 서버 TPS × safety.
            기본 0.9 = 서버 한도의 90%만 사용(10% 여유) → 처리율을 우선하되 약간의 윈도 누수 마진 유지.
            작을수록 보수적(느리지만 안전). period=1/safety(기본 ≈1.11s).
            경계 누수로 IGW00201 이 나도 rate_limit_backoff(기본 True)가 흡수한다.
        rate_limit_backoff: 반응형(reactive) 백오프 안전망 사용 여부. 기본 True.
            rate_limit 과 '독립'된 스위치다. IGW00201(호출초과)을 받으면 지수백오프
            (1→2→4→8초)+jitter 로 재시도해 매트릭스 드리프트(매트릭스 TPS가 실제보다 높은 경우)를
            흡수한다. False 면 IGW00201 을 즉시 APIError 로 그대로 표면화(기존 동작).
        auto_token: 요청 경로의 토큰 자동 발급/재발급 여부. 기본 True.
            True: 요청 시 토큰이 없으면 자동 발급하고, 토큰거부(IGW00121/00123) 응답을 받으면
                  revoke→재발급 후 재시도한다(stdin 프롬프트 없음).
            False: 자동 발급하지 않는다 → 토큰이 없으면 AuthError, 토큰거부는 APIError 로
                   표면화한다. 토큰은 get_token()/force_refresh()/revoke() 로 직접 관리한다.
        token_retry_limit: 단건 요청 내 토큰 재발급(revoke→재발급) 최대 재시도 수. 기본 5.
            auto_token=True 일 때만 적용되는 '무한 루프 방지용 요청당 상한'이다.

    Attributes:
        config: 설정 객체 (Config)
        token_manager: 토큰 관리자 (TokenManager)
        apis: API 레지스트리 (APIRegistry) — 메서드 호출 결과는 await 한다.
    """

    def __init__(
        self,
        config_path: str | Path | None = None,
        *,
        rate_limit: bool = True,
        # 안전계수: 실제 사용률 = 서버 TPS × safety. 0.9 = 서버 한도의 90%만 사용(10% 여유).
        rate_limit_safety: float = 0.9,
        rate_limit_backoff: bool = True,
        auto_token: bool = True,
        token_retry_limit: int = 5,
    ):
        self._core = _SyncCore(
            config_path,
            rate_limit=rate_limit,
            rate_limit_safety=rate_limit_safety,
            rate_limit_backoff=rate_limit_backoff,
            auto_token=auto_token,
            token_retry_limit=token_retry_limit,
        )

    # ── 동기 코어 위임 속성 ──────────────────────
    @property
    def config(self) -> Config:
        """설정 객체."""
        return self._core.config

    @property
    def token_manager(self) -> TokenManager:
        """토큰 관리자."""
        return self._core.token_manager

    # ── 저수준 비동기 HTTP (동기 코어를 스레드로 위임) ──
    async def _request(
        self,
        method: str,
        path: str,
        body: dict | None = None,
        params: dict | None = None,
        extra_headers: dict | None = None,
    ) -> APIResponse:
        return await asyncio.to_thread(self._core.request, method, path, body, params, extra_headers)

    async def post(self, path: str, body: dict | None = None, **kwargs: Any) -> APIResponse:
        """POST 요청 (비동기). 대부분의 DB증권 API는 POST 방식입니다."""
        return await asyncio.to_thread(self._core.post, path, body, **kwargs)

    async def get(self, path: str, params: dict | None = None, **kwargs: Any) -> APIResponse:
        """GET 요청 (비동기)."""
        return await asyncio.to_thread(self._core.get, path, params, **kwargs)

    # ── 연속조회(자동 페이징) — 저수준 경로 기반 ──────────────────────────
    async def post_paged(
        self,
        path: str,
        body: dict | None = None,
        *,
        params: dict | None = None,
        extra_headers: dict | None = None,
        max_pages: int | None = None,
        cont_key: str = "",
    ) -> list[APIResponse]:
        """POST 연속조회 자동 페이징 (비동기). cont_yn != 'Y' 까지 끝까지 반복 → list[APIResponse].

        raw 경로를 직접 호출할 때 사용. 타입드 API(client.apis.*)에는 fetch_all() 권장.
        유량제어가 페이지 호출을 자동 페이싱한다.
        """
        return await asyncio.to_thread(
            self._core.request_paged, "POST", path, body, params, extra_headers,
            max_pages=max_pages, cont_key=cont_key,
        )

    async def get_paged(
        self,
        path: str,
        params: dict | None = None,
        *,
        extra_headers: dict | None = None,
        max_pages: int | None = None,
        cont_key: str = "",
    ) -> list[APIResponse]:
        """GET 연속조회 자동 페이징 (비동기) → list[APIResponse]. 기본 끝까지(helper 동작)."""
        return await asyncio.to_thread(
            self._core.request_paged, "GET", path, None, params, extra_headers,
            max_pages=max_pages, cont_key=cont_key,
        )

    # ── 연속조회(자동 페이징) — 고수준 메서드 기반 (권장) ──────────────────
    async def fetch_all(
        self,
        endpoint: Callable[..., Awaitable[APIResponse]],
        /,
        *,
        page_delay: float = 0.0,
        start_cont_key: str = "",
        max_pages: int | None = None,
        **kwargs: Any,
    ) -> APIResponse:
        """타입드 엔드포인트를 연속조회로 끝까지 받아 하나의 APIResponse 로 병합.

        ※ 권장 형태는 메서드에 직접 `fetch_all=True` 를 주는 것이다(registry 의 _PagingProxy 가
          이 메서드로 위임한다):
              await client.apis.<group>.<method>(..., fetch_all=True, max_pages=2)
          이 저수준 형태 `client.fetch_all(메서드, ...)` 는 하위호환으로 유지된다.

        dbsec_helper.call_rest_paged 와 동일하게 **서버가 끝을 알릴 때(cont_yn != 'Y')까지
        전부** 받아온다. cont_yn/cont_key 를 직접 넘길 필요가 없고, list 블록(Out1/Out2 등)은
        페이지 간 이어붙여 .pages 에 원본 페이지들을 보존한다. 각 페이지 호출은 유량제어가
        자동 페이싱한다(별도 sleep 불필요).

        예:
            resp = await client.fetch_all(
                client.apis.kr_stock_quote.kr_stock_search_stocks,
                InputCondMrktDivCode="J",
            )
            df = resp.to_dataframe()      # 전 페이지 누적
            n_pages = len(resp.pages)     # 받은 페이지 수

        Args:
            endpoint: client.apis.<group>.<method> (cont_yn/cont_key 인자를 받는 메서드).
            page_delay: 페이지 사이 추가 지연(초). 기본 0 — 유량제어가 이미 페이싱하므로 보통 불필요.
            start_cont_key: 이전 세션 재개용 시작 연속키 ('' = 처음부터).
            max_pages: 선택적 상한. 기본 None = 끝까지 받되, 안전 상한 100페이지(_PAGED_SAFETY_CAP)
                에서 강제 중단한다(폭주 방지 — 더 받으려면 정수 명시). 정수를 주면 그 페이지 수에서
                멈춘다(상한에서 멈추면 마지막 페이지에 데이터가 남을 수 있어 경고 로그를 남긴다).
            **kwargs: 엔드포인트 메서드의 나머지 인자 (cont_yn/cont_key 는 자동 주입).
        """
        kwargs.pop("cont_yn", None)
        kwargs.pop("cont_key", None)
        max_pages = _normalize_max_pages(max_pages)
        pages: list[APIResponse] = []
        cur_yn, cur_key = ("Y", start_cont_key) if start_cont_key else ("N", "")
        while True:
            resp = await endpoint(cont_yn=cur_yn, cont_key=cur_key, **kwargs)
            pages.append(resp)
            if not resp.has_more:                 # 서버가 cont_yn != 'Y' → 마지막 페이지
                break
            # 무진행 가드: has_more=True 인데 다음 cont_key 가 비었거나 직전과 동일하면
            # 같은 요청이 무한 반복되므로(서버 이상) 경고 후 중단한다.
            next_key = resp.cont_key
            if not next_key or next_key == cur_key:
                logger.warning(
                    "fetch_all: 서버가 cont_yn='Y' 이나 cont_key 가 %s "
                    "— 무진행으로 판단해 %d페이지에서 중단(무한루프 방지).",
                    "비어 있음" if not next_key else f"직전과 동일({cur_key!r})", len(pages),
                )
                break
            if max_pages is not None and len(pages) >= max_pages:
                logger.warning(
                    "fetch_all: max_pages=%d 상한에서 중단 — cont_key=%r 부터 데이터가 더 남음",
                    max_pages, resp.cont_key,
                )
                break
            # 안전 상한: max_pages 미지정이어도 폭주 방지(더 받으려면 max_pages 명시).
            if max_pages is None and len(pages) >= _PAGED_SAFETY_CAP:
                logger.warning(
                    "fetch_all: 안전 상한 %d페이지 도달 — 중단(cont_key=%r 부터 더 있음). "
                    "더 받으려면 max_pages 를 명시하세요.", _PAGED_SAFETY_CAP, resp.cont_key,
                )
                break
            cur_yn, cur_key = "Y", next_key
            if page_delay:
                await asyncio.sleep(page_delay)
        return APIResponse.merge(pages)

    async def get_token(self) -> str:
        """유효 접근토큰 확보(비동기, 명시적 발급). 캐시 없으면 즉시 발급(프롬프트 없음)."""
        return await asyncio.to_thread(self._core.token_manager.get_token)

    async def force_refresh(self) -> str:
        """토큰 강제 갱신(비동기). 현재 토큰을 폐기(revoke)한 뒤 새로 발급해 반환한다."""
        return await asyncio.to_thread(self._core.token_manager.force_refresh)

    async def revoke(self) -> None:
        """토큰 폐기(비동기). 서버에 폐기 요청하고 로컬 캐시(.dbsec_token.json)를 삭제한다."""
        return await asyncio.to_thread(self._core.token_manager.revoke)

    # ── 전체 API 레지스트리 (생성된 메서드 재사용 → await) ──
    @cached_property
    def apis(self):
        """DB증권 OpenAPI 전체 API. 메서드 호출 결과는 await 한다.

        예: resp = await client.apis.kr_stock_quote.kr_stock_inquire_price(...)

        전체 그룹: auth, common, kr_stock_order, kr_stock_quote, kr_stock_realtime,
                   kr_futopt_order, kr_futopt_quote, kr_futopt_realtime, kr_chart,
                   ov_stock_order, ov_stock_quote, ov_stock_realtime,
                   ov_futopt_order, ov_futopt_quote, ov_futopt_realtime,
                   bond_order, bond_quote, bond_realtime, ws_common
        """
        from dbsec_sdk.apis.registry import APIRegistry
        # 레지스트리의 API 메서드는 self._client.post(...) 를 호출 → 여기선 코루틴 반환
        return APIRegistry(self)

    # ── WebSocket 팩토리 (이미 비동기) ──
    def create_websocket(self, ws_url: str | None = None):
        """실시간 데이터용 WebSocket 인스턴스를 생성합니다 (DBSecWebSocket).

        connect() → add_realtime() → run() → close() 순으로 사용합니다.
        mode 설정에 따라 운영(7070)/모의(17070) WebSocket에 연결됩니다.

        Args:
            ws_url: 접속할 WebSocket URL 을 수동 지정. None(기본)이면 config.ws_url
                (일반 그룹용 7070/17070). 해외선물옵션(ov_futopt)은 전용 포트(7071)를
                쓰므로 아래처럼 지정하세요:

                    ws = client.create_websocket(
                        ws_url=client.config.ws_url_for("ov_futopt_realtime"))

                (config.ws_url_for(group_slug) 가 ov_futopt_* 면 7071 URL 을 돌려줍니다.)
        """
        return self._core.create_websocket(ws_url)

    # ── 수명주기 ──
    async def aclose(self) -> None:
        """리소스 정리. 토큰 캐시는 기본 유지(다음 실행 재사용).

        명시적으로 토큰을 폐기하려면 `await client.revoke()` 를 호출하세요.
        """
        return None

    async def __aenter__(self) -> "DBSecClient":
        return self

    async def __aexit__(self, *args: object) -> None:
        await self.aclose()


# 하위호환 별칭: 과거 AsyncDBSecClient 를 참조하던 코드 지원 (이제 DBSecClient 가 비동기)
AsyncDBSecClient = DBSecClient
