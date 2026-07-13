"""국내선물옵션시세 API 모듈.

DB증권 OpenAPI 그룹: 국내선물옵션시세
group_slug: kr_futopt_quote

이 파일은 `_specs/kr_futopt_quote/*.json` 에서 자동 생성되었습니다.
스펙이 갱신되면 `_workspace/build_modules.py`로 재생성하세요.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from dbsec_sdk.client import DBSecClient

from dbsec_sdk.response import APIResponse


class KrFutoptQuoteAPI:
    """국내선물옵션시세 API 모음.

    사용법:
        >>> client = DBSecClient("config.yaml")
        >>> resp = client.apis.kr_futopt_quote.<method>(...)
    """

    # API 경로 매핑
    PATHS = {
        'kr_futopt_search_futures': '/api/v1/quote/kr-futureoption/inquiry/future-ticker',
        'kr_futopt_search_options': '/api/v1/quote/kr-futureoption/inquiry/option-ticker',
        'kr_futopt_inquire_price_multi': '/api/v1/quote/kr-futureoption/inquiry/multiprice',
        'kr_futopt_inquire_price': '/api/v1/quote/kr-futureoption/inquiry/price',
        'kr_futopt_inquire_orderbook': '/api/v1/quote/kr-futureoption/inquiry/orderbook',
        'kr_futopt_inquire_daily_executions': '/api/v1/quote/kr-futureoption/inquiry/daily-price',
        'kr_futopt_inquire_time_execution': '/api/v1/quote/kr-futureoption/inquiry/hour-price',
        'kr_futopt_option_board': '/api/v1/quote/kr-futureoption/inquiry/option-board',
    }
    # TR 코드 매핑
    TR_CODES = {
        'kr_futopt_search_futures': 'FCODES',
        'kr_futopt_search_options': 'OCODES',
        'kr_futopt_inquire_price_multi': 'FOMULTIPRICE',
        'kr_futopt_inquire_price': 'FOPRICE',
        'kr_futopt_inquire_orderbook': 'HOGA',
        'kr_futopt_inquire_daily_executions': 'DAYTRADE',
        'kr_futopt_inquire_time_execution': 'CONCLUSION',
        'kr_futopt_option_board': 'OSTOCK_CONDT',
    }

    def __init__(self, client: 'DBSecClient'):
        self._client = client

    def kr_futopt_search_futures(
        self,
        *,
        InputCondMrktDivCode: str,
        cont_yn: str = 'N',
        cont_key: str = '',
    ) -> APIResponse:
        """선물종목 조회 (FCODES).

        국내선물 종목조회 API입니다. ※ 연속키 조회를 통해 종목을 추가로 조회 할 수 있습니다.

        엔드포인트: POST /api/v1/quote/kr-futureoption/inquiry/future-ticker
        유량제어: 3 TPS
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=80d95623-7135-481b-b109-d7370f1a261b&api_id=43e60397-77df-4926-8969-3eb18f9f48e3

        Args:
            InputCondMrktDivCode: 입력조건시장분류코드 — F : 지수선물 JF : 주식선물 KF : 미니선물 CF : 상품선물 XF : 섹터선물 CM : 야간선물 EC : 야간상품선물 ES : KOSDAQ150선물 EK : 야간미니선물
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. 주요 응답 필드:
              - Out: Out
              - Mxpr1st: 1단계상한가
              - UnasShrnIscd: 기초자산종목코드
              - Llam3rd: 3단계하한가
              - Llam2nd: 2단계하한가
              - Llam1st: 1단계하한가
              - Mxpr3rd: 3단계상한가
              - Mxpr2nd: 2단계상한가
              - Iscd: 종목코드
              - StndIscd: 표준종목코드
              - KorIsnm: 한글종목명
              - Sdpr: 기준가

        """
        body = {
            'In': {
                'InputCondMrktDivCode': InputCondMrktDivCode,
            },
        }
        headers = {'cont_yn': cont_yn, 'cont_key': cont_key}
        return self._client.post(self.PATHS['kr_futopt_search_futures'], body, extra_headers=headers)

    def kr_futopt_search_options(
        self,
        *,
        InputCondMrktDivCode: str,
        cont_yn: str = 'N',
        cont_key: str = '',
    ) -> APIResponse:
        """옵션종목 조회 (OCODES).

        국내옵션 종목조회 API입니다. ※ 연속키 조회를 통해 종목을 추가로 조회 할 수 있습니다.

        엔드포인트: POST /api/v1/quote/kr-futureoption/inquiry/option-ticker
        유량제어: 10 TPS
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=80d95623-7135-481b-b109-d7370f1a261b&api_id=a51e61c7-a77f-408c-99bd-69f1ae4df730

        Args:
            InputCondMrktDivCode: 입력조건시장분류코드 — O : 지수옵션 JO : 주식옵션 KO : 미니옵션 WO : K200위클리옵션 EU : 야간옵션 SO : 코스닥 150옵션 EQ : KOSDAQ150옵션(야간) EM : 미니옵션(야간) EW : 위클리옵션(야간)
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. 주요 응답 필드:
              - Out: Out
              - Mxpr1st: 1단계상한가
              - UnasIsnm: 기초자산명
              - Mxpr2nd: 2단계상한가
              - Mxpr3rd: 3단계상한가
              - Llam1st: 1단계하한가
              - Llam2nd: 2단계하한가
              - Llam3rd: 3단계하한가
              - Acpr: 행사가
              - RmnnDynu: 잔존만기
              - Iscd: 종목코드
              - StndIscd: 표준종목코드
              - KorIsnm: 한글종목명
              - AtmClsCode: ATM구분코드
              - TrMltl: 거래승수
              - (이하 생략 — 가이드 참조)

        """
        body = {
            'In': {
                'InputCondMrktDivCode': InputCondMrktDivCode,
            },
        }
        headers = {'cont_yn': cont_yn, 'cont_key': cont_key}
        return self._client.post(self.PATHS['kr_futopt_search_options'], body, extra_headers=headers)

    def kr_futopt_inquire_price_multi(
        self,
        *,
        dataCnt: int,
        InputCondMrktDivCode1: str,
        InputIscd1: str,
        InputCondMrktDivCode2: str,
        InputIscd2: str,
        InputCondMrktDivCode3: str,
        InputIscd3: str,
        InputCondMrktDivCode4: str,
        InputIscd4: str,
        InputCondMrktDivCode5: str,
        InputIscd5: str,
        cont_yn: str = 'N',
        cont_key: str = '',
    ) -> APIResponse:
        """국내선옵 멀티현재가 조회 (FOMULTIPRICE).

        국내선물옵션 멀티 현재가 조회 API입니다. ※ 1회 호출에 최대 50종목의 시세를 확인 가능합니다. ※ "dataCnt" 필드에
        요청할 데이터의 개수를 입력하여 호출이 가능 합니다. (1~50) ※ "dataCnt" 필드의 값과 입력 데이터의 개수가 일치하지
        않으면 호출이 불가합니다. ※ 아래와 같이시장구분필드와 종목코드가 1:1 쌍을 이뤄야 호출이 정상적으로 이뤄집니다. -
        InputIscd1:F (시장구분필드), - InputCondMrktDivCode1:A0166000 (종목코드) ※
        [InputIscd1 ~ InputCondMrktDivCode1] & [InputCondMrktDivCode50 ~
        InputCondMrktDivCode50]과 같이 최대 50건 호출이 가능합니다.

        엔드포인트: POST /api/v1/quote/kr-futureoption/inquiry/multiprice
        유량제어: 2 TPS
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=80d95623-7135-481b-b109-d7370f1a261b&api_id=0d013d41-68cb-4ccb-92e6-893e27048217

        Args:
            dataCnt: 호출건수 — 1~50사이의 값 입력
            InputCondMrktDivCode1: 입력조건시장분류코드1 — F : 지수선물 JF : 주식선물 KF : 미니선물 CF : 상품선물 XF : 섹터선물 CM : 야간선물 EK : 야간미니선물 O : 지수옵션 JO : 주식옵션 KO : 미니옵션 WO : K200위클리옵션 EU : 야간옵션 EW : 위클리옵션(야간) SO: 코스닥 150옵션
            InputIscd1: 입력종목코드1 — 종목코드 입력 ex. 101VC000
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. 주요 응답 필드:
              - Out: Out
              - Iscd: 종목코드
              - Prpr: 현재가
              - Mxpr: 상한가
              - Llam: 하한가
              - Oprc: 시가
              - SdprVrssMrktRate: 기준가대비시가비율
              - PrprVrssOprcRate: 현재가대비시가비율
              - Hprc: 고가
              - SdprVrssHgprRate: 기준가대비고가비율
              - PrprVrssHgprRate: 현재가대비고가비율
              - Lprc: 저가
              - SdprVrssLwprRate: 기준가대비저가비율
              - PrprVrssLwprRate: 현재가대비저가비율
              - PrdyVrss: 전일대비
              - (이하 생략 — 가이드 참조)

        """
        body = {
            'In': {
                'dataCnt': dataCnt,
                'InputCondMrktDivCode1': InputCondMrktDivCode1,
                'InputIscd1': InputIscd1,
                'InputCondMrktDivCode2': InputCondMrktDivCode2,
                'InputIscd2': InputIscd2,
                'InputCondMrktDivCode3': InputCondMrktDivCode3,
                'InputIscd3': InputIscd3,
                'InputCondMrktDivCode4': InputCondMrktDivCode4,
                'InputIscd4': InputIscd4,
                'InputCondMrktDivCode5': InputCondMrktDivCode5,
                'InputIscd5': InputIscd5,
            },
        }
        headers = {'cont_yn': cont_yn, 'cont_key': cont_key}
        return self._client.post(self.PATHS['kr_futopt_inquire_price_multi'], body, extra_headers=headers)

    def kr_futopt_inquire_price(
        self,
        *,
        InputCondMrktDivCode: str,
        InputIscd1: str,
        cont_yn: str = 'N',
        cont_key: str = '',
    ) -> APIResponse:
        """현재가조회 (FOPRICE).

        국내선물옵션 현재가 조회 API입니다.

        엔드포인트: POST /api/v1/quote/kr-futureoption/inquiry/price
        유량제어: 5 TPS
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=80d95623-7135-481b-b109-d7370f1a261b&api_id=18f56401-9d9e-49c6-8e6b-3b226c1dc222

        Args:
            InputCondMrktDivCode: 입력조건시장분류코드 — F : 지수선물 JF : 주식선물 KF : 미니선물 CF : 상품선물 XF : 섹터선물 CM : 야간선물 EK : 야간미니선물 O : 지수옵션 JO : 주식옵션 KO : 미니옵션 WO : K200위클리옵션 EU : 야간옵션 EW : 위클리옵션(야간) SO: 코스닥 150옵션
            InputIscd1: 입력종목코드1 — 종목코드 입력 ex. 101VC000
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. 주요 응답 필드:
              - Thrr: 이론가
              - AcmlTrPbmn: 거래대금
              - AcmlVol: 거래량
              - PrdyVol: 전일거래량
              - Bidp1: 매수호가
              - Askp1: 매도호가
              - HtsOtstStplQty: 미결제약정수량
              - OtstStplQtyIcdc: 미결제증감
              - Dprt: 괴리율
              - PrdyVrss: 전일대비
              - PrdyCtrt: 전일대비율
              - MrktBasis: 시장베이시스
              - Prpr: 현재가
              - Mxpr: 상한가
              - Llam: 하한가
              - (이하 생략 — 가이드 참조)

        """
        body = {
            'In': {
                'InputCondMrktDivCode': InputCondMrktDivCode,
                'InputIscd1': InputIscd1,
            },
        }
        headers = {'cont_yn': cont_yn, 'cont_key': cont_key}
        return self._client.post(self.PATHS['kr_futopt_inquire_price'], body, extra_headers=headers)

    def kr_futopt_inquire_orderbook(
        self,
        *,
        InputCondMrktDivCode: str,
        InputIscd1: str,
        cont_yn: str = 'N',
        cont_key: str = '',
    ) -> APIResponse:
        """호가조회 (HOGA).

        국내선물옵션 호가 조회 API입니다.

        엔드포인트: POST /api/v1/quote/kr-futureoption/inquiry/orderbook
        유량제어: 5 TPS
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=80d95623-7135-481b-b109-d7370f1a261b&api_id=0ecec614-4830-4a7c-a0a0-7ba65cb54f3d

        Args:
            InputCondMrktDivCode: 입력조건시장분류코드 — F : 지수선물 JF : 주식선물 KF : 미니선물 CF : 상품선물 XF : 섹터선물 CM : 야간선물 O : 지수옵션 JO : 주식옵션 KO : 미니옵션 WO : K200위클리옵션 EU : 야간옵션 SO: 코스닥 150옵션
            InputIscd1: 입력종목코드1 — 종목코드 입력 ex. 005930
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
        return self._client.post(self.PATHS['kr_futopt_inquire_orderbook'], body, extra_headers=headers)

    def kr_futopt_inquire_daily_executions(
        self,
        *,
        InputCondMrktDivCode: str,
        InputIscd1: str,
        InputHourClsCode: str,
        cont_yn: str = 'N',
        cont_key: str = '',
    ) -> APIResponse:
        """일별체결조회 (DAYTRADE).

        국내선물옵션 일별 체결조회 API입니다.

        엔드포인트: POST /api/v1/quote/kr-futureoption/inquiry/daily-price
        유량제어: 2 TPS
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=80d95623-7135-481b-b109-d7370f1a261b&api_id=a6870035-beab-4c43-a0c2-86f102c330c7

        Args:
            InputCondMrktDivCode: 입력조건시장분류코드 — F : 지수선물 JF : 주식선물 KF : 미니선물 CF : 상품선물 XF : 섹터선물 CM : 야간선물 O : 지수옵션 JO : 주식옵션 KO : 미니옵션 WO : K200위클리옵션 EU : 야간옵션 SO: 코스닥 150옵션
            InputIscd1: 입력종목코드1 — 종목코드 입력 ex. 005930
            InputHourClsCode: 입력시간구분코드 — 1: 시간외단일가체결 2: 장전+장중+장후 3: 장전+장후 4: 장중 5: 장전+장중+장후+장종료(예상포함) 6: 예상제외 모두 7: 장전+장중+장후+장종료(예상불포함) 8: 예상 9: 장전+장중+장후+장종료 (예상,대량, 바스켓, 정리매매 제외) 10: 시간외단일가 예상
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. 주요 응답 필드:
              - Hour: 시간
              - Prpr: 현재가
              - PrdyVrssSign: 전일대비부호
              - PrdyVrss: 전일대비
              - ShnuCnqn: 매수체결량
              - SelnCnqn: 매도체결량

        """
        body = {
            'In': {
                'InputCondMrktDivCode': InputCondMrktDivCode,
                'InputIscd1': InputIscd1,
                'InputHourClsCode': InputHourClsCode,
            },
        }
        headers = {'cont_yn': cont_yn, 'cont_key': cont_key}
        return self._client.post(self.PATHS['kr_futopt_inquire_daily_executions'], body, extra_headers=headers)

    def kr_futopt_inquire_time_execution(
        self,
        *,
        InputCondMrktDivCode: str,
        InputIscd1: str,
        cont_yn: str = 'N',
        cont_key: str = '',
    ) -> APIResponse:
        """시간대별체결조회 (CONCLUSION).

        국내선물옵션 시간대별 체결조회 API입니다.

        엔드포인트: POST /api/v1/quote/kr-futureoption/inquiry/hour-price
        유량제어: 2 TPS
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=80d95623-7135-481b-b109-d7370f1a261b&api_id=587bb0f9-55bd-428e-b8e2-d5ab92c1eb5c

        Args:
            InputCondMrktDivCode: 입력조건시장분류코드 — F : 지수선물 JF : 주식선물 KF : 미니선물 CF : 상품선물 XF : 섹터선물 CM : 야간선물 O : 지수옵션 JO : 주식옵션 KO : 미니옵션 WO : K200위클리옵션 EU : 야간옵션 SO: 코스닥 150옵션
            InputIscd1: 입력종목코드1 — 종목코드 입력 ex. 005930
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. 주요 응답 필드:
              - Hour: 시간
              - Prpr: 현재가
              - PrdyVrssSign: 전일대비부호
              - PrdyCtrt: 전일대비율
              - CntgVol: 체결거래량

        """
        body = {
            'In': {
                'InputCondMrktDivCode': InputCondMrktDivCode,
                'InputIscd1': InputIscd1,
            },
        }
        headers = {'cont_yn': cont_yn, 'cont_key': cont_key}
        return self._client.post(self.PATHS['kr_futopt_inquire_time_execution'], body, extra_headers=headers)

    def kr_futopt_option_board(
        self,
        *,
        InputCondMrktDivCode1: str,
        InputMtrtYymm1: str,
        InputTrgtClsCode: str,
        cont_yn: str = 'N',
        cont_key: str = '',
    ) -> APIResponse:
        """옵션전광판 (OSTOCK_CONDT).

        당사 HTS [2501] - "선옵 만기월별시세" 화면과 유시한 기능을 제공하는 국내옵션 전광판 API입니다. ※ 행사가를
        기준으로 콜옵션/풋옵션 각 50종목에 대한 정보를 제공 합니다.

        엔드포인트: POST /api/v1/quote/kr-futureoption/inquiry/option-board
        유량제어: 1 TPS
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=80d95623-7135-481b-b109-d7370f1a261b&api_id=cc54c7e7-2e86-4688-b5cb-f5630fe48c60

        Args:
            InputCondMrktDivCode1: 입력조건시장분류코드1 — O : 지수옵션 KO : 미니옵션 WO : 위클리옵션 EU : 야간옵션 SO : 코스닥 150옵션 EQ : 코스닥 150옵션(야간) EM : 미니옵션(야간) EW : 위클리옵션(야간)
            InputMtrtYymm1: 입력입력만기년월1 — 일반옵션 : YYYYMM (ex.202602) 위클리옵션 : YYMMWW (ex.2602W3 -> 26년2월3주) W뒤의 숫자는 주차를 의미 (ex. 1주차 : W1, 2주차 W2 )
            InputTrgtClsCode: 입력대상구분코드 — 위클리 옵션 조회시에만 사용. 그 외 옵션 분류코드 사용시 "" 공백 입력 WKM : 코스피200 위클리 월 만기 WKI : 코스피200 위클리 목 만기 WQM : 코스닥150 위클리 월 만기 WQI : 코스닥150 위클리 목 만기
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. 주요 응답 필드:
              - OptnClsCode: 옵션구분코드 — 2 : 콜 3 : 풋
              - Acpr: 행사가
              - NearAtm: ATM구분코드
              - Iscd: 종목코드
              - Prpr: 현재가
              - PrdyVrss: 전일대비
              - PrdyVrssSign: 전일대비부호
              - PrdyCtrt: 전일대비율
              - Askp1: 매도호가1
              - Bidp1: 매수호가1
              - CntgVol: 체결거래량
              - TotalAskpCsnu: 총매도호가건수
              - TotalBidpCsnu: 총매수호가건수
              - TotalAskpRsqn: 총매도호가잔량
              - TotalBidpRsqn: 총매수호가잔량
              - (이하 생략 — 가이드 참조)

        """
        body = {
            'In': {
                'InputCondMrktDivCode1': InputCondMrktDivCode1,
                'InputMtrtYymm1': InputMtrtYymm1,
                'InputTrgtClsCode': InputTrgtClsCode,
            },
        }
        headers = {'cont_yn': cont_yn, 'cont_key': cont_key}
        return self._client.post(self.PATHS['kr_futopt_option_board'], body, extra_headers=headers)
