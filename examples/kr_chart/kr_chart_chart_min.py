"""분차트조회 (CHARTMIN) — standalone 예제.

그룹    : 국내주식/선물차트
엔드포인트: POST /api/v1/quote/kr-chart/min
TPS     : 4
가이드  : https://openapi.dbsec.co.kr/apiservice?group_id=0bc09824-e8c2-491a-8c9d-b99e64b4b907&api_id=f8581e1f-5621-4be6-a4e7-7cc8088d603f

국내주식/선물옵션 분차트 조회 API 입니다.

토큰은 examples/dbsec_helper.py 가 자동 발급/캐싱합니다.

실행:
    # examples/ 폴더에서 실행하는 경우:
    python kr_chart/kr_chart_chart_min.py
    # examples/kr_chart/ 폴더에서 실행하는 경우:
    python kr_chart_chart_min.py

── 응답 파라미터 (Out) ─ OUT_BEGIN ──────────────────────
  [TR CHARTMIN]
    Out  (배열)  Out
      Hour  (문자)  시간
      Date  (문자)  일자
      Prpr  (문자)  현재가
      Oprc  (문자)  시가
      Hprc  (문자)  고가
      Lprc  (문자)  저가
      CntgVol  (문자)  체결거래량

  공통: rsp_cd  응답코드  ·  rsp_msg  응답메시지
── OUT_END ──────────────────────────────────────────────
"""


import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from dbsec_helper import call_rest, print_response

resp, data = call_rest(
    url="/api/v1/quote/kr-chart/min",
    body={
        "In": {
            "dataCnt": "5",  # 호출건수 (str) - 입력범위: "1" ~ "2000" ""(공백입력) 또는 "0" 입력시 기본개수(400개)조회
            "InputCondMrktDivCode": "J",  # 입력조건시장분류코드 (str) - 주식:J 주식(NXT): NJ 주식(통합): UJ EN : ETN W: ELW F : 지수선물 JF : 주식선물 KF : 미니선물 CF : 상품선물 XF : 섹터선물 CM : 야간선물 O : 지수옵션 JO : 주식옵션 KO : 미니옵션 WO : K200위클리옵션 EU : 야간옵션 SO: 코스닥 150옵션 업종&지수: U ※ ETF종목의 경우 J 코드를 사용해 조회 부탁드립니다.
            "InputIscd1": "005930",  # 입력종목코드1 (str) - 주식(J, NJ, UJ) 선택시 주식종목코드 입력 - J(KRX 주식): - NJ(NXT 주식): - UJ(통합): ※ NXT/통합시세로 종목 조회 시 반드시 종목 앞에 구분자 (N-, U-)를 붙여서 호출 부탁드리겠습니다. 업종(U) 선택시 지수코드: 1001: KOSPI 2001: KOSDAQ 3001: KOSPI200 1002: 코스피(대형주) 1004: 코스피(소형주) 1053: KOSPI50종합지수 1054: KOSPI100종합지수 1163: 코스피고배당50 2002: 코스닥(대형주) 2004: 코스닥(소형주) 2203: 코스닥 150 3903: KP200레버리지지수 3907: 변동성지수 0100: KRX100 0600: KTOP 30 K001: KOVIXI00
            "InputDate1": "20260526",  # 입력날짜1 (str) - 조회 시작일을 YYYYMMDD 형식으로 입력 ex. 20241204
            "InputDivXtick": "600",  # 틱분틱일별구분코드 (str) - 30: 30초 60: 1분 600: 10분 3600: 60분 [60*N: N분]
            "InputOrgAdjPrc": "1",  # 수정주가사용여부 (str) - 0:수정주가 미사용 1: 수정주가 사용
        },
    },
    label="분차트조회",
)
print_response(resp, data)
