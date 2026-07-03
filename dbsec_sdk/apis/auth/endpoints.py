"""OAuth 인증 API 모듈.

DB증권 OpenAPI 그룹: OAuth 인증
group_slug: auth

이 파일은 `_specs/auth/*.json` 에서 자동 생성되었습니다.
스펙이 갱신되면 `_workspace/build_modules.py`로 재생성하세요.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from dbsec_sdk.client import DBSecClient

from dbsec_sdk.response import APIResponse


class AuthAPI:
    """OAuth 인증 API 모음.

    사용법:
        >>> client = DBSecClient("config.yaml")
        >>> resp = client.apis.auth.<method>(...)
    """

    # API 경로 매핑
    PATHS = {
        'token_issue': '/oauth2/token',
        'token_revoke': '/oauth2/revoke',
    }
    # TR 코드 매핑
    TR_CODES = {
        'token_issue': 'token',
        'token_revoke': 'revoke',
    }

    def __init__(self, client: 'DBSecClient'):
        self._client = client

    def token_issue(
        self,
        *,
        grant_type: str,
        appkey: str,
        appsecretkey: str,
        scope: str,
        cont_yn: str = 'N',
        cont_key: str = '',
    ) -> APIResponse:
        """접근토큰 발급 (token).

        본인을 인증하는 확인 절차로, 접근 토큰을 부여받아 오픈 API 활용이 가능합니다. ※ API호출 유량은 1분에 1건 입니다. ※
        접근토큰 유효기간 개인/법인 : 신청일시로부터 24시간 ※ 유효기간 만료 전 토큰을 발급을 하는경우, 동일한 토큰이 발급됩니다.
        (만료기간도 동일) 유효기간 만료 전 새 토큰이 필요한 경우 접근토큰 폐기 후 발급 부탁드립니다.

        엔드포인트: POST /oauth2/token
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=cc55b867-e049-421b-a798-be016370ff44&api_id=9e3097ab-7d39-4433-8002-00649604f0de

        Args:
            grant_type: 권한부여 Type — "client_credentials" 고정
            appkey: 고객 앱Key — 포탈에서 발급된 고객의 앱Key
            appsecretkey: 고객 앱 비밀Key — 포탈에서 발급된 고객의 앱 비밀Key
            scope: scope — "oob" 고정
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. 주요 응답 필드:
              - token: 접근토큰 — G/W 에서 발급하는 접근토큰
              - expire_in: 접근토큰 유효기간 — 유효기간(초)
              - scope: scope — "oob"
              - token_type: 토큰 유형 — Bearer

        """
        body = {
            'grant_type': grant_type,
            'appkey': appkey,
            'appsecretkey': appsecretkey,
            'scope': scope,
        }
        headers = {'cont_yn': cont_yn, 'cont_key': cont_key}
        return self._client.post(self.PATHS['token_issue'], body, extra_headers=headers)

    def token_revoke(
        self,
        *,
        appkey: str,
        appsecretkey: str,
        token_type_hint: str,
        token: str,
        cont_yn: str = 'N',
        cont_key: str = '',
    ) -> APIResponse:
        """접근토큰 폐기 (revoke).

        발급받은 접근토큰을 더 이상 활용하지 않을 때 사용합니다.

        엔드포인트: POST /oauth2/revoke
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=cc55b867-e049-421b-a798-be016370ff44&api_id=3395b34c-f48c-436f-a5fa-dbae6b224af8

        Args:
            appkey: 고객 앱Key — 포탈에서 발급된 고객의 앱Key
            appsecretkey: 고객 앱 비밀Key — 포탈에서 발급된 고객의 앱 비밀Key
            token_type_hint: 토큰 유형 hint — access_token, refresh_token 토큰 타입
            token: 접근토큰
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. 주요 응답 필드:
              - code: 응답코드
              - msg: 응답메세지

        """
        body = {
            'appkey': appkey,
            'appsecretkey': appsecretkey,
            'token_type_hint': token_type_hint,
            'token': token,
        }
        headers = {'cont_yn': cont_yn, 'cont_key': cont_key}
        return self._client.post(self.PATHS['token_revoke'], body, extra_headers=headers)
