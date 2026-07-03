"""주식취소주문- NXT거래소 (CSPAT00810) — standalone 예제.

그룹    : 국내주식주문
엔드포인트: POST /api/v1/trading/kr-stock/order-cancel-nxt
TPS     : 3
가이드  : https://openapi.dbsec.co.kr/apiservice?group_id=05ac28b8-624f-4115-8aed-cf55f24279dd&api_id=159a17c5-6cba-4887-a963-8464cdb95d65

NXT 주문에 대해 취소하는 API 입니다. ※ 이미 체결완료된 주문은 취소가 불가능합니다.

토큰은 examples/dbsec_helper.py 가 자동 발급/캐싱합니다.

실행:
    # examples/ 폴더에서 실행하는 경우:
    python kr_stock_order/kr_stock_order_cancel_nxt.py
    # examples/kr_stock_order/ 폴더에서 실행하는 경우:
    python kr_stock_order_cancel_nxt.py

── 응답 파라미터 (Out) ─ OUT_BEGIN ──────────────────────
  [TR CSPAT00810]
    Out  (오브젝트)  Out
      OrdNo  (숫자)  주문번호 — 취소주문으로 채번된 주문번호
      PrntOrdNo  (숫자)  모주문번호 — 원 주문시 사용된 주문번호
      OrdTime  (문자)  주문시각 — 주문시각(HHMMSSSSS - 시분초)
      ShtnIsuNo  (문자)  단축종목번호
      IsuNm  (문자)  종목명 — 주문 종목의 한글명

  공통: rsp_cd  응답코드  ·  rsp_msg  응답메시지
── OUT_END ──────────────────────────────────────────────
"""

# ⚠️  경고: 실제 매매가 실행될 수 있는 주문 API입니다.
#        반드시 모의투자 환경(mode='demo')에서 먼저 테스트하세요.
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from dbsec_helper import call_rest, print_response

resp, data = call_rest(
    url="/api/v1/trading/kr-stock/order-cancel-nxt",
    body={
        "In": {
            "OrgOrdNo": 340809,  # 원주문번호 (int) - 주식주문 완료시 Out되는 OrdNo 값 입력 (DB증권 거래 시스템에서 채번된 주문번호)
            "IsuNo": "A003620",  # 종목번호 (str) - 원주문시 사용한 종목번호
            "OrdQty": 19,  # 주문수량 (int) - 주식 주문수량
        },
    },
    label="주식취소주문- NXT거래소",
)
print_response(resp, data)
