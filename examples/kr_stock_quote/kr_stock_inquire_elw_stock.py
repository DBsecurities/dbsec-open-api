"""ELW 종목 조회 (WCODES) — standalone 예제.

그룹    : 국내주식시세
엔드포인트: POST /api/v1/quote/kr-stock/inquiry/elw-ticker
TPS     : 3
가이드  : https://openapi.dbsec.co.kr/apiservice?group_id=80005fb0-6feb-4b8b-904a-605c59e29b4f&api_id=7c9a349c-1629-4059-9f06-6bcf8c093fe0

국내 ELW 종목조회 API입니다. ※ 연속키 조회를 통해 종목을 추가로 조회 할 수 있습니다.

토큰은 examples/dbsec_helper.py 가 자동 발급/캐싱합니다.

실행:
    # examples/ 폴더에서 실행하는 경우:
    python kr_stock_quote/kr_stock_inquire_elw_stock.py
    # examples/kr_stock_quote/ 폴더에서 실행하는 경우:
    python kr_stock_inquire_elw_stock.py

── 응답 파라미터 (Out) ─ OUT_BEGIN ──────────────────────
  [TR WCODES]
    Out  (배열)  Out
      Iscd  (문자)  종목코드
      StndIscd  (문자)  표준종목코드
      KorIsnm  (문자)  한글종목명
      MrktClsCode  (문자)  시장분류구분코드

  공통: rsp_cd  응답코드  ·  rsp_msg  응답메시지
── OUT_END ──────────────────────────────────────────────
"""


import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from dbsec_helper import call_rest, print_response

resp, data = call_rest(
    url="/api/v1/quote/kr-stock/inquiry/elw-ticker",
    body={
        "In": {
            "InputCondMrktDivCode": "W",  # 입력조건시장분류코드 (str) - "W" 입력
        },
    },
    label="ELW 종목 조회",
)
print_response(resp, data)
