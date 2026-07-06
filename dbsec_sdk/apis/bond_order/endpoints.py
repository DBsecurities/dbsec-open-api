"""장내채권주문 API 모듈.

DB증권 OpenAPI 그룹: 장내채권주문
group_slug: bond_order

이 파일은 `_specs/bond_order/*.json` 에서 자동 생성되었습니다.
스펙이 갱신되면 `_workspace/build_modules.py`로 재생성하세요.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from dbsec_sdk.client import DBSecClient

from dbsec_sdk.response import APIResponse


class BondOrderAPI:
    """장내채권주문 API 모음.

    사용법:
        >>> client = DBSecClient("config.yaml")
        >>> resp = client.apis.bond_order.<method>(...)
    """

    # API 경로 매핑
    PATHS = {
        'bond_order_buy': '/api/v1/trading/krx-bond/order',
        'bond_order_modify': '/api/v1/trading/krx-bond/order-revision',
        'bond_order_cancel': '/api/v1/trading/krx-bond/order-cancel',
        'bond_inquire_executions': '/api/v1/trading/krx-bond/inquiry/transaction-history',
        'bond_inquire_balance': '/api/v1/trading/krx-bond/inquiry/balance',
        'bond_inquire_balance_eval': '/api/v1/trading/krx-bond/inquiry/balance-evalstatus',
    }
    # TR 코드 매핑
    TR_CODES = {
        'bond_order_buy': 'CSPAT02000',
        'bond_order_modify': 'CSPAT02100',
        'bond_order_cancel': 'CSPAT02200',
        'bond_inquire_executions': 'CSPAQ05700',
        'bond_inquire_balance': 'CSPAQ01200',
        'bond_inquire_balance_eval': 'CSPAQ07900',
    }

    def __init__(self, client: 'DBSecClient'):
        self._client = client

    def bond_order_buy(
        self,
        *,
        IsuNo: str,
        OrdQty: int,
        OrdPrc: int,
        BnsTpCode: str,
        BndBuyDt: str,
        TaxchrTpCode: str,
        SmbndEsmtnBnsTpCode: str,
        SmbndMktPtcnTpCode: str,
        LoanDt: str,
        cont_yn: str = 'N',
        cont_key: str = '',
    ) -> APIResponse:
        """채권주문 — 매수/매도 통합 (CSPAT02000).

        DB증권 공식 API 명칭은 '채권매수주문' 이지만, 본 엔드포인트는
        BnsTpCode 로 매수(2) / 매도(1) 를 모두 처리합니다.
        (메서드 이름 bond_order_buy 는 SDK 호환성 위해 유지)

        장내채권 주문 API입니다. ※ 매매시간 : 장내 (09:00 ~ 15:00) ※ 채권은 '금액(원)' 단위로 매매 됩니다.
        주식의 매매단위인 '주' 와 구분됩니다. (예시) DB금융투자 주식 10주 매수 -> DB금융투자 채권 10만원 매수 ※ 최소
        '주문수량' 단위는 1000원 입니다.

        엔드포인트: POST /api/v1/trading/krx-bond/order
        유량제어: 5 TPS
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=4a7257ed-b94a-462e-987d-132f064ed0d3&api_id=d3b2475e-2825-45ba-86de-16bbaa9745e5

        Args:
            IsuNo: 종목번호
            OrdQty: 주문수량
            OrdPrc: 주문가격
            BnsTpCode: 매매구분 — 1:매도 2:매수
            BndBuyDt: 채권매수일 — 채권매수일(매도주문시 입력), 매수시 " " 입력
            TaxchrTpCode: 과세집계구분 — 매수주문시: "" 입력 매도주문시 1:종합과세 2:분리과세
            SmbndEsmtnBnsTpCode: 소액채권종료동시매매구분 — 0:해당없음 1:소액시장참여
            SmbndMktPtcnTpCode: 소액채권시장참여구분 — 0:일반 1:소액
            LoanDt: 대출일자 — 신용구분코드 1 일시 예탁담보대출시 매도주문일자 기본: ""
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. 주요 응답 필드:
              - OrdNo: 주문번호
              - IsuNm: 종목명
              - BnsTpCode: 매매구분 — 매매구분

        """
        body = {
            'In': {
                'IsuNo': IsuNo,
                'OrdQty': OrdQty,
                'OrdPrc': OrdPrc,
                'BnsTpCode': BnsTpCode,
                'BndBuyDt': BndBuyDt,
                'TaxchrTpCode': TaxchrTpCode,
                'SmbndEsmtnBnsTpCode': SmbndEsmtnBnsTpCode,
                'SmbndMktPtcnTpCode': SmbndMktPtcnTpCode,
                'LoanDt': LoanDt,
            },
        }
        headers = {'cont_yn': cont_yn, 'cont_key': cont_key}
        return self._client.post(self.PATHS['bond_order_buy'], body, extra_headers=headers)

    def bond_order_modify(
        self,
        *,
        OrgOrdNo: int,
        IsuNo: str,
        OrdQty: int,
        OrdPrc: int,
        cont_yn: str = 'N',
        cont_key: str = '',
    ) -> APIResponse:
        """채권정정주문 (CSPAT02100).

        채권주문에 대해 정정하는 API 입니다. ※ 이미 체결완료된 주문은 정정이 불가능합니다.

        엔드포인트: POST /api/v1/trading/krx-bond/order-revision
        유량제어: 5 TPS
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=4a7257ed-b94a-462e-987d-132f064ed0d3&api_id=b2530a3f-5576-4185-a128-102ab564fd84

        Args:
            OrgOrdNo: 원주문번호
            IsuNo: 종목번호
            OrdQty: 주문수량
            OrdPrc: 주문가격
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. 주요 응답 필드:
              - OrdNo: 주문번호

        """
        body = {
            'In': {
                'OrgOrdNo': OrgOrdNo,
                'IsuNo': IsuNo,
                'OrdQty': OrdQty,
                'OrdPrc': OrdPrc,
            },
        }
        headers = {'cont_yn': cont_yn, 'cont_key': cont_key}
        return self._client.post(self.PATHS['bond_order_modify'], body, extra_headers=headers)

    def bond_order_cancel(
        self,
        *,
        OrgOrdNo: int,
        IsuNo: str,
        OrdQty: int,
        cont_yn: str = 'N',
        cont_key: str = '',
    ) -> APIResponse:
        """채권취소주문 (CSPAT02200).

        채권주문에 대해 취소하는 API 입니다. ※ 이미 체결완료된 주문은 취소가 불가능합니다.

        엔드포인트: POST /api/v1/trading/krx-bond/order-cancel
        유량제어: 5 TPS
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=4a7257ed-b94a-462e-987d-132f064ed0d3&api_id=0b1608cd-d704-467d-88d4-9dabd7ceaaf3

        Args:
            OrgOrdNo: 원주문번호
            IsuNo: 종목번호
            OrdQty: 주문수량
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. 주요 응답 필드:
              - OrdNo: 주문번호

        """
        body = {
            'In': {
                'OrgOrdNo': OrgOrdNo,
                'IsuNo': IsuNo,
                'OrdQty': OrdQty,
            },
        }
        headers = {'cont_yn': cont_yn, 'cont_key': cont_key}
        return self._client.post(self.PATHS['bond_order_cancel'], body, extra_headers=headers)

    def bond_inquire_executions(
        self,
        *,
        PrdtExecTpCode: str,
        BnsTpCode: str,
        BndIsuNo: str,
        OrdDt: str,
        cont_yn: str = 'N',
        cont_key: str = '',
    ) -> APIResponse:
        """채권주문체결조회 (CSPAQ05700).

        채권주문체결 조회 API 입니다.

        엔드포인트: POST /api/v1/trading/krx-bond/inquiry/transaction-history
        유량제어: 2 TPS
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=4a7257ed-b94a-462e-987d-132f064ed0d3&api_id=f0b45051-2960-4101-a4ad-352fc28d6383

        Args:
            PrdtExecTpCode: 체결구분 — 0. 전체 1. 체결 2. 미체결
            BnsTpCode: 매매구분 — 1:매도 2:매수
            BndIsuNo: 채권종목번호
            OrdDt: 주문일
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. 주요 응답 필드:
              - Out1: Out1
              - IsuNm: 종목명
              - SmbndBnsTrdObjCode: 소액채권매매거래대상코드 — 00 : 일반채권 01 : 소액채권 02 : CB(전환사채)
              - ThdayOrdNo: 당일주문번호
              - OrgOrdNo: 원주문번호
              - OrdQty: 주문수량
              - OrdPrc: 주문가격
              - TaxchrTpNm: 과세구분명
              - OrdTrxPtnCode: 주문처리유형코드 — 0:정상, 6:정정확인, 8:취소확인
              - BuyDt: 매수일
              - ExecQty: 체결수량
              - ExecPrc: 체결가
              - ErnRat: 수익율
              - BndIsuNo: 채권종목번호
              - AllExecQty: 전체체결수량
              - (이하 생략 — 가이드 참조)

        """
        body = {
            'In': {
                'PrdtExecTpCode': PrdtExecTpCode,
                'BnsTpCode': BnsTpCode,
                'BndIsuNo': BndIsuNo,
                'OrdDt': OrdDt,
            },
        }
        headers = {'cont_yn': cont_yn, 'cont_key': cont_key}
        return self._client.post(self.PATHS['bond_inquire_executions'], body, extra_headers=headers)

    def bond_inquire_balance(
        self,
        *,
        cont_yn: str = 'N',
        cont_key: str = '',
    ) -> APIResponse:
        """채권잔고조회 (CSPAQ01200).

        채권 잔고조회 API입니다.

        엔드포인트: POST /api/v1/trading/krx-bond/inquiry/balance
        유량제어: 2 TPS
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=4a7257ed-b94a-462e-987d-132f064ed0d3&api_id=e12626bf-b1ab-4bbe-aeac-43dad091f91a

        Returns:
            APIResponse. 주요 응답 필드:
              - Out: Out
              - IsuNo: 종목번호
              - IsuNm: 종목명
              - BuyDt: 매수일
              - OrdAbleQty: 주문가능수량
              - SellOrdQty: 매도주문수량
              - BalQty: 채권잔고수량
              - UseRestrcQty: 사용제한수량
              - LoanDt: 대출일
              - DueDt: 만기일자
              - LoanQty: 대출수량
              - LoanRfundQty: 대출상환수량
              - BuyPrc: 매수가

        """
        body = {
            'In': {},
        }
        headers = {'cont_yn': cont_yn, 'cont_key': cont_key}
        return self._client.post(self.PATHS['bond_inquire_balance'], body, extra_headers=headers)

    def bond_inquire_balance_eval(
        self,
        *,
        D2balBaseQryTp: str,
        OtptPtnTpCode: str,
        cont_yn: str = 'N',
        cont_key: str = '',
    ) -> APIResponse:
        """채권잔고평가조회 (CSPAQ07900).

        채권 잔고평가조회 API입니다.

        엔드포인트: POST /api/v1/trading/krx-bond/inquiry/balance-evalstatus
        유량제어: 2 TPS
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=4a7257ed-b94a-462e-987d-132f064ed0d3&api_id=a0b85223-af82-4b88-a31e-9762c003eaac

        Args:
            D2balBaseQryTp: D+2잔고기준조회구분 — 0:전부조회 1:D+2잔고 0이상만 조회
            OtptPtnTpCode: 출력유형구분 — 0:상장폐지종목 출력 1:상장폐지종목 제외
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. 주요 응답 필드:
              - Out: Out
              - IsuNo: 종목번호
              - IsuNm: 종목명
              - RegMktCode: 등록시장코드 — 00:비상장 10:유가증권 20:코스닥 30:프리보드
              - BalQty: 잔고수량
              - EvalAmt: 평가금액
              - BnsBaseBalQty: 매매기준잔고수량
              - SecBalPtnCode: 유가증권잔고유형코드 — 00:보통 01:채권 02:코스피선물대용 03:코스닥선물대용 04:주식옵션선물대용 05:CD/CP 10:채권
              - SecBalPtnNm: 유가증권잔고유형명
              - CrdayBuyExecQty: 금일매수체결수량
              - CrdaySellExecQty: 금일매도체결수량
              - SellPrc: 매도가
              - BuyPrc: 매수가
              - SellPnlAmt: 매도손익금액
              - PnlRat: 손익률
              - (이하 생략 — 가이드 참조)

        """
        body = {
            'In': {
                'D2balBaseQryTp': D2balBaseQryTp,
                'OtptPtnTpCode': OtptPtnTpCode,
            },
        }
        headers = {'cont_yn': cont_yn, 'cont_key': cont_key}
        return self._client.post(self.PATHS['bond_inquire_balance_eval'], body, extra_headers=headers)
