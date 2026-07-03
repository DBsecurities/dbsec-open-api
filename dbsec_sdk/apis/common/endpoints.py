"""공통 API 모듈.

DB증권 OpenAPI 그룹: 공통
group_slug: common

이 파일은 `_specs/common/*.json` 에서 자동 생성되었습니다.
스펙이 갱신되면 `_workspace/build_modules.py`로 재생성하세요.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from dbsec_sdk.client import DBSecClient

from dbsec_sdk.response import APIResponse


class CommonAPI:
    """공통 API 모음.

    사용법:
        >>> client = DBSecClient("config.yaml")
        >>> resp = client.apis.common.<method>(...)
    """

    # API 경로 매핑
    PATHS = {
        'inquire_issue_groups': '/api/v1/quote/common/group-stocks',
        'inquire_group_list': '/api/v1/quote/common/group-list',
    }
    # TR 코드 매핑
    TR_CODES = {
        'inquire_issue_groups': 'MCJDD88841',
        'inquire_group_list': 'MCJDD88840',
    }

    def __init__(self, client: 'DBSecClient'):
        self._client = client

    def inquire_issue_groups(
        self,
        *,
        usrdiv: str,
        grpno: str,
        cont_yn: str = 'N',
        cont_key: str = '',
    ) -> APIResponse:
        """관심그룹 종목조회 (MCJDD88841).

        관심그룹에 저장된 종목을 조회할 수 있는 API 입니다.

        엔드포인트: POST /api/v1/quote/common/group-stocks
        유량제어: 3 TPS
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=b5b58c45-0066-47ac-8854-67c4d7fb3d32&api_id=c8852378-8a17-41f3-8df5-9b61d633c805

        Args:
            usrdiv: 사용자구분 — "H" 고정
            grpno: 그룹넘버
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. 주요 응답 필드:
              - Out: Out
              - itemcnt: 조회건수
              - grpnm: 그룹명
              - Out1: Out1
              - itmseq: 종목순서
              - itmmk: 종목종류
              - itmcd: 종목코드 — 해외주식의 경우, 시장코드 + 종목코드 형태로 출력됩니다. (ex. "NSAAPL") 맨 앞의 시장코드 2자리를 제거하시고 사용 바랍니다. 관심종목의 해외주식 시장코드는 시세 조회...

        """
        body = {
            'In': {
                'usrdiv': usrdiv,
                'grpno': grpno,
            },
        }
        headers = {'cont_yn': cont_yn, 'cont_key': cont_key}
        return self._client.post(self.PATHS['inquire_issue_groups'], body, extra_headers=headers)

    def inquire_group_list(
        self,
        *,
        usrdiv: str,
        cont_yn: str = 'N',
        cont_key: str = '',
    ) -> APIResponse:
        """관심종목 그룹조회 (MCJDD88840).

        등록된 관심종목 그룹을 조회할 수 있는 API 입니다.

        엔드포인트: POST /api/v1/quote/common/group-list
        유량제어: 2 TPS
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=b5b58c45-0066-47ac-8854-67c4d7fb3d32&api_id=ec733ee3-b8c2-4194-bf9f-af773a9216a3

        Args:
            usrdiv: 사용자구분 — "H" 고정
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. 주요 응답 필드:
              - Out: Out
              - itmcnt: 그룹 내 종목수
              - grpno: 그룹 번호
              - grpnm: 그룹명

        """
        body = {
            'In': {
                'usrdiv': usrdiv,
            },
        }
        headers = {'cont_yn': cont_yn, 'cont_key': cont_key}
        return self._client.post(self.PATHS['inquire_group_list'], body, extra_headers=headers)
