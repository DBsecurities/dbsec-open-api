"""선물옵션 취소주문 (야간) (CFOHT00300) — standalone 예제.

그룹    : 국내선물옵션주문
엔드포인트: POST /api/v1/trading/night-futureoption/order-cancel
TPS     : 10
가이드  : https://openapi.dbsec.co.kr/apiservice?group_id=44c4a04f-f55e-4c1c-b4e2-b48ec4869aee&api_id=b5ca7d0b-30de-4723-b84f-d15c928ab346

야간선물옵션 주문에 대해 취소하는 API 입니다. ※ 이미 체결완료된 주문은 취소가 불가능합니다.

토큰은 examples/dbsec_helper.py 가 자동 발급/캐싱합니다.

실행:
    # examples/ 폴더에서 실행하는 경우:
    python kr_futopt_order/kr_futopt_order_cancel_night.py
    # examples/kr_futopt_order/ 폴더에서 실행하는 경우:
    python kr_futopt_order_cancel_night.py

── 응답 파라미터 (Out) ─ OUT_BEGIN ──────────────────────
  [TR CFOHT00300]
    Out  (오브젝트)  Out
      OrdNo  (숫자)  주문번호
      IsuNm  (문자)  종목명

  공통: rsp_cd  응답코드  ·  rsp_msg  응답메시지
── OUT_END ──────────────────────────────────────────────
"""

# ⚠️  경고: 실제 매매가 실행될 수 있는 주문 API입니다.
#        반드시 모의투자 환경(mode='demo')에서 먼저 테스트하세요.
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from dbsec_helper import call_rest, print_response

resp, data = call_rest(
    url="/api/v1/trading/night-futureoption/order-cancel",
    body={
        "In": {
            "FnoIsuNo": "175V2000",  # 선물옵션종목번호 (str) - 취소 주문을 진행할 원 주문에서 주문한 종목번호
            "OrgOrdNo": 5,  # 원주문번호 (int) - 취소 주문을 진행할 원 주문번호
            "CancQty": 3,  # 취소수량 (int) - 취소 주문을 진행할 취소수량입력
        },
    },
    label="선물옵션 취소주문 (야간)",
)
print_response(resp, data)
