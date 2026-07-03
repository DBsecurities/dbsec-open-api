"""주식종목 조회 (JCODES) — standalone 예제.

그룹    : 국내주식시세
엔드포인트: POST /api/v1/quote/kr-stock/inquiry/stock-ticker
TPS     : 3
가이드  : https://openapi.dbsec.co.kr/apiservice?group_id=80005fb0-6feb-4b8b-904a-605c59e29b4f&api_id=d8621b8b-11fd-4d01-b175-e6e3f6285215

국내주식 종목조회 API입니다. ※ 연속키 조회를 통해 종목을 추가로 조회 할 수 있습니다.

토큰은 examples/dbsec_helper.py 가 자동 발급/캐싱합니다.

실행:
    # examples/ 폴더에서 실행하는 경우:
    python kr_stock_quote/kr_stock_search_stocks.py
    # examples/kr_stock_quote/ 폴더에서 실행하는 경우:
    python kr_stock_search_stocks.py

── 응답 파라미터 (Out) ─ OUT_BEGIN ──────────────────────
  [TR JCODES]
    Out  (배열)  Out
      MrktClsName  (문자)  시장구분명 — 종목 시장구분 코드입니다. 구분자 목록: "ETF", "ETN","코넥스","코스닥","거래소(코스피)"
      Iscd  (문자)  종목코드
      StndIscd  (문자)  표준종목코드
      KorIsnm  (문자)  한글종목명
      MrktClsCode  (문자)  시장분류구분코드 — 1: 코스닥 4: 코스피

  공통: rsp_cd  응답코드  ·  rsp_msg  응답메시지
── OUT_END ──────────────────────────────────────────────
"""


import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from dbsec_helper import call_rest, print_response

resp, data = call_rest(
    url="/api/v1/quote/kr-stock/inquiry/stock-ticker",
    body={
        "In": {
            "InputCondMrktDivCode": "J",  # 입력조건시장분류코드 (str) - J : 주식 (KRX) NJ : 주식(NXT) UJ : 주식(통합) E : ETF EN : ETN
        },
    },
    label="주식종목 조회",
)
print_response(resp, data)
