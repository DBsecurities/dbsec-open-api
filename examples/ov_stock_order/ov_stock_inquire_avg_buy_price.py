"""해외주식 평균매입단가 조회 (CAZCQ03400) — standalone 예제.

그룹    : 해외주식주문
엔드포인트: POST /api/v1/trading/overseas-stock/inquiry/avg-pur-price
TPS     : 2
가이드  : https://openapi.dbsec.co.kr/apiservice?group_id=e4726f55-cc3b-45af-a1b5-852628fe5960&api_id=cd7db5da-e848-4d0f-b64d-3476f3b820cd

보유중인 해외주식 종목의 평균 매입단가를 조회할 수 있는 API입니다.

토큰은 examples/dbsec_helper.py 가 자동 발급/캐싱합니다.

실행:
    # examples/ 폴더에서 실행하는 경우:
    python ov_stock_order/ov_stock_inquire_avg_buy_price.py
    # examples/ov_stock_order/ 폴더에서 실행하는 경우:
    python ov_stock_inquire_avg_buy_price.py

── 응답 파라미터 (Out) ─ OUT_BEGIN ──────────────────────
  [TR CAZCQ03400]
    Out  (오브젝트)  Out
      AstkAvrPchsPrc  (숫자)  해외주식평균매입가
      AstkMktCode  (문자)  해외주식시장코드
      OwnSeCode  (문자)  자체증권거래소코드

  공통: rsp_cd  응답코드  ·  rsp_msg  응답메시지
── OUT_END ──────────────────────────────────────────────
"""

import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from dbsec_helper import call_rest, print_response

resp, data = call_rest(
    url="/api/v1/trading/overseas-stock/inquiry/avg-pur-price",
    body={
        "In": {
            "AstkIsuNo": "METU",  # 해외주식종목번호 (str) - 미국주식/ETF: "종목코드"
        },
    },
    label="해외주식 평균매입단가 조회",
)
print_response(resp, data)
