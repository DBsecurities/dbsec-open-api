"""해외주식종목 조회 (FSTKCODES) — standalone 예제.

그룹    : 해외주식시세
엔드포인트: POST /api/v1/quote/overseas-stock/inquiry/stock-ticker
TPS     : 2
가이드  : https://openapi.dbsec.co.kr/apiservice?group_id=a804e311-cb53-499b-9d8a-a4d838f0a484&api_id=22c67f31-c325-4898-8929-6ba9836d982f

해외주식 종목 조회 API 입니다.

토큰은 examples/dbsec_helper.py 가 자동 발급/캐싱합니다.

실행:
    # examples/ 폴더에서 실행하는 경우:
    python ov_stock_quote/ov_stock_search_stocks.py
    # examples/ov_stock_quote/ 폴더에서 실행하는 경우:
    python ov_stock_search_stocks.py

── 응답 파라미터 (Out) ─ OUT_BEGIN ──────────────────────
  [TR FSTKCODES]
    Out  (배열)  Out
      Iscd  (문자)  종목코드
      KorIsnm  (문자)  한글종목명
      BstpLargName  (문자)  업종대분류명
      ExchClsCode2  (문자)  거래소코드2
      SelnVolUnit  (문자)  매도량단위
      ShnuVolUnit  (문자)  매수량단위

  공통: rsp_cd  응답코드  ·  rsp_msg  응답메시지
── OUT_END ──────────────────────────────────────────────
"""


import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from dbsec_helper import call_rest, print_response

resp, data = call_rest(
    url="/api/v1/quote/overseas-stock/inquiry/stock-ticker",
    body={
        "In": {
            "InputDataCode": "NA",  # 입력해외증시구분코드 (str) - NY: 뉴욕 NA: 나스닥 AM: 아멕스
        },
    },
    label="해외주식종목 조회",
)
print_response(resp, data)
