"""채권잔고조회 (CSPAQ01200) — standalone 예제.

그룹    : 장내채권주문
엔드포인트: POST /api/v1/trading/krx-bond/inquiry/balance
TPS     : 2
가이드  : https://openapi.dbsec.co.kr/apiservice?group_id=4a7257ed-b94a-462e-987d-132f064ed0d3&api_id=e12626bf-b1ab-4bbe-aeac-43dad091f91a

채권 잔고조회 API입니다.

토큰은 examples/dbsec_helper.py 가 자동 발급/캐싱합니다.

실행:
    # examples/ 폴더에서 실행하는 경우:
    python bond_order/bond_inquire_balance.py
    # examples/bond_order/ 폴더에서 실행하는 경우:
    python bond_inquire_balance.py

── 응답 파라미터 (Out) ─ OUT_BEGIN ──────────────────────
  [TR CSPAQ01200]
    Out  (배열)  Out
      IsuNo  (문자)  종목번호
      IsuNm  (문자)  종목명
      BuyDt  (문자)  매수일
      OrdAbleQty  (숫자)  주문가능수량
      SellOrdQty  (숫자)  매도주문수량
      BalQty  (숫자)  채권잔고수량
      UseRestrcQty  (숫자)  사용제한수량
      LoanDt  (문자)  대출일
      DueDt  (문자)  만기일자
      LoanQty  (숫자)  대출수량
      LoanRfundQty  (숫자)  대출상환수량
      BuyPrc  (숫자)  매수가

  공통: rsp_cd  응답코드  ·  rsp_msg  응답메시지
── OUT_END ──────────────────────────────────────────────
"""

import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from dbsec_helper import call_rest, print_response

resp, data = call_rest(
    url="/api/v1/trading/krx-bond/inquiry/balance",
    body={
        "In": {
        },
    },
    label="채권잔고조회",
)
print_response(resp, data)
