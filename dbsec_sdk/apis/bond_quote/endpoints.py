"""장내채권시세 API 모듈.

DB증권 OpenAPI 그룹: 장내채권시세
group_slug: bond_quote

이 파일은 `_specs/bond_quote/*.json` 에서 자동 생성되었습니다.
스펙이 갱신되면 `_workspace/build_modules.py`로 재생성하세요.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from dbsec_sdk.client import DBSecClient

from dbsec_sdk.response import APIResponse


class BondQuoteAPI:
    """장내채권시세 API 모음.

    사용법:
        >>> client = DBSecClient("config.yaml")
        >>> resp = client.apis.bond_quote.<method>(...)
    """

    # API 경로 매핑
    PATHS = {
        'bond_search_detail': '/api/v1/quote/krx-bond/search',
        'bond_inquire_price': '/api/v1/quote/krx-bond/inquiry/price',
        'bond_inquire_orderbook': '/api/v1/quote/krx-bond/inquiry/orderbook',
    }
    # TR 코드 매핑
    TR_CODES = {
        'bond_search_detail': 'BO_SEARCH',
        'bond_inquire_price': 'BO_SISE',
        'bond_inquire_orderbook': 'BO_HOGA',
    }

    def __init__(self, client: 'DBSecClient'):
        self._client = client

    def bond_search_detail(
        self,
        *,
        InputSerhName: str,
        InputBondStndIscd: str,
        InputCrdtClsCode: str,
        InputDivClsCode: str,
        InputRmnnDynu1: str,
        InputCompDiviType: str,
        InputCntgErt1: str,
        cont_yn: str = 'N',
        cont_key: str = '',
    ) -> APIResponse:
        """장내채권 상세검색 (BO_SEARCH).

        장내채권 상세검색 API 입니다.

        엔드포인트: POST /api/v1/quote/krx-bond/search
        유량제어: 2 TPS
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=b86989c1-9666-42d2-a446-492376f71f1b&api_id=ed6b9416-bd89-4c99-9a8a-7599f0e14474

        Args:
            InputSerhName: 입력검색명 — 기본값: "" 종목명으로 검색 가능 EX. 국고
            InputBondStndIscd: 입력채권구분코드 — 0:채권종류(전체) 1:국채 2:지방채 3:회사채 4:특수채 5:금융채 6:일반사채 7:주식관련사채
            InputCrdtClsCode: 입력신용구분코드 — 0:신용등급(전체) 1:AAA+ ~ AAA- 2:AA+ ~ AA- 3:A+ ~ A- 4:BBB+ ~ BBB- 5:BBB- 미만 6:없음
            InputDivClsCode: 입력분류구분코드 — 0:이자종류(전체) 1:할인채 2:복리채 3:단리채 4:이표채
            InputRmnnDynu1: 입력잔존일수1 — 0:잔존기간(전체) 1:6개월 내 2:6개월~1년 3:1년~2년 4:2년~3년
            InputCompDiviType: 입력비교구분코드 — 0: 수익률조건 전체 1:이상 2:이하
            InputCntgErt1: 입력수익률1 — 수익률 입력 (정수만 입력가능) EX. 3
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. 주요 응답 필드:
              - Out: Out
              - StndIscd: 표준종목코드
              - KorIsnm: 한글종목명
              - BondClsName: 채권구분명
              - CrdtVltnGrad1: 신용평가등급1
              - IntKindName: 이자지급방법
              - Prpr: 현재가
              - PrdyVrss: 전일대비
              - PrdyVrssSign: 전일대비부호
              - BondCntgErt: 체결수익률
              - RdmpDate: 상환일
              - SrfcMnrt: 표면금리

        """
        body = {
            'In': {
                'InputSerhName': InputSerhName,
                'InputBondStndIscd': InputBondStndIscd,
                'InputCrdtClsCode': InputCrdtClsCode,
                'InputDivClsCode': InputDivClsCode,
                'InputRmnnDynu1': InputRmnnDynu1,
                'InputCompDiviType': InputCompDiviType,
                'InputCntgErt1': InputCntgErt1,
            },
        }
        headers = {'cont_yn': cont_yn, 'cont_key': cont_key}
        return self._client.post(self.PATHS['bond_search_detail'], body, extra_headers=headers)

    def bond_inquire_price(
        self,
        *,
        InputCondMrktDivCode: str,
        InputIscd1: str,
        cont_yn: str = 'N',
        cont_key: str = '',
    ) -> APIResponse:
        """장내채권 현재가조회 (BO_SISE).

        엔드포인트: POST /api/v1/quote/krx-bond/inquiry/price
        유량제어: 2 TPS
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=b86989c1-9666-42d2-a446-492376f71f1b&api_id=106586fa-701b-49f8-9d21-eefe8b81e1a6

        Args:
            InputCondMrktDivCode: 입력조건시장분류코드 — 소액:SB 일반:B
            InputIscd1: 입력종목코드1 — 채권 종목코드 입력
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. 주요 응답 필드:
              - Prpr: 현재가
              - PrdyVrss: 전일대비
              - PrdyVrssSign: 전일대비부호
              - PrdyCtrt: 전일대비율
              - AcmlVol: 누적거래량
              - PrdyErt: 전일수익률
              - Mxpr: 상한가
              - Llam: 하한가
              - PrdyClpr: 전일종가

        """
        body = {
            'In': {
                'InputCondMrktDivCode': InputCondMrktDivCode,
                'InputIscd1': InputIscd1,
            },
        }
        headers = {'cont_yn': cont_yn, 'cont_key': cont_key}
        return self._client.post(self.PATHS['bond_inquire_price'], body, extra_headers=headers)

    def bond_inquire_orderbook(
        self,
        *,
        InputCondMrktDivCode: str,
        InputIscd1: str,
        cont_yn: str = 'N',
        cont_key: str = '',
    ) -> APIResponse:
        """장내채권 호가 조회 (BO_HOGA).

        장내채권 호가조회 API 입니다.

        엔드포인트: POST /api/v1/quote/krx-bond/inquiry/orderbook
        유량제어: 2 TPS
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=b86989c1-9666-42d2-a446-492376f71f1b&api_id=1bf5ef83-606b-4b5d-a129-8a35e503aeee

        Args:
            InputCondMrktDivCode: 입력조건시장분류코드 — 소액:SB 일반:B
            InputIscd1: 입력종목코드1 — 채권 종목코드 입력
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. 주요 응답 필드:
              - Askp1: 매도호가1
              - Askp2: 매도호가2
              - Askp3: 매도호가3
              - Askp4: 매도호가4
              - Askp5: 매도호가5
              - Bidp1: 매수호가1
              - Bidp2: 매수호가2
              - Bidp3: 매수호가3
              - Bidp4: 매수호가4
              - Bidp5: 매수호가5
              - AskpRsqn1: 매도호가잔량1
              - AskpRsqn2: 매도호가잔량2
              - AskpRsqn3: 매도호가잔량3
              - AskpRsqn4: 매도호가잔량4
              - AskpRsqn5: 매도호가잔량5
              - (이하 생략 — 가이드 참조)

        """
        body = {
            'In': {
                'InputCondMrktDivCode': InputCondMrktDivCode,
                'InputIscd1': InputIscd1,
            },
        }
        headers = {'cont_yn': cont_yn, 'cont_key': cont_key}
        return self._client.post(self.PATHS['bond_inquire_orderbook'], body, extra_headers=headers)
