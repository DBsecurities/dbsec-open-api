"""해외주식시세 API 모듈.

DB증권 OpenAPI 그룹: 해외주식시세
group_slug: ov_stock_quote

이 파일은 `_specs/ov_stock_quote/*.json` 에서 자동 생성되었습니다.
스펙이 갱신되면 `_workspace/build_modules.py`로 재생성하세요.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from dbsec_sdk.client import DBSecClient

from dbsec_sdk.response import APIResponse


class OvStockQuoteAPI:
    """해외주식시세 API 모음.

    사용법:
        >>> client = DBSecClient("config.yaml")
        >>> resp = client.apis.ov_stock_quote.<method>(...)
    """

    # API 경로 매핑
    PATHS = {
        'ov_stock_search_stocks': '/api/v1/quote/overseas-stock/inquiry/stock-ticker',
        'ov_stock_inquire_price_multi': '/api/v1/quote/overseas-stock/inquiry/multiprice',
        'ov_stock_inquire_price': '/api/v1/quote/overseas-stock/inquiry/price',
        'ov_stock_inquire_orderbook': '/api/v1/quote/overseas-stock/inquiry/orderbook',
        'ov_stock_inquire_time_execution': '/api/v1/quote/overseas-stock/inquiry/hour-price',
        'ov_stock_chart_tick': '/api/v1/quote/overseas-stock/chart/tick',
        'ov_stock_chart_min': '/api/v1/quote/overseas-stock/chart/min',
        'ov_stock_chart_day': '/api/v1/quote/overseas-stock/chart/day',
        'ov_stock_chart_week': '/api/v1/quote/overseas-stock/chart/week',
        'ov_stock_chart_month': '/api/v1/quote/overseas-stock/chart/month',
        'ov_stock_inquire_condition_rise_fall': '/api/v1/quote/overseas-stock/inquiry/rank-list',
    }
    # TR 코드 매핑
    TR_CODES = {
        'ov_stock_search_stocks': 'FSTKCODES',
        'ov_stock_inquire_price_multi': 'FSTKMULTIPRICE',
        'ov_stock_inquire_price': 'FSTKPRICE',
        'ov_stock_inquire_orderbook': 'FSTKHOGA',
        'ov_stock_inquire_time_execution': 'FSTKCONCLUSION',
        'ov_stock_chart_tick': 'FSTKCHARTTICK',
        'ov_stock_chart_min': 'FSTKCHARTMIN',
        'ov_stock_chart_day': 'FSTKCHARTDAY',
        'ov_stock_chart_week': 'FSTKCHARTWEEK',
        'ov_stock_chart_month': 'FSTKCHARTMONTH',
        'ov_stock_inquire_condition_rise_fall': 'FSTKRANKLIST',
    }

    def __init__(self, client: 'DBSecClient'):
        self._client = client

    def ov_stock_search_stocks(
        self,
        *,
        InputDataCode: str,
        cont_yn: str = 'N',
        cont_key: str = '',
    ) -> APIResponse:
        """해외주식종목 조회 (FSTKCODES).

        해외주식 종목 조회 API 입니다.

        엔드포인트: POST /api/v1/quote/overseas-stock/inquiry/stock-ticker
        유량제어: 2 TPS
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=a804e311-cb53-499b-9d8a-a4d838f0a484&api_id=22c67f31-c325-4898-8929-6ba9836d982f

        Args:
            InputDataCode: 입력해외증시구분코드 — NY: 뉴욕 NA: 나스닥 AM: 아멕스
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. 주요 응답 필드:
              - Out: Out
              - Iscd: 종목코드
              - KorIsnm: 한글종목명
              - BstpLargName: 업종대분류명
              - ExchClsCode2: 거래소코드2
              - SelnVolUnit: 매도량단위
              - ShnuVolUnit: 매수량단위

        """
        body = {
            'In': {
                'InputDataCode': InputDataCode,
            },
        }
        headers = {'cont_yn': cont_yn, 'cont_key': cont_key}
        return self._client.post(self.PATHS['ov_stock_search_stocks'], body, extra_headers=headers)

    def ov_stock_inquire_price_multi(
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
        """해외주식 멀티현재가조회 (FSTKMULTIPRICE).

        해외주식시세 멀티 현재가 조회 API입니다. ※ 1회 호출에 최대 50종목의 시세를 확인 가능합니다. ※ "dataCnt" 필드에
        요청할 데이터의 개수를 입력하여 호출이 가능 합니다. (1~50) ※ "dataCnt" 필드의 값과 입력 데이터의 개수가 일치하지
        않으면 호출이 불가합니다. ※ 아래와 같이시장구분필드와 종목코드가 1:1 쌍을 이뤄야 호출이 정상적으로 이뤄집니다. -
        InputIscd1:J (시장구분필드), - InputCondMrktDivCode1:005930 (종목코드) ※
        [InputIscd1 ~ InputCondMrktDivCode1] & [InputCondMrktDivCode50 ~
        InputCondMrktDivCode50]과 같이 최대 50건 호출이 가능합니다.

        엔드포인트: POST /api/v1/quote/overseas-stock/inquiry/multiprice
        유량제어: 1 TPS
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=a804e311-cb53-499b-9d8a-a4d838f0a484&api_id=729276aa-9913-444e-b637-8efc316de84e

        Args:
            dataCnt: 호출건수 — 1~50사이의 값 입력
            InputCondMrktDivCode1: 입력조건시장분류코드1 — FY:뉴욕 FN:나스닥 FA:아멕스
            InputIscd1: 입력종목코드1 — 해외주식 종목코드 (ex. TQQQ)
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. 주요 응답 필드:
              - Out: Out
              - Iscd: 종목코드
              - KorIsnm: 한글종목명
              - Sdpr: 기준가
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
        return self._client.post(self.PATHS['ov_stock_inquire_price_multi'], body, extra_headers=headers)

    def ov_stock_inquire_price(
        self,
        *,
        InputCondMrktDivCode: str,
        InputIscd1: str,
        cont_yn: str = 'N',
        cont_key: str = '',
    ) -> APIResponse:
        """해외주식현재가조회 (FSTKPRICE).

        해외주식 현재가 조회 API 입니다.

        엔드포인트: POST /api/v1/quote/overseas-stock/inquiry/price
        유량제어: 2 TPS
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=a804e311-cb53-499b-9d8a-a4d838f0a484&api_id=1c4d54aa-9f0f-4036-bb76-202c7116398d

        Args:
            InputCondMrktDivCode: 입력조건시장분류코드 — FY:뉴욕 FN:나스닥 FA:아멕스
            InputIscd1: 입력종목코드1 — 해외주식 종목코드 (ex. TQQQ)
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. 주요 응답 필드:
              - Sdpr: 기준가
              - prdyVol: 전일거래량
              - AcmlVol: 거래량
              - AcmlTrPbmn: 거래대금
              - Per: PER
              - PrdyCtrt: 전일대비율
              - PrdyVrss: 전일대비
              - askp1: 매도호가
              - bidp1: 매수호가
              - Prpr: 현재가
              - Mxpr: 상한가
              - Llam: 하한가
              - Oprc: 시가
              - SdprVrssMrktRate: 기준가대비시가비율
              - PrprVrssOprcRate: 현재가대비시가비율
              - (이하 생략 — 가이드 참조)

        """
        body = {
            'In': {
                'InputCondMrktDivCode': InputCondMrktDivCode,
                'InputIscd1': InputIscd1,
            },
        }
        headers = {'cont_yn': cont_yn, 'cont_key': cont_key}
        return self._client.post(self.PATHS['ov_stock_inquire_price'], body, extra_headers=headers)

    def ov_stock_inquire_orderbook(
        self,
        *,
        InputCondMrktDivCode: str,
        InputIscd1: str,
        cont_yn: str = 'N',
        cont_key: str = '',
    ) -> APIResponse:
        """해외주식호가조회 (FSTKHOGA).

        해외주식 호가 조회 API 입니다.

        엔드포인트: POST /api/v1/quote/overseas-stock/inquiry/orderbook
        유량제어: 2 TPS
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=a804e311-cb53-499b-9d8a-a4d838f0a484&api_id=70caf020-96aa-4ffb-8637-aae4ec54cb39

        Args:
            InputCondMrktDivCode: 입력조건시장분류코드 — FY:뉴욕 FN:나스닥 FA:아멕스
            InputIscd1: 입력종목코드1 — 해외주식 종목코드 (ex. TQQQ)
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
        return self._client.post(self.PATHS['ov_stock_inquire_orderbook'], body, extra_headers=headers)

    def ov_stock_inquire_time_execution(
        self,
        *,
        InputCondMrktDivCode: str,
        InputIscd1: str,
        InputHourClsCode: str,
        InputDivXtick: str,
        InputSctnClsCode: str,
        cont_yn: str = 'N',
        cont_key: str = '',
    ) -> APIResponse:
        """해외주식시간대별체결조회 (FSTKCONCLUSION).

        해외주식 시간대별 체결조회 API입니다.

        엔드포인트: POST /api/v1/quote/overseas-stock/inquiry/hour-price
        유량제어: 2 TPS
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=a804e311-cb53-499b-9d8a-a4d838f0a484&api_id=e4c85422-9d4a-4e46-917c-ef7988fba8c8

        Args:
            InputCondMrktDivCode: 입력조건시장분류코드 — FY:뉴욕 FN:나스닥 FA:아멕스
            InputIscd1: 입력종목코드1 — 해외주식 종목코드 입력 (ex. TQQQ)
            InputHourClsCode: 입력시간구분코드 — 0: 전체 1: 장전 2: 장중 3: 장후 4: 장전+장중 5: 장전+장후
            InputDivXtick: 입력X틱분틱일별구분코드 — 30: 30초 60: 1분 600: 10분 3600: 60분 [60*N: N분]
            InputSctnClsCode: 입력구간구분코드 — 0:default 1:당일 2:전일
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
                'InputHourClsCode': InputHourClsCode,
                'InputDivXtick': InputDivXtick,
                'InputSctnClsCode': InputSctnClsCode,
            },
        }
        headers = {'cont_yn': cont_yn, 'cont_key': cont_key}
        return self._client.post(self.PATHS['ov_stock_inquire_time_execution'], body, extra_headers=headers)

    def ov_stock_chart_tick(
        self,
        *,
        InputOrgAdjPrc: str,
        InputPwDataIncuYn: str,
        InputDate1: str,
        dataCnt: str,
        InputHourClsCode: str,
        InputCondMrktDivCode: str,
        InputIscd1: str,
        InputDate2: str,
        InputDivXtick: str,
        cont_yn: str = 'N',
        cont_key: str = '',
    ) -> APIResponse:
        """해외주식 틱차트조회 (FSTKCHARTTICK).

        해외주식 틱차트 조회 API 입니다.

        엔드포인트: POST /api/v1/quote/overseas-stock/chart/tick
        유량제어: 4 TPS
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=a804e311-cb53-499b-9d8a-a4d838f0a484&api_id=4811f7d4-439a-42be-b4a0-4d768874a997

        Args:
            InputOrgAdjPrc: 수정주가사용여부 — 0:수정주가 미사용 1: 수정주가 사용
            InputPwDataIncuYn: 기간지정여부코드 — "Y": 기간지정 "N":기간미지정 (InputDate2 부터 이전날짜 계속조회)
            InputDate1: 입력날짜1 — 조회 시작일을 YYYYMMDD 형식으로 입력 ex. 20241201
            dataCnt: 호출건수 — 입력범위: "1" ~ "2000" ""(공백입력) 또는 "0" 입력시 기본개수(400개)조회
            InputHourClsCode: 입력시간구분코드 — "0" 입력
            InputCondMrktDivCode: 입력조건시장분류코드 — FY:뉴욕 FN:나스닥 FA:아멕스
            InputIscd1: 입력종목코드1 — 해외주식 종목코드 (ex. TQQQ)
            InputDate2: 입력날짜2 — 조회 마감일을 YYYYMMDD 형식으로 입력 ex. 20241204 (이 날짜부터 이전 데이터를 조회합니다.)
            InputDivXtick: 틱분틱일별구분코드 — 틱건수 (기본값: 0)
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. 주요 응답 필드:
              - Out: Out
              - Hour: 시간
              - Date: 일자
              - Prpr: 현재가
              - Oprc: 시가
              - Hprc: 고가
              - Lprc: 저가
              - CntgVol: 체결거래량

        """
        body = {
            'In': {
                'InputOrgAdjPrc': InputOrgAdjPrc,
                'InputPwDataIncuYn': InputPwDataIncuYn,
                'InputDate1': InputDate1,
                'dataCnt': dataCnt,
                'InputHourClsCode': InputHourClsCode,
                'InputCondMrktDivCode': InputCondMrktDivCode,
                'InputIscd1': InputIscd1,
                'InputDate2': InputDate2,
                'InputDivXtick': InputDivXtick,
            },
        }
        headers = {'cont_yn': cont_yn, 'cont_key': cont_key}
        return self._client.post(self.PATHS['ov_stock_chart_tick'], body, extra_headers=headers)

    def ov_stock_chart_min(
        self,
        *,
        InputOrgAdjPrc: str,
        dataCnt: str,
        InputPwDataIncuYn: str,
        InputHourClsCode: str,
        InputCondMrktDivCode: str,
        InputIscd1: str,
        InputDate1: str,
        InputDate2: str,
        InputDivXtick: str,
        cont_yn: str = 'N',
        cont_key: str = '',
    ) -> APIResponse:
        """해외주식 분차트조회 (FSTKCHARTMIN).

        해외주식 분차트 조회 API 입니다.

        엔드포인트: POST /api/v1/quote/overseas-stock/chart/min
        유량제어: 4 TPS
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=a804e311-cb53-499b-9d8a-a4d838f0a484&api_id=eff74363-ad04-4c0e-8009-91a744e9324d

        Args:
            InputOrgAdjPrc: 수정주가사용여부 — 0:수정주가 미사용 1: 수정주가 사용
            dataCnt: 호출건수 — 입력범위: "1" ~ "2000" ""(공백입력) 또는 "0" 입력시 기본개수(400개)조회
            InputPwDataIncuYn: 기간지정여부코드 — "Y": 기간지정 "N":기간미지정 (InputDate2 부터 이전날짜 계속조회)
            InputHourClsCode: 입력시간구분코드 — "0" 입력
            InputCondMrktDivCode: 입력조건시장분류코드 — FY:뉴욕 FN:나스닥 FA:아멕스
            InputIscd1: 입력종목코드1 — 해외주식 종목코드 (ex. TQQQ)
            InputDate1: 입력날짜1 — 조회 시작일 (YYYYMMDD)
            InputDate2: 입력날짜2 — 조회 마감일 (YYYYMMDD)
            InputDivXtick: 분일별구분코드 — 30: 30초 60: 1분 600: 10분 3600: 60분 [60*N: N분]
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. 주요 응답 필드:
              - Out: Out
              - Hour: 시간
              - Date: 일자
              - Prpr: 현재가
              - Oprc: 시가
              - Hprc: 고가
              - Lprc: 저가
              - CntgVol: 체결거래량

        """
        body = {
            'In': {
                'InputOrgAdjPrc': InputOrgAdjPrc,
                'dataCnt': dataCnt,
                'InputPwDataIncuYn': InputPwDataIncuYn,
                'InputHourClsCode': InputHourClsCode,
                'InputCondMrktDivCode': InputCondMrktDivCode,
                'InputIscd1': InputIscd1,
                'InputDate1': InputDate1,
                'InputDate2': InputDate2,
                'InputDivXtick': InputDivXtick,
            },
        }
        headers = {'cont_yn': cont_yn, 'cont_key': cont_key}
        return self._client.post(self.PATHS['ov_stock_chart_min'], body, extra_headers=headers)

    def ov_stock_chart_day(
        self,
        *,
        InputCondMrktDivCode: str,
        InputOrgAdjPrc: str,
        InputIscd1: str,
        InputDate1: str,
        InputDate2: str,
        cont_yn: str = 'N',
        cont_key: str = '',
    ) -> APIResponse:
        """해외주식 일차트조회 (FSTKCHARTDAY).

        해외주식 일차트 조회 API 입니다.

        엔드포인트: POST /api/v1/quote/overseas-stock/chart/day
        유량제어: 4 TPS
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=a804e311-cb53-499b-9d8a-a4d838f0a484&api_id=98c2bedf-af8b-41b2-ac54-5b91ded72530

        Args:
            InputCondMrktDivCode: 입력조건시장분류코드 — FY:뉴욕 FN:나스닥 FA:아멕스
            InputOrgAdjPrc: 수정주가사용여부 — 0:수정주가 미사용 1: 수정주가 사용
            InputIscd1: 입력종목코드1 — 해외주식 종목코드 (ex. TQQQ)
            InputDate1: 입력날짜1 — 조회 시작일 (YYYYMMDD)
            InputDate2: 입력날짜2 — 조회 마감일 (YYYYMMDD)
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. 주요 응답 필드:
              - Out: Out
              - Hour: 시간
              - Date: 일자
              - Prpr: 현재가
              - Oprc: 시가
              - Hprc: 고가
              - Lprc: 저가
              - AcmlVol: 누적체결거래량

        """
        body = {
            'In': {
                'InputCondMrktDivCode': InputCondMrktDivCode,
                'InputOrgAdjPrc': InputOrgAdjPrc,
                'InputIscd1': InputIscd1,
                'InputDate1': InputDate1,
                'InputDate2': InputDate2,
            },
        }
        headers = {'cont_yn': cont_yn, 'cont_key': cont_key}
        return self._client.post(self.PATHS['ov_stock_chart_day'], body, extra_headers=headers)

    def ov_stock_chart_week(
        self,
        *,
        InputCondMrktDivCode: str,
        InputOrgAdjPrc: str,
        InputIscd1: str,
        InputDate1: str,
        InputDate2: str,
        InputPeriodDivCode: str,
        cont_yn: str = 'N',
        cont_key: str = '',
    ) -> APIResponse:
        """해외주식 주차트조회 (FSTKCHARTWEEK).

        해외주식 주차트 조회 API 입니다.

        엔드포인트: POST /api/v1/quote/overseas-stock/chart/week
        유량제어: 4 TPS
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=a804e311-cb53-499b-9d8a-a4d838f0a484&api_id=136794ff-8ba0-48d5-96d0-eb8fc68060fb

        Args:
            InputCondMrktDivCode: 입력조건시장분류코드 — FY:뉴욕 FN:나스닥 FA:아멕스
            InputOrgAdjPrc: 수정주가사용여부 — 0:수정주가 미사용 1: 수정주가 사용
            InputIscd1: 입력종목코드1 — 해외주식 종목코드 (ex. TQQQ)
            InputDate1: 입력날짜1 — 조회 시작일 (YYYYMMDD)
            InputDate2: 입력날짜2 — 조회 마감일 (YYYYMMDD)
            InputPeriodDivCode: 입력일/주/월/년 — W
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. 주요 응답 필드:
              - Out: Out
              - Hour: 시간
              - Date: 일자
              - Prpr: 현재가
              - Oprc: 시가
              - Hprc: 고가
              - Lprc: 저가
              - AcmlVol: 누적체결거래량

        """
        body = {
            'In': {
                'InputCondMrktDivCode': InputCondMrktDivCode,
                'InputOrgAdjPrc': InputOrgAdjPrc,
                'InputIscd1': InputIscd1,
                'InputDate1': InputDate1,
                'InputDate2': InputDate2,
                'InputPeriodDivCode': InputPeriodDivCode,
            },
        }
        headers = {'cont_yn': cont_yn, 'cont_key': cont_key}
        return self._client.post(self.PATHS['ov_stock_chart_week'], body, extra_headers=headers)

    def ov_stock_chart_month(
        self,
        *,
        InputOrgAdjPrc: str,
        InputCondMrktDivCode: str,
        InputIscd1: str,
        InputDate1: str,
        InputDate2: str,
        cont_yn: str = 'N',
        cont_key: str = '',
    ) -> APIResponse:
        """해외주식 월차트조회 (FSTKCHARTMONTH).

        해외주식 월차트 조회 API 입니다.

        엔드포인트: POST /api/v1/quote/overseas-stock/chart/month
        유량제어: 4 TPS
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=a804e311-cb53-499b-9d8a-a4d838f0a484&api_id=789a2830-7620-4a44-8107-336b0fd3f611

        Args:
            InputOrgAdjPrc: 수정주가사용여부 — 0:수정주가 미사용 1: 수정주가 사용
            InputCondMrktDivCode: 입력조건시장분류코드 — FY:뉴욕 FN:나스닥 FA:아멕스
            InputIscd1: 입력종목코드1 — 해외주식 종목코드 (ex. TQQQ)
            InputDate1: 입력날짜1 — 조회 시작일 (YYYYMMDD)
            InputDate2: 입력날짜2 — 조회 마감일 (YYYYMMDD)
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. 주요 응답 필드:
              - Out: Out
              - Hour: 시간
              - Date: 일자
              - Prpr: 현재가
              - Oprc: 시가
              - Hprc: 고가
              - Lprc: 저가
              - AcmlVol: 누적체결거래량

        """
        body = {
            'In': {
                'InputOrgAdjPrc': InputOrgAdjPrc,
                'InputCondMrktDivCode': InputCondMrktDivCode,
                'InputIscd1': InputIscd1,
                'InputDate1': InputDate1,
                'InputDate2': InputDate2,
            },
        }
        headers = {'cont_yn': cont_yn, 'cont_key': cont_key}
        return self._client.post(self.PATHS['ov_stock_chart_month'], body, extra_headers=headers)

    def ov_stock_inquire_condition_rise_fall(
        self,
        *,
        InputRealDelayClsCode: str,
        InputDataCode: str,
        InputDateClsCode: str,
        InputRankSortClsCode1: str,
        InputVolClsCode: str,
        InputTrPbmn1: str,
        InputDprice1: str,
        InputDprice2: str,
        cont_yn: str = 'N',
        cont_key: str = '',
    ) -> APIResponse:
        """해외주식 상승하락조회 (FSTKRANKLIST).

        해외주식 조건상승하락 조회 API입니다. ※ 해외주식 상승/하락률 조건에 맞는 종목을 제공합니다.

        엔드포인트: POST /api/v1/quote/overseas-stock/inquiry/rank-list
        유량제어: 2 TPS
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=a804e311-cb53-499b-9d8a-a4d838f0a484&api_id=28acef41-26f3-4d3d-bc55-8aca7587a576

        Args:
            InputRealDelayClsCode: 지연실시간구분코드 — 0: 지연 1: 실시간
            InputDataCode: 입력해외증시구분코드 — NY: 뉴욕 NA: 나스닥 AM: 아멕스 US:미국
            InputDateClsCode: 입력일자구분코드 — 0: 당일 1: 전일
            InputRankSortClsCode1: 입력순위정렬구분코드1 — 249: 상승율 250: 하락율
            InputVolClsCode: 입력거래량구분코드 — 7: 10만주이상 8: 50만주이상 9: 100만주이상 10:500만주이상 11:1000만주이상 12:5000만주이상
            InputTrPbmn1: 거래대금최소값
            InputDprice1: 가격최소값
            InputDprice2: 가격최대값
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. 주요 응답 필드:
              - Out: Out
              - Iscd: 종목코드
              - KorIsnm: 한글종목명
              - MrktClsName: 시장구분명
              - Prpr: 현재가
              - PrdyVrssSign: 전일대비부호
              - PrdyVrss: 전일대비
              - PrdyCtrt: 전일대비율
              - PrdyClpr: 전일종가
              - AcmlVol: 거래량
              - AcmlTrPbmn: 거래대금

        """
        body = {
            'In': {
                'InputRealDelayClsCode': InputRealDelayClsCode,
                'InputDataCode': InputDataCode,
                'InputDateClsCode': InputDateClsCode,
                'InputRankSortClsCode1': InputRankSortClsCode1,
                'InputVolClsCode': InputVolClsCode,
                'InputTrPbmn1': InputTrPbmn1,
                'InputDprice1': InputDprice1,
                'InputDprice2': InputDprice2,
            },
        }
        headers = {'cont_yn': cont_yn, 'cont_key': cont_key}
        return self._client.post(self.PATHS['ov_stock_inquire_condition_rise_fall'], body, extra_headers=headers)
