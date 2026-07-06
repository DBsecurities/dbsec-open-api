"""OAuth2 토큰 수명주기 관리 모듈.

DB증권 Open API 인증 흐름:
1. APP_KEY + APP_SECRET으로 접근토큰(Access Token) 발급
2. 토큰을 REST/WebSocket 요청 헤더에 포함하여 인증
3. 토큰 유효기간: 24시간

토큰 발급/갱신/폐기는 명시적 메서드로 제공한다:
- get_token()      — 유효 토큰 확보(캐시에 없으면 발급). 프롬프트 없음.
- force_refresh()  — 폐기(revoke) 후 재발급으로 강제 갱신.
- revoke()         — 서버 폐기 + 캐시 삭제.

요청 경로(get_headers / WebSocket)의 토큰 자동 확보는 auto_token 으로 제어한다:
- auto_token=True (기본): 요청 시 토큰이 없거나 만료/무효면 자동으로 발급·재발급한다
  (stdin 프롬프트 없이). 토큰거부 응답(IGW00121/00123)의 재발급은 client 요청 루프가 처리.
- auto_token=False: 자동 발급하지 않는다 → 유효 토큰이 없으면 AuthError. 호출자가
  get_token()/force_refresh() 로 토큰을 직접 관리해야 한다.

특성:
- 24시간 이내에 재발급을 요청하면 서버는 기존 토큰(만료시간 동일)을 반환한다.
  새 토큰이 필요하면 revoke 후 발급해야 하므로, 갱신은 force_refresh() 를 쓴다.
- 토큰은 만료 '시각'까지 그대로 사용한다(만료 전 미리 갱신하지 않음). 만료 후의
  처리는 위 auto_token 정책을 따른다.

사용법:
    config = Config("config.yaml")
    tm = TokenManager(config, auto_token=True)
    token = tm.get_token()      # 명시적 발급/확보 (없으면 발급)
    tm.force_refresh()          # 명시적 갱신 (revoke 후 재발급)
    tm.revoke()                 # 명시적 폐기
"""

from __future__ import annotations

import datetime as _dt
import json
import threading
import time
from pathlib import Path

import requests

from dbsec_sdk.config import Config
from dbsec_sdk.exceptions import AuthError

# 캐시 파일의 issued/expires 사람이 읽기 좋은 표기용 (examples/dbsec_helper 와 동일)
_KST = _dt.timezone(_dt.timedelta(hours=9), name="KST")


class TokenManager:
    """OAuth2 접근토큰(Access Token) 관리자.

    토큰 발급 엔드포인트: POST /oauth2/token
    토큰 폐기 엔드포인트: POST /oauth2/revoke

    참고: 토큰 발급/폐기는 DB증권 정책상 1분 1건(IGW00201) 제한이 있으나,
    아래 파일 캐시로 24h 토큰을 재사용하므로 클라이언트측 빈도 제어는 두지 않는다.

    토큰 캐시 (examples/dbsec_helper 와 동일 파일·구조 — 메모리 상태 없이 파일 I/O):
        - 토큰은 저장소 루트의 단일 캐시 파일(.dbsec_token.json)에만 저장된다.
          examples(dbsec_helper) 와 같은 파일을 공유하므로 SDK·예제가 토큰을 상호 재사용한다.
        - get_token() 은 매번 파일에서 유효 토큰을 읽고, 없으면 발급 후 저장한다.
        - mode 는 파일 내용으로 검증한다(불일치 시 무효 → 재발급). 인스턴스가 토큰을
          메모리에 들고 있지 않으므로, 새 프로세스든 여러 client 든 같은 캐시를 공유한다.

    생명주기 (요청 경로의 자동 발급/재발급은 auto_token 으로 제어):
        1. get_token() — 캐시에 유효 토큰 있으면 그대로 반환, 없으면 발급(프롬프트 없음).
        2. 토큰은 만료 '시각'까지 사용한다(만료 전 미리 갱신하지 않음).
        3. 요청 경로는 _token_for_request() 로 토큰을 확보한다 — 없을 때 auto_token=True
           면 발급, False 면 AuthError.
        4. 24시간 이내 재발급 시 서버가 동일 토큰을 반환 → 갱신은 force_refresh()(revoke 후 발급).
    """

    # API 경로
    TOKEN_PATH = "oauth2/token"    # 토큰 발급
    REVOKE_PATH = "oauth2/revoke"  # 토큰 폐기

    # 만료 마진 없음 — 토큰을 만료 '시각'까지 사용한다(만료 전 미리 갱신하지 않음).

    def __init__(self, config: Config, *, auto_token: bool = True):
        self._config = config
        # 요청 경로(get_headers/WebSocket)에서 유효 토큰이 없을 때 자동 발급할지 여부.
        # True(기본): 없으면 발급. False: AuthError 로 알리고 호출자가 직접 관리.
        self._auto_token = bool(auto_token)
        # 동시(멀티스레드/async) 환경에서 force_refresh 의 revoke→재발급 폭주 방지용 락.
        # (AsyncDBSecClient 는 asyncio.to_thread 로 동기 경로를 동시 실행한다.)
        self._refresh_lock = threading.Lock()
        # 메모리 토큰 상태 없음 — 토큰은 항상 캐시 파일에서 읽고 쓴다
        # (examples/dbsec_helper 와 동일 구조)
        # 참고: 토큰 발급은 DB증권 정책상 1분 1건 제한(IGW00201)이지만,
        #       파일 캐시(24h 토큰 재사용)로 사실상 회피되므로 클라이언트측 제어는 두지 않는다.

    # ──────────────────────────────────────────
    # 토큰 파일 캐시 (저장소 루트 .dbsec_token.json — examples 와 공유)
    # 토큰 발급은 1분 1건 제한이라, 매 프로세스마다 재발급하면 IGW00201 이 난다.
    # production/demo 혼선은 파일 내용의 mode 검증으로 막는다(불일치 시 재발급).
    # examples/dbsec_helper 와 동일한 파일·JSON 포맷·검증 로직을 공유한다.
    # ──────────────────────────────────────────

    @property
    def _cache_path(self) -> Path:
        """저장소 루트의 단일 토큰 캐시 파일 경로 (examples 와 공유).

        실행 위치(cwd)와 무관하게 항상 저장소 루트의 .dbsec_token.json 에 저장한다.
        examples(dbsec_helper) 와 같은 파일을 공유하며, mode 는 파일 내용으로 검증한다
        (mode 불일치 시 _load_cached_token 이 None 을 반환 → 재발급).
        """
        return Path(__file__).resolve().parent.parent / ".dbsec_token.json"

    def _save_token(self, access_token: str, expires_in: int) -> None:
        """발급된 토큰을 만료시각·모드와 함께 캐시 파일에 저장.

        examples/dbsec_helper._save_token 과 동일한 포맷 (issued/expires epoch +
        KST 문자열 + expires_in_hours).
        """
        issued = int(time.time())
        expires_in = int(expires_in or 0)
        expires = issued + expires_in
        _hours_f = expires_in / 3600
        expires_in_hours = int(_hours_f) if _hours_f == int(_hours_f) else round(_hours_f, 1)
        fmt = lambda ts: _dt.datetime.fromtimestamp(ts, _KST).strftime("%Y-%m-%d %H:%M:%S %Z")
        try:
            self._cache_path.write_text(json.dumps({
                "access_token":     access_token,
                "issued_at":        issued,
                "issued_at_kst":    fmt(issued),
                "expires_at":       expires,
                "expires_at_kst":   fmt(expires),
                "expires_in":       expires_in,        # 서버 응답 그대로 (초)
                "expires_in_hours": expires_in_hours,  # 가독용: 86400 → 24
                "mode":             self._config.mode,
            }, ensure_ascii=False, indent=2), encoding="utf-8")
        except Exception:
            pass  # 캐시 저장 실패는 치명적이지 않음 (이번 호출 토큰은 그대로 사용)

    def _load_cached_token(self) -> str | None:
        """캐시에서 유효 토큰 반환. 만료(만료 시각 도달)/모드불일치/파일없음 시 None.

        만료 마진 없이 만료 '시각'까지 토큰을 유효로 본다(만료 전 미리 갱신하지 않음).
        """
        p = self._cache_path
        if not p.exists():
            return None
        try:
            data = json.loads(p.read_text(encoding="utf-8"))
        except Exception:
            return None
        if data.get("expires_at", 0) <= int(time.time()):  # 만료 시각까지 사용 (미리 갱신 안 함)
            return None
        if data.get("mode") != self._config.mode:
            return None
        return data.get("access_token")

    def _clear_cache(self) -> None:
        """캐시 파일 삭제 (폐기 시)."""
        try:
            self._cache_path.unlink(missing_ok=True)
        except Exception:
            pass

    def get_token(self) -> str:
        """유효한 접근토큰을 확보해 반환합니다 (명시적 발급).

        캐시에 유효한 토큰이 있으면 그대로 반환하고, 없으면 즉시 발급합니다
        (stdin 프롬프트 없음). 호출자가 직접 부르는 명시적 메서드이므로
        auto_token 설정과 무관하게 항상 발급합니다.

        토큰을 강제로 새로 받으려면(만료 임박 등) force_refresh() 를 사용하세요.

        Returns:
            유효한 접근토큰 문자열

        Raises:
            AuthError: 발급에 실패한 경우
        """
        cached = self._load_cached_token()
        if cached:
            return cached
        return self._fetch_token()

    def _token_for_request(self) -> str:
        """요청 경로(get_headers/WebSocket)용 토큰을 확보합니다.

        캐시에 유효 토큰이 있으면 사용하고, 없으면 auto_token 정책을 따릅니다:
          · auto_token=True  → 즉시 발급(프롬프트 없음)
          · auto_token=False → AuthError (호출자가 get_token() 으로 직접 발급)

        Raises:
            AuthError: auto_token=False 인데 유효 토큰이 없는 경우, 또는 발급 실패.
        """
        cached = self._load_cached_token()
        if cached:
            return cached
        if self._auto_token:
            return self._fetch_token()
        raise AuthError(
            "유효한 접근토큰이 없습니다 (auto_token=False). "
            "client.get_token() 으로 발급하거나, DBSecClient(auto_token=True) 로 설정하세요."
        )

    def force_refresh(self, invalid_token: str | None = None) -> str:
        """현재 토큰을 폐기(revoke)하고 새 토큰을 발급한다 (강제 갱신, 비인터랙티브).

        명시적 갱신 메서드다. auto_token=True 인 경우, client 요청 루프가 토큰거부
        응답(IGW00121/00123)을 받으면 '요청에 사용한(=무효로 판정된) 토큰'을
        invalid_token 으로 넘겨 이 메서드를 호출한다.

        DB증권은 24시간 이내 재발급 시 기존(무효) 토큰을 그대로 반환하므로,
        반드시 revoke 로 서버·캐시의 기존 토큰을 비운 뒤 새로 발급한다.

        Args:
            invalid_token: 호출자가 '무효'로 판정한(그 요청에 실제 사용한) 토큰. 주어지면,
                락 획득 후 캐시의 현재 토큰이 이 값과 다르면(=다른 스레드가 이미 재발급함)
                revoke 하지 않고 그 새 토큰을 그대로 반환한다 — 방금 발급된 유효 토큰을
                실수로 폐기하는 것을 막는다. None(사용자의 명시적 호출)이면 항상 재발급한다.

        Returns:
            새로 발급된(또는 다른 스레드가 이미 재발급한) 접근토큰.

        동시 호출 안전: 여러 스레드가 같은 무효 토큰으로 동시에 들어와도, 락 안에서
        '무효 토큰(invalid_token) vs 현재 캐시 토큰'을 비교하므로 먼저 진입한 스레드만
        재발급하고 나머지는 갱신된 토큰을 그대로 받는다 — 불필요한 revoke→재발급 폭주와
        1분 1건 제한 충돌, 그리고 '방금 발급된 유효 토큰을 폐기'하는 사고를 함께 막는다.
        (기존 before/after 스냅샷 방식은 스냅샷을 갱신 완료 후에 뜨면 before==after 라
        새 토큰을 revoke 해버리는 결함이 있었다.)

        Raises:
            AuthError: 재발급 실패 시 (예: 1분 1건 제한 IGW00201, 자격증명 오류).
        """
        with self._refresh_lock:
            current = self._load_cached_token()
            if invalid_token is not None and current and current != invalid_token:
                # 다른 스레드가 이미 새 토큰으로 갱신함 → 재발급 생략(새 토큰 보존)
                return current
            self.revoke()              # 서버 폐기 + 캐시 삭제 (실패해도 캐시는 삭제됨)
            return self._fetch_token()  # 새 토큰 발급 후 캐시 저장

    def get_headers(self, extra: dict | None = None) -> dict:
        """REST API 호출용 공통 헤더를 반환합니다.

        Bearer 토큰을 포함합니다. 토큰은 _token_for_request() 로 확보하므로
        auto_token=False 이고 유효 토큰이 없으면 AuthError 가 발생합니다.

        Args:
            extra: 추가로 포함할 헤더 (예: {"cont_yn": "Y"})

        Returns:
            API 호출에 사용할 헤더 dict
        """
        headers = {
            "content-type": "application/json; charset=utf-8",
            "authorization": f"Bearer {self._token_for_request()}",
        }
        if extra:
            headers.update(extra)
        return headers

    def revoke(self) -> None:
        """토큰을 폐기합니다.

        캐시 파일의 토큰을 서버에 폐기 요청하고 캐시 파일을 삭제합니다.
        DB증권은 24시간 이내 재발급 시 기존 토큰(만료시간 동일)을 반환하므로,
        새 토큰이 필요한 경우 반드시 이 메서드를 먼저 호출해야 합니다.

        폐기 요청 실패 시에도 캐시 파일은 삭제됩니다.
        (examples/dbsec_helper.revoke_token 과 동일 구조)
        """
        token = self._load_cached_token()
        if token:
            url = f"{self._config.base_url}/{self.REVOKE_PATH}"
            # /oauth2/* 는 application/x-www-form-urlencoded 요구 (JSON 으로 보내면 IGW00133)
            body = {
                "appkey": self._config.app_key,
                "appsecretkey": self._config.app_secret,
                "token_type_hint": "access_token",
                "token": token,
            }
            try:
                requests.post(
                    url,
                    headers={"content-type": "application/x-www-form-urlencoded"},
                    data=body,
                    timeout=10,
                )
            except Exception:
                pass  # 폐기 실패해도 캐시 삭제는 진행

        # 캐시 파일 삭제
        self._clear_cache()

    def _fetch_token(self) -> str:
        """서버에 토큰 발급을 요청하고, 캐시에 저장한 뒤 토큰을 반환합니다.

        POST /oauth2/token
        Content-Type: application/x-www-form-urlencoded  (JSON 으로 보내면 IGW00133)
        요청 body: {
            "grant_type": "client_credentials",
            "appkey": "APP_KEY",
            "appsecretkey": "APP_SECRET",
            "scope": "oob"
        }

        응답 body: {
            "access_token": "토큰문자열",
            "token_type": "Bearer",
            "expires_in": 86400
        }

        Returns:
            발급된 접근토큰 문자열

        Raises:
            AuthError: HTTP 200이 아니거나 access_token이 없는 경우
        """
        url = f"{self._config.base_url}/{self.TOKEN_PATH}"
        # /oauth2/* 는 application/x-www-form-urlencoded 요구 (JSON 으로 보내면 IGW00133)
        body = {
            "grant_type": "client_credentials",
            "appkey": self._config.app_key,
            "appsecretkey": self._config.app_secret,
            "scope": "oob",
        }

        resp = requests.post(
            url,
            headers={"content-type": "application/x-www-form-urlencoded"},
            data=body,
            timeout=10,
        )
        if resp.status_code != 200:
            raise AuthError(f"토큰 발급 실패: {resp.status_code} {resp.text}")

        data = resp.json()
        access_token = data.get("access_token", "")
        if not access_token:
            raise AuthError(f"토큰이 응답에 없음: {data}")

        # expires_in: 토큰 유효 시간(초). 기본값 86400 (24시간)
        expires_in = int(data.get("expires_in", 86400))
        # 캐시 파일에 저장 → 다음 호출/프로세스가 재발급 없이 재사용 (1분 1건 제한 회피)
        self._save_token(access_token, expires_in)
        return access_token
