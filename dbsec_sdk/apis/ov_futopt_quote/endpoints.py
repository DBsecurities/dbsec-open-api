"""해외선물옵션시세 API 모듈.

DB증권 OpenAPI 그룹: 해외선물옵션시세
group_slug: ov_futopt_quote

이 파일은 `_specs/ov_futopt_quote/*.json` 에서 자동 생성되었습니다.
스펙이 갱신되면 `_workspace/build_modules.py`로 재생성하세요.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from dbsec_sdk.client import DBSecClient

from dbsec_sdk.response import APIResponse


class OvFutoptQuoteAPI:
    """해외선물옵션시세 API 모음.

    사용법:
        >>> client = DBSecClient("config.yaml")
        >>> resp = client.apis.ov_futopt_quote.<method>(...)
    """

    # API 경로 매핑
    PATHS = {
        'ov_futopt_inquire_orderbook_price': '/api/v1/quote/overseas-futureoption/inquiry/orderbook-price',
        'ov_futopt_daily_price_trend': '/api/v1/quote/overseas-futureoption/inquiry/daily-price',
        'ov_futopt_future_chart_tick': '/api/v1/quote/overseas-futureoption/future-chart/tick',
        'ov_futopt_future_chart_min': '/api/v1/quote/overseas-futureoption/future-chart/min',
        'ov_futopt_future_chart_day_week_month': '/api/v1/quote/overseas-futureoption/future-chart/dwmonth',
        'ov_futopt_option_chart_tick': '/api/v1/quote/overseas-futureoption/option-chart/tick',
        'ov_futopt_option_chart_min': '/api/v1/quote/overseas-futureoption/option-chart/min',
        'ov_futopt_option_chart_day_week_month': '/api/v1/quote/overseas-futureoption/option-chart/dwmonth',
    }
    # TR 코드 매핑
    TR_CODES = {
        'ov_futopt_inquire_orderbook_price': 'pibo7042',
        'ov_futopt_daily_price_trend': 'pibo7044',
        'ov_futopt_future_chart_tick': 'pibg7301',
        'ov_futopt_future_chart_min': 'pibg7302',
        'ov_futopt_future_chart_day_week_month': 'pibg7303',
        'ov_futopt_option_chart_tick': 'pibg7401',
        'ov_futopt_option_chart_min': 'pibg7402',
        'ov_futopt_option_chart_day_week_month': 'pibg7403',
    }

    def __init__(self, client: 'DBSecClient'):
        self._client = client

    def ov_futopt_inquire_orderbook_price(
        self,
        *,
        Code: str,
        cont_yn: str = 'N',
        cont_key: str = '',
    ) -> APIResponse:
        """호가 & 현재가 조회 (pibo7042).

        해외선물옵션 호가 & 현재가 조회 API 입니다. ※ 해외선물옵션 API시세 신청이 되어있지 않은 경우 시세를 수신 하실 수
        없습니다. ※ API시세(유료) 신청방법 GTS(Happy+ Global) : [1761] API시세 신청

        엔드포인트: POST /api/v1/quote/overseas-futureoption/inquiry/orderbook-price
        유량제어: 2 TPS
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=e1035c5a-edb1-4b7d-8336-04e2ab76ed35&api_id=a1345aa1-aa24-4a98-bdc6-73d5120b7035

        Args:
            Code: 종목코드 — 종목코드 입력
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. 주요 응답 필드:
              - Code: 종목코드
              - Last: 현재가
              - Diff: 대비
              - Rate: 대비율
              - Open: 시가 — 당일 시가
              - High: 고가 — 당일 고가
              - Lowp: 저가 — 당일 저가
              - Clos: 종가 — 전일 종가
              - Tvol: 누적거래량
              - Lvol: 직전체결량
              - Htim: 현재시간
              - Out1: Out1
              - Askp: 매수호가가격
              - Askq: 매수호가수량
              - Askn: 매수호가건수
              - (이하 생략 — 가이드 참조)

        """
        body = {
            'In': {
                'Code': Code,
            },
        }
        headers = {'cont_yn': cont_yn, 'cont_key': cont_key}
        return self._client.post(self.PATHS['ov_futopt_inquire_orderbook_price'], body, extra_headers=headers)

    def ov_futopt_daily_price_trend(
        self,
        *,
        Code: str,
        cont_yn: str = 'N',
        cont_key: str = '',
    ) -> APIResponse:
        """일자별 시세추이 (pibo7044).

        해외선물옵션 일자별 시세추이 조회 API 입니다. ※ 해외선물옵션 API시세 신청이 되어있지 않은 경우 시세를 수신 하실 수
        없습니다. ※ API시세(유료) 신청방법 GTS(Happy+ Global) : [1761] API시세 신청

        엔드포인트: POST /api/v1/quote/overseas-futureoption/inquiry/daily-price
        유량제어: 2 TPS
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=e1035c5a-edb1-4b7d-8336-04e2ab76ed35&api_id=5b43af78-1f7e-46e2-b96c-054512499a2c

        Args:
            Code: 종목코드 — 종목코드 입력
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. 주요 응답 필드:
              - Code: 종목코드
              - Ikey: 조회구분
              - Sdir: 정렬방식
              - Aflg: 추가위치
              - Ckey: 다음조회가능여부
              - Nrow: 조회건수
              - Kval: 다음키값
              - Date: 영업일자
              - Open: 시가
              - High: 고가
              - Lowp: 저가
              - Clos: 종가
              - Diff: 대비
              - Rate: 대비율
              - Tvol: 누적거래량
              - (이하 생략 — 가이드 참조)

        """
        body = {
            'In': {
                'Code': Code,
            },
        }
        headers = {'cont_yn': cont_yn, 'cont_key': cont_key}
        return self._client.post(self.PATHS['ov_futopt_daily_price_trend'], body, extra_headers=headers)

    def ov_futopt_future_chart_tick(
        self,
        *,
        Code: str,
        Tick: str,
        Dcnt: str,
        Dedt: str,
        cont_yn: str = 'N',
        cont_key: str = '',
    ) -> APIResponse:
        """해외선물 틱차트조회 (pibg7301).

        해외선물 틱차트 조회 API 입니다. ※ 해외선물옵션 API시세 신청이 되어있지 않은 경우 시세를 수신 하실 수 없습니다. ※
        API시세(유료) 신청방법 GTS(Happy+ Global) : [1761] API시세 신청

        엔드포인트: POST /api/v1/quote/overseas-futureoption/future-chart/tick
        유량제어: 10 TPS
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=e1035c5a-edb1-4b7d-8336-04e2ab76ed35&api_id=89feef7a-aaee-4619-a235-7b045e4d7835

        Args:
            Code: 종목코드 — 종목코드 입력
            Tick: N tick — N틱 (최대 900틱)
            Dcnt: 조회건수 — 요청 데이터건수 (최대400)
            Dedt: 조회일자 — 조회일자입력: YYYYMMDD 당일인 경우: 99999999
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. 주요 응답 필드:
              - Pind: price indicator
              - Nrec: 조회건수
              - Ikey: 조회구분
              - Sdir: 정렬방식
              - Aflg: 추가위치
              - Nrow: 조회건수
              - Out1: Out1
              - Date: 체결일자
              - Bday: 영업일자
              - Time: 체결시간
              - Clos: 종가
              - Lvol: 체결량
              - Open: 시가
              - High: 고가
              - Lowp: 저가
              - (이하 생략 — 가이드 참조)

        """
        body = {
            'In': {
                'Code': Code,
                'Tick': Tick,
                'Dcnt': Dcnt,
                'Dedt': Dedt,
            },
        }
        headers = {'cont_yn': cont_yn, 'cont_key': cont_key}
        return self._client.post(self.PATHS['ov_futopt_future_chart_tick'], body, extra_headers=headers)

    def ov_futopt_future_chart_min(
        self,
        *,
        Code: str,
        Tick: str,
        Dcnt: str,
        Dedt: str,
        cont_yn: str = 'N',
        cont_key: str = '',
    ) -> APIResponse:
        """해외선물 분차트조회 (pibg7302).

        해외선물 분차트 조회 API 입니다. ※ 해외선물옵션 API시세 신청이 되어있지 않은 경우 시세를 수신 하실 수 없습니다. ※
        API시세(유료) 신청방법 GTS(Happy+ Global) : [1761] API시세 신청

        엔드포인트: POST /api/v1/quote/overseas-futureoption/future-chart/min
        유량제어: 2 TPS
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=e1035c5a-edb1-4b7d-8336-04e2ab76ed35&api_id=6511102e-0906-4f30-aaca-63a07c04ea11

        Args:
            Code: 종목코드 — 종목코드 입력
            Tick: N분봉 — N분 (최대 900분)
            Dcnt: 조회건수 — 요청 데이터건수 (최대400건)
            Dedt: 조회일자 — 조회일자 (YYYYMMDD), 당일: 99999999 세팅
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. 주요 응답 필드:
              - Pind: price indicator
              - Nrec: 조회건수
              - Ikey: 조회구분
              - Sdir: 정렬방식
              - Aflg: 추가위치
              - Ckey: 다음조회가능여부
              - Nrow: 조회건수
              - Kval: 다음키값
              - Date: 체결일자
              - Bday: 영업일자
              - Time: 체결시간
              - Clos: 종가
              - Lvol: 체결량
              - Open: 시가
              - High: 고가
              - (이하 생략 — 가이드 참조)

        """
        body = {
            'In': {
                'Code': Code,
                'Tick': Tick,
                'Dcnt': Dcnt,
                'Dedt': Dedt,
            },
        }
        headers = {'cont_yn': cont_yn, 'cont_key': cont_key}
        return self._client.post(self.PATHS['ov_futopt_future_chart_min'], body, extra_headers=headers)

    def ov_futopt_future_chart_day_week_month(
        self,
        *,
        Code: str,
        Dtgb: str,
        Dcnt: str,
        Dedt: str,
        cont_yn: str = 'N',
        cont_key: str = '',
    ) -> APIResponse:
        """해외선물 일주월차트조회 (pibg7303).

        해외선물 일주월 차트 조회 API 입니다. ※ 해외선물옵션 API시세 신청이 되어있지 않은 경우 시세를 수신 하실 수 없습니다.
        ※ API시세(유료) 신청방법 GTS(Happy+ Global) : [1761] API시세 신청

        엔드포인트: POST /api/v1/quote/overseas-futureoption/future-chart/dwmonth
        유량제어: 2 TPS
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=e1035c5a-edb1-4b7d-8336-04e2ab76ed35&api_id=d1fb4793-e606-4683-a50e-640e4361f00a

        Args:
            Code: 종목코드 — 종목코드 입력
            Dtgb: 데이터구분 — 0: 일(daily) 1: 주(weekly) 2: 월(monthly)
            Dcnt: 조회건수 — 요청 데이터건수 (최대400건)
            Dedt: 조회일자 — 조회일자 (YYYYMMDD), 당일: 99999999 세팅
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. 주요 응답 필드:
              - Pind: price indicator
              - Nrec: 조회건수
              - Ikey: 조회구분
              - Sdir: 정렬방식
              - Aflg: 추가위치
              - Ckey: 다음조회가능여부
              - Nrow: 조회건수
              - Kval: 다음키값
              - Date: 체결일자
              - Clos: 종가
              - Tvol: 누적거래량
              - Open: 시가
              - High: 고가
              - Lowp: 저가

        """
        body = {
            'In': {
                'Code': Code,
                'Dtgb': Dtgb,
                'Dcnt': Dcnt,
                'Dedt': Dedt,
            },
        }
        headers = {'cont_yn': cont_yn, 'cont_key': cont_key}
        return self._client.post(self.PATHS['ov_futopt_future_chart_day_week_month'], body, extra_headers=headers)

    def ov_futopt_option_chart_tick(
        self,
        *,
        Code: str,
        Tick: str,
        Dcnt: str,
        Dedt: str,
        cont_yn: str = 'N',
        cont_key: str = '',
    ) -> APIResponse:
        """해외옵션 틱차트조회 (pibg7401).

        해외옵션 틱 차트 조회 API 입니다. ※ 해외선물옵션 API시세 신청이 되어있지 않은 경우 시세를 수신 하실 수 없습니다. ※
        API시세(유료) 신청방법 GTS(Happy+ Global) : [1761] API시세 신청

        엔드포인트: POST /api/v1/quote/overseas-futureoption/option-chart/tick
        유량제어: 10 TPS
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=e1035c5a-edb1-4b7d-8336-04e2ab76ed35&api_id=32cc74fd-28c0-4756-a7ff-369b56c90df1

        Args:
            Code: 종목코드 — 종목코드 입력
            Tick: N tick — N틱 (최대 900틱)
            Dcnt: 조회건수 — 요청 데이터건수 (최대400건)
            Dedt: 조회일자 — 조회일자입력: YYYYMMDD 당일인 경우: 99999999
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. 주요 응답 필드:
              - Pind: price indicator
              - Nrec: 조회건수
              - Ikey: 조회구분
              - Sdir: 정렬방식
              - Aflg: 추가위치
              - Ckey: 다음조회가능여부
              - Nrow: 조회건수
              - Kval: 다음키값
              - Date: 체결일자
              - Bday: 영업일자
              - Time: 체결시간
              - Clos: 종가
              - Lvol: 체결량
              - Open: 시가
              - High: 고가
              - (이하 생략 — 가이드 참조)

        """
        body = {
            'In': {
                'Code': Code,
                'Tick': Tick,
                'Dcnt': Dcnt,
                'Dedt': Dedt,
            },
        }
        headers = {'cont_yn': cont_yn, 'cont_key': cont_key}
        return self._client.post(self.PATHS['ov_futopt_option_chart_tick'], body, extra_headers=headers)

    def ov_futopt_option_chart_min(
        self,
        *,
        Code: str,
        Tick: str,
        Dcnt: str,
        Dedt: str,
        cont_yn: str = 'N',
        cont_key: str = '',
    ) -> APIResponse:
        """해외옵션 분차트조회 (pibg7402).

        해외옵션 분차트 조회 API 입니다. ※ 해외선물옵션 API시세 신청이 되어있지 않은 경우 시세를 수신 하실 수 없습니다. ※
        API시세(유료) 신청방법 GTS(Happy+ Global) : [1761] API시세 신청

        엔드포인트: POST /api/v1/quote/overseas-futureoption/option-chart/min
        유량제어: 2 TPS
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=e1035c5a-edb1-4b7d-8336-04e2ab76ed35&api_id=8b592328-c2af-47f4-8230-b2bbc864e5a4

        Args:
            Code: 종목코드 — 종목코드 입력
            Tick: N분봉 — N분 (최대 900분)
            Dcnt: 조회건수 — 요청 데이터건수 (최대400건)
            Dedt: 조회일자 — 조회일자 (YYYYMMDD), 당일: 99999999 세팅
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. 주요 응답 필드:
              - Pind: price indicator
              - Nrec: 조회건수
              - Ikey: 조회구분
              - Sdir: 정렬방식
              - Aflg: 추가위치
              - Ckey: 다음조회가능여부
              - Nrow: 조회건수
              - Kval: 다음키값
              - Date: 체결일자
              - Bday: 영업일자
              - Time: 체결시간
              - Clos: 종가
              - Lvol: 체결량
              - Open: 시가
              - High: 고가
              - (이하 생략 — 가이드 참조)

        """
        body = {
            'In': {
                'Code': Code,
                'Tick': Tick,
                'Dcnt': Dcnt,
                'Dedt': Dedt,
            },
        }
        headers = {'cont_yn': cont_yn, 'cont_key': cont_key}
        return self._client.post(self.PATHS['ov_futopt_option_chart_min'], body, extra_headers=headers)

    def ov_futopt_option_chart_day_week_month(
        self,
        *,
        Code: str,
        Dtgb: str,
        Dcnt: str,
        Dedt: str,
        cont_yn: str = 'N',
        cont_key: str = '',
    ) -> APIResponse:
        """해외옵션 일주월차트조회 (pibg7403).

        해외옵션 일주월 차트 조회 API 입니다. ※ 해외선물옵션 API시세 신청이 되어있지 않은 경우 시세를 수신 하실 수 없습니다.
        ※ API시세(유료) 신청방법 GTS(Happy+ Global) : [1761] API시세 신청

        엔드포인트: POST /api/v1/quote/overseas-futureoption/option-chart/dwmonth
        유량제어: 2 TPS
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=e1035c5a-edb1-4b7d-8336-04e2ab76ed35&api_id=ab7a0411-be7b-4f90-885f-0c99ff2bccd3

        Args:
            Code: 종목코드 — 종목코드 입력
            Dtgb: 데이터구분 — 0: 일(daily) 1: 주(weekly) 2: 월(monthly)
            Dcnt: 조회건수 — 요청 데이터건수 (최대400건)
            Dedt: 조회일자 — 조회일자 (YYYYMMDD), 당일: 99999999 세팅
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. 주요 응답 필드:
              - Pind: price indicator
              - Nrec: 조회건수
              - Ikey: 조회구분
              - Sdir: 정렬방식
              - Aflg: 추가위치
              - Ckey: 다음조회가능여부
              - Nrow: 조회건수
              - Kval: 다음키값
              - Date: 체결일자
              - Clos: 종가
              - Tvol: 누적거래량
              - Open: 시가
              - High: 고가
              - Lowp: 저가

        """
        body = {
            'In': {
                'Code': Code,
                'Dtgb': Dtgb,
                'Dcnt': Dcnt,
                'Dedt': Dedt,
            },
        }
        headers = {'cont_yn': cont_yn, 'cont_key': cont_key}
        return self._client.post(self.PATHS['ov_futopt_option_chart_day_week_month'], body, extra_headers=headers)
