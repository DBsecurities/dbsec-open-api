"""채권취소주문 (CSPAT02200) — standalone 예제.

그룹    : 장내채권주문
엔드포인트: POST /api/v1/trading/krx-bond/order-cancel
TPS     : 5
가이드  : https://openapi.dbsec.co.kr/apiservice?group_id=4a7257ed-b94a-462e-987d-132f064ed0d3&api_id=0b1608cd-d704-467d-88d4-9dabd7ceaaf3

채권주문에 대해 취소하는 API 입니다. ※ 이미 체결완료된 주문은 취소가 불가능합니다.

토큰은 examples/dbsec_helper.py 가 자동 발급/캐싱합니다.

실행:
    # examples/ 폴더에서 실행하는 경우:
    python bond_order/bond_order_cancel.py
    # examples/bond_order/ 폴더에서 실행하는 경우:
    python bond_order_cancel.py

── 응답 파라미터 (Out) ─ OUT_BEGIN ──────────────────────
  [TR CSPAT02200]
    Out  (오브젝트)  Out
      OrdNo  (숫자)  주문번호

  공통: rsp_cd  응답코드  ·  rsp_msg  응답메시지
── OUT_END ──────────────────────────────────────────────
"""

# ⚠️  경고: 실제 매매가 실행될 수 있는 주문 API입니다.
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from dbsec_helper import call_rest, print_response

resp, data = call_rest(
    url="/api/v1/trading/krx-bond/order-cancel",
    body={
        "In": {
            "OrgOrdNo": 8,  # 원주문번호 (int)
            "IsuNo": "KR6000301C31",  # 종목번호 (str)
            "OrdQty": 10000,  # 주문수량 (int)
        },
    },
    label="채권취소주문",
)
print_response(resp, data)
