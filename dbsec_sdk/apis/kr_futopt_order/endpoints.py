"""국내선물옵션주문 API 모듈.

DB증권 OpenAPI 그룹: 국내선물옵션주문
group_slug: kr_futopt_order

이 파일은 `_specs/kr_futopt_order/*.json` 에서 자동 생성되었습니다.
스펙이 갱신되면 `_workspace/build_modules.py`로 재생성하세요.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from dbsec_sdk.client import DBSecClient

from dbsec_sdk.response import APIResponse


class KrFutoptOrderAPI:
    """국내선물옵션주문 API 모음.

    사용법:
        >>> client = DBSecClient("config.yaml")
        >>> resp = client.apis.kr_futopt_order.<method>(...)
    """

    # API 경로 매핑
    PATHS = {
        'kr_futopt_order': '/api/v1/trading/kr-futureoption/order',
        'kr_futopt_order_modify': '/api/v1/trading/kr-futureoption/order-revision',
        'kr_futopt_order_cancel': '/api/v1/trading/kr-futureoption/order-cancel',
        'kr_futopt_inquire_executions': '/api/v1/trading/kr-futureoption/inquiry/transaction-history',
        'kr_futopt_inquire_psbl_quantity': '/api/v1/trading/kr-futureoption/inquiry/able-orderqty',
        'kr_futopt_inquire_balance': '/api/v1/trading/kr-futureoption/inquiry/balance',
        'kr_futopt_inquire_balance_eval': '/api/v1/trading/kr-futureoption/inquiry/balance-evalstatus',
        'kr_futopt_inquire_realized_pnl': '/api/v1/trading/kr-futureoption/inquiry/day-rlzpnl',
        'kr_futopt_inquire_estimated_deposit': '/api/v1/trading/kr-futureoption/inquiry/deposit-detail',
        'kr_futopt_order_night': '/api/v1/trading/night-futureoption/order',
        'kr_futopt_order_modify_night': '/api/v1/trading/night-futureoption/order-revision',
        'kr_futopt_order_cancel_night': '/api/v1/trading/night-futureoption/order-cancel',
        'kr_futopt_inquire_executions_night': '/api/v1/trading/night-futureoption/inquiry/cmedt',
        'kr_futopt_inquire_balance_night': '/api/v1/trading/night-futureoption/inquiry/balance',
    }
    # TR 코드 매핑
    TR_CODES = {
        'kr_futopt_order': 'CFOAT00100',
        'kr_futopt_order_modify': 'CFOAT00200',
        'kr_futopt_order_cancel': 'CFOAT00300',
        'kr_futopt_inquire_executions': 'CFOAQ04000',
        'kr_futopt_inquire_psbl_quantity': 'CFOAQ42400',
        'kr_futopt_inquire_balance': 'CFOAQ02500',
        'kr_futopt_inquire_balance_eval': 'CFOAQ50100',
        'kr_futopt_inquire_realized_pnl': 'CFOAQ02600',
        'kr_futopt_inquire_estimated_deposit': 'CFOEQ11100',
        'kr_futopt_order_night': 'CFOHT00100',
        'kr_futopt_order_modify_night': 'CFOHT00200',
        'kr_futopt_order_cancel_night': 'CFOHT00300',
        'kr_futopt_inquire_executions_night': 'CFOHQ04000',
        'kr_futopt_inquire_balance_night': 'CFOHQ02500',
    }

    def __init__(self, client: 'DBSecClient'):
        self._client = client

    def kr_futopt_order(
        self,
        *,
        FnoIsuNo: str,
        BnsTpCode: str,
        FnoOrdprcPtnCode: str,
        OrdPrc: int,
        OrdQty: int,
        cont_yn: str = 'N',
        cont_key: str = '',
    ) -> APIResponse:
        """선물옵션 주문 (CFOAT00100).

        국내선물옵션 주문이 가능한 API입니다. ※ 모의투자 계좌로 사용가능한 API입니다. ※ 모의투자 주문 시 "지정가, 시장가,
        최유리지정가" 주문 유형만 입력 가능합니다. ※ 수수료 및 제세금 안내는 아래 링크 참고 부탁드립니다.
        https://www.dbsec.co.kr/custcenter/jobservice/cu_FeeTrading_viw10.do ※
        선물옵션 거래제도 안내는 아래 링크 참고 부탁드립니다. https://www.dbsec.co.kr/custcenter/jobservice/cu_TradeFuture_viw.do

        엔드포인트: POST /api/v1/trading/kr-futureoption/order
        유량제어: 10 TPS
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=44c4a04f-f55e-4c1c-b4e2-b48ec4869aee&api_id=5ca0a623-4424-4515-a9b9-1e736ea2be92

        Args:
            FnoIsuNo: 선물옵션종목번호 — 선물옵션 종목 코드 입력 선물 EX) 211V2060 옵션 EX) 201V2347
            BnsTpCode: 매매구분 — 1:매도 2:매수
            FnoOrdprcPtnCode: 선물옵션호가유형코드 — 00:지정가 03:시장가 05:조건부지정가 06:최유리지정가 10:지정가(IOC) 20:지정가(FOK) 13:시장가(IOC) 23:시장가(FOK) 16:최유리지정가(IOC) 26:최유리지정가(FOK)
            OrdPrc: 주문가격
            OrdQty: 주문수량
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. 주요 응답 필드:
              - OrdNo: 주문번호
              - IsuNm: 종목명

        """
        body = {
            'In': {
                'FnoIsuNo': FnoIsuNo,
                'BnsTpCode': BnsTpCode,
                'FnoOrdprcPtnCode': FnoOrdprcPtnCode,
                'OrdPrc': OrdPrc,
                'OrdQty': OrdQty,
            },
        }
        headers = {'cont_yn': cont_yn, 'cont_key': cont_key}
        return self._client.post(self.PATHS['kr_futopt_order'], body, extra_headers=headers)

    def kr_futopt_order_modify(
        self,
        *,
        FnoIsuNo: str,
        OrgOrdNo: int,
        FnoOrdprcPtnCode: str,
        OrdPrc: float,
        MdfyQty: int,
        cont_yn: str = 'N',
        cont_key: str = '',
    ) -> APIResponse:
        """선물옵션 정정주문 (CFOAT00200).

        선물옵션 주문에 대해 정정하는 API 입니다. ※ 모의투자 계좌로 사용가능한 API입니다. ※ 이미 체결완료된 주문은 정정이
        불가능합니다.

        엔드포인트: POST /api/v1/trading/kr-futureoption/order-revision
        유량제어: 10 TPS
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=44c4a04f-f55e-4c1c-b4e2-b48ec4869aee&api_id=26a01517-ed97-4bf9-a66f-eb4be7abb87f

        Args:
            FnoIsuNo: 선물옵션종목번호 — 선물옵션 종목 코드 입력 선물 EX) 211V2060 옵션 EX) 201V2347
            OrgOrdNo: 원주문번호
            FnoOrdprcPtnCode: 선물옵션호가유형코드 — 00:지정가 03:시장가 05:조건부지정가 06:최유리지정가 10:지정가(IOC) 20:지정가(FOK)
            OrdPrc: 주문가격
            MdfyQty: 정정수량
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. 주요 응답 필드:
              - OrdNo: 주문번호
              - IsuNm: 종목명

        """
        body = {
            'In': {
                'FnoIsuNo': FnoIsuNo,
                'OrgOrdNo': OrgOrdNo,
                'FnoOrdprcPtnCode': FnoOrdprcPtnCode,
                'OrdPrc': OrdPrc,
                'MdfyQty': MdfyQty,
            },
        }
        headers = {'cont_yn': cont_yn, 'cont_key': cont_key}
        return self._client.post(self.PATHS['kr_futopt_order_modify'], body, extra_headers=headers)

    def kr_futopt_order_cancel(
        self,
        *,
        FnoIsuNo: str,
        OrgOrdNo: int,
        CancQty: int,
        cont_yn: str = 'N',
        cont_key: str = '',
    ) -> APIResponse:
        """선물옵션 취소주문 (CFOAT00300).

        선물옵션 주문에 대해 취소하는 API 입니다. ※ 모의투자 계좌로 사용가능한 API입니다. ※ 이미 체결완료된 주문은 취소가
        불가능합니다.

        엔드포인트: POST /api/v1/trading/kr-futureoption/order-cancel
        유량제어: 10 TPS
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=44c4a04f-f55e-4c1c-b4e2-b48ec4869aee&api_id=d478ab5d-4e4b-4003-bb6b-d4f38dd487d1

        Args:
            FnoIsuNo: 선물옵션종목번호 — 선물옵션 종목 코드 입력 선물 EX) 211V2060 옵션 EX) 201V2347
            OrgOrdNo: 원주문번호
            CancQty: 취소수량
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. 주요 응답 필드:
              - OrdNo: 주문번호
              - IsuNm: 종목명

        """
        body = {
            'In': {
                'FnoIsuNo': FnoIsuNo,
                'OrgOrdNo': OrgOrdNo,
                'CancQty': CancQty,
            },
        }
        headers = {'cont_yn': cont_yn, 'cont_key': cont_key}
        return self._client.post(self.PATHS['kr_futopt_order_cancel'], body, extra_headers=headers)

    def kr_futopt_inquire_executions(
        self,
        *,
        ExecTpCode: str,
        BnsTpCode: str,
        IsuTpCode: str,
        FnoIsuNo: str,
        cont_yn: str = 'N',
        cont_key: str = '',
    ) -> APIResponse:
        """선물옵션 체결조회 (CFOAQ04000).

        선물옵션 주문의 체결 여부 조회가 가능한 API 입니다. ※ 모의투자 계좌로 사용가능한 API입니다.

        엔드포인트: POST /api/v1/trading/kr-futureoption/inquiry/transaction-history
        유량제어: 2 TPS
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=44c4a04f-f55e-4c1c-b4e2-b48ec4869aee&api_id=73f68889-f613-4a16-bc1a-5e3cdaf75b0c

        Args:
            ExecTpCode: 체결구분코드 — 0:전체 1:체결 2:미체결
            BnsTpCode: 매매구분코드 — 0:전체 1:매도 2:매수
            IsuTpCode: 종목구분코드 — "": 전 종목조회 F:선물 C:콜옵션 P:풋옵션 S:스프레드
            FnoIsuNo: 선물옵션종목번호 — 공백 입력시 전 종목 조회 종목번호 입력시 해당 종목만 조회
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. 주요 응답 필드:
              - Out: Out
              - OrdNo: 주문번호
              - OrgOrdNo: 원주문번호
              - FnoIsuNo: 선물옵션종목번호
              - IsuNm: 종목명
              - FnoIsuPtnTpCode: 선물옵션종목유형구분 — F:선물 C:콜옵션 P:풋옵션 S:스프레드
              - BnsTpCode: 매매구분코드 — 1:매도 2:매수
              - MrcTpCode: 정정취소구분코드 — 0:정상 1:정정 2:취소
              - FnoOrdprcPtnCode: 선물옵션호가유형코드 — 00:지정가 03:시장가 05:조건부지정가 06:최유리지정가
              - OrdQty: 주문수량
              - OrdPrc: 주문가격
              - AllExecQty: 전체체결수량
              - AvrExecPrc: 평균체결가
              - UnercQty: 미체결수량
              - MrcQty: 정정취소수량
              - (이하 생략 — 가이드 참조)

        """
        body = {
            'In': {
                'ExecTpCode': ExecTpCode,
                'BnsTpCode': BnsTpCode,
                'IsuTpCode': IsuTpCode,
                'FnoIsuNo': FnoIsuNo,
            },
        }
        headers = {'cont_yn': cont_yn, 'cont_key': cont_key}
        return self._client.post(self.PATHS['kr_futopt_inquire_executions'], body, extra_headers=headers)

    def kr_futopt_inquire_psbl_quantity(
        self,
        *,
        FnoOrdprcPtnCode: str,
        BnsTpCode: str,
        FnoIsuNo: str,
        OrdPrc: int,
        cont_yn: str = 'N',
        cont_key: str = '',
    ) -> APIResponse:
        """선물옵션 주문가능수량 (CFOAQ42400).

        선물옵션 주문가능수량 조회 API 입니다. ※ 모의투자 계좌로 사용가능한 API입니다.

        엔드포인트: POST /api/v1/trading/kr-futureoption/inquiry/able-orderqty
        유량제어: 2 TPS
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=44c4a04f-f55e-4c1c-b4e2-b48ec4869aee&api_id=2c3c7308-2fc1-4a27-acef-5c9352036365

        Args:
            FnoOrdprcPtnCode: 선물옵션호가유형코드 — 00:지정가 03:시장가
            BnsTpCode: 매매구분 — 1:매도 2:매수
            FnoIsuNo: 선물옵션종목번호 — 선물옵션 종목 코드 입력 선물 EX) 211V2060 옵션 EX) 201V2347
            OrdPrc: 주문가
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. 주요 응답 필드:
              - QryDt: 조회일
              - FnoLmtSetupTpCode: 선물옵션한도설정구분 — 0:제한없음 1:수량 2:금액 3:수량+금액
              - FutsHldLmtQty: 선물보유한도수량
              - OptHldLmtQty: 옵션보유한도수량
              - EqoHldLmtQty: 주식옵션보유한도수량
              - FutsHldLmtAmt: 선물보유한도금액
              - OptHldLmtAmt: 옵션보유한도금액
              - EqoHldLmtAmt: 주식옵션보유한도금액
              - HldLmtOrdAbleQty: 보유한도주문가능수량 — 보유한도에 의한 주문가능수량
              - OrdPrc: 주문가
              - CurPrc: 현재가
              - NewOrdAbleQty: 신규주문가능수량
              - LqdtOrdAbleQty: 청산주문가능수량
              - OrdPrcOrdAbleQty: 주문가격주문가능수량 — 주문가격에 의한 주문가능수량
              - OptSellUnsttRestrcQty: 옵션매도미결제제한수량
              - (이하 생략 — 가이드 참조)

        """
        body = {
            'In': {
                'FnoOrdprcPtnCode': FnoOrdprcPtnCode,
                'BnsTpCode': BnsTpCode,
                'FnoIsuNo': FnoIsuNo,
                'OrdPrc': OrdPrc,
            },
        }
        headers = {'cont_yn': cont_yn, 'cont_key': cont_key}
        return self._client.post(self.PATHS['kr_futopt_inquire_psbl_quantity'], body, extra_headers=headers)

    def kr_futopt_inquire_balance(
        self,
        *,
        cont_yn: str = 'N',
        cont_key: str = '',
    ) -> APIResponse:
        """선물옵션 잔고 조회 (CFOAQ02500).

        선물옵션 잔고 조회 API 입니다. ※ 모의투자 계좌로 사용가능한 API입니다. ※ 잔고가 전부 표시되지 않는경우 연속키 조회를
        통해 확인하실 수 있습니다. ※ Output 필드 중 "총매매금액, 총평가금액, 총평가손익금액, 총수익률, 당일 실현손익금액"
        필드는 모의투자 계좌에서만 값이 제공 됩니다.

        엔드포인트: POST /api/v1/trading/kr-futureoption/inquiry/balance
        유량제어: 2 TPS
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=44c4a04f-f55e-4c1c-b4e2-b48ec4869aee&api_id=0f2f94c7-27f3-4f42-8a8b-862224618d1b

        Returns:
            APIResponse. 주요 응답 필드:
              - TotBnsAmt: 총매매금액
              - TotEvalAmt: 총평가금액
              - TotEvalPnlAmt: 총평가손익금액
              - TotErnrat: 총수익률
              - ThdayRlzPnlAmt: 당일실현손익금액
              - EvalDpstgTotamt: 평가예탁총액
              - OrdAbleAmt: 주문가능금액
              - CmsnAmt: 수수료금액
              - Out1: Out1
              - FnoIsuNo: 선물옵션종목번호
              - IsuNm: 종목명
              - BnsTpCode: 매매구분
              - LqdtOrdAbleQty: 청산주문가능수량
              - PrdayUnsttQty: 전일미결제수량
              - IncdecQty: 증감수량
              - (이하 생략 — 가이드 참조)

        """
        body = {
            'In': {},
        }
        headers = {'cont_yn': cont_yn, 'cont_key': cont_key}
        return self._client.post(self.PATHS['kr_futopt_inquire_balance'], body, extra_headers=headers)

    def kr_futopt_inquire_balance_eval(
        self,
        *,
        OrdDt: str,
        BalEvalTp: str,
        FutsPrcEvalTp: str,
        cont_yn: str = 'N',
        cont_key: str = '',
    ) -> APIResponse:
        """선물옵션 잔고_평가현황조회 (CFOAQ50100).

        선물옵션 잔고/평가현황 조회 API 입니다. ※ 모의투자 계좌로 사용가능한 API입니다. ※ 잔고가 전부 표시되지 않는경우 연속키
        조회를 통해 확인하실 수 있습니다.

        엔드포인트: POST /api/v1/trading/kr-futureoption/inquiry/balance-evalstatus
        유량제어: 2 TPS
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=44c4a04f-f55e-4c1c-b4e2-b48ec4869aee&api_id=af116c58-19a5-4bbe-8abf-5632829f327b

        Args:
            OrdDt: 주문일 — 일자를 '00000000'로 전송시 당일기준으로 산출함
            BalEvalTp: 잔고평가구분 — 0:기본설정 1:이동평균법 2:선입선출법
            FutsPrcEvalTp: 선물가격평가구분 — 1:당초가 2:전일종가
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. 주요 응답 필드:
              - EvalDpsamtTotamt: 평가예탁금총액
              - MnyEvalDpstgAmt: 현금평가예탁금액
              - DpsamtTotamt: 예탁금총액
              - DpstgMny: 예탁현금
              - DpstgSubst: 예탁대용
              - PsnOutAbleTotAmt: 인출가능총금액
              - PsnOutAbleCurAmt: 인출가능현금액
              - PsnOutAbleSubstAmt: 인출가능대용금액
              - OrdAbleTotAmt: 주문가능총금액
              - MnyOrdAbleAmt: 현금주문가능금액
              - CsgnMgnTotamt: 위탁증거금총액
              - MnyCsgnMgn: 현금위탁증거금액
              - MtmgnTotamt: 유지증거금총액
              - MnyMaintMgn: 현금유지증거금액
              - EvalAmtSum: 평가금액합계
              - (이하 생략 — 가이드 참조)

        """
        body = {
            'In': {
                'OrdDt': OrdDt,
                'BalEvalTp': BalEvalTp,
                'FutsPrcEvalTp': FutsPrcEvalTp,
            },
        }
        headers = {'cont_yn': cont_yn, 'cont_key': cont_key}
        return self._client.post(self.PATHS['kr_futopt_inquire_balance_eval'], body, extra_headers=headers)

    def kr_futopt_inquire_realized_pnl(
        self,
        *,
        cont_yn: str = 'N',
        cont_key: str = '',
    ) -> APIResponse:
        """선물옵션 당일실현손익 (CFOAQ02600).

        선물옵션 종목별 당일 매매 실현손익조회 API 입니다. ※ 모의투자 계좌로 사용가능한 API입니다.

        엔드포인트: POST /api/v1/trading/kr-futureoption/inquiry/day-rlzpnl
        유량제어: 1 TPS
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=44c4a04f-f55e-4c1c-b4e2-b48ec4869aee&api_id=650b70b8-1712-405e-a4b7-4db23a5d9290

        Returns:
            APIResponse. 주요 응답 필드:
              - Out: Out
              - FnoIsuNo: 선물옵션종목번호
              - BnsTpCode: 매매구분
              - PrdayUnsttQty: 전일미결제수량
              - UnsttQty: 미결제수량
              - LqdtQty: 청산수량
              - ThdayRlzPnlAmt: 당일실현손익금액

        """
        body = {
            'In': {},
        }
        headers = {'cont_yn': cont_yn, 'cont_key': cont_key}
        return self._client.post(self.PATHS['kr_futopt_inquire_realized_pnl'], body, extra_headers=headers)

    def kr_futopt_inquire_estimated_deposit(
        self,
        *,
        BnsDt: str,
        cont_yn: str = 'N',
        cont_key: str = '',
    ) -> APIResponse:
        """선물옵션 가정산예탁금 상세 (CFOEQ11100).

        선물옵션 계좌의 가정산예탁금 정보조회 API입니다. ※ 모의투자 계좌로 사용가능한 API입니다.

        엔드포인트: POST /api/v1/trading/kr-futureoption/inquiry/deposit-detail
        유량제어: 1 TPS
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=44c4a04f-f55e-4c1c-b4e2-b48ec4869aee&api_id=58f71b7f-064c-4e44-8c8e-9a417bf366f2

        Args:
            BnsDt: 매매일
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. 주요 응답 필드:
              - AcntNm: 계좌명
              - OpnmkDpsamtTotamt: 개장시예탁금총액 — 개장시예수금현황.개장시예탁총액
              - OpnmkDps: 개장시예수금 — 개장시예수금현황.개장시예탁현금
              - OpnmkMnyrclAmt: 개장시현금미수금
              - OpnmkSubstAmt: 개장시대용금액 — 개장시예수금현황.개장시예탁대용
              - TotAmt: 총금액 — 예수금현황.예탁총액
              - Dps: 예수금 — 예수금현황.예탁현금
              - MnyrclAmt: 현금미수금액
              - SubstDsgnAmt: 대용지정금액 — 예수금현황.예탁대용
              - CsgnMgn: 위탁증거금액
              - MnyCsgnMgn: 현금위탁증거금액
              - MaintMgn: 유지증거금액
              - MnyMaintMgn: 현금유지증거금액
              - OutAbleAmt: 출금가능총액 — 예수금현황.인출가능총액
              - MnyoutAbleAmt: 출금가능금액 — 예수금현황.인출가능현금
              - (이하 생략 — 가이드 참조)

        """
        body = {
            'In': {
                'BnsDt': BnsDt,
            },
        }
        headers = {'cont_yn': cont_yn, 'cont_key': cont_key}
        return self._client.post(self.PATHS['kr_futopt_inquire_estimated_deposit'], body, extra_headers=headers)

    def kr_futopt_order_night(
        self,
        *,
        FnoIsuNo: str,
        BnsTpCode: str,
        FnoOrdprcPtnCode: str,
        OrdPrc: float,
        OrdQty: int,
        cont_yn: str = 'N',
        cont_key: str = '',
    ) -> APIResponse:
        """선물옵션 주문 (야간) (CFOHT00100).

        야간 선물옵션 주문이 가능한 API입니다. ※ 야간선물옵선 거래신청이 완료된 계좌만 야간선물옵션 거래가 가능합니다. ※ 신청방법
        HTS : [2300]야간선물옵션참여신청 MTS : 선물옵션 > 야간시장 > 야간선옵거래신청 ※ 수수료 및 제세금 안내는 아래
        링크 참고 부탁드립니다. https://www.dbsec.co.kr/custcenter/jobservice/cu_FeeTrading_viw10.do ※ 거래제도 거래일: 월요일 야간 ~
        토요일 오전 거래시간: 18:00 ~ 익일 05:00 (동시호가 17:30 ~ 18:00) ＊ 유럽 Summer time 적용시
        18:00 ~ 04:00 ※ 야간선물옵션 거래제도 상세안내는 아래 링크 참고 부탁드립니다. https://www.dbsec.co.kr/custcenter/jobservice/cu_TradeEurex_viw.do

        엔드포인트: POST /api/v1/trading/night-futureoption/order
        유량제어: 10 TPS
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=44c4a04f-f55e-4c1c-b4e2-b48ec4869aee&api_id=a8e66f9f-5fda-437e-adfc-a130a5c66437

        Args:
            FnoIsuNo: 선물옵션종목번호 — 선물옵션 종목 코드 입력 선물 EX) 211V2060 옵션 EX) 201V2347
            BnsTpCode: 매매구분 — 1:매도 2:매수
            FnoOrdprcPtnCode: 선물옵션호가유형코드 — 00:지정가 10:지정가(IOC)
            OrdPrc: 주문가격
            OrdQty: 주문수량
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. 주요 응답 필드:
              - OrdNo: 주문번호
              - IsuNm: 종목명

        """
        body = {
            'In': {
                'FnoIsuNo': FnoIsuNo,
                'BnsTpCode': BnsTpCode,
                'FnoOrdprcPtnCode': FnoOrdprcPtnCode,
                'OrdPrc': OrdPrc,
                'OrdQty': OrdQty,
            },
        }
        headers = {'cont_yn': cont_yn, 'cont_key': cont_key}
        return self._client.post(self.PATHS['kr_futopt_order_night'], body, extra_headers=headers)

    def kr_futopt_order_modify_night(
        self,
        *,
        FnoIsuNo: str,
        OrgOrdNo: int,
        FnoOrdprcPtnCode: str,
        OrdPrc: float,
        MdfyQty: int,
        cont_yn: str = 'N',
        cont_key: str = '',
    ) -> APIResponse:
        """선물옵션 정정주문 (야간) (CFOHT00200).

        야간선물옵션 주문에 대해 정정하는 API 입니다. ※ 이미 체결완료된 주문은 정정이 불가능합니다.

        엔드포인트: POST /api/v1/trading/night-futureoption/order-revision
        유량제어: 10 TPS
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=44c4a04f-f55e-4c1c-b4e2-b48ec4869aee&api_id=a18296b3-5290-4083-8f09-67dbd85b6f53

        Args:
            FnoIsuNo: 선물옵션종목번호
            OrgOrdNo: 원주문번호
            FnoOrdprcPtnCode: 선물옵션호가유형코드 — 00:지정가 10:지정가(IOC)
            OrdPrc: 주문가격
            MdfyQty: 정정수량
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. 주요 응답 필드:
              - OrdNo: 주문번호
              - IsuNm: 종목명

        """
        body = {
            'In': {
                'FnoIsuNo': FnoIsuNo,
                'OrgOrdNo': OrgOrdNo,
                'FnoOrdprcPtnCode': FnoOrdprcPtnCode,
                'OrdPrc': OrdPrc,
                'MdfyQty': MdfyQty,
            },
        }
        headers = {'cont_yn': cont_yn, 'cont_key': cont_key}
        return self._client.post(self.PATHS['kr_futopt_order_modify_night'], body, extra_headers=headers)

    def kr_futopt_order_cancel_night(
        self,
        *,
        CancQty: int,
        FnoIsuNo: str,
        OrgOrdNo: int,
        cont_yn: str = 'N',
        cont_key: str = '',
    ) -> APIResponse:
        """선물옵션 취소주문 (야간) (CFOHT00300).

        야간선물옵션 주문에 대해 취소하는 API 입니다. ※ 이미 체결완료된 주문은 취소가 불가능합니다.

        엔드포인트: POST /api/v1/trading/night-futureoption/order-cancel
        유량제어: 10 TPS
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=44c4a04f-f55e-4c1c-b4e2-b48ec4869aee&api_id=b5ca7d0b-30de-4723-b84f-d15c928ab346

        Args:
            CancQty: 취소수량 — 취소 주문을 진행할 취소수량입력
            FnoIsuNo: 선물옵션종목번호 — 취소 주문을 진행할 원 주문에서 주문한 종목번호
            OrgOrdNo: 원주문번호 — 취소 주문을 진행할 원 주문번호
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. 주요 응답 필드:
              - OrdNo: 주문번호
              - IsuNm: 종목명

        """
        body = {
            'In': {
                'CancQty': CancQty,
                'FnoIsuNo': FnoIsuNo,
                'OrgOrdNo': OrgOrdNo,
            },
        }
        headers = {'cont_yn': cont_yn, 'cont_key': cont_key}
        return self._client.post(self.PATHS['kr_futopt_order_cancel_night'], body, extra_headers=headers)

    def kr_futopt_inquire_executions_night(
        self,
        *,
        ExecTpCode: str,
        BnsTpCode: str,
        IsuTpCode: str,
        FnoIsuNo: str,
        cont_yn: str = 'N',
        cont_key: str = '',
    ) -> APIResponse:
        """선물옵션 체결조회 (야간) (CFOHQ04000).

        야간선물옵션 체결조회 API 입니다. ※ 체결내역이 전부 표시되지 않는경우 연속키 조회를 통해 확인하실 수 있습니다.

        엔드포인트: POST /api/v1/trading/night-futureoption/inquiry/cmedt
        유량제어: 2 TPS
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=44c4a04f-f55e-4c1c-b4e2-b48ec4869aee&api_id=fc852deb-cbd0-451c-a66e-83aa282cede2

        Args:
            ExecTpCode: 체결구분코드 — 0:전체 1:체결 2:미체결
            BnsTpCode: 매매구분코드 — 0:전체 1:매도 2:매수
            IsuTpCode: 종목구분코드 — F:선물 C:콜옵션 P:풋옵션 S:스프레드
            FnoIsuNo: 선물옵션종목번호 — "": 전체 종목 조회 (종목번호 입력시 해당 종목만 조회)
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. 주요 응답 필드:
              - Out: Out
              - OrdNo: 주문번호
              - OrgOrdNo: 원주문번호
              - FnoIsuNo: 선물옵션종목번호
              - IsuNm: 종목명
              - PrdgrpClssCode: 상품군분류코드
              - FnoIsuPtnTpCode: 선물옵션종목유형구분 — F:선물 C:콜옵션 P:풋옵션 S:스프레드
              - BnsTpCode: 매매구분코드 — 1:매도 2:매수
              - MrcTpCode: 정정취소구분코드 — 0:정상 1:정정 2:취소
              - FnoOrdprcPtnCode: 선물옵션호가유형코드 — 00:지정가 03:시장가 05:조건부지정가 06:최유리지정가
              - OrdQty: 주문수량
              - OrdPrc: 주문가격
              - AllExecQty: 전체체결수량
              - AvrExecPrc: 평균체결가
              - UnercQty: 미체결수량
              - (이하 생략 — 가이드 참조)

        """
        body = {
            'In': {
                'ExecTpCode': ExecTpCode,
                'BnsTpCode': BnsTpCode,
                'IsuTpCode': IsuTpCode,
                'FnoIsuNo': FnoIsuNo,
            },
        }
        headers = {'cont_yn': cont_yn, 'cont_key': cont_key}
        return self._client.post(self.PATHS['kr_futopt_inquire_executions_night'], body, extra_headers=headers)

    def kr_futopt_inquire_balance_night(
        self,
        *,
        QryTpCode: str,
        cont_yn: str = 'N',
        cont_key: str = '',
    ) -> APIResponse:
        """선물옵션 잔고조회 (야간) (CFOHQ02500).

        야간선물옵션 잔고조회 API 입니다. ※ 잔고가 전부 표시되지 않는경우 연속키 조회를 통해 확인하실 수 있습니다.

        엔드포인트: POST /api/v1/trading/night-futureoption/inquiry/balance
        유량제어: 2 TPS
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=44c4a04f-f55e-4c1c-b4e2-b48ec4869aee&api_id=1bee0db4-d037-4983-95f2-08bc5fa8b876

        Args:
            QryTpCode: 조회구분코드 — 0:전체조회 1:개별조회 합산 2:개별조회 그리드
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. 주요 응답 필드:
              - TotBnsAmt: 총매매금액
              - TotEvalAmt: 총평가금액
              - TotEvalPnlAmt: 총평가손익금액
              - TotErnrat: 총수익률
              - ThdayRlzPnlAmt: 당일실현손익금액
              - EvalDpstgTotamt: 평가예탁총액
              - OrdAbleAmt: 주문가능금액
              - CmsnAmt: 수수료금액
              - Out1: Out1
              - FnoIsuNo: 선물옵션종목번호
              - IsuNm: 종목명
              - BnsTpCode: 매매구분
              - LqdtOrdAbleQty: 청산주문가능수량
              - PrdayUnsttQty: 전일미결제수량
              - IncdecQty: 증감수량
              - (이하 생략 — 가이드 참조)

        """
        body = {
            'In': {
                'QryTpCode': QryTpCode,
            },
        }
        headers = {'cont_yn': cont_yn, 'cont_key': cont_key}
        return self._client.post(self.PATHS['kr_futopt_inquire_balance_night'], body, extra_headers=headers)
