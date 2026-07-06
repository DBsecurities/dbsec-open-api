"""해외주식주문 API 모듈.

DB증권 OpenAPI 그룹: 해외주식주문
group_slug: ov_stock_order

이 파일은 `_specs/ov_stock_order/*.json` 에서 자동 생성되었습니다.
스펙이 갱신되면 `_workspace/build_modules.py`로 재생성하세요.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from dbsec_sdk.client import DBSecClient

from dbsec_sdk.response import APIResponse


class OvStockOrderAPI:
    """해외주식주문 API 모음.

    사용법:
        >>> client = DBSecClient("config.yaml")
        >>> resp = client.apis.ov_stock_order.<method>(...)
    """

    # API 경로 매핑
    PATHS = {
        'ov_stock_order': '/api/v1/trading/overseas-stock/order',
        'ov_stock_inquire_executions': '/api/v1/trading/overseas-stock/inquiry/transaction-history',
        'ov_stock_inquire_balance_margin': '/api/v1/trading/overseas-stock/inquiry/balance-margin',
        'ov_stock_inquire_trade_history': '/api/v1/trading/overseas-stock/inquiry/trading-history',
        'ov_stock_inquire_trading_history': '/api/v1/trading/overseas-stock/inquiry/trade-history',
        'ov_stock_inquire_psbl_amount': '/api/v1/trading/overseas-stock/inquiry/able-orderqty',
        'ov_stock_inquire_realized_pnl': '/api/v1/trading/overseas-stock/inquiry/day-rlzpnl',
        'ov_stock_inquire_deposit_detail': '/api/v1/trading/overseas-stock/inquiry/deposit-detail',
        'ov_stock_inquire_avg_buy_price': '/api/v1/trading/overseas-stock/inquiry/avg-pur-price',
    }
    # TR 코드 매핑
    TR_CODES = {
        'ov_stock_order': 'CAZCT00100',
        'ov_stock_inquire_executions': 'CAZCQ00100',
        'ov_stock_inquire_balance_margin': 'CAZCQ00400',
        'ov_stock_inquire_trade_history': 'CAZCQ00200',
        'ov_stock_inquire_trading_history': 'CAZCQ01600',
        'ov_stock_inquire_psbl_amount': 'CAZCQ01300',
        'ov_stock_inquire_realized_pnl': 'CAZCQ00300',
        'ov_stock_inquire_deposit_detail': 'CAZCQ01400',
        'ov_stock_inquire_avg_buy_price': 'CAZCQ03400',
    }

    def __init__(self, client: 'DBSecClient'):
        self._client = client

    def ov_stock_order(
        self,
        *,
        AstkIsuNo: str,
        AstkBnsTpCode: str,
        AstkOrdprcPtnCode: str,
        AstkOrdCndiTpCode: str,
        AstkOrdQty: int,
        AstkOrdPrc: int,
        OrdTrdTpCode: str,
        OrgOrdNo: int,
        cont_yn: str = 'N',
        cont_key: str = '',
    ) -> APIResponse:
        """해외주식 주문 (CAZCT00100).

        해외주식(미국) 주문이 가능한 API입니다. ※ 모의투자 계좌로 사용가능한 API입니다. ※ 해외주식 거래신청 후 이용
        가능합니다. - 신청방법 HTS : [7322] 해외주식 시작하기 MTS : 해외주식 > 서비스신청 > 해외주식 거래신청,
        통합증거금 이용신청, 해외ETP(ETF,ETN) 거래신청 ※ 수수료 및 제세금 안내는 아래 링크 참고 부탁드립니다.
        https://www.dbsec.co.kr/custcenter/jobservice/cu_FeeTrading_viw10.do ※
        해외주식 양도소득세 안내는 아래 링크 참고 부탁드립니다. https://www.dbsec.co.kr/research/osst/re_OsstDealInfo_viw40.do ※ 거래시간 미국 정규장: 23:30 ~ 익일
        06:00 (서머타임 적용시 22:30 ~ 익일 05:00) 미국 프리장: 18:00 ~ 23:30 (서머타임 적용시 17:00
        ~ 22:30) 미국 애프터장: 익일 06:00 ~ 07:00 (서머타임 적용시 05:00 ~ 07:00) ※ 해외주식 주문유형
        안내 1. 지정가: 희망 거래 가격을 지정하여 주문 &#183; 이용가능 국가: 미국 &#183; 거래가능 시간: 정규장
        프리/애프터마켓 2. 시장가: 즉시 체결될 수 있는 가격으로 주문 &#183; 이용가능 국가: 미국 &#183; 거래가능 시간:
        정규장 * 당사 시장가 매수 주문은 자체 기준에 따라 현재가 대비 불리한 가격의 지정가로 주문됩니다. 더불어 현재가보다 기준가격을
        높게 산정하므로, 주문가능수량은 지정가 주문수량보다 적을 수 있으니 참고하시기 바랍니다. 3. 장개시 주문: 정규장 시작과 동시에
        지정가 또는 시장가로 주문 &#183; MOO(장개시 시장가): 정규장 시작과 동시에 시초가로 체결 시키는 주문(단, 매도만
        가능) &#183; LOO(장개시 지정가): 정규장 시작과 동시에 시초가가 지정한 가격보다 같거나 유리하면 체결 시키는 주문
        &#183; 이용가능 국가: 미국 &#183; 거래가능 시간: 프리마켓 (장 시작 10분 전까지 가능) 4. 장마감 주문: 정규장
        종료와 동시에 지정가 또는 시장가로 주문 &#183; MOC(장마감 시장가): 정규장 종료와 동시에 종가로 체결 시키는 주문(단,
        매도만 가능) &#183; LOC(장마감 지정가): 정규장 종료와 동시에 종가가 지정한 가격보다 같거나 유리하면 체결시키는 주문
        &#183; 이용가능 국가: 미국 &#183; 거래가능 시간: 프리마켓, 정규장(장 마감 10분 전까지 가능) 5. 알고리즘
        주문: 거래소가 아닌 해외중계업체의 자체 알고리즘에 따라 주문 &#183; TWAP(시간 가중평균가격): 주문 시점 기준부터
        비슷한 시간 간격으로 비슷한 수량을 분할해 체결 시키는 주문 &#183; VWAP(거래량 가중평균가격): 주문 시점 기준부터 시장
        가격 및 거래량의 변화를 모니터링하여, 거래량이 많을 때는 많이, 거래량이 적을 때는 적게 분할 체결시키는 주문 &#183;
        이용가능 국가: 미국 &#183; 거래가능 시간: 정규장 * TWAP/VWAP 주문은 지정가, 시장가로 구분되며 매수할 때는
        지정가, 매도할 때는 시장가로 주문 가능합니다. * TWAP/VWAP 지정가 매수 주문은 지정한 가격 이하에서만 유형 특성에 따라
        분할 체결시키는 주문입니다. * TWAP/VWAP 주문은 100주 단위로 체결되며, 100주 미만으로 주문 가능하나 한 번에
        체결될 수 있습니다. ※ 유의사항 &#183; 시장가(MOO, MOC 포함) 주문의 경우 시장 급변동으로 인해 원치 않는 가격으로
        체결될 수 있음에 유의하시기 바랍니다. &#183; 장전(프리)/정규장 거래시간에 접수된 미체결 주문은 장후(애프터) 거래시간까지
        유효합니다.

        엔드포인트: POST /api/v1/trading/overseas-stock/order
        유량제어: 10 TPS
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=e4726f55-cc3b-45af-a1b5-852628fe5960&api_id=43bc0191-3745-4ba8-937e-7af51e65085c

        Args:
            AstkIsuNo: 해외주식종목번호 — 미국주식/ETF: "종목코드" (EX. AAPL, SOXL, QQQ)
            AstkBnsTpCode: 해외주식매매구분코드 — 1:매도 2:매수
            AstkOrdprcPtnCode: 해외주식호가유형코드 — 1: 지정가 2: 시장가 3: LOO 4: MOO (매도주문 시 사용가능) 5: LOC 6: MOC (매도주문 시 사용가능) 7: VWAP지정가 (매수/매도 주문 모두 사용가능) 8: TWAP지정가 (매수/매도 주문 모두 사용가능) 9: VWAP시장가 (매도주문시에만 사용가능) A: TWAP시장가 (매도주문시에만 사용가능)
            AstkOrdCndiTpCode: 해외주식주문조건구분코드 — 1:FAS(일반) 2:IOC 3:FOK
            AstkOrdQty: 해외주식주문수량
            AstkOrdPrc: 해외주식주문가격 — 시장가주문시: 0
            OrdTrdTpCode: 주문거래구분코드 — 0:주문 1:정정주문 2:취소주문
            OrgOrdNo: 원주문번호 — 정정주문, 취소주문시 원 주문번호 입력 매수/매도주문시: 0
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. 주요 응답 필드:
              - OrdNo: 주문번호

        """
        body = {
            'In': {
                'AstkIsuNo': AstkIsuNo,
                'AstkBnsTpCode': AstkBnsTpCode,
                'AstkOrdprcPtnCode': AstkOrdprcPtnCode,
                'AstkOrdCndiTpCode': AstkOrdCndiTpCode,
                'AstkOrdQty': AstkOrdQty,
                'AstkOrdPrc': AstkOrdPrc,
                'OrdTrdTpCode': OrdTrdTpCode,
                'OrgOrdNo': OrgOrdNo,
            },
        }
        headers = {'cont_yn': cont_yn, 'cont_key': cont_key}
        return self._client.post(self.PATHS['ov_stock_order'], body, extra_headers=headers)

    def ov_stock_inquire_executions(
        self,
        *,
        QrySrtDt: str,
        QryEndDt: str,
        AstkIsuNo: str,
        AstkBnsTpCode: str,
        OrdxctTpCode: str,
        StnlnTpCode: str,
        QryTpCode: str,
        OnlineYn: str,
        CvrgOrdYn: str,
        WonFcurrTpCode: str,
        cont_yn: str = 'N',
        cont_key: str = '',
    ) -> APIResponse:
        """해외주식 체결내역조회 (CAZCQ00100).

        해외주식 체결/미체결 내역을 조회하는 API입니다. ※ 모의투자 계좌로 사용가능한 API입니다. ※ 원화환산은 가장 최근
        최초고시환율을 기준으로 계산합니다. ※ 체결내역이 전부 표시되지 않는경우 연속키 조회를 통해 확인하실 수 있습니다.

        엔드포인트: POST /api/v1/trading/overseas-stock/inquiry/transaction-history
        유량제어: 2 TPS
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=e4726f55-cc3b-45af-a1b5-852628fe5960&api_id=6aca1814-eea1-4e5c-94da-828143c343f2

        Args:
            QrySrtDt: 조회시작일자 — "": 당일조회 기간조회시 YYYYMMDD 형식의 날짜 입력 (EX.20240101)
            QryEndDt: 조회종료일자 — "": 당일조회 기간조회시 YYYYMMDD 형식의 날짜 입력 (EX.20240102)
            AstkIsuNo: 해외주식종목번호 — 미국주식/ETF: "종목코드" (EX. AAPL, SOXL, QQQ) 종목코드 미입력시 전체 종목 조회
            AstkBnsTpCode: 해외주식매매구분코드 — 0.전체 1.매도 2.매수
            OrdxctTpCode: 주문체결구분코드 — 0:전체 1:체결 2:미체결
            StnlnTpCode: 정렬구분코드 — 0:역순 1:정순
            QryTpCode: 조회구분코드 — 0:합산별 1:건별
            OnlineYn: 온라인여부 — 0:전체 Y:온라인 N:오프라인
            CvrgOrdYn: 반대매매주문여부 — 0:전체 Y:반대매매 N:일반주문
            WonFcurrTpCode: 원화외화구분코드 — 1:원화 2:외화
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. 주요 응답 필드:
              - Out: Out
              - OrdDt: 주문일자
              - OrdNo: 주문번호
              - ExecNo: 체결번호
              - OrgOrdNo: 원주문번호
              - AstkIsuNo: 해외주식종목번호
              - AstkHanglIsuNm: 해외주식한글종목명
              - SymCode: 심볼코드
              - OwnSeCode: 자체증권거래소코드
              - AstkSeNm: 해외주식증권거래소명
              - ShtnCntrySymCode: 단축국가심볼코드
              - CntryNm: 국가명
              - AstkBnsTpCode: 해외주식매매구분코드
              - OtptItemNm1: 출력항목명1
              - AstkOrdQty: 해외주식주문수량
              - (이하 생략 — 가이드 참조)

        """
        body = {
            'In': {
                'QrySrtDt': QrySrtDt,
                'QryEndDt': QryEndDt,
                'AstkIsuNo': AstkIsuNo,
                'AstkBnsTpCode': AstkBnsTpCode,
                'OrdxctTpCode': OrdxctTpCode,
                'StnlnTpCode': StnlnTpCode,
                'QryTpCode': QryTpCode,
                'OnlineYn': OnlineYn,
                'CvrgOrdYn': CvrgOrdYn,
                'WonFcurrTpCode': WonFcurrTpCode,
            },
        }
        headers = {'cont_yn': cont_yn, 'cont_key': cont_key}
        return self._client.post(self.PATHS['ov_stock_inquire_executions'], body, extra_headers=headers)

    def ov_stock_inquire_balance_margin(
        self,
        *,
        TrxTpCode: str,
        CmsnTpCode: str,
        WonFcurrTpCode: str,
        DpntBalTpCode: str,
        cont_yn: str = 'N',
        cont_key: str = '',
    ) -> APIResponse:
        """해외주식 잔고/증거금 조회 (CAZCQ00400).

        해외주식 잔고조회 API 입니다. 보유중인 주식/증거금 잔고에 대한 정보를 제공합니다. ※ 모의투자 계좌로 사용가능한
        API입니다. ※ 잔고가 전부 표시되지 않는경우 연속키 조회를 통해 확인하실 수 있습니다. ※ 원화환산은 가장 최근 최초고시환율을
        기준으로 계산합니다. ※ 예수금, 잔고평가, 출금가능 등의 금액은 추정치로 실제와 차이가 있을 수 있습니다.

        엔드포인트: POST /api/v1/trading/overseas-stock/inquiry/balance-margin
        유량제어: 3 TPS
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=e4726f55-cc3b-45af-a1b5-852628fe5960&api_id=8b7f35a4-1d2c-4e56-921d-c0be4611d1ee

        Args:
            TrxTpCode: 처리구분코드 — 1:외화잔고 2:주식잔고상세 3:주식잔고(국가별) 9:당일실현손익
            CmsnTpCode: 수수료구분코드 — 0:전부 미포함 1:매수제비용만 포함 2:매수제비용+매도제비용
            WonFcurrTpCode: 원화외화구분코드 — 1:원화 2:외화
            DpntBalTpCode: 소수점잔고구분코드 — 0: 전체 1: 일반 2: 소수점
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. 주요 응답 필드:
              - Dps: 예수금
              - OrdAbleAmt: 주문가능금액
              - MnyoutAbleAmt: 출금가능금액
              - BalEvalAmt: 잔고평가금액
              - EvalPnlAmt: 평가손익금액
              - ErnRat: 수익율
              - PchsAmt: 매입금액
              - Cmsn: 수수료
              - TaxAmt: 세금금액
              - ThdayRlzPnlAmt: 당일실현손익금액
              - AssetAmtTotamt: 자산금액총액
              - UnsttAmt: 미결제금액
              - Out1: Out1
              - CrcyCode: 통화코드
              - CrcyCodeNm: 통화코드명
              - (이하 생략 — 가이드 참조)

        """
        body = {
            'In': {
                'TrxTpCode': TrxTpCode,
                'CmsnTpCode': CmsnTpCode,
                'WonFcurrTpCode': WonFcurrTpCode,
                'DpntBalTpCode': DpntBalTpCode,
            },
        }
        headers = {'cont_yn': cont_yn, 'cont_key': cont_key}
        return self._client.post(self.PATHS['ov_stock_inquire_balance_margin'], body, extra_headers=headers)

    def ov_stock_inquire_trade_history(
        self,
        *,
        QrySrtDt: str,
        QryEndDt: str,
        AstkIsuNo: str,
        AstkBnsTpCode: str,
        StnlnTpCode: str,
        QryTpCode: str,
        WonFcurrTpCode: str,
        BaseDdTpCode: str,
        DpntBalTpCode: str,
        cont_yn: str = 'N',
        cont_key: str = '',
    ) -> APIResponse:
        """해외주식 매매내역 조회 (CAZCQ00200).

        해외주식 매매내역을 조회하는 API입니다. ※ 모의투자 계좌로 사용가능한 API입니다. ※ 원화환산은 가장 최근 최초고시환율을
        기준으로 계산합니다. ※ 매매내역이 전부 표시되지 않는경우 연속키 조회를 통해 확인하실 수 있습니다.

        엔드포인트: POST /api/v1/trading/overseas-stock/inquiry/trading-history
        유량제어: 2 TPS
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=e4726f55-cc3b-45af-a1b5-852628fe5960&api_id=f70342e8-2f36-4e6f-9a60-807da4fd0522

        Args:
            QrySrtDt: 조회시작일자 — YYYYMMDD EX.20240101
            QryEndDt: 조회종료일자 — YYYYMMDD EX.20240105
            AstkIsuNo: 해외주식종목번호 — 미국주식/ETF: "종목코드" (EX. AAPL, SOXL, QQQ)
            AstkBnsTpCode: 해외주식매매구분코드 — 0:전체 1:매도 2:매수
            StnlnTpCode: 정렬구분코드 — 0:역순 1:정순
            QryTpCode: 조회구분코드 — 0:합산별 1:건별
            WonFcurrTpCode: 원화외화구분코드 — 1:원화 2:외화
            BaseDdTpCode: 기준일구분코드 — 1:매매일 2:결제일
            DpntBalTpCode: 소수점잔고구분코드 — 0:전체 1:일반 2:소수점
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. 주요 응답 필드:
              - Out: Out
              - OrdDt: 주문일자
              - OrdNo: 주문번호
              - AstkMktCode: 해외주식시장코드
              - AstkMktNm: 해외주식시장명
              - AstkIsuNo: 해외주식종목번호
              - AstkHanglIsuNm: 해외주식한글종목명
              - SymCode: 심볼코드
              - OwnSeCode: 자체증권거래소코드
              - AstkSeNm: 해외주식증권거래소명
              - ShtnCntrySymCode: 단축국가심볼코드
              - AstkBnsTpCode: 해외주식매매구분코드
              - BnsTpNm: 매매구분명
              - AstkExecQty: 해외주식체결수량
              - AstkExecPrc: 해외주식체결가격
              - (이하 생략 — 가이드 참조)

        """
        body = {
            'In': {
                'QrySrtDt': QrySrtDt,
                'QryEndDt': QryEndDt,
                'AstkIsuNo': AstkIsuNo,
                'AstkBnsTpCode': AstkBnsTpCode,
                'StnlnTpCode': StnlnTpCode,
                'QryTpCode': QryTpCode,
                'WonFcurrTpCode': WonFcurrTpCode,
                'BaseDdTpCode': BaseDdTpCode,
                'DpntBalTpCode': DpntBalTpCode,
            },
        }
        headers = {'cont_yn': cont_yn, 'cont_key': cont_key}
        return self._client.post(self.PATHS['ov_stock_inquire_trade_history'], body, extra_headers=headers)

    def ov_stock_inquire_trading_history(
        self,
        *,
        QrySrtDt: str,
        QryEndDt: str,
        StnlnTpCode: str,
        AstkIsuNo: str,
        QryTpCode: str,
        DpntBalTpCode: str,
        cont_yn: str = 'N',
        cont_key: str = '',
    ) -> APIResponse:
        """해외주식 거래내역 조회 (CAZCQ01600).

        해외주식 계좌의 거래내역을 조회하는 API입니다. ※ 모의투자 계좌로 사용가능한 API입니다. ※ 거래내역이 전부 표시되지
        않는경우 연속키 조회를 통해 확인하실 수 있습니다.

        엔드포인트: POST /api/v1/trading/overseas-stock/inquiry/trade-history
        유량제어: 2 TPS
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=e4726f55-cc3b-45af-a1b5-852628fe5960&api_id=141f22b1-b905-4f65-a462-6a0a744f3075

        Args:
            QrySrtDt: 조회시작일자 — YYYYMMDD EX.20240101
            QryEndDt: 조회종료일자 — YYYYMMDD EX.20240110
            StnlnTpCode: 정렬구분코드 — 0:역순 1:정순
            AstkIsuNo: 해외주식종목번호 — 미국주식/ETF: "종목코드" (EX. AAPL, SOXL, QQQ)
            QryTpCode: 조회구분코드 — 0:전체 1:입출금 2:입출고 3:매매
            DpntBalTpCode: 소수점잔고구분코드 — 0: 전체 1: 일반 2: 소수점
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. 주요 응답 필드:
              - Out: Out
              - TrdDt: 거래일자
              - TrdTime: 거래시각
              - SmryNm: 적요명
              - AstkIsuNo: 해외주식종목번호
              - AstkEngIsuNm: 해외주식영문종목명
              - AstkHanglIsuNm: 해외주식한글종목명
              - AstkMktCode: 해외주식시장코드
              - SymCode: 심볼코드
              - OwnSeCode: 자체증권거래소코드
              - AstkSeNm: 해외주식증권거래소명
              - CrcyCode: 통화코드
              - AstkTrdQty: 해외주식거래수량
              - AstkBnsAmt: 해외주식매매금액
              - AstkTrdUprc: 해외주식거래단가
              - (이하 생략 — 가이드 참조)

        """
        body = {
            'In': {
                'QrySrtDt': QrySrtDt,
                'QryEndDt': QryEndDt,
                'StnlnTpCode': StnlnTpCode,
                'AstkIsuNo': AstkIsuNo,
                'QryTpCode': QryTpCode,
                'DpntBalTpCode': DpntBalTpCode,
            },
        }
        headers = {'cont_yn': cont_yn, 'cont_key': cont_key}
        return self._client.post(self.PATHS['ov_stock_inquire_trading_history'], body, extra_headers=headers)

    def ov_stock_inquire_psbl_amount(
        self,
        *,
        TrxTpCode: str,
        AstkIsuNo: str,
        AstkOrdPrc: int,
        WonFcurrTpCode: str,
        cont_yn: str = 'N',
        cont_key: str = '',
    ) -> APIResponse:
        """해외주식 주문가능금액조회 (CAZCQ01300).

        해외주식 주문가능금액조회 API입니다. ※ 모의투자 계좌로 사용가능한 API입니다.

        엔드포인트: POST /api/v1/trading/overseas-stock/inquiry/able-orderqty
        유량제어: 2 TPS
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=e4726f55-cc3b-45af-a1b5-852628fe5960&api_id=0793f887-f97d-48f6-8808-630217c93022

        Args:
            TrxTpCode: 처리구분코드 — 1:매도 2:매수
            AstkIsuNo: 해외주식종목번호 — 미국주식/ETF: "종목코드" (EX. AAPL, SOXL, QQQ)
            AstkOrdPrc: 해외주식주문가격
            WonFcurrTpCode: 원화외화구분코드 — 1: 원화 2: 외화
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. 주요 응답 필드:
              - AstkOrdAbleAmt: 해외주식주문가능금액 — 해당통화 기준
              - AstkOrdAbleQty: 해외주식주문가능수량 — 해당통화 기준
              - AstkOrdAbleAmt0: 해외주식주문가능금액0 — 통합증거금 기준
              - AstkOrdAbleQty0: 해외주식주문가능수량0 — 통합증거금 기준
              - AstkOrdAbleAmt1: 해외주식주문가능금액1 — 미수금포함 기준
              - AstkOrdAbleQty1: 해외주식주문가능수량1 — 미수금포함 기준
              - CsldtMgnUseYn: 통합증거금사용여부 — (Y/N)
              - OtptItemNm0: 출력항목명0 — 통합증거금사용여부 (Y/N)
              - Mgnrt: 증거금율 — 종목증거금률
              - OtptItemNm1: 출력항목명1 — 계좌증거금률
              - Mgnrt0: 증거금율0 — 적용증거금률

        """
        body = {
            'In': {
                'TrxTpCode': TrxTpCode,
                'AstkIsuNo': AstkIsuNo,
                'AstkOrdPrc': AstkOrdPrc,
                'WonFcurrTpCode': WonFcurrTpCode,
            },
        }
        headers = {'cont_yn': cont_yn, 'cont_key': cont_key}
        return self._client.post(self.PATHS['ov_stock_inquire_psbl_amount'], body, extra_headers=headers)

    def ov_stock_inquire_realized_pnl(
        self,
        *,
        TrxTpCode: str,
        QrySrtDt: str,
        QryEndDt: str,
        AstkIsuNo: str,
        WonFcurrTpCode: str,
        EvrprcYn: str,
        DpntBalTpCode: str,
        cont_yn: str = 'N',
        cont_key: str = '',
    ) -> APIResponse:
        """해외주식 실현손익 조회 (CAZCQ00300).

        해외주식 실현손익을 조회하는 API입니다. ※ 모의투자 계좌로 사용가능한 API입니다. ※ 원화환산은 가장 최근 최초고시환율을
        기준으로 계산합니다. ※ 실현손익내역이 전부 표시되지 않는경우 연속키 조회를 통해 확인하실 수 있습니다.

        엔드포인트: POST /api/v1/trading/overseas-stock/inquiry/day-rlzpnl
        유량제어: 2 TPS
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=e4726f55-cc3b-45af-a1b5-852628fe5960&api_id=2c20c615-d03a-4afc-92f6-b00aed42eaeb

        Args:
            TrxTpCode: 처리구분코드 — 1:국가별 및 일별국가별 실현손익 2:일별국가별종목별 실현손익
            QrySrtDt: 조회시작일자 — YYYYMMDD EX.20240101
            QryEndDt: 조회종료일자 — YYYYMMDD EX.20240105
            AstkIsuNo: 해외주식종목번호 — 미국주식/ETF: "종목코드" (EX. AAPL, SOXL, QQQ)
            WonFcurrTpCode: 원화외화구분코드 — 1:원화 2:외화
            EvrprcYn: 제비용여부 — Y:예(기본) N:아니요
            DpntBalTpCode: 소수점잔고구분코드 — 0: 전체 1: 일반 2: 소수점
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. 주요 응답 필드:
              - Out2: Out2
              - AstkMktCode: 해외주식시장코드
              - AstkMktNm: 해외주식시장명
              - OrdDt: 주문일자
              - CrcyCode: 통화코드
              - AstkIsuNo: 해외주식종목번호
              - AstkHanglIsuNm: 해외주식한글종목명
              - SymCode: 심볼코드
              - OwnSeCode: 자체증권거래소코드
              - AstkSeNm: 해외주식증권거래소명
              - ShtnCntrySymCode: 단축국가심볼코드
              - AstkBuyExecQty: 해외주식매수체결수량 — 사용안함
              - AstkBuyExecAmt: 해외주식매수체결금액 — 사용안함
              - AstkAvrPchsPrc: 해외주식평균매입가
              - AstkBuyExecCmsn: 해외주식매수체결수수료 — 사용안함
              - (이하 생략 — 가이드 참조)

        """
        body = {
            'In': {
                'TrxTpCode': TrxTpCode,
                'QrySrtDt': QrySrtDt,
                'QryEndDt': QryEndDt,
                'AstkIsuNo': AstkIsuNo,
                'WonFcurrTpCode': WonFcurrTpCode,
                'EvrprcYn': EvrprcYn,
                'DpntBalTpCode': DpntBalTpCode,
            },
        }
        headers = {'cont_yn': cont_yn, 'cont_key': cont_key}
        return self._client.post(self.PATHS['ov_stock_inquire_realized_pnl'], body, extra_headers=headers)

    def ov_stock_inquire_deposit_detail(
        self,
        *,
        cont_yn: str = 'N',
        cont_key: str = '',
    ) -> APIResponse:
        """해외주식 예수금상세 (CAZCQ01400).

        해외주식 상세 예수금을 조회하는 API입니다. ※ 모의투자 계좌로 사용가능한 API입니다. ※ 원화환산은 가장 최근 최초고시환율을
        기준으로 계산합니다. ※ 예수금, 주문가능, 출금가능, 평가자산총액 등의 금액은 추정치로 실제와 차이가 있을 수 있습니다.

        엔드포인트: POST /api/v1/trading/overseas-stock/inquiry/deposit-detail
        유량제어: 2 TPS
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=e4726f55-cc3b-45af-a1b5-852628fe5960&api_id=44fd2ef3-756b-4715-a271-570397b33936

        Returns:
            APIResponse. 주요 응답 필드:
              - OtptItemNm: 출력항목명
              - DpsBaseDt0: 예수금기준일자0 — 당일기준
              - DpsBaseDt1: 예수금기준일자1 — D+1
              - DpsBaseDt2: 예수금기준일자2 — D+2
              - DpsBaseDt3: 예수금기준일자3 — D+3
              - DpsBaseDt4: 예수금기준일자4 — D+4
              - Out1: Out1
              - CrcyCode: 통화코드
              - CrcyCodeNm: 통화코드명
              - OtptItemNm0: 출력항목명0
              - OtptItemNm1: 출력항목명1
              - OtptItemNm2: 출력항목명2
              - OtptItemNm3: 출력항목명3
              - AstkDps0: 해외주식예수금0
              - AstkBnsAmt0: 해외주식매매금액0
              - (이하 생략 — 가이드 참조)

        """
        body = {
            'In': {},
        }
        headers = {'cont_yn': cont_yn, 'cont_key': cont_key}
        return self._client.post(self.PATHS['ov_stock_inquire_deposit_detail'], body, extra_headers=headers)

    def ov_stock_inquire_avg_buy_price(
        self,
        *,
        AstkIsuNo: str,
        cont_yn: str = 'N',
        cont_key: str = '',
    ) -> APIResponse:
        """해외주식 평균매입단가 조회 (CAZCQ03400).

        보유중인 해외주식 종목의 평균 매입단가를 조회할 수 있는 API입니다.

        엔드포인트: POST /api/v1/trading/overseas-stock/inquiry/avg-pur-price
        유량제어: 2 TPS
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=e4726f55-cc3b-45af-a1b5-852628fe5960&api_id=cd7db5da-e848-4d0f-b64d-3476f3b820cd

        Args:
            AstkIsuNo: 해외주식종목번호 — 미국주식/ETF: "종목코드" (EX. AAPL, SOXL, QQQ)
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. 주요 응답 필드:
              - AstkAvrPchsPrc: 해외주식평균매입가
              - AstkMktCode: 해외주식시장코드
              - OwnSeCode: 자체증권거래소코드

        """
        body = {
            'In': {
                'AstkIsuNo': AstkIsuNo,
            },
        }
        headers = {'cont_yn': cont_yn, 'cont_key': cont_key}
        return self._client.post(self.PATHS['ov_stock_inquire_avg_buy_price'], body, extra_headers=headers)
