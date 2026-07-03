"""국내주식시세 API 모듈.

DB증권 OpenAPI 그룹: 국내주식시세
group_slug: kr_stock_quote

이 파일은 `_specs/kr_stock_quote/*.json` 에서 자동 생성되었습니다.
스펙이 갱신되면 `_workspace/build_modules.py`로 재생성하세요.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from dbsec_sdk.client import DBSecClient

from dbsec_sdk.response import APIResponse


class KrStockQuoteAPI:
    """국내주식시세 API 모음.

    사용법:
        >>> client = DBSecClient("config.yaml")
        >>> resp = client.apis.kr_stock_quote.<method>(...)
    """

    # API 경로 매핑
    PATHS = {
        'kr_stock_search_stocks': '/api/v1/quote/kr-stock/inquiry/stock-ticker',
        'kr_stock_inquire_elw_stock': '/api/v1/quote/kr-stock/inquiry/elw-ticker',
        'kr_stock_inquire_price_multi': '/api/v1/quote/kr-stock/inquiry/multiprice',
        'kr_stock_inquire_price': '/api/v1/quote/kr-stock/inquiry/price',
        'kr_stock_inquire_orderbook': '/api/v1/quote/kr-stock/inquiry/orderbook',
        'kr_stock_inquire_time_execution': '/api/v1/quote/kr-stock/inquiry/hour-price',
        'kr_stock_inquire_daily_executions': '/api/v1/quote/kr-stock/inquiry/daily-price',
        'kr_stock_inquire_condition_rise_fall': '/api/v1/quote/kr-stock/inquiry/rank-list',
        'kr_stock_inquire_daily_industry_investor': '/api/v1/quote/kr-stock/inquiry/daily-investor-u',
        'kr_stock_inquire_daily_issue_investor': '/api/v1/quote/kr-stock/inquiry/daily-investor',
        'kr_stock_inquire_etf_etn_stock': '/api/v1/quote/kr-stock/inquiry/etf-holdings',
        'kr_stock_inquire_sector_codes': '/api/v1/quote/kr-stock/inquiry/sector-cls',
        'kr_stock_inquire_sector_components': '/api/v1/quote/kr-stock/inquiry/sector-components',
        'kr_stock_inquire_industry_codes': '/api/v1/quote/kr-stock/inquiry/industry-cls',
        'kr_stock_inquire_industry_components': '/api/v1/quote/kr-stock/inquiry/industry-components',
    }
    # TR 코드 매핑
    TR_CODES = {
        'kr_stock_search_stocks': 'JCODES',
        'kr_stock_inquire_elw_stock': 'WCODES',
        'kr_stock_inquire_price_multi': 'MULTIPRICE',
        'kr_stock_inquire_price': 'PRICE',
        'kr_stock_inquire_orderbook': 'HOGA',
        'kr_stock_inquire_time_execution': 'CONCLUSION',
        'kr_stock_inquire_daily_executions': 'DAYTRADE',
        'kr_stock_inquire_condition_rise_fall': 'RANKLIST',
        'kr_stock_inquire_daily_industry_investor': 'UPTJJDAY',
        'kr_stock_inquire_daily_issue_investor': 'DAYSTOCKTJJ',
        'kr_stock_inquire_etf_etn_stock': 'ETFCOMPCODE',
        'kr_stock_inquire_sector_codes': 'SECTORCOND',
        'kr_stock_inquire_sector_components': 'SECTORCONDLIST',
        'kr_stock_inquire_industry_codes': 'USTOCKCOND',
        'kr_stock_inquire_industry_components': 'USTOCKCONDLIST',
    }

    def __init__(self, client: 'DBSecClient'):
        self._client = client

    def kr_stock_search_stocks(
        self,
        *,
        InputCondMrktDivCode: str,
        cont_yn: str = 'N',
        cont_key: str = '',
    ) -> APIResponse:
        """주식종목 조회 (JCODES).

        국내주식 종목조회 API입니다. ※ 연속키 조회를 통해 종목을 추가로 조회 할 수 있습니다.

        엔드포인트: POST /api/v1/quote/kr-stock/inquiry/stock-ticker
        유량제어: 3 TPS
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=80005fb0-6feb-4b8b-904a-605c59e29b4f&api_id=d8621b8b-11fd-4d01-b175-e6e3f6285215

        Args:
            InputCondMrktDivCode: 입력조건시장분류코드 — J : 주식 (KRX) NJ : 주식(NXT) UJ : 주식(통합) E : ETF EN : ETN
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. 주요 응답 필드:
              - Out: Out
              - MrktClsName: 시장구분명 — 종목 시장구분 코드입니다. 구분자 목록: "ETF", "ETN","코넥스","코스닥","거래소(코스피)"
              - Iscd: 종목코드
              - StndIscd: 표준종목코드
              - KorIsnm: 한글종목명
              - MrktClsCode: 시장분류구분코드 — 1: 코스닥 4: 코스피

        """
        body = {
            'In': {
                'InputCondMrktDivCode': InputCondMrktDivCode,
            },
        }
        headers = {'cont_yn': cont_yn, 'cont_key': cont_key}
        return self._client.post(self.PATHS['kr_stock_search_stocks'], body, extra_headers=headers)

    def kr_stock_inquire_elw_stock(
        self,
        *,
        InputCondMrktDivCode: str,
        cont_yn: str = 'N',
        cont_key: str = '',
    ) -> APIResponse:
        """ELW 종목 조회 (WCODES).

        국내 ELW 종목조회 API입니다. ※ 연속키 조회를 통해 종목을 추가로 조회 할 수 있습니다.

        엔드포인트: POST /api/v1/quote/kr-stock/inquiry/elw-ticker
        유량제어: 3 TPS
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=80005fb0-6feb-4b8b-904a-605c59e29b4f&api_id=7c9a349c-1629-4059-9f06-6bcf8c093fe0

        Args:
            InputCondMrktDivCode: 입력조건시장분류코드 — "W" 입력
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. 주요 응답 필드:
              - Out: Out
              - Iscd: 종목코드
              - StndIscd: 표준종목코드
              - KorIsnm: 한글종목명
              - MrktClsCode: 시장분류구분코드

        """
        body = {
            'In': {
                'InputCondMrktDivCode': InputCondMrktDivCode,
            },
        }
        headers = {'cont_yn': cont_yn, 'cont_key': cont_key}
        return self._client.post(self.PATHS['kr_stock_inquire_elw_stock'], body, extra_headers=headers)

    def kr_stock_inquire_price_multi(
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
        """국내주식 멀티현재가조회 (MULTIPRICE).

        국내시세 멀티 현재가 조회 API입니다. ※ 1회 호출에 최대 50종목의 시세를 확인 가능합니다. ※ "dataCnt" 필드에
        요청할 데이터의 개수를 입력하여 호출이 가능 합니다. (1~50) ※ "dataCnt" 필드의 값과 입력 데이터의 개수가 일치하지
        않으면 호출이 불가합니다. ※ 아래와 같이시장구분필드와 종목코드가 1:1 쌍을 이뤄야 호출이 정상적으로 이뤄집니다. -
        InputCondMrktDivCode1:J (시장구분필드), - InputIscd1:005930 (종목코드) ※
        [InputIscd1 ~ InputCondMrktDivCode1] & [InputIscd50 ~
        InputCondMrktDivCode50]과 같이 최대 50건 호출이 가능합니다.

        엔드포인트: POST /api/v1/quote/kr-stock/inquiry/multiprice
        유량제어: 2 TPS
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=80005fb0-6feb-4b8b-904a-605c59e29b4f&api_id=3abd4f11-4a92-48f3-bc3e-726a97a47905

        Args:
            dataCnt: 호출건수 — 1~50사이의 값 입력
            InputCondMrktDivCode1: 입력조건시장분류코드1 — 주식:J 주식(NXT): NJ 주식(통합): UJ ETN: EN ELW: W 업종&지수: U F : 지수선물 JF : 주식선물 KF : 미니선물 CF : 상품선물 XF : 섹터선물 CM : 야간선물 O : 지수옵션 JO : 주식옵션 KO : 미니옵션 WO : K200위클리옵션 EU : 야간옵션 SO: 코스닥 150옵션 ※ ETF종목의 경우 J 코드를 사용해...
            InputIscd1: 입력종목코드1 — 주식(J, NJ, UJ) 선택시 주식종목코드 입력 - J(KRX 주식): (ex. 005930) - NJ(NXT 주식): (ex. N-005930) - UJ(통합): (ex. U-005930) ※ NXT/통합시세로 종목 조회 시 반드시 종목 앞에 구분자 (N-, U-)를 붙여서 호출 부탁드리겠습니다. 업종(U) 선택시 지수코드: 1001: KOSPI 200...
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
        return self._client.post(self.PATHS['kr_stock_inquire_price_multi'], body, extra_headers=headers)

    def kr_stock_inquire_price(
        self,
        *,
        InputCondMrktDivCode: str,
        InputIscd1: str,
        cont_yn: str = 'N',
        cont_key: str = '',
    ) -> APIResponse:
        """현재가조회 (PRICE).

        국내주식 현재가 조회 API입니다.

        엔드포인트: POST /api/v1/quote/kr-stock/inquiry/price
        유량제어: 5 TPS
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=80005fb0-6feb-4b8b-904a-605c59e29b4f&api_id=d7f6a691-8fe6-4733-901f-c2535417dc46

        Args:
            InputCondMrktDivCode: 입력조건시장분류코드 — 주식:J 주식(NXT): NJ 주식(통합): UJ ETN: EN ELW: W 업종&지수: U ※ ETF종목의 경우 J 코드를 사용해 조회 부탁드립니다.
            InputIscd1: 입력종목코드1 — 주식(J, NJ, UJ) 선택시 주식종목코드 입력 - J(KRX 주식): (ex. 005930) - NJ(NXT 주식): (ex. N-005930) - UJ(통합): (ex. U-005930) ※ NXT/통합시세로 종목 조회 시 반드시 종목 앞에 구분자 (N-, U-)를 붙여서 호출 부탁드리겠습니다. 업종(U) 선택시 지수코드: 1001: KOSPI 200...
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. 주요 응답 필드:
              - PrdyVrss: 전일대비
              - Pbr: PBR
              - OtstStplQtyIcdc: 미결제증감
              - HtsOtstStplQty: 미결제약정수량
              - Askp1: 매도호가
              - Bidp1: 매수호가
              - PrdyVol: 전일거래량
              - AcmlVol: 거래량
              - AcmlTrPbmn: 거래대금
              - Per: PER
              - PrdyCtrt: 전일대비율
              - Sdpr: 기준가
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
        return self._client.post(self.PATHS['kr_stock_inquire_price'], body, extra_headers=headers)

    def kr_stock_inquire_orderbook(
        self,
        *,
        InputCondMrktDivCode: str,
        InputIscd1: str,
        cont_yn: str = 'N',
        cont_key: str = '',
    ) -> APIResponse:
        """호가조회 (HOGA).

        국내주식 호가 조회 API입니다.

        엔드포인트: POST /api/v1/quote/kr-stock/inquiry/orderbook
        유량제어: 3 TPS
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=80005fb0-6feb-4b8b-904a-605c59e29b4f&api_id=14be0244-5a65-4219-9639-f32d6ec3f374

        Args:
            InputCondMrktDivCode: 입력조건시장분류코드 — 주식:J 주식(NXT): NJ 주식(통합): UJ ETN: EN ELW: W ※ ETF종목의 경우 J 코드를 사용해 조회 부탁드립니다.
            InputIscd1: 입력종목코드1 — 종목코드 입력 - J(KRX 주식): (ex. 005930) - NJ(NXT 주식): (ex. N-005930) - UJ(통합): (ex. U-005930) ※ NXT/통합시세로 종목 조회 시 반드시 종목 앞에 구분자 (N-, U-)를 붙여서 호출 부탁드리겠습니다.
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
        return self._client.post(self.PATHS['kr_stock_inquire_orderbook'], body, extra_headers=headers)

    def kr_stock_inquire_time_execution(
        self,
        *,
        InputCondMrktDivCode: str,
        InputIscd1: str,
        cont_yn: str = 'N',
        cont_key: str = '',
    ) -> APIResponse:
        """시간대별체결조회 (CONCLUSION).

        국내주식 시간대별 체결 조회 API입니다.

        엔드포인트: POST /api/v1/quote/kr-stock/inquiry/hour-price
        유량제어: 3 TPS
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=80005fb0-6feb-4b8b-904a-605c59e29b4f&api_id=01b99bab-7f12-4098-97e1-99fdda029ca2

        Args:
            InputCondMrktDivCode: 입력조건시장분류코드 — 주식:J 주식(NXT): NJ 주식(통합): UJ ETN: EN ELW: W ※ ETF종목의 경우 J 코드를 사용해 조회 부탁드립니다.
            InputIscd1: 입력종목코드1 — 종목코드 입력 - J(KRX 주식): (ex. 005930) - NJ(NXT 주식): (ex. N-005930) - UJ(통합): (ex. U-005930) ※ NXT/통합시세로 종목 조회 시 반드시 종목 앞에 구분자 (N-, U-)를 붙여서 호출 부탁드리겠습니다.
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
        return self._client.post(self.PATHS['kr_stock_inquire_time_execution'], body, extra_headers=headers)

    def kr_stock_inquire_daily_executions(
        self,
        *,
        InputCondMrktDivCode: str,
        InputIscd1: str,
        InputHourClsCode: str,
        cont_yn: str = 'N',
        cont_key: str = '',
    ) -> APIResponse:
        """일별체결조회 (DAYTRADE).

        국내주식 일별체결 조회 API입니다.

        엔드포인트: POST /api/v1/quote/kr-stock/inquiry/daily-price
        유량제어: 3 TPS
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=80005fb0-6feb-4b8b-904a-605c59e29b4f&api_id=6738128a-9cc7-46ce-b59f-dda6162a12b8

        Args:
            InputCondMrktDivCode: 입력조건시장분류코드 — 주식:J 주식(NXT): NJ 주식(통합): UJ ETN: EN ELW: W ※ ETF종목의 경우 J 코드를 사용해 조회 부탁드립니다.
            InputIscd1: 입력종목코드1 — 종목코드 입력 - J(KRX 주식): (ex. 005930) - NJ(NXT 주식): (ex. N-005930) - UJ(통합): (ex. U-005930) ※ NXT/통합시세로 종목 조회 시 반드시 종목 앞에 구분자 (N-, U-)를 붙여서 호출 부탁드리겠습니다.
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
        return self._client.post(self.PATHS['kr_stock_inquire_daily_executions'], body, extra_headers=headers)

    def kr_stock_inquire_condition_rise_fall(
        self,
        *,
        InputDateClsCode: str,
        InputRankSortClsCode1: str,
        InputMrktClsCode: str,
        InputBstpIscd: str,
        cont_yn: str = 'N',
        cont_key: str = '',
    ) -> APIResponse:
        """주식조건상승하락조회 (RANKLIST).

        국내주식 주식조건상승하락 조회 API입니다. ※ 국내주식 상승/하락률을 조건에 맞는 종목을 제공합니다.

        엔드포인트: POST /api/v1/quote/kr-stock/inquiry/rank-list
        유량제어: 3 TPS
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=80005fb0-6feb-4b8b-904a-605c59e29b4f&api_id=668de023-eb33-4f96-a687-51b5cc1b97ec

        Args:
            InputDateClsCode: 입력일자구분코드 — 당일:0 전일:1 주간:2 월간:5
            InputRankSortClsCode1: 입력순위정렬구분코드1 — 상승률:12 하락율:11
            InputMrktClsCode: 입력시장구분코드 — 전체:A 코스피:K 코스닥:Q
            InputBstpIscd: 입력업종코드 — 입력시장구분코드 "A" 일시 입력 X 코스피:1001 코스닥:2001
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. 주요 응답 필드:
              - Out: Out
              - Iscd: 종목코드
              - KorIsnm: 한글종목명
              - DataRank: 순위
              - Prpr: 현재가
              - PrdyVrssSign: 전일대비부호
              - PrdyVrss: 전일대비
              - PrdyCtrt: 전일대비율

        """
        body = {
            'In': {
                'InputDateClsCode': InputDateClsCode,
                'InputRankSortClsCode1': InputRankSortClsCode1,
                'InputMrktClsCode': InputMrktClsCode,
                'InputBstpIscd': InputBstpIscd,
            },
        }
        headers = {'cont_yn': cont_yn, 'cont_key': cont_key}
        return self._client.post(self.PATHS['kr_stock_inquire_condition_rise_fall'], body, extra_headers=headers)

    def kr_stock_inquire_daily_industry_investor(
        self,
        *,
        InputCondMrktDivCode: str,
        InputIscd1: str,
        InputDate1: str,
        InputDate2: str,
        cont_yn: str = 'N',
        cont_key: str = '',
    ) -> APIResponse:
        """일별업종별투자자조회 (UPTJJDAY).

        국내 일별업종별투자자조회 API입니다.

        엔드포인트: POST /api/v1/quote/kr-stock/inquiry/daily-investor-u
        유량제어: 2 TPS
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=80005fb0-6feb-4b8b-904a-605c59e29b4f&api_id=a4dc3cb3-ee90-4b40-a833-835a8bc2ac15

        Args:
            InputCondMrktDivCode: 입력조건시장분류코드 — 주식&ETF:J 주식(NXT): NJ 주식(통합): UJ ETN: EN ELW: W
            InputIscd1: 입력종목코드1 — 종목코드 입력 - J(KRX 주식): (ex. 005930) - NJ(NXT 주식): (ex. N-005930) - UJ(통합): (ex. U-005930) ※ NXT/통합시세로 종목 조회 시 반드시 종목 앞에 구분자 (N-, U-)를 붙여서 호출 부탁드리겠습니다.
            InputDate1: 입력날짜1 — YYYYMMDD
            InputDate2: 입력날짜2 — YYYYMMDD
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. 주요 응답 필드:
              - Date: 일자
              - Prpr: 현재가
              - PrdyVrssSign: 전일대비부호
              - PrdyVrss: 전일대비
              - PrdyCtrt: 전일대비율
              - AcmlVol: 거래량
              - AcmlTrPbmn: 거래대금
              - OrgnShnuVol: 기관계매수수량
              - OrgnSelnVol: 기관계매도수량
              - OrgnShnuTrPbmn: 기관계매수금액
              - OrgnSelnTrPbmn: 기관계매도금액
              - FrgnRegShnuVol: 외국인매수수량
              - FrgnRegSelnVol: 외국인매도수량
              - FrgnRegShnuTrPbmn: 외국인매수금액
              - FrgnRegSelnTrPbmn: 외국인매도금액
              - (이하 생략 — 가이드 참조)

        """
        body = {
            'In': {
                'InputCondMrktDivCode': InputCondMrktDivCode,
                'InputIscd1': InputIscd1,
                'InputDate1': InputDate1,
                'InputDate2': InputDate2,
            },
        }
        headers = {'cont_yn': cont_yn, 'cont_key': cont_key}
        return self._client.post(self.PATHS['kr_stock_inquire_daily_industry_investor'], body, extra_headers=headers)

    def kr_stock_inquire_daily_issue_investor(
        self,
        *,
        InputCondMrktDivCode: str,
        InputIscd1: str,
        InputDate1: str,
        InputDate2: str,
        cont_yn: str = 'N',
        cont_key: str = '',
    ) -> APIResponse:
        """일별종목별투자자조회 (DAYSTOCKTJJ).

        국내 일별종목별투자자조회 API입니다.

        엔드포인트: POST /api/v1/quote/kr-stock/inquiry/daily-investor
        유량제어: 2 TPS
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=80005fb0-6feb-4b8b-904a-605c59e29b4f&api_id=2a750d3d-5ea2-4bb6-b3d6-411956d42e75

        Args:
            InputCondMrktDivCode: 입력조건시장분류코드 — 주식&ETF:J 주식(NXT): NJ 주식(통합): UJ ETN: EN ELW: W
            InputIscd1: 입력종목코드1 — 종목코드 입력 - J(KRX 주식): (ex. 005930) - NJ(NXT 주식): (ex. N-005930) - UJ(통합): (ex. U-005930) ※ NXT/통합시세로 종목 조회 시 반드시 종목 앞에 구분자 (N-, U-)를 붙여서 호출 부탁드리겠습니다.
            InputDate1: 입력날짜1 — YYYYMMDD
            InputDate2: 입력날짜2 — YYYYMMDD
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. 주요 응답 필드:
              - Date: 일자
              - Prpr: 현재가
              - PrdyVrssSign: 전일대비부호
              - PrdyVrss: 전일대비
              - PrdyCtrt: 전일대비율
              - AcmlVol: 거래량
              - AcmlTrPbmn: 거래대금
              - OrgnShnuVol: 기관계매수수량
              - OrgnSelnVol: 기관계매도수량
              - OrgnShnuTrPbmn: 기관계매수금액
              - OrgnSelnTrPbmn: 기관계매도금액
              - FrgnRegShnuVol: 외국인매수수량
              - FrgnRegSelnVol: 외국인매도수량
              - FrgnRegShnuTrPbmn: 외국인매수금액
              - FrgnRegSelnTrPbmn: 외국인매도금액
              - (이하 생략 — 가이드 참조)

        """
        body = {
            'In': {
                'InputCondMrktDivCode': InputCondMrktDivCode,
                'InputIscd1': InputIscd1,
                'InputDate1': InputDate1,
                'InputDate2': InputDate2,
            },
        }
        headers = {'cont_yn': cont_yn, 'cont_key': cont_key}
        return self._client.post(self.PATHS['kr_stock_inquire_daily_issue_investor'], body, extra_headers=headers)

    def kr_stock_inquire_etf_etn_stock(
        self,
        *,
        InputMrktClsCode: str,
        InputCondMrktDivCode: str,
        InputIscd1: str,
        cont_yn: str = 'N',
        cont_key: str = '',
    ) -> APIResponse:
        """국내 ETF/ETN 구성종목조회 (ETFCOMPCODE).

        엔드포인트: POST /api/v1/quote/kr-stock/inquiry/etf-holdings
        유량제어: 2 TPS
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=80005fb0-6feb-4b8b-904a-605c59e29b4f&api_id=660ce8d7-00ab-41dc-b9b3-bb7322cd4729

        Args:
            InputMrktClsCode: 입력시장구분코드 — "A" 고정
            InputCondMrktDivCode: 입력조건시장분류코드 — ETF 종목 조회시 : J ETN 종목조회시 : EN
            InputIscd1: 입력종목코드1 — 종목코드 입력
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. 주요 응답 필드:
              - Out: Out
              - KorIsnm: 한글종목명
              - Prpr: 현재가
              - PrdyVrssSign: 전일대비부호
              - PrdyVrss: 전일대비
              - PrdyCtrt: 전일대비율
              - EtfCuUnitScrtCnt: ETFCU단위증권수
              - EtfCnfgRate: ETF구성비율
              - Iscd: 종목코드

        """
        body = {
            'In': {
                'InputMrktClsCode': InputMrktClsCode,
                'InputCondMrktDivCode': InputCondMrktDivCode,
                'InputIscd1': InputIscd1,
            },
        }
        headers = {'cont_yn': cont_yn, 'cont_key': cont_key}
        return self._client.post(self.PATHS['kr_stock_inquire_etf_etn_stock'], body, extra_headers=headers)

    def kr_stock_inquire_sector_codes(
        self,
        *,
        InputSectorGroupClsCode: str,
        cont_yn: str = 'N',
        cont_key: str = '',
    ) -> APIResponse:
        """섹터분류코드 조회 (SECTORCOND).

        국내주식 섹터 분류코드를 조회 할 수 있는 API입니다.

        엔드포인트: POST /api/v1/quote/kr-stock/inquiry/sector-cls
        유량제어: 2 TPS
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=80005fb0-6feb-4b8b-904a-605c59e29b4f&api_id=5e9ee146-7a0b-4759-a6ef-d778e4d7bedd

        Args:
            InputSectorGroupClsCode: 입력섹터그룹구분코드 — "S" 고정
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. 주요 응답 필드:
              - Out: Out
              - SectorGroupCode: 섹터그룹코드
              - SectorGroupName: 섹터그룹명

        """
        body = {
            'In': {
                'InputSectorGroupClsCode': InputSectorGroupClsCode,
            },
        }
        headers = {'cont_yn': cont_yn, 'cont_key': cont_key}
        return self._client.post(self.PATHS['kr_stock_inquire_sector_codes'], body, extra_headers=headers)

    def kr_stock_inquire_sector_components(
        self,
        *,
        InputSectorGroupClsCode: str,
        InputRankSortClsCode1: str,
        InputSectorGroupIscd: str,
        cont_yn: str = 'N',
        cont_key: str = '',
    ) -> APIResponse:
        """섹터구성종목 조회 (SECTORCONDLIST).

        국내주식 섹터 구성종목을 조회 할 수 있는 API입니다.

        엔드포인트: POST /api/v1/quote/kr-stock/inquiry/sector-components
        유량제어: 2 TPS
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=80005fb0-6feb-4b8b-904a-605c59e29b4f&api_id=d11dcc68-9e80-4e53-ac21-ea95172e7416

        Args:
            InputSectorGroupClsCode: 입력섹터그룹구분코드 — "S" 고정
            InputRankSortClsCode1: 입력순위정렬구분코드 — 2: 시가총액 DESC 4: 현재가 DESC 12: 등락율 DESC 13: 거래량 DESC 42: 거래대금 DESC
            InputSectorGroupIscd: 입력섹터그룹코드 — 섹터분류코드조회 API에서 조회된 값 사용 ex. "9155"입력시 반도체 대표주 섹터 구성종목 조회
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. 주요 응답 필드:
              - Out: Out
              - Iscd: 종목코드
              - KorIsnm: 한글종목명
              - Avls: 시가총액 — 단위: 100만원
              - AvlsRlim: 시가총액비중
              - Prpr: 현재가
              - PrdyVrssSign: 전일대비부호 — 2: 상승 3: 보합 5: 하락
              - PrdyVrss: 전일대비
              - PrdyCtrt: 전일대비율
              - AcmlVol: 거래량
              - AcmlTrPbmn: 거래대금

        """
        body = {
            'In': {
                'InputSectorGroupClsCode': InputSectorGroupClsCode,
                'InputRankSortClsCode1': InputRankSortClsCode1,
                'InputSectorGroupIscd': InputSectorGroupIscd,
            },
        }
        headers = {'cont_yn': cont_yn, 'cont_key': cont_key}
        return self._client.post(self.PATHS['kr_stock_inquire_sector_components'], body, extra_headers=headers)

    def kr_stock_inquire_industry_codes(
        self,
        *,
        InputMrktClsCode: str,
        InputCondMrktDivCode: str,
        cont_yn: str = 'N',
        cont_key: str = '',
    ) -> APIResponse:
        """업종분류코드 조회 (USTOCKCOND).

        국내 업종분류코드를 조회 할 수 있는 API 입니다.

        엔드포인트: POST /api/v1/quote/kr-stock/inquiry/industry-cls
        유량제어: 2 TPS
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=80005fb0-6feb-4b8b-904a-605c59e29b4f&api_id=d373d73b-9d99-474e-a990-048132353d61

        Args:
            InputMrktClsCode: 입력시장구분코드 — 입력시장 구분코드로, 입력값은 "U" 고정입니다.
            InputCondMrktDivCode: 입력조건시장분류코드 — K: 코스피 Q: 코스닥 K2: Kospi200 KR: KRX
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. 주요 응답 필드:
              - 입력조건시장분류코드: 입력조건시장분류코드
              - Iscd: 종목코드
              - KorIsnm: 한글종목명

        """
        body = {
            'In': {
                'InputMrktClsCode': InputMrktClsCode,
                'InputCondMrktDivCode': InputCondMrktDivCode,
            },
        }
        headers = {'cont_yn': cont_yn, 'cont_key': cont_key}
        return self._client.post(self.PATHS['kr_stock_inquire_industry_codes'], body, extra_headers=headers)

    def kr_stock_inquire_industry_components(
        self,
        *,
        InputBstpIscd: str,
        InputRankSortClsCode1: str,
        InputCondMrktDivCode: str,
        cont_yn: str = 'N',
        cont_key: str = '',
    ) -> APIResponse:
        """업종구성종목 조회 (USTOCKCONDLIST).

        국내 업종구성종목을 조회 할 수 있는 API 입니다.

        엔드포인트: POST /api/v1/quote/kr-stock/inquiry/industry-components
        유량제어: 2 TPS
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=80005fb0-6feb-4b8b-904a-605c59e29b4f&api_id=e75a5938-c6bb-4bb4-b424-06a021f6f560

        Args:
            InputBstpIscd: 입력업종코드 — 업종분류코드조회 API에서 조회된 값 사용 ex. "1024"입력시 증권 업종 구성종목 조회
            InputRankSortClsCode1: 입력순위정렬구분코드 — 2: 시가총액 DESC 4: 현재가 DESC 12: 등락율 DESC 13: 거래량 DESC 42: 거래대금 DESC
            InputCondMrktDivCode: 입력조건시장분류코드 — "UJ" 고정
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. 주요 응답 필드:
              - Out: Out
              - Iscd: 종목코드
              - KorIsnm: 한글종목명
              - Avls: 시가총액 — 단위: 100만원
              - AvlsRlim: 시가총액비중
              - Prpr: 현재가
              - PrdyVrssSign: 전일대비부호 — 2: 상승 3: 보합 5: 하락
              - PrdyVrss: 전일대비
              - PrdyCtrt: 전일대비율
              - AcmlVol: 거래량
              - AcmlTrPbmn: 거래대금

        """
        body = {
            'In': {
                'InputBstpIscd': InputBstpIscd,
                'InputRankSortClsCode1': InputRankSortClsCode1,
                'InputCondMrktDivCode': InputCondMrktDivCode,
            },
        }
        headers = {'cont_yn': cont_yn, 'cont_key': cont_key}
        return self._client.post(self.PATHS['kr_stock_inquire_industry_components'], body, extra_headers=headers)
