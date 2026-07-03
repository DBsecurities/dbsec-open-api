"""국내주식/선물차트 API 모듈.

DB증권 OpenAPI 그룹: 국내주식/선물차트
group_slug: kr_chart

이 파일은 `_specs/kr_chart/*.json` 에서 자동 생성되었습니다.
스펙이 갱신되면 `_workspace/build_modules.py`로 재생성하세요.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from dbsec_sdk.client import DBSecClient

from dbsec_sdk.response import APIResponse


class KrChartAPI:
    """국내주식/선물차트 API 모음.

    사용법:
        >>> client = DBSecClient("config.yaml")
        >>> resp = client.apis.kr_chart.<method>(...)
    """

    # API 경로 매핑
    PATHS = {
        'kr_chart_chart_tick': '/api/v1/quote/kr-chart/tick',
        'kr_chart_chart_min': '/api/v1/quote/kr-chart/min',
        'kr_chart_chart_day': '/api/v1/quote/kr-chart/day',
        'kr_chart_chart_week': '/api/v1/quote/kr-chart/week',
        'kr_chart_chart_month': '/api/v1/quote/kr-chart/month',
    }
    # TR 코드 매핑
    TR_CODES = {
        'kr_chart_chart_tick': 'CHARTTICK',
        'kr_chart_chart_min': 'CHARTMIN',
        'kr_chart_chart_day': 'CHARTDAY',
        'kr_chart_chart_week': 'CHARTWEEK',
        'kr_chart_chart_month': 'CHARTMONTH',
    }

    def __init__(self, client: 'DBSecClient'):
        self._client = client

    def kr_chart_chart_tick(
        self,
        *,
        InputOrgAdjPrc: str,
        InputCondMrktDivCode: str,
        dataCnt: str,
        InputIscd1: str,
        InputDate1: str,
        InputDivXtick: str,
        cont_yn: str = 'N',
        cont_key: str = '',
    ) -> APIResponse:
        """틱차트조회 (CHARTTICK).

        국내주식/선물옵션 틱차트 조회 API 입니다.

        엔드포인트: POST /api/v1/quote/kr-chart/tick
        유량제어: 4 TPS
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=0bc09824-e8c2-491a-8c9d-b99e64b4b907&api_id=efe731f7-0f2a-45d1-81da-335ebeacd552

        Args:
            InputOrgAdjPrc: 수정주가사용여부 — 0:수정주가 미사용 1: 수정주가 사용
            InputCondMrktDivCode: 입력조건시장분류코드 — 주식:J 주식(NXT): NJ 주식(통합): UJ EN : ETN W: ELW F : 지수선물 JF : 주식선물 KF : 미니선물 CF : 상품선물 XF : 섹터선물 CM : 야간선물 O : 지수옵션 JO : 주식옵션 KO : 미니옵션 WO : K200위클리옵션 EU : 야간옵션 SO: 코스닥 150옵션 업종&지수: U ※ ETF종목의 경우 J 코드를 사용...
            dataCnt: 호출건수 — 입력범위: "1" ~ "2000" ""(공백입력) 또는 "0" 입력시 기본개수(400개)조회
            InputIscd1: 입력종목코드1 — 주식(J, NJ, UJ) 선택시 주식종목코드 입력 - J(KRX 주식): (ex. 005930) - NJ(NXT 주식): (ex. N-005930) - UJ(통합): (ex. U-005930) ※ NXT/통합시세로 종목 조회 시 반드시 종목 앞에 구분자 (N-, U-)를 붙여서 호출 부탁드리겠습니다. 업종(U) 선택시 지수코드: 1001: KOSPI 200...
            InputDate1: 입력날짜1 — 조회 시작일을 YYYYMMDD 형식으로 입력 ex. 20241204
            InputDivXtick: 틱분틱일별구분코드 — N Tick 입력 ex. 100
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
                'InputCondMrktDivCode': InputCondMrktDivCode,
                'dataCnt': dataCnt,
                'InputIscd1': InputIscd1,
                'InputDate1': InputDate1,
                'InputDivXtick': InputDivXtick,
            },
        }
        headers = {'cont_yn': cont_yn, 'cont_key': cont_key}
        return self._client.post(self.PATHS['kr_chart_chart_tick'], body, extra_headers=headers)

    def kr_chart_chart_min(
        self,
        *,
        InputOrgAdjPrc: str,
        InputCondMrktDivCode: str,
        dataCnt: str,
        InputIscd1: str,
        InputDate1: str,
        InputDivXtick: str,
        cont_yn: str = 'N',
        cont_key: str = '',
    ) -> APIResponse:
        """분차트조회 (CHARTMIN).

        국내주식/선물옵션 분차트 조회 API 입니다.

        엔드포인트: POST /api/v1/quote/kr-chart/min
        유량제어: 4 TPS
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=0bc09824-e8c2-491a-8c9d-b99e64b4b907&api_id=f8581e1f-5621-4be6-a4e7-7cc8088d603f

        Args:
            InputOrgAdjPrc: 수정주가사용여부 — 0:수정주가 미사용 1: 수정주가 사용
            InputCondMrktDivCode: 입력조건시장분류코드 — 주식:J 주식(NXT): NJ 주식(통합): UJ EN : ETN W: ELW F : 지수선물 JF : 주식선물 KF : 미니선물 CF : 상품선물 XF : 섹터선물 CM : 야간선물 O : 지수옵션 JO : 주식옵션 KO : 미니옵션 WO : K200위클리옵션 EU : 야간옵션 SO: 코스닥 150옵션 업종&지수: U ※ ETF종목의 경우 J 코드를 사용...
            dataCnt: 호출건수 — 입력범위: "1" ~ "2000" ""(공백입력) 또는 "0" 입력시 기본개수(400개)조회
            InputIscd1: 입력종목코드1 — 주식(J, NJ, UJ) 선택시 주식종목코드 입력 - J(KRX 주식): (ex. 005930) - NJ(NXT 주식): (ex. N-005930) - UJ(통합): (ex. U-005930) ※ NXT/통합시세로 종목 조회 시 반드시 종목 앞에 구분자 (N-, U-)를 붙여서 호출 부탁드리겠습니다. 업종(U) 선택시 지수코드: 1001: KOSPI 200...
            InputDate1: 입력날짜1 — 조회 시작일을 YYYYMMDD 형식으로 입력 ex. 20241204
            InputDivXtick: 틱분틱일별구분코드 — 30: 30초 60: 1분 600: 10분 3600: 60분 [60*N: N분]
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
                'InputCondMrktDivCode': InputCondMrktDivCode,
                'dataCnt': dataCnt,
                'InputIscd1': InputIscd1,
                'InputDate1': InputDate1,
                'InputDivXtick': InputDivXtick,
            },
        }
        headers = {'cont_yn': cont_yn, 'cont_key': cont_key}
        return self._client.post(self.PATHS['kr_chart_chart_min'], body, extra_headers=headers)

    def kr_chart_chart_day(
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
        """일차트조회 (CHARTDAY).

        국내주식/선물옵션 일차트 조회 API 입니다.

        엔드포인트: POST /api/v1/quote/kr-chart/day
        유량제어: 4 TPS
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=0bc09824-e8c2-491a-8c9d-b99e64b4b907&api_id=85fa3c5f-c317-43ab-8590-f57a28f2f8e9

        Args:
            InputOrgAdjPrc: 수정주가사용여부 — 0:수정주가 미사용 1: 수정주가 사용
            InputCondMrktDivCode: 입력조건시장분류코드 — 주식:J 주식(NXT): NJ 주식(통합): UJ EN : ETN W: ELW F : 지수선물 JF : 주식선물 KF : 미니선물 CF : 상품선물 XF : 섹터선물 CM : 야간선물 O : 지수옵션 JO : 주식옵션 KO : 미니옵션 WO : K200위클리옵션 EU : 야간옵션 SO: 코스닥 150옵션 업종&지수: U ※ ETF종목의 경우 J 코드를 사용...
            InputIscd1: 입력종목코드1 — 주식(J, NJ, UJ) 선택시 주식종목코드 입력 - J(KRX 주식): (ex. 005930) - NJ(NXT 주식): (ex. N-005930) - UJ(통합): (ex. U-005930) ※ NXT/통합시세로 종목 조회 시 반드시 종목 앞에 구분자 (N-, U-)를 붙여서 호출 부탁드리겠습니다. 업종(U) 선택시 지수코드: 1001: KOSPI 200...
            InputDate1: 입력날짜1 — YYYYMMDD (조회 시작일)
            InputDate2: 입력날짜2 — YYYYMMDD (조회 종료일)
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. 주요 응답 필드:
              - Out: Out
              - Hour: 시간
              - Date: 일자
              - Prpr: 현재가 — UJ 통합시세 조회시 종가(현재가)는 KRX 거래소 종가가 아닌, NXT 거래소 종가를 사용합니다.
              - Oprc: 시가
              - Hprc: 고가
              - Lprc: 저가
              - CntgVol: 체결거래량

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
        return self._client.post(self.PATHS['kr_chart_chart_day'], body, extra_headers=headers)

    def kr_chart_chart_week(
        self,
        *,
        InputOrgAdjPrc: str,
        InputPeriodDivCode: str,
        InputCondMrktDivCode: str,
        InputIscd1: str,
        InputDate1: str,
        InputDate2: str,
        cont_yn: str = 'N',
        cont_key: str = '',
    ) -> APIResponse:
        """주차트조회 (CHARTWEEK).

        국내주식/선물옵션 주차트 조회 API 입니다.

        엔드포인트: POST /api/v1/quote/kr-chart/week
        유량제어: 4 TPS
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=0bc09824-e8c2-491a-8c9d-b99e64b4b907&api_id=2a108f78-c73f-409f-82fa-d81befc899f8

        Args:
            InputOrgAdjPrc: 수정주가사용여부 — 0:수정주가 미사용 1: 수정주가 사용
            InputPeriodDivCode: 입력주 — "W"
            InputCondMrktDivCode: 입력조건시장분류코드 — 주식:J 주식(NXT): NJ 주식(통합): UJ EN : ETN W: ELW F : 지수선물 JF : 주식선물 KF : 미니선물 CF : 상품선물 XF : 섹터선물 CM : 야간선물 O : 지수옵션 JO : 주식옵션 KO : 미니옵션 WO : K200위클리옵션 EU : 야간옵션 SO: 코스닥 150옵션 업종&지수: U ※ ETF종목의 경우 J 코드를 사용...
            InputIscd1: 입력종목코드1 — 주식(J, NJ, UJ) 선택시 주식종목코드 입력 - J(KRX 주식): (ex. 005930) - NJ(NXT 주식): (ex. N-005930) - UJ(통합): (ex. U-005930) ※ NXT/통합시세로 종목 조회 시 반드시 종목 앞에 구분자 (N-, U-)를 붙여서 호출 부탁드리겠습니다. 업종(U) 선택시 지수코드: 1001: KOSPI 200...
            InputDate1: 입력날짜1 — YYYYMMDD (조회 시작일)
            InputDate2: 입력날짜2 — YYYYMMDD (조회 종료일)
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. 주요 응답 필드:
              - Out: Out
              - Hour: 시간
              - Date: 일자
              - Prpr: 현재가 — UJ 통합시세 조회시 종가(현재가)는 KRX 거래소 종가가 아닌, NXT 거래소 종가를 사용합니다.
              - Oprc: 시가
              - Hprc: 고가
              - Lprc: 저가
              - CntgVol: 체결거래량

        """
        body = {
            'In': {
                'InputOrgAdjPrc': InputOrgAdjPrc,
                'InputPeriodDivCode': InputPeriodDivCode,
                'InputCondMrktDivCode': InputCondMrktDivCode,
                'InputIscd1': InputIscd1,
                'InputDate1': InputDate1,
                'InputDate2': InputDate2,
            },
        }
        headers = {'cont_yn': cont_yn, 'cont_key': cont_key}
        return self._client.post(self.PATHS['kr_chart_chart_week'], body, extra_headers=headers)

    def kr_chart_chart_month(
        self,
        *,
        InputOrgAdjPrc: str,
        InputCondMrktDivCode: str,
        InputIscd1: str,
        InputDate1: str,
        InputDate2: str,
        InputPeriodDivCode: str,
        cont_yn: str = 'N',
        cont_key: str = '',
    ) -> APIResponse:
        """월차트조회 (CHARTMONTH).

        국내주식/선물옵션 월차트 조회 API 입니다.

        엔드포인트: POST /api/v1/quote/kr-chart/month
        유량제어: 4 TPS
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=0bc09824-e8c2-491a-8c9d-b99e64b4b907&api_id=e34ed58e-6f91-4faa-8112-b9206395f2f0

        Args:
            InputOrgAdjPrc: 수정주가사용여부 — 0:수정주가 미사용 1: 수정주가 사용
            InputCondMrktDivCode: 입력조건시장분류코드 — 주식:J 주식(NXT): NJ 주식(통합): UJ EN : ETN W: ELW F : 지수선물 JF : 주식선물 KF : 미니선물 CF : 상품선물 XF : 섹터선물 CM : 야간선물 O : 지수옵션 JO : 주식옵션 KO : 미니옵션 WO : K200위클리옵션 EU : 야간옵션 SO: 코스닥 150옵션 업종&지수: U ※ ETF종목의 경우 J 코드를 사용...
            InputIscd1: 입력종목코드1 — 주식(J, NJ, UJ) 선택시 주식종목코드 입력 - J(KRX 주식): (ex. 005930) - NJ(NXT 주식): (ex. N-005930) - UJ(통합): (ex. U-005930) ※ NXT/통합시세로 종목 조회 시 반드시 종목 앞에 구분자 (N-, U-)를 붙여서 호출 부탁드리겠습니다. 업종(U) 선택시 지수코드: 1001: KOSPI 200...
            InputDate1: 입력날짜1 — YYYYMMDD (조회 시작일)
            InputDate2: 입력날짜2 — YYYYMMDD (조회 종료일)
            InputPeriodDivCode: 입력일 - 월/년 — M:월 Y:년
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. 주요 응답 필드:
              - Out: Out
              - Hour: 시간
              - Date: 일자
              - Prpr: 현재가 — UJ 통합시세 조회시 종가(현재가)는 KRX 거래소 종가가 아닌, NXT 거래소 종가를 사용합니다.
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
                'InputPeriodDivCode': InputPeriodDivCode,
            },
        }
        headers = {'cont_yn': cont_yn, 'cont_key': cont_key}
        return self._client.post(self.PATHS['kr_chart_chart_month'], body, extra_headers=headers)
