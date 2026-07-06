"""DB증권 OpenAPI standalone 예제 공통 헬퍼.

config.yaml 로드 + 토큰 캐싱(루트 .dbsec_token.json) + REST/WebSocket 호출 + 응답 출력.
사용법은 examples/<group>/README.md 또는 각 함수 docstring 참조.
"""
from __future__ import annotations

import asyncio
import datetime as _dt
import json
import sys
import time
from pathlib import Path

import requests
import yaml

# Windows cp949 콘솔에서 ⚠ ✓ 등 일부 유니코드 출력 시 UnicodeEncodeError 가 나는 것을
# 방지하기 위해 본 헬퍼를 import 하는 시점에 stdout/stderr 을 UTF-8 로 재설정.
# (Python 3.7+) errors="replace" → 정말 인코딩 불가한 글자는 ? 로 대체, 죽지 않음.
for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8", errors="replace")  # type: ignore[union-attr]
    except Exception:
        pass


# ─────────────────────────────────────────
# 경로 / 상수
# ─────────────────────────────────────────
_KST = _dt.timezone(_dt.timedelta(hours=9), name="KST")
_EXAMPLES_DIR = Path(__file__).resolve().parent
_REPO_ROOT    = _EXAMPLES_DIR.parent
_CONFIG_PATH  = _REPO_ROOT / "config.yaml"
# 토큰 캐시는 저장소 루트의 단일 파일(.dbsec_token.json) — dbsec_sdk(auth) 와 공유한다.
# mode 는 파일 내용으로 검증하므로(불일치 시 재발급) 모드별 파일 분리 없이 안전.
_TOKEN_CACHE  = _REPO_ROOT / ".dbsec_token.json"

_OV_FUTOPT_PREFIXES = ("ov_futopt",)

# 연속조회(call_rest_paged) 안전 상한: max_pages 미지정이어도 이 페이지 수에서 강제 중단.
# 서버가 cont_yn='Y' 를 무한 반복하거나 cont_key 가 진행하지 않는 이상 상황의 폭주 방지.
_PAGED_SAFETY_CAP = 100

# 누락된 environment 키 안내 시 보여줄 예시 값 (config.yaml.example 과 동일)
# 해외선물옵션(ov_futopt)은 모의투자 미지원으로, 운영/모의 구분 없이 단일 URL 이므로 ws_demo 키는 생략한다.
_ENV_EXAMPLES = {
    "base_url":                 "https://openapi.dbsec.co.kr:8443",
    "ws_production":            "wss://openapi.dbsec.co.kr:7070/websocket",
    "ws_demo":                  "wss://openapi.dbsec.co.kr:17070/websocket",
    "ws_production_ov_futopt":  "wss://openapi.dbsec.co.kr:7071/websocket",
}


# ─────────────────────────────────────────
# 설정 로드
# ─────────────────────────────────────────
class ConfigError(Exception):
    """config.yaml 누락/잘못된 설정에 대한 사용자 친화적 에러."""
    pass


def _require_env(env: dict, key: str) -> str:
    """environment.<key> 가 있으면 반환. 없으면 친절한 안내 메시지로 ConfigError."""
    value = env.get(key)
    if value:
        return value
    example = _ENV_EXAMPLES.get(key, "<적절한 값>")
    raise ConfigError(
        f"\n┌─ config.yaml 설정 누락 ─────────────────────────────\n"
        f"│ environment.{key} 항목이 없거나 비어있습니다.\n"
        f"│\n"
        f"│ 파일: {_CONFIG_PATH}\n"
        f"│ 아래 줄을 environment 섹션에 추가해 주세요:\n"
        f"│\n"
        f"│     {key}: \"{example}\"\n"
        f"│\n"
        f"│ (전체 형식은 config.yaml.example 참고)\n"
        f"└─────────────────────────────────────────────────────"
    )


def _ws_url(env: dict, mode: str, ov_futopt: bool = False) -> str:
    """config.yaml 의 environment.ws_* 값 반환. 누락 시 ConfigError.

    해외선물옵션(ov_futopt)은 DB증권 시스템 자체가 모의투자 미지원이므로
    demo 모드에서는 명시적으로 차단한다.
    """
    if ov_futopt and mode != "production":
        raise ConfigError(
            "\n┌─ 해외선물옵션은 모의투자 미지원 ───────────────────────\n"
            "│ ov_futopt_* 그룹은 DB증권 시스템 자체가 모의투자를\n"
            "│ 지원하지 않습니다 — 운영(production) 환경에서만 호출 가능.\n"
            "│\n"
            f"│ 현재 mode: \"{mode}\"\n"
            f"│ 파일      : {_CONFIG_PATH}\n"
            "│\n"
            "│ 해결 — config.yaml 의 environment.mode 를 \"production\" 으로\n"
            "│ 변경하고 실전투자 앱키(prd_app_key/prd_app_secret)를 입력하세요.\n"
            "└─────────────────────────────────────────────────────"
        )
    suffix = "_ov_futopt" if ov_futopt else ""
    base   = "production" if mode == "production" else "demo"
    return _require_env(env, f"ws_{base}{suffix}")


def load_config() -> dict:
    """config.yaml 파싱 → 평탄화된 dict.

    mode("production"/"demo")에 따라 prd_* / vtl_* 앱키를 선택해 한 쌍만 반환.
    REST 에 필수인 base_url 만 즉시 검증한다. WebSocket URL(ws_general/ws_ov_futopt)은
    실제 ws_url_for() 가 호출될 때 lazy 하게 검증 — 해외선옵 모의투자처럼
    특정 환경에서 미지원인 항목이 있어도 그와 무관한 REST 예제는 그대로 실행된다.

    Returns: {mode, app_key, app_secret, base_url, _env(원본 environment dict)}
    """
    if not _CONFIG_PATH.exists():
        raise FileNotFoundError(
            f"config.yaml 을 찾을 수 없습니다: {_CONFIG_PATH}\n"
            "  → cp config.yaml.example config.yaml 후 키를 입력하세요."
        )
    cfg = yaml.safe_load(_CONFIG_PATH.read_text(encoding="utf-8")) or {}
    auth, env = cfg.get("auth", {}), cfg.get("environment", {})
    mode = str(env.get("mode", "demo")).strip()
    # mode 검증: "demo"/"production" 외(오타·대소문자)면 즉시 차단.
    # 검증이 없으면 오타(예: "Demo","prod") 시 prefix 가 조용히 "prd"(실전 키)로
    # 폴백돼 '모의라 믿고 실주문'이 나갈 수 있으므로 명확히 막는다.
    if mode not in ("demo", "production"):
        raise ConfigError(
            "\n┌─ 잘못된 mode 값 ───────────────────────────────────\n"
            f"│ environment.mode = \"{mode}\" 은(는) 허용되지 않습니다.\n"
            "│ \"demo\"(모의투자) 또는 \"production\"(실전) 중 하나여야 합니다.\n"
            "│ (대소문자·오타 주의 — 예: \"Demo\", \"prod\", \"real\" 불가)\n"
            "│\n"
            f"│ 파일: {_CONFIG_PATH}\n"
            "└─────────────────────────────────────────────────────"
        )
    prefix = "vtl" if mode == "demo" else "prd"   # 모의투자=vtl, 운영=prd
    return {
        "mode":         mode,
        "app_key":      auth.get(f"{prefix}_app_key", "") or "",
        "app_secret":   auth.get(f"{prefix}_app_secret", "") or "",
        "base_url":     _require_env(env, "base_url"),
        "_env":         env,
    }


def ws_url_for(group_slug: str | None, cfg: dict | None = None) -> str:
    """그룹 slug 로 WebSocket URL 선택. ov_futopt_* 그룹만 7071/17071 전용 포트.

    이 함수가 호출되는 시점에만 ws_* 키 누락 여부를 검증한다 (lazy validation).
    """
    cfg = cfg or load_config()
    is_ov = bool(group_slug and any(group_slug.startswith(p) for p in _OV_FUTOPT_PREFIXES))
    return _ws_url(cfg["_env"], cfg["mode"], ov_futopt=is_ov)


def _infer_group_slug() -> str | None:
    """호출 스크립트 경로에서 그룹 slug 추론 — examples/<group>/<file>.py 구조 가정.

    REST 예제는 group_slug 인자를 명시적으로 받지 않으므로,
    ov_futopt 모의투자 차단 등 그룹 컨텍스트가 필요한 가드는 이 함수를 사용한다.
    examples/ 하위가 아니면 None.
    """
    try:
        main_file = Path(sys.argv[0]).resolve()
    except Exception:
        return None
    parts = main_file.parts
    try:
        idx = parts.index(_EXAMPLES_DIR.name)
    except ValueError:
        return None
    return parts[idx + 1] if idx + 1 < len(parts) - 1 else None


def _guard_ov_futopt_demo(cfg: dict, group_slug: str | None = None) -> None:
    """ov_futopt_* 그룹 호출인데 demo 모드면 ConfigError 로 명확히 차단.

    DB증권 해외선물옵션은 시스템 차원에서 모의투자 미지원이므로 호출 자체가 실패한다.
    REST/WS 진입점에서 일관되게 호출해 사용자 혼동을 줄인다.
    """
    slug = group_slug or _infer_group_slug()
    if not slug:
        return
    if not any(slug.startswith(p) for p in _OV_FUTOPT_PREFIXES):
        return
    if cfg.get("mode") == "production":
        return
    raise ConfigError(
        "\n┌─ 해외선물옵션은 모의투자 미지원 ───────────────────────\n"
        "│ ov_futopt_* 그룹은 DB증권 시스템 자체가 모의투자를\n"
        "│ 지원하지 않습니다 — 운영(production) 환경에서만 호출 가능.\n"
        "│\n"
        f"│ 현재 mode  : \"{cfg.get('mode')}\"\n"
        f"│ 호출 그룹  : {slug}\n"
        f"│ config 파일: {_CONFIG_PATH}\n"
        "│\n"
        "│ 해결 — config.yaml 의 environment.mode 를 \"production\" 으로\n"
        "│ 변경하고 실전투자 앱키(prd_app_key/prd_app_secret)를 입력하세요.\n"
        "└─────────────────────────────────────────────────────"
    )


# ─────────────────────────────────────────
# 토큰 캐시 (루트 .dbsec_token.json)
# ─────────────────────────────────────────
def _save_token(access_token: str, expires_in: int, mode: str) -> None:
    """발급된 토큰을 만료시각·모드와 함께 캐시에 저장.

    매 발급마다 issued/expires (epoch + KST 문자열) 를 새 값으로 갱신한다.
    expires_in 은 서버가 내려준 raw 초 + 사람이 읽기 좋은 시간 단위를 같이 저장.
    """
    issued  = int(time.time())
    expires_in = int(expires_in or 0)
    expires = issued + expires_in
    # 정수 시간이면 int 로, 아니면 소수점 1자리까지 — JSON 가독성 ↑
    _hours_f = expires_in / 3600
    expires_in_hours = int(_hours_f) if _hours_f == int(_hours_f) else round(_hours_f, 1)
    fmt = lambda ts: _dt.datetime.fromtimestamp(ts, _KST).strftime("%Y-%m-%d %H:%M:%S %Z")
    _TOKEN_CACHE.write_text(json.dumps({
        "access_token":     access_token,
        "issued_at":        issued,
        "issued_at_kst":    fmt(issued),
        "expires_at":       expires,
        "expires_at_kst":   fmt(expires),
        "expires_in":       expires_in,        # 서버 응답 그대로 (초)
        "expires_in_hours": expires_in_hours,  # 가독용: 86400 → 24
        "mode":             mode,
    }, ensure_ascii=False, indent=2), encoding="utf-8")


def load_cached_token(mode: str | None = None) -> str | None:
    """캐시에서 유효 토큰 반환. 만료/모드불일치 시 None.

    만료 1분 전부터 None 반환 — 호출 도중 만료되는 사고 방지.
    """
    if not _TOKEN_CACHE.exists():
        return None
    try:
        data = json.loads(_TOKEN_CACHE.read_text(encoding="utf-8"))
    except Exception:
        return None
    if data.get("expires_at", 0) <= int(time.time()) + 60:   # 만료 1분 여유
        return None
    if mode and data.get("mode") != mode:
        return None
    return data.get("access_token")


def clear_cached_token() -> None:
    """루트 .dbsec_token.json 파일 삭제. 토큰 폐기 후 호출."""
    if _TOKEN_CACHE.exists():
        _TOKEN_CACHE.unlink()


# ─────────────────────────────────────────
# OAuth (토큰 발급/폐기) — /oauth2/* 는 form-encoded body
# ─────────────────────────────────────────
def _safe_json(resp) -> dict:
    """응답이 JSON 이 아니어도 죽지 않도록 — 실패 시 {raw: text}."""
    try:
        return resp.json()
    except Exception:
        return {"raw": resp.text}


def _oauth_post(cfg: dict, path: str, data: dict):
    """OAuth 엔드포인트 공통 form-encoded POST.

    /oauth2/token, /oauth2/revoke 둘 다 application/x-www-form-urlencoded 요구.
    """
    resp = requests.post(
        f"{cfg['base_url']}{path}",
        headers={"content-type": "application/x-www-form-urlencoded"},
        data=data, timeout=30,
    )
    return resp, _safe_json(resp)


def issue_token(cfg: dict | None = None):
    """새 토큰 발급. 성공 시 루트 .dbsec_token.json 캐시에 저장 → (resp, data).

    유효기간 24시간. 만료 전 재발급 시 동일 토큰이 내려옴 (DB증권 정책).
    """
    cfg = cfg or load_config()
    resp, data = _oauth_post(cfg, "/oauth2/token", {
        "grant_type":   "client_credentials",
        "appkey":       cfg["app_key"],
        "appsecretkey": cfg["app_secret"],
        "scope":        "oob",
    })
    if resp.ok and data.get("access_token"):
        _save_token(data["access_token"], data.get("expires_in", 0), cfg["mode"])
    return resp, data


def revoke_token(cfg: dict | None = None, token: str | None = None):
    """토큰 폐기 + 캐시 파일 삭제.

    토큰 인자가 없으면 캐시에서 읽어와 폐기. 캐시도 비어있으면 (None, info) 반환.
    """
    cfg = cfg or load_config()
    token = token or load_cached_token()
    if not token:
        return None, {"info": "폐기할 토큰 없음 — 캐시(루트 .dbsec_token.json)가 비어있거나 만료됨"}
    resp, data = _oauth_post(cfg, "/oauth2/revoke", {
        "appkey":          cfg["app_key"],
        "appsecretkey":    cfg["app_secret"],
        "token_type_hint": "access_token",
        "token":           token,
    })
    clear_cached_token()
    return resp, data


def get_token(cfg: dict | None = None) -> str:
    """REST 호출 직전에 쓰는 헬퍼 — 캐시 우선, 없거나 만료면 사용자에게 선택지 제시.

    캐시가 비었거나 만료된 경우:
      · 안내 메시지 출력 — 현재 환경 / 캐시 위치 / 수동 발급 방법
      · 자동 발급에 사용될 정보 출력 — config 파일 경로 / 사용 앱키 필드(마스킹) /
        호출 엔드포인트 (사용자가 무엇을 보고 발급할지 확인 가능)
      · [1] 자동 발급 후 계속  [2] 실행 취소  선택을 받음
      · 입력이 비었거나 EOF (non-interactive 환경 — pipe / CI 등)면 안전하게 취소

    발급까지 실패하면 응답을 출력하고 SystemExit 으로 즉시 중단.
    """
    cfg = cfg or load_config()
    cached = load_cached_token(cfg["mode"])
    if cached:
        return cached

    env_label = "운영(production)" if cfg["mode"] == "production" else "모의투자(demo)"
    key_field = "prd_app_key" if cfg["mode"] == "production" else "vtl_app_key"
    ak = cfg["app_key"] or ""
    app_key_masked = (ak[:6] + "..." + ak[-4:]) if len(ak) >= 10 else (ak or "(미설정)")
    print()
    print("━" * 72)
    print("⚠ 유효한 접근토큰 캐시가 없습니다.")
    print("━" * 72)
    print(f"  현재 환경         : {env_label}")
    print(f"  토큰 캐시 위치    : {_TOKEN_CACHE}")
    print(f"  수동 발급 스크립트: python examples/auth/token_issue.py")
    print()
    print("  ─ 자동 발급에 사용될 정보 ─")
    print(f"    config 파일     : {_CONFIG_PATH}")
    print(f"    사용 앱키 필드  : auth.{key_field} = {app_key_masked}")
    print(f"    호출 엔드포인트 : POST {cfg['base_url']}/oauth2/token")
    print()
    print("어떻게 진행하시겠습니까?")
    print("  [1] 토큰을 지금 자동 발급하고 본 예제를 이어서 실행")
    print("  [2] 실행 취소 (이후 auth/token_issue.py 를 직접 실행해 발급)")
    print("━" * 72)
    try:
        choice = input("선택 (1/2) [기본=2]: ").strip()
    except (EOFError, KeyboardInterrupt):
        choice = ""

    if choice != "1":
        raise SystemExit(
            "실행 취소 — 다음 명령으로 토큰을 먼저 발급해 주세요:\n"
            "    python examples/auth/token_issue.py"
        )

    print("\n토큰 자동 발급 중...")
    resp, data = issue_token(cfg)
    if not (resp.ok and data.get("access_token")):
        print_response(resp, data, label="접근토큰 발급 (자동)")
        raise SystemExit("토큰 발급 실패 — 본 API 호출 중단")
    print(f"✓ 토큰 발급 완료 — 캐시 저장: {_TOKEN_CACHE}\n")
    return data["access_token"]


# ─────────────────────────────────────────
# REST API 호출
# ─────────────────────────────────────────
def _label_from_path(path: str) -> str:
    """endpoint path 끝 1~2 segment 를 출력 라벨로 사용 (호출자가 label 안 줬을 때)."""
    parts = [p for p in path.split("/") if p]
    return "/".join(parts[-2:]) if len(parts) >= 2 else (parts[-1] if parts else path)


def call_rest(url: str, body: dict | None = None, *,
              cfg: dict | None = None, label: str | None = None,
              method: str = "POST", verbose: bool = False):
    """REST 단건 호출 (JSON body + Bearer 토큰). → (resp, data) 반환.

    함수는 요청만 하고 결과를 반환한다(출력은 호출자 몫). 예제는 보통
    `resp, data = call_rest(...)` 로 받아 `print_response(resp, data)` 로 출력하거나
    `data["Out"][...]` 처럼 값을 추출해서 쓴다. label 미지정 시 url 끝 segment 로 자동 추출.

    verbose:
      · False (기본) → 출력 없음. (resp, data) 만 반환 — 호출자가 직접 출력/가공.
      · True         → 응답 본문 전체 JSON 을 자동 출력(빠른 확인용).

    응답 헤더 cont_yn=='Y' 이면 (= 서버가 더 보낼 데이터가 남았다고 알릴 때)
    verbose=True 에 한해 응답 출력 뒤에 한 줄로 안내를 덧붙여 사용자가
    누락된 데이터의 존재를 인지하고 call_rest_paged() 로 전환할 수 있도록 한다.

    연속조회가 필요하면 call_rest_paged() 를 사용.

    Returns: (resp, data)
    """
    cfg   = cfg or load_config()
    _guard_ov_futopt_demo(cfg)
    token = get_token(cfg)
    label = label or _label_from_path(url)

    resp = requests.request(method, f"{cfg['base_url']}{url}",
        headers={
            "content-type":  "application/json; charset=utf-8",
            "authorization": f"Bearer {token}",
            "cont_yn":       "N",
            "cont_key":      "",
        },
        json=body or {}, timeout=30)
    data = _safe_json(resp)
    if verbose:
        print_response(resp, data, label=label)

    if verbose and resp.headers.get("cont_yn", "N") == "Y":
        next_key = resp.headers.get("cont_key", "")
        if next_key:
            print(
                f"\n→ 연속 데이터 있음 (cont_key={next_key!r}). "
                f"전체를 받으려면 call_rest 대신 call_rest_paged 로 변경해서 사용바랍니다."
            )

    return resp, data


def call_rest_paged(url: str, body: dict | None = None, *,
                    cfg: dict | None = None, label: str | None = None,
                    method: str = "POST", cont_key: str = "",
                    page_sleep: float = 0.5,
                    max_pages: int | str | None = "",
                    verbose: bool = False,
                    progress: bool = True):
    """REST 자동 페이징 — 응답 헤더 cont_yn=='Y' 인 동안 반복 호출. → list[(resp, data)] 반환.

    DB증권 연속조회 프로토콜:
      · 첫 호출: cont_key="" → 헤더 cont_yn=N (처음부터 조회)
                 cont_key="저장된 키" → 헤더 cont_yn=Y (그 키부터 이어받기)
      · 이후 호출: 직전 응답의 cont_key 를 그대로 패스스루, cont_yn=Y
      · 종료: 응답 헤더 cont_yn != "Y" (서버가 더 줄 게 없다는 시그널)

    안전 장치:
      · page_sleep: 0.5초 = 2 TPS 안전선. 1 TPS API 는 1.0 권장.
      · max_pages : 받을 페이지 수 상한. "" (공백) 또는 None = 전체 페이지 조회,
                    정수 N(예: 3) 또는 숫자문자열("3") = 그 페이지 수만큼만 호출.
                    틱/체결처럼 방대한 데이터를 맛보기로 몇 페이지만 받고 싶을 때 사용.

    출력 (데이터 반환과 별개인 진행 피드백):
      · progress=True (기본) → 페이지마다 한 줄 요약(print_summary) + 종료 라인.
                    페이징은 수십~수백 페이지 × page_sleep 로 오래 걸릴 수 있어,
                    멈춘 것처럼 보이지 않도록 진행 상황만 가볍게 표시한다.
      · verbose=True → 페이지마다 본문 JSON 전체 출력 (빠른 확인용, progress 포함).
      · verbose=False, progress=False → 완전 무음 — 반환값만 (프로그래매틱 사용).

    Returns: list[(resp, data), ...] — 각 페이지 호출 결과를 순서대로.
    """
    # max_pages: "" / None → 제한 없음(전체 페이지), 정수·숫자문자열 → 그 페이지 수만큼만
    max_pages = None if max_pages in ("", None) else int(max_pages)
    cfg   = cfg or load_config()
    _guard_ov_futopt_demo(cfg)
    token = get_token(cfg)
    label = label or _label_from_path(url)
    base_headers = {
        "content-type":  "application/json; charset=utf-8",
        "authorization": f"Bearer {token}",
    }

    pages = []
    # cont_key 가 비어 있으면 첫 호출 N (처음부터), 주어졌으면 Y (그 키부터 이어받기)
    cur_yn, cur_key = ("Y", cont_key) if cont_key else ("N", "")
    page_no = 0
    while True:
        page_no += 1
        page_label = f"{label} (p{page_no})"
        resp = requests.request(method, f"{cfg['base_url']}{url}",
            headers={**base_headers, "cont_yn": cur_yn, "cont_key": cur_key},
            json=body or {}, timeout=30)
        data = _safe_json(resp)
        if verbose:
            print_response(resp, data, label=page_label)     # 본문 전체
        elif progress:
            print_summary(resp, data, label=page_label)      # 진행 한 줄 요약
        pages.append((resp, data))

        next_yn  = resp.headers.get("cont_yn", "N")
        next_key = resp.headers.get("cont_key", "")
        if next_yn != "Y":
            if verbose or progress:
                print(f"\n━ 자동 페이징 종료: 총 {page_no} 페이지 (서버 cont_yn={next_yn!r})")
            return pages
        # 무진행 가드: cont_yn='Y' 인데 다음 cont_key 가 비었거나 직전과 동일하면
        # 같은 요청이 무한 반복되므로(서버 이상) 경고 후 중단한다(무한루프 방지).
        if not next_key or next_key == cur_key:
            reason = "비어 있음" if not next_key else f"직전과 동일({cur_key!r})"
            print(f"\n━ 자동 페이징 중단: 서버가 cont_yn='Y' 이나 cont_key 가 {reason} "
                  f"— 무진행으로 판단(총 {page_no} 페이지)")
            return pages
        if max_pages is not None and page_no >= max_pages:
            if verbose or progress:
                print(f"\n━ 자동 페이징 중단: max_pages={max_pages} 상한 도달 "
                      f"(다음 cont_key={next_key!r} 부터 데이터가 더 남음)")
            return pages
        # 안전 상한: max_pages 미지정이어도 폭주 방지(더 받으려면 max_pages 지정).
        if max_pages is None and page_no >= _PAGED_SAFETY_CAP:
            print(f"\n━ 자동 페이징 중단: 안전 상한 {_PAGED_SAFETY_CAP} 페이지 도달 "
                  f"(다음 cont_key={next_key!r} 부터 더 있음). 더 받으려면 max_pages 를 지정하세요.")
            return pages
        if verbose:
            print(f"  → 다음 페이지로 이어감  cont_key={next_key!r}")
        cur_yn, cur_key = "Y", next_key
        time.sleep(page_sleep)


# ─────────────────────────────────────────
# WebSocket 구독
# ─────────────────────────────────────────
# 참고: 계정 단위(주문접수/체결/잔고) 실시간 TR 목록 — 호출 시 tr_type="3" 으로 지정.
# 등록만 있고 해제는 없다 (세션 종료가 곧 해제). tr_key 는 app_key.
# IS0: 국내주식 주문접수, IS1: 국내주식 주문체결, IS2: 해외주식 주문체결,
# IF0: 국내선물옵션 주문체결, O: 해외선물옵션 주문체결, P: 해외선물옵션 잔고.
# 안내용 목록일 뿐, 헬퍼는 tr_type 을 자동판별하지 않습니다(호출자가 직접 지정).
_ACCOUNT_LEVEL_TR_CDS = frozenset({"IS0", "IS1", "IS2", "IF0", "O", "P"})


async def ws_subscribe(tr_cd: str, tr_key: str = "",
                       group_slug: str | None = None,
                       tr_type: str | int = "1",
                       on_message=None) -> None:
    """WebSocket 구독 + 수신 루프 — tr_type 을 호출자가 직접 지정합니다.

    프로토콜 (header.tr_type) — 자동판별하지 않으니 호출 시 명시하세요:
      · "1" = 일반 시세 TR (S00, S01, V60 등) 구독 시작 (기본값)
      · "3" = 계정 단위 TR (IS0/IS1/IS2/IF0/O/P — 주문접수/체결/잔고 등) 계좌등록.
              해제 메시지 없음 (세션 종료가 곧 해제). tr_key 는 app_key.
      · "2" = 일반 시세 구독 해제 (종료 시 헬퍼가 자동 송신)

    동작:
      · group_slug 가 ov_futopt_* 면 7071/17071 포트, 그 외엔 7070/17070
      · 메시지마다 on_message(msg) 호출 (기본 print)
      · Ctrl+C / KeyboardInterrupt 시 시세구독(tr_type="1")만 해제 메시지 송신 후 종료
    """
    import websockets   # 지연 import (REST 만 쓰는 경우 의존성 불필요)

    cfg, token = load_config(), None
    _guard_ov_futopt_demo(cfg, group_slug)
    token = get_token(cfg)
    url = ws_url_for(group_slug, cfg)

    tr_type = str(tr_type).strip()       # "1"/"2"/"3" 또는 1/2/3 정수 허용
    is_account_level = tr_type == "3"    # 계좌등록은 해제 메시지가 없음

    sub_msg = lambda t: json.dumps({
        "header": {"token": token, "tr_type": t},
        "body":   {"tr_cd": tr_cd, "tr_key": tr_key},
    })

    async with websockets.connect(url) as ws:
        await ws.send(sub_msg(tr_type))
        kind = "계좌등록" if is_account_level else "구독 시작"
        print(f"{kind}  tr_cd={tr_cd}  tr_key={tr_key!r}  tr_type={tr_type}  url={url}")
        try:
            while True:
                msg = await ws.recv()
                time.sleep(0.5)   # 메시지 폭주 방지용 (실제 사용 환경에 맞게 조절)
                (on_message or print)(msg)
        except (KeyboardInterrupt, asyncio.CancelledError):
            pass
        except Exception as e:
            # 서버측 정상 종료(ConnectionClosedOK) 등 — traceback 노출 방지
            print(f"\n연결 종료  tr_cd={tr_cd}  reason={type(e).__name__}: {e}")
        finally:
            # 시세구독(tr_type="1")만 명시 해제. 계좌등록("3") 등은 해제 메시지 없음.
            if not is_account_level:
                try:
                    await ws.send(sub_msg("2"))
                except Exception:
                    pass
                print(f"\n구독 해제  tr_cd={tr_cd}  tr_key={tr_key!r}")
            else:
                print(f"\n세션 종료  tr_cd={tr_cd}  tr_key={tr_key!r}")


def run_ws(coro) -> None:
    """WebSocket 코루틴 진입점 — Ctrl+C 를 traceback 없이 처리한다.

    Python 3.13 의 asyncio.run() 은 인터럽트 시 cleanup 후 KeyboardInterrupt 를
    다시 raise 하기 때문에 ws_subscribe 의 finally 가 동작해도 호출 측에 trace 가 노출된다.
    이 wrapper 가 그것을 흡수한다.
    """
    try:
        asyncio.run(coro)
    except KeyboardInterrupt:
        pass


# ─────────────────────────────────────────
# 응답 출력
# ─────────────────────────────────────────
def _build_header(label: str, resp, rsp_cd: str, rsp_msg: str) -> str:
    """출력 첫 줄 — 라벨 + HTTP 상태 + rsp_cd + rsp_msg 한 줄로."""
    head = f"[{label}]  " if label else ""
    rsp_cd_part = f"  rsp_cd={rsp_cd}" if rsp_cd else ""
    return f"{head}HTTP {resp.status_code} {resp.reason}{rsp_cd_part}  {rsp_msg}"


def print_response(resp, data: dict, label: str = "") -> None:
    """단건 응답 출력 — 헤더 라인 + JSON 본문 전체.

    rsp_cd / rsp_msg 키는 표준 응답 외에 OAuth 의 code/message 포맷도 함께 인식.
    """
    rsp_cd  = data.get("rsp_cd") or data.get("code") or ""
    rsp_msg = data.get("rsp_msg") or data.get("message") or data.get("msg") or ""
    print()
    print("━" * 72)
    print(_build_header(label, resp, rsp_cd, rsp_msg))
    print("━" * 72)
    print(json.dumps(data, ensure_ascii=False, indent=2))


def print_summary(resp, data: dict, label: str = "") -> None:
    """한 줄 요약 — 자동 페이징 verbose=False 모드용.

    본문 출력 없이 헤더 + 첫 번째 list 필드 건수 + 다음 cont_key 만 한 줄로.
    """
    rsp_cd  = data.get("rsp_cd") or data.get("code") or ""
    rsp_msg = (data.get("rsp_msg") or data.get("message") or data.get("msg") or "")[:30]
    record = ""
    for k, v in data.items():
        if isinstance(v, list) and v:
            record = f"  {k}:{len(v)}건"
            break
    next_part = (f"  next_key={resp.headers.get('cont_key', '')!r}"
                 if resp.headers.get("cont_yn", "N") == "Y" else "")
    print(_build_header(label, resp, rsp_cd, rsp_msg) + record + next_part)
