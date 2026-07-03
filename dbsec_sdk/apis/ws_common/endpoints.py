"""웹소켓(공통) API 모듈.

DB증권 OpenAPI 그룹: 웹소켓(공통)
group_slug: ws_common

이 파일은 `_specs/ws_common/*.json` 에서 자동 생성되었습니다.
스펙이 갱신되면 `_workspace/build_modules.py`로 재생성하세요.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from dbsec_sdk.client import DBSecClient

from dbsec_sdk.response import APIResponse


class WsCommonAPI:
    """웹소켓(공통) API 모음.

    사용법:
        >>> client = DBSecClient("config.yaml")
        >>> resp = client.apis.ws_common.<method>(...)
    """

    # API 경로 매핑
    PATHS = {
        'ws_session_disconnect': '/api/v1/websocket/disconnectSession',
    }
    # TR 코드 매핑
    TR_CODES = {
        'ws_session_disconnect': 'DisconnectSession',
    }

    def __init__(self, client: 'DBSecClient'):
        self._client = client

    def ws_session_disconnect(
        self,
        *,
        cont_yn: str = 'N',
        cont_key: str = '',
    ) -> APIResponse:
        """웹소켓 세션 초기화 (DisconnectSession).

        접속중인 모든 웹소켓 세션을 초기화 하는 API 입니다. ※ 발급받은 토큰정보와 일치하는 계좌의 세션이 초기화 됩니다.

        엔드포인트: POST /api/v1/websocket/disconnectSession
        유량제어: 1 TPS
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=0140b583-0f93-4aff-897b-e350b3652b40&api_id=cc424a15-7d38-46d6-ab6e-5d46b2b386fc

        Returns:
            APIResponse. 주요 응답 필드:
              - acntNo: 계좌번호 — 웹소켓 세션 초기화를 완료한 계좌번호
              - result: result — 처리 메세지

        """
        body = {
        }
        headers = {'cont_yn': cont_yn, 'cont_key': cont_key}
        return self._client.post(self.PATHS['ws_session_disconnect'], body, extra_headers=headers)
