"""월차트조회 (CHARTMONTH) — standalone 예제.

그룹    : 국내주식/선물차트
엔드포인트: POST /api/v1/quote/kr-chart/month
TPS     : 4
가이드  : https://openapi.dbsec.co.kr/apiservice?group_id=0bc09824-e8c2-491a-8c9d-b99e64b4b907&api_id=e34ed58e-6f91-4faa-8112-b9206395f2f0

국내주식/선물옵션 월차트 조회 API 입니다.

토큰은 examples/dbsec_helper.py 가 자동 발급/캐싱합니다.

실행:
    # examples/ 폴더에서 실행하는 경우:
    python kr_chart/kr_chart_chart_month.py
    # examples/kr_chart/ 폴더에서 실행하는 경우:
    python kr_chart_chart_month.py

── 응답 파라미터 (Out) ─ OUT_BEGIN ──────────────────────
  [TR CHARTMONTH]
    Out  (배열)  Out
      Hour  (문자)  시간
      Date  (문자)  일자
      Prpr  (문자)  현재가 — UJ 통합시세 조회시 종가(현재가)는 KRX 거래소 종가가 아닌, NXT 거래소 종가를 사용합니다.
      Oprc  (문자)  시가
      Hprc  (문자)  고가
      Lprc  (문자)  저가
      AcmlVol  (문자)  누적체결거래량

  공통: rsp_cd  응답코드  ·  rsp_msg  응답메시지
── OUT_END ──────────────────────────────────────────────
"""


import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from dbsec_helper import call_rest, print_response

resp, data = call_rest(
    url="/api/v1/quote/kr-chart/month",
    body={
        "In": {
            "InputCondMrktDivCode": "J",  # 입력조건시장분류코드 (str) - 주식:J 주식(NXT): NJ 주식(통합): UJ EN : ETN W: ELW F : 지수선물 JF : 주식선물 KF : 미니선물 CF : 상품선물 XF : 섹터선물 CM : 야간선물 O : 지수옵션 JO : 주식옵션 KO : 미니옵션 WO : K200위클리옵션 EU : 야간옵션 SO: 코스닥 150옵션 업종&지수: U ※ ETF종목의 경우 J 코드를 사용해 조회 부탁드립니다.
            "InputIscd1": "005930",  # 입력종목코드1 (str) - 주식(J, NJ, UJ) 선택시 주식종목코드 입력 - J(KRX 주식): - NJ(NXT 주식): - UJ(통합): ※ NXT/통합시세로 종목 조회 시 반드시 종목 앞에 구분자 (N-, U-)를 붙여서 호출 부탁드리겠습니다. 업종(U) 선택시 지수코드: 1001: KOSPI 2001: KOSDAQ 3001: KOSPI200 1002: 코스피(대형주) 1004: 코스피(소형주) 1053: KOSPI50종합지수 1054: KOSPI100종합지수 1163: 코스피고배당50 2002: 코스닥(대형주) 2004: 코스닥(소형주) 2203: 코스닥 150 3903: KP200레버리지지수 3907: 변동성지수 0100: KRX100 0600: KTOP 30 K001: KOVIXI00
            "InputPeriodDivCode": "M",  # 입력일 - 월/년 (str) - M:월 Y:년
            "InputDate1": "20250501",  # 입력날짜1 (str) - YYYYMMDD (조회 시작일)
            "InputDate2": "20260501",  # 입력날짜2 (str) - YYYYMMDD (조회 종료일)
            "InputOrgAdjPrc": "1",  # 수정주가사용여부 (str) - 0:수정주가 미사용 1: 수정주가 사용
        },
    },
    label="월차트조회",
)
print_response(resp, data)
