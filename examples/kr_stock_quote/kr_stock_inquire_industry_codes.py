"""업종분류코드 조회 (USTOCKCOND) — standalone 예제.

그룹    : 국내주식시세
엔드포인트: POST /api/v1/quote/kr-stock/inquiry/industry-cls
TPS     : 2
가이드  : https://openapi.dbsec.co.kr/apiservice?group_id=80005fb0-6feb-4b8b-904a-605c59e29b4f&api_id=d373d73b-9d99-474e-a990-048132353d61

국내 업종분류코드를 조회 할 수 있는 API 입니다.

토큰은 examples/dbsec_helper.py 가 자동 발급/캐싱합니다.

실행:
    # examples/ 폴더에서 실행하는 경우:
    python kr_stock_quote/kr_stock_inquire_industry_codes.py
    # examples/kr_stock_quote/ 폴더에서 실행하는 경우:
    python kr_stock_inquire_industry_codes.py

── 응답 파라미터 (Out) ─ OUT_BEGIN ──────────────────────
  [TR USTOCKCOND]
    입력조건시장분류코드  (배열)  입력조건시장분류코드
      Iscd  (문자)  종목코드
      KorIsnm  (문자)  한글종목명

  공통: rsp_cd  응답코드  ·  rsp_msg  응답메시지
── OUT_END ──────────────────────────────────────────────
"""


import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from dbsec_helper import call_rest, print_response

resp, data = call_rest(
    url="/api/v1/quote/kr-stock/inquiry/industry-cls",
    body={
        "In": {
            "InputCondMrktDivCode": "U",  # 입력조건시장분류코드 (str) - K: 코스피 Q: 코스닥 K2: Kospi200 KR: KRX
            "InputMrktClsCode": "K",  # 입력시장구분코드 (str) - 입력시장 구분코드로, 입력값은 "U" 고정입니다.
        },
    },
    label="업종분류코드 조회",
)
print_response(resp, data)
