"""선물옵션 당일실현손익 (CFOAQ02600) — standalone 예제.

그룹    : 국내선물옵션주문
엔드포인트: POST /api/v1/trading/kr-futureoption/inquiry/day-rlzpnl
TPS     : 1
가이드  : https://openapi.dbsec.co.kr/apiservice?group_id=44c4a04f-f55e-4c1c-b4e2-b48ec4869aee&api_id=650b70b8-1712-405e-a4b7-4db23a5d9290

선물옵션 종목별 당일 매매 실현손익조회 API 입니다. ※ 모의투자 계좌로 사용가능한 API입니다.

토큰은 examples/dbsec_helper.py 가 자동 발급/캐싱합니다.

실행:
    # examples/ 폴더에서 실행하는 경우:
    python kr_futopt_order/kr_futopt_inquire_realized_pnl.py
    # examples/kr_futopt_order/ 폴더에서 실행하는 경우:
    python kr_futopt_inquire_realized_pnl.py

── 응답 파라미터 (Out) ─ OUT_BEGIN ──────────────────────
  [TR CFOAQ02600]
    Out  (배열)  Out
      FnoIsuNo  (문자)  선물옵션종목번호
      BnsTpCode  (문자)  매매구분
      PrdayUnsttQty  (숫자)  전일미결제수량
      UnsttQty  (숫자)  미결제수량
      LqdtQty  (숫자)  청산수량
      ThdayRlzPnlAmt  (숫자)  당일실현손익금액

  공통: rsp_cd  응답코드  ·  rsp_msg  응답메시지
── OUT_END ──────────────────────────────────────────────
"""

import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from dbsec_helper import call_rest, print_response

resp, data = call_rest(
    url="/api/v1/trading/kr-futureoption/inquiry/day-rlzpnl",
    body={
        "In": {
        },
    },
    label="선물옵션 당일실현손익",
)
print_response(resp, data)
