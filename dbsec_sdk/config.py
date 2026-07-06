"""설정 관리 모듈.

DB증권 Open API 클라이언트에 필요한 모든 설정을 관리합니다.
설정 우선순위: YAML 파일 → 환경변수 → 기본값

사용법:
    # YAML 파일로 설정
    config = Config("config.yaml")

    # 환경변수로 설정 (YAML 없이)
    # DBSEC_PRD_APP_KEY/SECRET, DBSEC_VTL_APP_KEY/SECRET, DBSEC_MODE 등을 설정.
    config = Config()
"""

from __future__ import annotations

import os
from pathlib import Path

import yaml
from dotenv import load_dotenv


# ──────────────────────────────────────────────
# 기본 URL 상수
# REST API는 운영/모의 동일 (앱 속성으로 내부 분기)
# WebSocket은 포트가 다름 + 해외선물옵션은 별도 포트(7071) — 운영 전용
# (해외선물옵션은 DB증권 시스템 자체가 모의투자 미지원)
# ──────────────────────────────────────────────
_DEFAULT_BASE_URL = "https://openapi.dbsec.co.kr:8443"
_WS_URLS = {
    "production":            "wss://openapi.dbsec.co.kr:7070/websocket",
    "demo":                  "wss://openapi.dbsec.co.kr:17070/websocket",
    "production_ov_futopt":  "wss://openapi.dbsec.co.kr:7071/websocket",
}

# 해외선물옵션 그룹 슬러그 (전용 WebSocket 포트 사용, 운영 전용)
_OV_FUTOPT_GROUPS = {"ov_futopt_order", "ov_futopt_quote", "ov_futopt_realtime"}


class Config:
    """DB증권 API 설정 클래스.

    REST API URL은 운영/모의투자 동일합니다. APP_KEY/SECRET 은 mode 에 따라
    config.yaml 의 prd_* 또는 vtl_* 키 중 하나가 자동 선택됩니다.

    Args:
        config_path: config.yaml 파일 경로. None이면 환경변수만 사용.

    Attributes:
        app_key: API 인증용 앱 키 (mode 에 따라 prd/vtl 자동 선택)
        app_secret: API 인증용 앱 시크릿
        base_url: REST API 기본 URL
        mode: 실행 모드 ("production" 또는 "demo")
        ws_url: WebSocket URL (일반 그룹용, mode 에 따라 자동 결정)
    """

    def __init__(self, config_path: str | Path | None = None):
        # .env 파일이 있으면 환경변수로 로드
        load_dotenv()

        # 설정 파일 경로 보관 (안내 메시지 등에 사용) — 환경변수만 쓰면 None
        self._config_path: Path | None = Path(config_path) if config_path else None

        # YAML 설정 데이터 로드
        self._data: dict = {}
        if self._config_path and self._config_path.exists():
            with open(self._config_path, encoding="utf-8") as f:
                self._data = yaml.safe_load(f) or {}

    @property
    def config_path(self) -> Path | None:
        """로드한 config.yaml 경로 (환경변수만 사용한 경우 None)."""
        return self._config_path

    # ──────────────────────────────────────────
    # 인증 정보
    # ──────────────────────────────────────────

    @property
    def app_key(self) -> str:
        """현재 mode 에 맞는 APP_KEY 반환.

        - mode == "demo"       → auth.vtl_app_key  (env: DBSEC_VTL_APP_KEY)
        - mode == "production" → auth.prd_app_key  (env: DBSEC_PRD_APP_KEY)
        """
        if self.mode == "demo":
            return self._get("auth", "vtl_app_key", env="DBSEC_VTL_APP_KEY")
        return self._get("auth", "prd_app_key", env="DBSEC_PRD_APP_KEY")

    @property
    def app_secret(self) -> str:
        """현재 mode 에 맞는 APP_SECRET 반환.

        - mode == "demo"       → auth.vtl_app_secret  (env: DBSEC_VTL_APP_SECRET)
        - mode == "production" → auth.prd_app_secret  (env: DBSEC_PRD_APP_SECRET)
        """
        if self.mode == "demo":
            return self._get("auth", "vtl_app_secret", env="DBSEC_VTL_APP_SECRET")
        return self._get("auth", "prd_app_secret", env="DBSEC_PRD_APP_SECRET")

    # ──────────────────────────────────────────
    # 접속 환경
    # ──────────────────────────────────────────

    @property
    def base_url(self) -> str:
        """REST API 기본 URL. 운영/모의투자 동일."""
        return self._get("environment", "base_url", env="DBSEC_BASE_URL", default=_DEFAULT_BASE_URL)

    @property
    def mode(self) -> str:
        """실행 모드. "production"(운영) 또는 "demo"(모의투자).
        이 값은 APP_KEY 선택과 WebSocket 포트 선택에 영향을 미칩니다.
        REST API URL 자체는 mode 와 무관하게 동일합니다.

        Raises:
            ValueError: "demo"/"production" 이외의 값(오타·대소문자 포함)인 경우.
                검증 없이 두면 오타 시 REST 는 실전(prd) 앱키로, WebSocket 은 demo 로
                엇갈려 폴백돼 '모의라고 믿고 실주문'이 나갈 수 있어 명시적으로 차단한다.
        """
        mode = self._get("environment", "mode", env="DBSEC_MODE", default="demo").strip()
        if mode not in ("demo", "production"):
            raise ValueError(
                f"잘못된 mode 값입니다: {mode!r}. "
                "environment.mode(또는 DBSEC_MODE)는 \"demo\"(모의투자) 또는 "
                "\"production\"(실전) 이어야 합니다 — 대소문자·오타 주의 "
                "(예: \"Demo\", \"prod\", \"real\", \"test\" 는 허용되지 않습니다)."
            )
        return mode

    @property
    def ws_url(self) -> str:
        """WebSocket URL (일반 그룹).

        해외선물옵션 그룹(ov_futopt_*)은 다른 포트를 쓰므로 ws_url_for() 사용.

        - production: wss://openapi.dbsec.co.kr:7070/websocket
        - demo:       wss://openapi.dbsec.co.kr:17070/websocket
        """
        return self.ws_url_for(group_slug=None)

    def ws_url_for(self, group_slug: str | None) -> str:
        """그룹별 WebSocket URL 반환.

        - 해외선물옵션(ov_futopt_*): production=7071 (모의투자 미지원 — DB증권 시스템 제약)
        - 그 외:                       production=7070, demo=17070
        """
        is_ov_futopt = group_slug in _OV_FUTOPT_GROUPS
        if is_ov_futopt and self.mode != "production":
            raise ValueError(
                f"해외선물옵션({group_slug})은 모의투자 미지원입니다 — "
                "DB증권 시스템 자체가 ov_futopt_* 그룹의 demo 환경을 제공하지 않습니다. "
                "config.yaml 의 environment.mode 를 \"production\" 으로 변경하고 "
                "실전투자 앱키(prd_app_key/prd_app_secret)를 사용하세요."
            )
        if self.mode == "production":
            key = "ws_production_ov_futopt" if is_ov_futopt else "ws_production"
            default = _WS_URLS["production_ov_futopt"] if is_ov_futopt else _WS_URLS["production"]
        else:
            key = "ws_demo"
            default = _WS_URLS["demo"]
        return self._get("environment", key, default=default)

    # ──────────────────────────────────────────
    # 내부 헬퍼
    # ──────────────────────────────────────────

    def _get(self, section: str, key: str, env: str | None = None, default: str = "") -> str:
        """설정값 조회. 우선순위: YAML → 환경변수 → 기본값.

        Args:
            section: YAML 최상위 섹션 (예: "auth", "environment")
            key: 섹션 내 키 (예: "prd_app_key")
            env: 대응하는 환경변수명 (예: "DBSEC_PRD_APP_KEY")
            default: YAML과 환경변수 모두 없을 때 반환할 기본값
        """
        # 1) YAML 파일에서 조회
        val = self._data.get(section, {}).get(key)
        if val is not None:
            return str(val)
        # 2) 환경변수에서 조회
        if env:
            val = os.getenv(env)
            if val is not None:
                return val
        # 3) 기본값 반환
        return default
