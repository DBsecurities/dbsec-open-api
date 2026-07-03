"""국내 ETF/ETN 구성종목조회 (ETFCOMPCODE) — standalone 예제.

그룹    : 국내주식시세
엔드포인트: POST /api/v1/quote/kr-stock/inquiry/etf-holdings
TPS     : 2
가이드  : https://openapi.dbsec.co.kr/apiservice?group_id=80005fb0-6feb-4b8b-904a-605c59e29b4f&api_id=660ce8d7-00ab-41dc-b9b3-bb7322cd4729



토큰은 examples/dbsec_helper.py 가 자동 발급/캐싱합니다.

실행:
    # examples/ 폴더에서 실행하는 경우:
    python kr_stock_quote/kr_stock_inquire_etf_etn_stock.py
    # examples/kr_stock_quote/ 폴더에서 실행하는 경우:
    python kr_stock_inquire_etf_etn_stock.py

── 응답 파라미터 (Out) ─ OUT_BEGIN ──────────────────────
  [TR ETFCOMPCODE]
    Out  (배열)  Out
      KorIsnm  (문자)  한글종목명
      Prpr  (문자)  현재가
      PrdyVrssSign  (문자)  전일대비부호
      PrdyVrss  (문자)  전일대비
      PrdyCtrt  (문자)  전일대비율
      EtfCuUnitScrtCnt  (문자)  ETFCU단위증권수
      EtfCnfgRate  (문자)  ETF구성비율
      Iscd  (문자)  종목코드

  공통: rsp_cd  응답코드  ·  rsp_msg  응답메시지
── OUT_END ──────────────────────────────────────────────
"""


import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from dbsec_helper import call_rest, print_response

resp, data = call_rest(
    url="/api/v1/quote/kr-stock/inquiry/etf-holdings",
    body={
        "In": {
            "InputMrktClsCode": "A",  # 입력시장구분코드 (str) - "A" 고정
            "InputCondMrktDivCode": "J",  # 입력조건시장분류코드 (str) - ETF 종목 조회시 : J ETN 종목조회시 : EN
            "InputIscd1": "0098N0",  # 입력종목코드1 (str) - 종목코드 입력
        },
    },
    label="국내 ETF/ETN 구성종목조회",
)
print_response(resp, data)
