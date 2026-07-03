"""국내주식주문 API 모듈.

DB증권 OpenAPI 그룹: 국내주식주문
group_slug: kr_stock_order

이 파일은 `_specs/kr_stock_order/*.json` 에서 자동 생성되었습니다.
스펙이 갱신되면 `_workspace/build_modules.py`로 재생성하세요.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from dbsec_sdk.client import DBSecClient

from dbsec_sdk.response import APIResponse


class KrStockOrderAPI:
    """국내주식주문 API 모음.

    사용법:
        >>> client = DBSecClient("config.yaml")
        >>> resp = client.apis.kr_stock_order.<method>(...)
    """

    # API 경로 매핑
    PATHS = {
        'kr_stock_order': '/api/v1/trading/kr-stock/order',
        'kr_stock_order_modify': '/api/v1/trading/kr-stock/order-revision',
        'kr_stock_order_cancel': '/api/v1/trading/kr-stock/order-cancel',
        'kr_stock_order_nxt': '/api/v1/trading/kr-stock/order-nxt',
        'kr_stock_order_modify_nxt': '/api/v1/trading/kr-stock/order-revision-nxt',
        'kr_stock_order_cancel_nxt': '/api/v1/trading/kr-stock/order-cancel-nxt',
        'kr_stock_inquire_executions': '/api/v1/trading/kr-stock/inquiry/transaction-history',
        'kr_stock_inquire_psbl_quantity': '/api/v1/trading/kr-stock/inquiry/able-orderqty',
        'kr_stock_inquire_balance': '/api/v1/trading/kr-stock/inquiry/balance',
        'kr_stock_inquire_daily_pnl': '/api/v1/trading/kr-stock/inquiry/daily-ernrate',
        'kr_stock_inquire_deposit': '/api/v1/trading/kr-stock/inquiry/acnt-deposit',
        'kr_stock_inquire_daily_trade': '/api/v1/trading/kr-stock/inquiry/daliy-trade-report',
        'kr_stock_inquire_period_returns': '/api/v1/trading/kr-stock/inquiry/rdterm-ernrate',
        'kr_stock_inquire_realized_pnl': '/api/v1/trading/kr-stock/inquiry/stock-ernrate',
        'kr_stock_inquire_credit_limit': '/api/v1/trading/kr-stock/inquiry/able-crdlimit',
        'kr_stock_inquire_credit_repayment': '/api/v1/trading/kr-stock/inquiry/able-crdrepayment',
        'kr_stock_inquire_trading_history': '/api/v1/trading/kr-stock/inquiry/trading-history',
    }
    # TR 코드 매핑
    TR_CODES = {
        'kr_stock_order': 'CSPAT00600',
        'kr_stock_order_modify': 'CSPAT00700',
        'kr_stock_order_cancel': 'CSPAT00800',
        'kr_stock_order_nxt': 'CSPAT00610',
        'kr_stock_order_modify_nxt': 'CSPAT00710',
        'kr_stock_order_cancel_nxt': 'CSPAT00810',
        'kr_stock_inquire_executions': 'CSPAQ04800',
        'kr_stock_inquire_psbl_quantity': 'CSPBQ00100',
        'kr_stock_inquire_balance': 'CSPAQ03420',
        'kr_stock_inquire_daily_pnl': 'CSPAQ01800',
        'kr_stock_inquire_deposit': 'CDPCQ00100',
        'kr_stock_inquire_daily_trade': 'CSPEQ00400',
        'kr_stock_inquire_period_returns': 'FOCCQ10800',
        'kr_stock_inquire_realized_pnl': 'CSPAQ07800',
        'kr_stock_inquire_credit_limit': 'CSPAQ00600',
        'kr_stock_inquire_credit_repayment': 'CSPAQ09400',
        'kr_stock_inquire_trading_history': 'CDPCQ04700',
    }

    def __init__(self, client: 'DBSecClient'):
        self._client = client

    def kr_stock_order(
        self,
        *,
        IsuNo: str,
        TrchNo: int,
        OrdQty: int,
        OrdPrc: int,
        BnsTpCode: str,
        OrdprcPtnCode: str,
        MgntrnCode: str,
        LoanDt: str,
        OrdCndiTpCode: str,
        cont_yn: str = 'N',
        cont_key: str = '',
    ) -> APIResponse:
        """주식종합주문 (CSPAT00600).

        국내주식주문(현금&신용) API 입니다. ※ 모의투자 계좌로 사용가능한 API입니다. ※ 모의투자 주문 시 "지정가, 시장가,
        최유리지정가, 최우선지정가" 주문 유형만 입력 가능합니다. ※ 수수료 및 제세금 안내는 아래 링크 참고 부탁드립니다.
        https://www.dbsec.co.kr/custcenter/jobservice/cu_FeeTrading_viw10.do ※
        신용주문은 신용약정등록 계좌만 가능합니다. ※ 주식매매 거래제도 안내는 아래 링크 참고 부탁드립니다. https://www.dbsec.co.kr/custcenter/jobservice/cu_TradeStock_viw.do

        엔드포인트: POST /api/v1/trading/kr-stock/order
        유량제어: 10 TPS
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=05ac28b8-624f-4115-8aed-cf55f24279dd&api_id=c047bef4-020c-4ecb-9f6f-1597ee410a89

        Args:
            IsuNo: 종목번호 — 주식/ETF: 종목코드6자리 or "A"+"종목코드" EX. (005930 or A005930) ETN: Q + 종목코드 (EX. Q580036) ELW: J + 종목코드 (EX. J58J463)
            TrchNo: 트렌치번호 — 주문시 거래소 구분용도로 사용 1 : KRX ※ 1로 고정하셔서 사용 부탁드립니다. (SOR 주문 구분은 추후 제공 예정)
            OrdQty: 주문수량 — 주식 주문수량
            OrdPrc: 주문가 — * 지정가주문 이외의 주문 (시장가, 시간외 등)은 주문가를 0 으로 입력하는것을 권고
            BnsTpCode: 매매구분 — 1:매도 2:매수
            OrdprcPtnCode: 호가유형코드 — 00:지정가 03:시장가 05:조건부지정가 06:최유리지정가 07:최우선지정가 14: 중간가호가 61:장개시전시간외 81:시간외종가 82:시간외단일가
            MgntrnCode: 신용거래코드 — 000:보통 (일반주문시 사용 신용주문X) 101:유통융자상환 103:자기융자상환 105:유통대주상환 107:자기대주상환 180:예탁담보대출상환(신용)
            LoanDt: 대출일 — 일반 주문시: '00000000' 신용매수시: 오늘날짜 (YYYYMMDD) 입력 신용매도시: 매도할 종목의 결제일자(YYYYMMDD)입력 (대출일자X)
            OrdCndiTpCode: 주문조건구분 — 0:없음 1:IOC 2:FOK
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. 주요 응답 필드:
              - OrdSplitYn: 주문분할여부 — 0 : N 1 : Y KRX/NXT로 분할 되었는지 여부 (SOR주문여부가 아님에 유의) (추후 SOR 지원시 사용)
              - ConnOrdNo: 연결주문번호 — 신규필드 SOR 로 분할된 주문의 연결고리가 되는 KEY ※ SOR로 KRX/NXT 분할된경우(주문분할여부 '1')에 값 셋팅 예정 (추후 SOR 지원시 사용)
              - NxtOrdNo: NXT주문번호 — NXT 주문번호 (추후 SOR 지원시 사용)
              - OrdNo: 주문번호 — 주문시 DB증권 거래시스템에서 채번된 주문번호
              - OrdTime: 주문시각 — 주문시각(HHMMSSSSS - 시분초)
              - ShtnIsuNo: 단축종목번호
              - SpotOrdQty: 실물주문수량
              - MnyOrdAmt: 현금주문금액 — 주문시 사용된 주문금액 시장가 주문시 "0" 으로 표시
              - IsuNm: 종목명 — 주문 종목의 한글명

        """
        body = {
            'In': {
                'IsuNo': IsuNo,
                'TrchNo': TrchNo,
                'OrdQty': OrdQty,
                'OrdPrc': OrdPrc,
                'BnsTpCode': BnsTpCode,
                'OrdprcPtnCode': OrdprcPtnCode,
                'MgntrnCode': MgntrnCode,
                'LoanDt': LoanDt,
                'OrdCndiTpCode': OrdCndiTpCode,
            },
        }
        headers = {'cont_yn': cont_yn, 'cont_key': cont_key}
        return self._client.post(self.PATHS['kr_stock_order'], body, extra_headers=headers)

    def kr_stock_order_modify(
        self,
        *,
        OrgOrdNo: int,
        IsuNo: str,
        OrdQty: int,
        OrdprcPtnCode: str,
        OrdCndiTpCode: str,
        OrdPrc: int,
        cont_yn: str = 'N',
        cont_key: str = '',
    ) -> APIResponse:
        """주식정정주문 (CSPAT00700).

        주문에 대해 정정하는 API 입니다. ※ 모의투자 계좌로 사용가능한 API입니다. ※ 이미 체결완료된 주문은 정정이 불가능합니다.

        엔드포인트: POST /api/v1/trading/kr-stock/order-revision
        유량제어: 3 TPS
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=05ac28b8-624f-4115-8aed-cf55f24279dd&api_id=c4e2f114-21b0-4165-8d03-195821d91031

        Args:
            OrgOrdNo: 원주문번호 — 주식주문 완료시 Out되는 OrdNo 값 입력 (DB증권 거래 시스템에서 채번된 주문번호)
            IsuNo: 종목번호 — 원주문시 사용한 종목번호
            OrdQty: 주문수량 — 주식 주문수량
            OrdprcPtnCode: 호가유형코드 — 00:지정가 03:시장가 05:조건부지정가 06:최유리지정가 07:최우선지정가 14: 중간가호가 61:장개시전시간외 81:시간외종가 82:시간외단일가
            OrdCndiTpCode: 주문조건구분 — 0:없음 1:IOC 2:FOK
            OrdPrc: 주문가 — 정정주문 1주당 주문가격
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. 주요 응답 필드:
              - OrdNo: 주문번호 — 정정주문으로 채번된 주문번호
              - PrntOrdNo: 모주문번호 — 원 주문시 사용된 주문번호
              - OrdTime: 주문시각 — 주문시각(HHMMSSSSS - 시분초)
              - ShtnIsuNo: 단축종목번호
              - OrdAmt: 주문금액 — 정정주문시 사용된 금액 시장가 주문시 "0" 으로 표시
              - IsuNm: 종목명 — 주문 종목의 한글명

        """
        body = {
            'In': {
                'OrgOrdNo': OrgOrdNo,
                'IsuNo': IsuNo,
                'OrdQty': OrdQty,
                'OrdprcPtnCode': OrdprcPtnCode,
                'OrdCndiTpCode': OrdCndiTpCode,
                'OrdPrc': OrdPrc,
            },
        }
        headers = {'cont_yn': cont_yn, 'cont_key': cont_key}
        return self._client.post(self.PATHS['kr_stock_order_modify'], body, extra_headers=headers)

    def kr_stock_order_cancel(
        self,
        *,
        OrgOrdNo: int,
        IsuNo: str,
        OrdQty: int,
        cont_yn: str = 'N',
        cont_key: str = '',
    ) -> APIResponse:
        """주식취소주문 (CSPAT00800).

        주문에 대해 취소하는 API 입니다. ※ 모의투자 계좌로 사용가능한 API입니다. ※ 이미 체결완료된 주문은 취소가 불가능합니다.

        엔드포인트: POST /api/v1/trading/kr-stock/order-cancel
        유량제어: 3 TPS
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=05ac28b8-624f-4115-8aed-cf55f24279dd&api_id=918fae75-579d-429b-9960-0c9634b88371

        Args:
            OrgOrdNo: 원주문번호 — 주식주문 완료시 Out되는 OrdNo 값 입력 (DB금융투자 거래 시스템에서 채번된 주문번호)
            IsuNo: 종목번호 — 원주문시 사용한 종목번호
            OrdQty: 주문수량 — 주식 주문수량
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. 주요 응답 필드:
              - OrdNo: 주문번호 — 취소주문으로 채번된 주문번호
              - PrntOrdNo: 모주문번호 — 원 주문시 사용된 주문번호
              - OrdTime: 주문시각 — 주문시각(HHMMSSSSS - 시분초)
              - ShtnIsuNo: 단축종목번호
              - IsuNm: 종목명 — 주문 종목의 한글명

        """
        body = {
            'In': {
                'OrgOrdNo': OrgOrdNo,
                'IsuNo': IsuNo,
                'OrdQty': OrdQty,
            },
        }
        headers = {'cont_yn': cont_yn, 'cont_key': cont_key}
        return self._client.post(self.PATHS['kr_stock_order_cancel'], body, extra_headers=headers)

    def kr_stock_order_nxt(
        self,
        *,
        IsuNo: str,
        OrdQty: int,
        OrdPrc: int,
        BnsTpCode: str,
        OrdprcPtnCode: str,
        MgntrnCode: str,
        LoanDt: str,
        OrdCndiTpCode: str,
        cont_yn: str = 'N',
        cont_key: str = '',
    ) -> APIResponse:
        """주식종합주문- NXT거래소 (CSPAT00610).

        NXT거래소 전용 국내주식 주문 API 입니다. ※ 주문 전 MTS/HTS등 당사 매체를 통해 최선집행의무 동의를 하셔야 주문이
        가능하십니다. ※ 수수료 및 제세금 안내는 아래 링크 참고 부탁드립니다.
        https://www.dbsec.co.kr/custcenter/jobservice/cu_FeeTrading_viw10.do ※
        주식매매 거래제도 안내는 아래 링크 참고 부탁드립니다.
        https://www.dbsec.co.kr/custcenter/jobservice/cu_TradeStock_viw.do ※ NXT
        거래소 접수시간 프리마켓 : 08:00 ~ 08:50, [주문가능구분] : 지정가,최유리,최우선 메인마켓 : 09:00:30 ~
        15:20, [주문가능구분] : 모든주문구분 가능 애프터마켓 : 15:30 ~ 20:00, [주문가능구분] :
        지정가,최유리,최우선 (15:30~40: 지정가만 가능) 종가매매 : 15:00 ~ 16:00, [주문가능구분] : 시간외종가

        엔드포인트: POST /api/v1/trading/kr-stock/order-nxt
        유량제어: 10 TPS
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=05ac28b8-624f-4115-8aed-cf55f24279dd&api_id=13143c06-cf97-4ea5-a9b9-3d30fe6b1fec

        Args:
            IsuNo: 종목번호 — 주식/ETF: 종목코드6자리 or "A"+"종목코드" EX. (005930 or A005930) ETN: Q + 종목코드 (EX. Q580036) ELW: J + 종목코드 (EX. J58J463)
            OrdQty: 주문수량 — 주식 주문수량
            OrdPrc: 주문가 — * 지정가주문 이외의 주문 (시장가, 시간외 등)은 주문가를 0 으로 입력하는것을 권고
            BnsTpCode: 매매구분 — 1:매도 2:매수
            OrdprcPtnCode: 호가유형코드 — 00:지정가 03:시장가 05:조건부지정가 06:최유리지정가 07:최우선지정가 14: 중간가호가 61:장개시전시간외 81:시간외종가 82:시간외단일가
            MgntrnCode: 신용거래코드 — 000:보통 (일반주문시 사용 신용주문X) 101:유통융자상환 103:자기융자상환 105:유통대주상환 107:자기대주상환 180:예탁담보대출상환(신용)
            LoanDt: 대출일 — 일반 주문시: '00000000' 신용매수시: 오늘날짜 (YYYYMMDD) 입력 신용매도시: 매도할 종목의 결제일자(YYYYMMDD)입력 (대출일자X)
            OrdCndiTpCode: 주문조건구분 — 0:없음 1:IOC 2:FOK
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. 주요 응답 필드:
              - OrdNo: 주문번호 — 주문시 DB증권 거래시스템에서 채번된 주문번호
              - OrdTime: 주문시각 — 주문시각(HHMMSSSSS - 시분초)
              - ShtnIsuNo: 단축종목번호
              - SpotOrdQty: 실물주문수량
              - MnyOrdAmt: 현금주문금액
              - IsuNm: 종목명 — 주문 종목의 한글명

        """
        body = {
            'In': {
                'IsuNo': IsuNo,
                'OrdQty': OrdQty,
                'OrdPrc': OrdPrc,
                'BnsTpCode': BnsTpCode,
                'OrdprcPtnCode': OrdprcPtnCode,
                'MgntrnCode': MgntrnCode,
                'LoanDt': LoanDt,
                'OrdCndiTpCode': OrdCndiTpCode,
            },
        }
        headers = {'cont_yn': cont_yn, 'cont_key': cont_key}
        return self._client.post(self.PATHS['kr_stock_order_nxt'], body, extra_headers=headers)

    def kr_stock_order_modify_nxt(
        self,
        *,
        OrgOrdNo: int,
        IsuNo: str,
        OrdQty: int,
        OrdprcPtnCode: str,
        OrdCndiTpCode: str,
        OrdPrc: int,
        cont_yn: str = 'N',
        cont_key: str = '',
    ) -> APIResponse:
        """주식정정주문- NXT거래소 (CSPAT00710).

        NXT 주문에 대해 정정하는 API 입니다. ※ 이미 체결완료된 주문은 정정이 불가능합니다.

        엔드포인트: POST /api/v1/trading/kr-stock/order-revision-nxt
        유량제어: 3 TPS
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=05ac28b8-624f-4115-8aed-cf55f24279dd&api_id=e9b883fe-6978-476a-b3a4-faba34107006

        Args:
            OrgOrdNo: 원주문번호 — 주식주문 완료시 Out되는 OrdNo 값 입력 (DB증권 거래 시스템에서 채번된 주문번호)
            IsuNo: 종목번호 — 원주문시 사용한 종목번호 (선택)
            OrdQty: 주문수량 — 주식 주문수량
            OrdprcPtnCode: 호가유형코드 — 00:지정가 03:시장가 05:조건부지정가 06:최유리지정가 07:최우선지정가 14: 중간가호가 61:장개시전시간외 81:시간외종가 82:시간외단일가
            OrdCndiTpCode: 주문조건구분 — 0:없음 1:IOC 2:FOK
            OrdPrc: 주문가 — 정정주문 1주당 주문가격
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. 주요 응답 필드:
              - OrdNo: 주문번호 — 정정주문으로 채번된 주문번호
              - PrntOrdNo: 모주문번호 — 원 주문시 사용된 주문번호
              - OrdTime: 주문시각 — 주문시각(HHMMSSSSS - 시분초)
              - ShtnIsuNo: ShtnIsuNo
              - OrdAmt: 주문금액 — 정정주문시 사용된 금액 시장가 주문시 "0" 으로 표시
              - IsuNm: 종목명 — 주문 종목의 한글명

        """
        body = {
            'In': {
                'OrgOrdNo': OrgOrdNo,
                'IsuNo': IsuNo,
                'OrdQty': OrdQty,
                'OrdprcPtnCode': OrdprcPtnCode,
                'OrdCndiTpCode': OrdCndiTpCode,
                'OrdPrc': OrdPrc,
            },
        }
        headers = {'cont_yn': cont_yn, 'cont_key': cont_key}
        return self._client.post(self.PATHS['kr_stock_order_modify_nxt'], body, extra_headers=headers)

    def kr_stock_order_cancel_nxt(
        self,
        *,
        OrgOrdNo: int,
        IsuNo: str,
        OrdQty: int,
        cont_yn: str = 'N',
        cont_key: str = '',
    ) -> APIResponse:
        """주식취소주문- NXT거래소 (CSPAT00810).

        NXT 주문에 대해 취소하는 API 입니다. ※ 이미 체결완료된 주문은 취소가 불가능합니다.

        엔드포인트: POST /api/v1/trading/kr-stock/order-cancel-nxt
        유량제어: 3 TPS
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=05ac28b8-624f-4115-8aed-cf55f24279dd&api_id=159a17c5-6cba-4887-a963-8464cdb95d65

        Args:
            OrgOrdNo: 원주문번호 — 주식주문 완료시 Out되는 OrdNo 값 입력 (DB증권 거래 시스템에서 채번된 주문번호)
            IsuNo: 종목번호 — 원주문시 사용한 종목번호
            OrdQty: 주문수량 — 주식 주문수량
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. 주요 응답 필드:
              - OrdNo: 주문번호 — 취소주문으로 채번된 주문번호
              - PrntOrdNo: 모주문번호 — 원 주문시 사용된 주문번호
              - OrdTime: 주문시각 — 주문시각(HHMMSSSSS - 시분초)
              - ShtnIsuNo: 단축종목번호
              - IsuNm: 종목명 — 주문 종목의 한글명

        """
        body = {
            'In': {
                'OrgOrdNo': OrgOrdNo,
                'IsuNo': IsuNo,
                'OrdQty': OrdQty,
            },
        }
        headers = {'cont_yn': cont_yn, 'cont_key': cont_key}
        return self._client.post(self.PATHS['kr_stock_order_cancel_nxt'], body, extra_headers=headers)

    def kr_stock_inquire_executions(
        self,
        *,
        SorTpYn: str,
        ExecYn: str,
        TrdMktCode: str,
        BnsTpCode: str,
        IsuTpCode: str,
        QryTp: str,
        cont_yn: str = 'N',
        cont_key: str = '',
    ) -> APIResponse:
        """체결/미체결조회 (CSPAQ04800).

        국내주식 체결/미체결 내역을 확인하는 API입니다. ※ 모의투자 계좌로 사용가능한 API입니다.

        엔드포인트: POST /api/v1/trading/kr-stock/inquiry/transaction-history
        유량제어: 2 TPS
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=05ac28b8-624f-4115-8aed-cf55f24279dd&api_id=815bbd65-8208-4428-b82a-18c32c13a092

        Args:
            SorTpYn: SOR구분여부 — 0 : N 1 : Y 2 : 전체
            ExecYn: 체결여부 — 0:전체 1:체결 2:미체결(정정취소가능)
            TrdMktCode: 거래시장코드 — 0 : 전체 1 : KRX 2 : NXT
            BnsTpCode: 매매구분 — 0:전체 1:매도 2:매수
            IsuTpCode: 종목구분 — 0:전체
            QryTp: 조회구분 — 0:전체 1:ELW 2:ELW제외
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. 주요 응답 필드:
              - Out1: Out1
              - TrdMktCode: 시장구분코드 — 1:KRX 2:NXT
              - OrdNo: 주문번호
              - OrdSplitYn: 주문분할여부 — 0 : N 1 : Y KRX/NXT로 분할 되었는지 여부 (SOR주문여부가 아님에 유의)
              - ConnOrdNo: 연결주문번호 — SOR 로 분할된 주문의 연결고리가 되는 KEY ※ SOR로 KRX/NXT 분할된경우(주문분할여부 '1')에 값 셋팅 예정
              - SorTpYn: SOR구분여부 — 0 : N 1 : Y
              - OrgOrdNo: 원주문번호
              - IsuNo: 종목번호
              - OrdMktCode: 주문시장코드 — 00:전체 10:KSE 20:KOSDAQ 25:KONEX 30:OTCBB
              - BnsTpCode: 매매구분 — 1:매도 2:매수
              - OrdPtnCode: 주문유형코드 — 01:현금매도 02:현금매수 03:신용매도 04:신용매수 05:저축
              - OrdprcPtnCode: 호가유형코드 — 00:지정가 03:시장가 05:조건부지정가 06:최유리지정가
              - OrdQty: 주문수량
              - OrdPrc: 주문가
              - AllExecQty: 전체체결수량
              - (이하 생략 — 가이드 참조)

        """
        body = {
            'In': {
                'SorTpYn': SorTpYn,
                'ExecYn': ExecYn,
                'TrdMktCode': TrdMktCode,
                'BnsTpCode': BnsTpCode,
                'IsuTpCode': IsuTpCode,
                'QryTp': QryTp,
            },
        }
        headers = {'cont_yn': cont_yn, 'cont_key': cont_key}
        return self._client.post(self.PATHS['kr_stock_inquire_executions'], body, extra_headers=headers)

    def kr_stock_inquire_psbl_quantity(
        self,
        *,
        BnsTpCode: str,
        IsuNo: str,
        OrdPrc: int,
        cont_yn: str = 'N',
        cont_key: str = '',
    ) -> APIResponse:
        """주식주문가능수량조회 (CSPBQ00100).

        국내주식 주문가능수량 조회 API 입니다. ※ 모의투자 계좌로 사용가능한 API입니다.

        엔드포인트: POST /api/v1/trading/kr-stock/inquiry/able-orderqty
        유량제어: 2 TPS
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=05ac28b8-624f-4115-8aed-cf55f24279dd&api_id=4634714a-1ebb-481f-830d-a053524acc97

        Args:
            BnsTpCode: 매매구분 — 1:매도 2:매수
            IsuNo: 종목번호 — 주식/ETF: 종목코드6자리 or "A"+"종목코드" EX. (005930 or A005930) ETN: Q + 종목코드 (EX. Q580036) ELW: J + 종목코드 (EX. J58J463)
            OrdPrc: 주문가격 — 매매구분 "매도" 선택시 0 입력 "매수" 선택시 입력된 주문가격으로 주문가능수량 산정 (가격 0 으로 설정시 금일 종가가 존재하는경우 금일종가 기준, 없을경우 상한가 기준으로 산정)
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. 주요 응답 필드:
              - IsuNm: 종목명
              - BnsTpNm: 매매구분 — 1:매도 2:매수
              - Dps: 예수금
              - SubstAmt: 대용금액
              - MnyMgn: 현금증거금액
              - SubstMgn: 대용증거금액
              - MnyOrdAbleAmt: 현금주문가능금액
              - SubstOrdAbleAmt: 대용주문가능금액
              - CrdtPldgRuseAmt: 신용담보재사용금액
              - AbleAmt: 가능금액
              - MgnRat100pctOrdAbleAmt: 증거금률100퍼센트주문가능금액
              - MgnRat100OrdAbleQty: 증거금률100퍼센트주문가능수량
              - LoanPldgRat: 대출담보율
              - PldgMaintRat: 담보유지비율
              - OrdAbleQty: 주문가능수량
              - (이하 생략 — 가이드 참조)

        """
        body = {
            'In': {
                'BnsTpCode': BnsTpCode,
                'IsuNo': IsuNo,
                'OrdPrc': OrdPrc,
            },
        }
        headers = {'cont_yn': cont_yn, 'cont_key': cont_key}
        return self._client.post(self.PATHS['kr_stock_inquire_psbl_quantity'], body, extra_headers=headers)

    def kr_stock_inquire_balance(
        self,
        *,
        QryTpCode0: str,
        cont_yn: str = 'N',
        cont_key: str = '',
    ) -> APIResponse:
        """주식잔고조회 (CSPAQ03420).

        주식 잔고조회 API 입니다. 보유중인 주식 잔고에 대한 정보를 제공합니다. ※ 모의투자 계좌로 사용가능한 API입니다. ※
        잔고가 전부 표시되지 않는경우 연속키 조회를 통해 확인하실 수 있습니다.

        엔드포인트: POST /api/v1/trading/kr-stock/inquiry/balance
        유량제어: 2 TPS
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=05ac28b8-624f-4115-8aed-cf55f24279dd&api_id=07a86b9a-0548-47cd-baa9-24395d4ea4bb

        Args:
            QryTpCode0: 조회구분코드0 — 0:전체 1:비상장제외 2:비상장,코넥스,kotc 제외
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. 주요 응답 필드:
              - TotBuyAmt: 총매수금액 — 체결기준 매수금액
              - TotEvalAmt: 총평가금액 — 체결기준 총평가금액
              - TotEvalPnlAmt: 총평가손익금액
              - TotErnrat: 총수익률
              - ThdaySellAmt: 당일매도금액
              - ThdayBuyAmt: 당일매수금액
              - ThdayRlzPnlAmt: 당일실현손익금액
              - CrdtBnsAmt: 신용매매금액
              - DpsastAmt: 예탁자산금액
              - Dps2: 예수금2 — D+2 예수금
              - Out1: Out1
              - IsuNo: 종목번호
              - IsuNm: 종목명
              - BalQty: 잔고수량 — 결제기준 잔고
              - BalQty0: 잔고수량0 — 체결기준 잔고 (T+2)
              - (이하 생략 — 가이드 참조)

        """
        body = {
            'In': {
                'QryTpCode0': QryTpCode0,
            },
        }
        headers = {'cont_yn': cont_yn, 'cont_key': cont_key}
        return self._client.post(self.PATHS['kr_stock_inquire_balance'], body, extra_headers=headers)

    def kr_stock_inquire_daily_pnl(
        self,
        *,
        QryTp: str,
        cont_yn: str = 'N',
        cont_key: str = '',
    ) -> APIResponse:
        """당일매매손익 조회 (CSPAQ01800).

        당일 실현손익을 조회 할 수 있는 API 입니다. 당일 실현손익을 실시간으로 조회 가능합니다. 기간별, 종목별 실현손익 확인이
        필요하신 경우 "주식 실현손익조회" API 사용 부탁드립니다.

        엔드포인트: POST /api/v1/trading/kr-stock/inquiry/daily-ernrate
        유량제어: 2 TPS
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=05ac28b8-624f-4115-8aed-cf55f24279dd&api_id=d159f8ec-a52d-40ec-bf05-99b6f8b68744

        Args:
            QryTp: 조회구분 — "2" 고정입력
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. 주요 응답 필드:
              - Out: Out
              - AcntNm: 계좌명
              - CrdaySellExecAmt: 금일매도체결금액
              - SellExecQty: 매도체결수량
              - CrdayBuyExecAmt: 금일매수체결금액
              - BuyExecQty: 매수체결수량
              - AdjstAmt: 정산금액
              - DtTotPnlAmt: 일총손익금액
              - MnyOrdAbleAmt: 현금주문가능금액
              - MnyoutAbleAmt: 출금가능금액
              - Evrprc: 제비용
              - BalEvalAmt: 잔고평가금액
              - InvstPlAmt: 투자손익금액
              - InvstOrgAmt: 투자원금
              - PnlRat: 손익율
              - (이하 생략 — 가이드 참조)

        """
        body = {
            'In': {
                'QryTp': QryTp,
            },
        }
        headers = {'cont_yn': cont_yn, 'cont_key': cont_key}
        return self._client.post(self.PATHS['kr_stock_inquire_daily_pnl'], body, extra_headers=headers)

    def kr_stock_inquire_deposit(
        self,
        *,
        cont_yn: str = 'N',
        cont_key: str = '',
    ) -> APIResponse:
        """계좌예수금조회 (CDPCQ00100).

        계좌의 예수금에대한 정보를 제공하는 API 입니다. ※ 모의투자 계좌로 사용가능한 API입니다. ※ CMA 계좌일 경우 전일,
        당일 매매 존재 시 D+1, D+2 예수금은 (-) 금액으로 표시될 수 있습니다.

        엔드포인트: POST /api/v1/trading/kr-stock/inquiry/acnt-deposit
        유량제어: 1 TPS
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=05ac28b8-624f-4115-8aed-cf55f24279dd&api_id=3876bc95-5981-4009-91ca-2408cd56cf6d

        Returns:
            APIResponse. 주요 응답 필드:
              - DpsBalAmt: 예수금잔고금액
              - MgnMny: 증거금현금
              - PldgCurAmt: 담보현금액
              - AddCrdtPldgMny: 추가신용담보현금
              - RcvblEnsrAmt: 미수확보금액
              - SubstAmt: 대용금액
              - SubstMgn: 대용증거금액
              - PldgSubstAmt0: 담보대용금액0
              - AddCrdtPldgSubst: 추가신용담보대용
              - RgtsbAmt: 권리대용금액
              - ChckAmt: 수표금액
              - UnSettEtcChckAmt: 미결제기타수표금액
              - CrdtPldgRuseAmt: 신용담보재사용금액
              - Imreq: 신용설정보증금
              - DpslRestrcAmt: 처분제한금액
              - (이하 생략 — 가이드 참조)

        """
        body = {
            'In': {},
        }
        headers = {'cont_yn': cont_yn, 'cont_key': cont_key}
        return self._client.post(self.PATHS['kr_stock_inquire_deposit'], body, extra_headers=headers)

    def kr_stock_inquire_daily_trade(
        self,
        *,
        IsuNo: str,
        BnsDt: str,
        cont_yn: str = 'N',
        cont_key: str = '',
    ) -> APIResponse:
        """일자별매매내역 (CSPEQ00400).

        일자별 매매내역을 확인 할 수 있는 API 입니다. ※ 모의투자 계좌로 사용가능한 API입니다. ※ 종목코드 미입력시, 해당일에
        매매된 모든 종목이 출력됩니다.

        엔드포인트: POST /api/v1/trading/kr-stock/inquiry/daliy-trade-report
        유량제어: 1 TPS
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=05ac28b8-624f-4115-8aed-cf55f24279dd&api_id=97c0b3a7-e28b-4317-83bd-cbb7ee6bac48

        Args:
            IsuNo: 종목번호 — "": 공백 설정 시 전 종목 조회 주식/ETF: 종목코드6자리 or "A"+"종목코드" EX. (005930 or A005930) ETN: Q + 종목코드 (EX. Q580036) ELW: J + 종목코드 (EX. J58J463)
            BnsDt: 매매일 — YYYYMMDD 형식의 날짜 입력 (EX. 20240102)
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. 주요 응답 필드:
              - SellQty: 매도수량
              - BuyQty: 매수수량
              - SellAdjstAmt: 매도정산금액
              - BuyAdjstAmt: 매수정산금액
              - BnsDt: 매매일
              - SettDt: 결제일
              - QryDt: 조회일
              - Out1: Out1
              - IsuNo: 종목번호
              - IsuNm: 종목명
              - IsuSeqno: 일련번호
              - SettRnkCode: 결제순위코드 — 10.프리보드 20.코스닥 30.거래소
              - OrdTrdPtnCode: 주문거래유형코드 — 00.위탁 01.신용 02.저축 03.상품 04.선물대용
              - TrdTpNm: 거래구분
              - TrdTpNm1: 거래구분명1
              - (이하 생략 — 가이드 참조)

        """
        body = {
            'In': {
                'IsuNo': IsuNo,
                'BnsDt': BnsDt,
            },
        }
        headers = {'cont_yn': cont_yn, 'cont_key': cont_key}
        return self._client.post(self.PATHS['kr_stock_inquire_daily_trade'], body, extra_headers=headers)

    def kr_stock_inquire_period_returns(
        self,
        *,
        TermTpCode: str,
        QrySrtDt: str,
        QryEndDt: str,
        cont_yn: str = 'N',
        cont_key: str = '',
    ) -> APIResponse:
        """임의기간수익률집계 (FOCCQ10800).

        설정한 기간동안의 수익률을 집계할 수 있는 API 입니다. ※ 수익률은 전일 체결분까지 반영됩니다.

        엔드포인트: POST /api/v1/trading/kr-stock/inquiry/rdterm-ernrate
        유량제어: 1 TPS
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=05ac28b8-624f-4115-8aed-cf55f24279dd&api_id=533bd6bd-8ab9-4673-83f3-4146041d871d

        Args:
            TermTpCode: 기간구분코드 — 1:일별 2:월별
            QrySrtDt: 조회시작일자 — YYYYMMDD 형식의 날짤 입력 (EX. 20240101)
            QryEndDt: 조회종료일자 — YYYYMMDD 형식의 날짤 입력 (EX. 20240105)
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. 주요 응답 필드:
              - Out: Out
              - BaseDt: 기준일자
              - FdEvalAmt: 기초평가금액
              - EotEvalAmt: 기말평가금액
              - TermAvrbalAmt: 기간평잔금액
              - InvstPrftAmt: 투자이익금액
              - TrstCmsnAmt: 수탁수수료금액
              - EvrTax: 제세금
              - InAmt: 입금액
              - SecinAmt: 입고금액
              - OutAmt: 출금액
              - SecoutAmt: 출고금액
              - MnyinCmpErnRat: 입금대비수익율
              - TblnBaseErnRat: 잔액기준수익율
              - AvrbalErnRat: 평잔수익율
              - (이하 생략 — 가이드 참조)

        """
        body = {
            'In': {
                'TermTpCode': TermTpCode,
                'QrySrtDt': QrySrtDt,
                'QryEndDt': QryEndDt,
            },
        }
        headers = {'cont_yn': cont_yn, 'cont_key': cont_key}
        return self._client.post(self.PATHS['kr_stock_inquire_period_returns'], body, extra_headers=headers)

    def kr_stock_inquire_realized_pnl(
        self,
        *,
        SrtDt: str,
        EndDt: str,
        IsuNo: str,
        CmsnAppTpCode: str,
        cont_yn: str = 'N',
        cont_key: str = '',
    ) -> APIResponse:
        """주식 실현손익조회 (CSPAQ07800).

        종목&기간별 실현손익을 조회 할 수 있는 API 입니다. 당일 실현손익의 경우, 장 마감 후 확인 가능합니다. 실시간 당일
        실현손익 확인이 필요하신 경우 "당일매매손익 조회" API 사용 부탁드립니다.

        엔드포인트: POST /api/v1/trading/kr-stock/inquiry/stock-ernrate
        유량제어: 1 TPS
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=05ac28b8-624f-4115-8aed-cf55f24279dd&api_id=c2eb049b-d54b-4d60-9645-129552f15edf

        Args:
            SrtDt: 시작일자 — YYYYMMDD 형식의 날짜 입력 (EX. 20240101)
            EndDt: 종료일자 — YYYYMMDD 형식의 날짜 입력 (EX. 20240102)
            IsuNo: 종목번호 — 주식/ETF: 종목코드6자리 or "A"+"종목코드" "": 전체 종목 표시 (공백으로 설정 시 기간 내 거래된 모든 특정 종목이 아닌 모든 종목을 표시합니다) EX. (005930 or A005930) ETN: Q + 종목코드 (EX. Q580036) ELW: J + 종목코드 (EX. J58J463)
            CmsnAppTpCode: 수수료적용구분코드 — 0: 제비용 미포함, 1: 제비용 포함
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. 주요 응답 필드:
              - BuyAmt: 매수금액
              - SellAmt: 매도금액
              - RlzPnlAmt: 실현손익금액
              - BuyCmsn: 매수수수료
              - SellCmsn: 매도수수료
              - TaxAmt: 세금금액
              - PnlRat: 손익율
              - AdjstAmt: 정산금액
              - Out1: Out1
              - BnsDt: 매매일자
              - CodeNm: 코드명
              - IsuNo: 종목번호
              - IsuNm: 종목명
              - SellPnlAmt: 매도손익금액
              - PnlRat0: 손익율0 — 실현수익률
              - (이하 생략 — 가이드 참조)

        """
        body = {
            'In': {
                'SrtDt': SrtDt,
                'EndDt': EndDt,
                'IsuNo': IsuNo,
                'CmsnAppTpCode': CmsnAppTpCode,
            },
        }
        headers = {'cont_yn': cont_yn, 'cont_key': cont_key}
        return self._client.post(self.PATHS['kr_stock_inquire_realized_pnl'], body, extra_headers=headers)

    def kr_stock_inquire_credit_limit(
        self,
        *,
        LoanDtlClssCode: str,
        IsuNo: str,
        OrdPrc: int,
        cont_yn: str = 'N',
        cont_key: str = '',
    ) -> APIResponse:
        """계좌별신용한도조회 (CSPAQ00600).

        종목에 대한 신용 한도를 조회할 수 있는 API 입니다. ※ 모의투자 계좌로 사용가능한 API입니다. ※ 신용 약정등록이 완료된
        계좌만 사용가능합니다.

        엔드포인트: POST /api/v1/trading/kr-stock/inquiry/able-crdlimit
        유량제어: 1 TPS
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=05ac28b8-624f-4115-8aed-cf55f24279dd&api_id=485bffdb-5d83-4ab0-8707-e115602e6280

        Args:
            LoanDtlClssCode: 대출상세분류코드 — 01 : 유통융자 03 : 자기융자 05 : 유통대주 07 : 자기대주
            IsuNo: 종목번호 — 주식/ETF: 종목코드6자리 or "A"+"종목코드" EX. (005930 or A005930) ETN: Q + 종목코드 (EX. Q580036) ELW: J + 종목코드 (EX. J58J463)
            OrdPrc: 주문가
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. 주요 응답 필드:
              - OrdPrc: 주문가
              - SloanLmtAmt: 대주한도
              - SloanAmtSum: 대주금액합계
              - SloanNewAmt: 대주신규금액
              - SloanRfundAmt: 대주상환금액
              - MktcplMloanLmtAmt: 유통융자한도금액
              - MktcplMloanAmtSum: 유통융자금액합계
              - MktcplMloanNewAmt: 유통융자신규금액
              - MktcplMloanRfundAmt: 유통융자상환금액
              - SfaccMloanLmtAmt: 자기융자한도금액
              - SfaccMloanAmtSum: 자기융자금액합계
              - SfaccMloanNewAmt: 자기융자신규금액
              - SfaccMloanRfundAmt: 자기융자상환금액
              - BrnMktcplMloanLmtAmt: 지점유통융자한도금액 — 내용확인필요
              - BrnMktcplMloanNewAmt: 지점유통융자신규금액
              - (이하 생략 — 가이드 참조)

        """
        body = {
            'In': {
                'LoanDtlClssCode': LoanDtlClssCode,
                'IsuNo': IsuNo,
                'OrdPrc': OrdPrc,
            },
        }
        headers = {'cont_yn': cont_yn, 'cont_key': cont_key}
        return self._client.post(self.PATHS['kr_stock_inquire_credit_limit'], body, extra_headers=headers)

    def kr_stock_inquire_credit_repayment(
        self,
        *,
        IsuNo: str,
        BnsTpCode: str,
        cont_yn: str = 'N',
        cont_key: str = '',
    ) -> APIResponse:
        """신용상환가능총수량조회 (CSPAQ09400).

        종목에 대한 신용상황가능 수량을 조회할 수 있는 API입니다. ※ 신용 약정등록이 완료된 계좌만 사용가능합니다.

        엔드포인트: POST /api/v1/trading/kr-stock/inquiry/able-crdrepayment
        유량제어: 1 TPS
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=05ac28b8-624f-4115-8aed-cf55f24279dd&api_id=0caa0bba-7ac1-49f9-b859-5ddb305f6d71

        Args:
            IsuNo: 종목번호 — 주식/ETF: 종목코드6자리 or "A"+"종목코드" EX. (005930 or A005930) ETN: Q + 종목코드 (EX. Q580036) ELW: J + 종목코드 (EX. J58J463)
            BnsTpCode: 매매구분코드 — 1:매도 2:매수
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. 주요 응답 필드:
              - OrdAbleQty: 주문가능수량

        """
        body = {
            'In': {
                'IsuNo': IsuNo,
                'BnsTpCode': BnsTpCode,
            },
        }
        headers = {'cont_yn': cont_yn, 'cont_key': cont_key}
        return self._client.post(self.PATHS['kr_stock_inquire_credit_repayment'], body, extra_headers=headers)

    def kr_stock_inquire_trading_history(
        self,
        *,
        QryTp: str,
        QrySrtDt: str,
        QryEndDt: str,
        SrtNo: int,
        IsuNo: str,
        cont_yn: str = 'N',
        cont_key: str = '',
    ) -> APIResponse:
        """계좌거래내역 조회 (CDPCQ04700).

        국내주식 거래내역을 확인하는 API입니다. ※ 모의투자 계좌로 사용가능한 API입니다.

        엔드포인트: POST /api/v1/trading/kr-stock/inquiry/trading-history
        유량제어: 2 TPS
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=05ac28b8-624f-4115-8aed-cf55f24279dd&api_id=1a4fcb20-874c-40a7-bd7a-1b099289de0f

        Args:
            QryTp: 조회구분 — 0:전체 1:입출금 2:입출고 3:매매 4.이체/대체
            QrySrtDt: 조회시작일
            QryEndDt: 조회종료일 — 조회기간 최대 12개월(선물옵션계좌의 경우 6개월)
            SrtNo: 시작번호 — 기본값: 0 조회구분 "0.전체"인 경우 CMA매매내역 생략시 1 입력
            IsuNo: 종목번호 — "" : 공백 입력시 전체 종목 조회 "A+종목번호" 입력시 특정 종목 내역 조회 ex. "A016610" 설정시 DB증권 종목 내역만 확인
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. 주요 응답 필드:
              - AcntNm: 계좌명
              - AcntNo: 계좌번호
              - TrdDt: 거래일자
              - TrdNo: 거래번호
              - TpCodeNm: 구분코드명
              - SmryNo: 적요번호
              - SmryNm: 적요명
              - CancTpNm: 취소구분 — 0:정상 1:취소
              - TrdQty: 거래수량
              - Trtax: 거래세
              - AdjstAmt: 정산금액
              - OvdSum: 연체합
              - DpsBfbalAmt: 예수금전잔금액
              - SellPldgRfundAmt: 매도담보상환금
              - DpspdgLoanBfbalAmt: 예탁담보대출전잔금액
              - (이하 생략 — 가이드 참조)

        """
        body = {
            'In': {
                'QryTp': QryTp,
                'QrySrtDt': QrySrtDt,
                'QryEndDt': QryEndDt,
                'SrtNo': SrtNo,
                'IsuNo': IsuNo,
            },
        }
        headers = {'cont_yn': cont_yn, 'cont_key': cont_key}
        return self._client.post(self.PATHS['kr_stock_inquire_trading_history'], body, extra_headers=headers)
