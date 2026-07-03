"""유량제어(Rate Limiting) 모듈.

DB증권 Open API 의 호출 빈도를 클라이언트에서 선제적으로 제어한다.
서버는 초과 시 IGW00201("호출 거래건수를 초과하였습니다")로 거부하므로,
동시/고속 호출 시 클라이언트측 제어가 필요하다.

구성:
    RateLimiter        — 동기 min-interval(균등 간격) 페이서 (REST 용)
    AsyncRateLimiter   — 비동기 min-interval 페이서 (WebSocket connect 등)
    RateLimitController — 2-tier 오케스트레이터
        · 앱(계좌) 레벨 글로벌 리미터  (APP_TPS = 20 TPS)
        · 엔드포인트(path) 레벨 리미터  (docs/api_support_matrix.md 의 TPS 컬럼)

엔드포인트별 TPS 의 단일 소스는 docs/api_support_matrix.md 의 'TPS' 컬럼이다(수기 관리).
매트릭스는 경로(path)가 없으므로, endpoints.py 의 PATHS(메서드↔경로)와 조인하여
path→TPS 를 구성한다(중복 관리 방지: 별도 rate_limits 파일/생성기 없음).

왜 Sliding-Window 가 아니라 min-interval(균등 간격) 인가:
    Sliding-Window 는 윈도에 여유가 있으면 max_calls 개를 '한꺼번에(버스트)'
    통과시킨다. 그런데 서버는 자체 1초 카운팅 윈도로 집계하므로, 직전 호출이
    서버 윈도에 남아 있으면 (직전 N개 + 이번 버스트)가 합산 한도를 넘어
    IGW00201 이 발생한다. 실측에서 동시 12콜 중 2콜이 이렇게 누수됐다.
    → 호출 사이 '최소 간격(min_interval = period / max_calls)'을 강제해 버스트를
      없애고 요청을 균등 분산한다. 시작 시 버스트가 없으므로 직전 호출과
      합산돼도 한도를 넘지 않는다. 실측: 동시 12~15콜 sync/async 모두 0 누수.

안전마진(safety):
    유효율 = max_calls / period = TPS * safety (RateLimitController 가 period=1/safety
    로 주입). 기본 safety=0.9 → 유효율 TPS의 90%, min_interval = 1/(TPS*0.9).
    0<safety<=1. (가드 작을수록 빠르나 경계 누수 위험↑; 누수 시 IGW00201 은 client 의
    rate_limit_backoff 안전망이 흡수.)
"""

from __future__ import annotations

import asyncio
import importlib
import re
import threading
import time
from pathlib import Path

# ── 엔드포인트별 TPS 레지스트리 (단일 소스: docs/api_support_matrix.md) ──
APP_TPS = 20      # 앱(계좌) 글로벌 유량제어 (DB증권 정책)
DEFAULT_TPS = 1   # 매트릭스에 TPS 가 없는 엔드포인트 기본값

# 패키지(dbsec_sdk/)의 형제 디렉터리 docs/ 의 매트릭스
_MATRIX_MD = Path(__file__).resolve().parent.parent / "docs" / "api_support_matrix.md"
# 메서드 슬러그 패턴: 소문자/숫자 + 밑줄 1개 이상 (TR코드·한글 컬럼과 구분)
_METHOD_RE = re.compile(r"^[a-z][a-z0-9]*(?:_[a-z0-9]+)+$")


def _matrix_method_tps() -> dict[str, int]:
    """매트릭스 표에서 {메서드 슬러그: TPS} 추출.

    각 행을 '|' 로 분리해 '메서드 슬러그처럼 보이는 셀'과 '숫자만 있는 셀(TPS)'을
    찾는다. 컬럼 순서/개수와 무관. TPS 가 '-' 인 행(실시간/OAuth 등)은 제외된다.
    """
    out: dict[str, int] = {}
    try:
        text = _MATRIX_MD.read_text(encoding="utf-8")
    except OSError:
        return out
    for line in text.splitlines():
        line = line.strip()
        if not line.startswith("|"):
            continue
        cells = [c.strip().strip("`") for c in line.strip("|").split("|")]
        method = next((c for c in cells if _METHOD_RE.match(c)), None)
        tps = next((c for c in cells if c.isdigit()), None)
        if method and tps:
            out[method] = int(tps)
    return out


def _load_rate_limits() -> dict[str, int]:
    """path -> TPS 구성: 매트릭스(메서드→TPS) ⋈ endpoints PATHS(메서드→경로).

    endpoints 모듈을 지연 임포트해 PATHS(경로↔메서드)를 읽는다(임포트 순환 회피).
    매트릭스/엔드포인트를 못 읽으면 빈 dict(모두 DEFAULT_TPS 적용).
    """
    method_tps = _matrix_method_tps()
    if not method_tps:
        return {}
    reg: dict[str, int] = {}
    apis_dir = Path(__file__).resolve().parent / "apis"
    try:
        subdirs = [d for d in apis_dir.iterdir() if (d / "endpoints.py").exists()]
    except OSError:
        return reg
    for sub in subdirs:
        try:
            mod = importlib.import_module(f"dbsec_sdk.apis.{sub.name}.endpoints")
        except Exception:
            continue
        for obj in vars(mod).values():
            if isinstance(obj, type) and hasattr(obj, "PATHS"):
                for slug, path in obj.PATHS.items():
                    if slug in method_tps:
                        reg[path] = method_tps[slug]
    return reg


# path -> TPS (지연 빌드: 첫 조회 시 1회 구성하여 캐시 → 임포트 순환/비용 회피)
_RATE_LIMITS_CACHE: dict[str, int] | None = None


def get_rate_limits() -> dict[str, int]:
    """path -> TPS 레지스트리(지연 빌드 + 캐시)."""
    global _RATE_LIMITS_CACHE
    if _RATE_LIMITS_CACHE is None:
        _RATE_LIMITS_CACHE = _load_rate_limits()
    return _RATE_LIMITS_CACHE


class RateLimiter:
    """동기 min-interval(균등 간격) 유량제어기 (스레드 안전).

    호출을 일정 간격(min_interval = period / max_calls)으로 균등 분산한다.
    버스트를 허용하지 않으므로 서버 카운팅 윈도와의 경계 누수가 없다.

    Args:
        max_calls: 기간(period) 당 허용 호출 수.
        period: 기간(초). 기본 1.0. (유효율 = max_calls / period)

    Example::

        limiter = RateLimiter(max_calls=5, period=1.0)  # 5 TPS, 0.2s 간격
        for _ in range(100):
            limiter.acquire()   # 직전 호출과 0.2s 미만이면 자동 대기
            requests.post(...)
    """

    def __init__(self, max_calls: int, period: float = 1.0):
        self.max_calls = max(1, int(max_calls))
        self.period = float(period)
        self.min_interval = self.period / self.max_calls
        self._next_time = 0.0  # 다음 호출이 허용되는 monotonic 시각
        self._lock = threading.Lock()

    def acquire(self) -> float:
        """호출 권한 획득. 최소 간격 미충족 시 대기하고, 대기한 시간(초)을 반환."""
        with self._lock:
            now = time.monotonic()
            slot = self._next_time if self._next_time > now else now
            waited = slot - now
            if waited > 0:
                time.sleep(waited)
            self._next_time = slot + self.min_interval
            return waited


class AsyncRateLimiter:
    """비동기 min-interval 유량제어기.

    RateLimiter 와 동일 알고리즘이나 asyncio.Lock + asyncio.sleep 사용.
    WebSocket 연결(6 TPM) 등 비동기 컨텍스트용.
    """

    def __init__(self, max_calls: int, period: float = 1.0):
        self.max_calls = max(1, int(max_calls))
        self.period = float(period)
        self.min_interval = self.period / self.max_calls
        self._next_time = 0.0
        self._lock = asyncio.Lock()

    async def acquire(self) -> float:
        async with self._lock:
            now = time.monotonic()
            slot = self._next_time if self._next_time > now else now
            waited = slot - now
            if waited > 0:
                await asyncio.sleep(waited)
            self._next_time = slot + self.min_interval
            return waited


class RateLimitController:
    """2-tier 유량제어 오케스트레이터 (동기/스레드 안전).

    request 전송 직전 acquire(path) 를 호출하면:
        1) 앱(계좌) 레벨 글로벌 리미터 통과 (APP_TPS)
        2) 해당 path 의 엔드포인트 리미터 통과 (RATE_LIMITS[path] or DEFAULT_TPS)
    두 관문을 모두 통과해야 호출이 진행된다.

    Args:
        enabled: False 면 모든 acquire 가 즉시 통과 (테스트/디버깅용).
        safety:  안전계수(0<safety<=1). period = 1.0/safety. 기본 0.9.

    Note:
        AsyncDBSecClient 는 동기 클라이언트를 asyncio.to_thread 로 감싸므로,
        이 동기 컨트롤러를 그대로 공유한다(별도 비동기 컨트롤러 불필요).
        oauth2/* 경로는 client._request 를 거치지 않으므로(파일 캐시로 1분 1건 회피)
        이 컨트롤러의 대상이 아니다.
    """

    def __init__(self, *, enabled: bool = True, safety: float = 0.9):
        if not (0.0 < safety <= 1.0):
            raise ValueError("safety 는 0 초과 1 이하여야 합니다.")
        self.enabled = enabled
        self.safety = safety
        self._period = 1.0 / safety
        self._app = RateLimiter(APP_TPS, self._period)
        self._by_path: dict[str, RateLimiter] = {}
        self._lock = threading.Lock()

    def _tps_for(self, path: str) -> int:
        # 레지스트리 키는 선행 슬래시 포함 경로. client 가 넘기는 path 와 정규화 일치.
        key = path if path.startswith("/") else "/" + path
        return get_rate_limits().get(key, DEFAULT_TPS)

    def _limiter_for(self, path: str) -> RateLimiter:
        with self._lock:
            lim = self._by_path.get(path)
            if lim is None:
                lim = RateLimiter(self._tps_for(path), self._period)
                self._by_path[path] = lim
            return lim

    def acquire(self, path: str) -> float:
        """path 호출 권한 획득. 두 관문 대기시간 합(초) 반환."""
        if not self.enabled:
            return 0.0
        waited = self._app.acquire()           # 1) 앱 글로벌
        waited += self._limiter_for(path).acquire()  # 2) 엔드포인트
        return waited
