"""해외주식 월차트조회 (FSTKCHARTMONTH) — standalone 예제.

그룹    : 해외주식시세
엔드포인트: POST /api/v1/quote/overseas-stock/chart/month
TPS     : 4
가이드  : https://openapi.dbsec.co.kr/apiservice?group_id=a804e311-cb53-499b-9d8a-a4d838f0a484&api_id=789a2830-7620-4a44-8107-336b0fd3f611

해외주식 월차트 조회 API 입니다.

토큰은 examples/dbsec_helper.py 가 자동 발급/캐싱합니다.

실행:
    # examples/ 폴더에서 실행하는 경우:
    python ov_stock_quote/ov_stock_chart_month.py
    # examples/ov_stock_quote/ 폴더에서 실행하는 경우:
    python ov_stock_chart_month.py

── 응답 파라미터 (Out) ─ OUT_BEGIN ──────────────────────
  [TR FSTKCHARTMONTH]
    Out  (배열)  Out
      Hour  (문자)  시간
      Date  (문자)  일자
      Prpr  (문자)  현재가
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
    url="/api/v1/quote/overseas-stock/chart/month",
    body={
        "In": {
            "InputCondMrktDivCode": "FN",  # 입력조건시장분류코드 (str) - FY:뉴욕 FN:나스닥 FA:아멕스
            "InputIscd1": "TSLA",  # 입력종목코드1 (str) - 해외주식 종목코드
            "InputDate1": "20260101",  # 입력날짜1 (str) - 조회 시작일 (YYYYMMDD)
            "InputDate2": "20260526",  # 입력날짜2 (str) - 조회 마감일 (YYYYMMDD)
            "InputOrgAdjPrc": "1",  # 수정주가사용여부 (str) - 0:수정주가 미사용 1: 수정주가 사용
        },
    },
    label="해외주식 월차트조회",
)
print_response(resp, data)
