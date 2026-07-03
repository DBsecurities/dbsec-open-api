"""선물옵션 정정주문 (CFOAT00200) — standalone 예제.

그룹    : 국내선물옵션주문
엔드포인트: POST /api/v1/trading/kr-futureoption/order-revision
TPS     : 10
가이드  : https://openapi.dbsec.co.kr/apiservice?group_id=44c4a04f-f55e-4c1c-b4e2-b48ec4869aee&api_id=26a01517-ed97-4bf9-a66f-eb4be7abb87f

선물옵션 주문에 대해 정정하는 API 입니다. ※ 모의투자 계좌로 사용가능한 API입니다. ※ 이미 체결완료된 주문은 정정이 불가능합니다.

토큰은 examples/dbsec_helper.py 가 자동 발급/캐싱합니다.

실행:
    # examples/ 폴더에서 실행하는 경우:
    python kr_futopt_order/kr_futopt_order_modify.py
    # examples/kr_futopt_order/ 폴더에서 실행하는 경우:
    python kr_futopt_order_modify.py

── 응답 파라미터 (Out) ─ OUT_BEGIN ──────────────────────
  [TR CFOAT00200]
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
    url="/api/v1/trading/kr-futureoption/order-revision",
    body={
        "In": {
            "FnoIsuNo": "106V3000",  # 선물옵션종목번호 (str) - 선물옵션 종목 코드 입력 선물 EX) 211V2060 옵션 EX) 201V2347
            "OrgOrdNo": 2104,  # 원주문번호 (int)
            "FnoOrdprcPtnCode": "00",  # 선물옵션호가유형코드 (str) - 00:지정가 03:시장가 05:조건부지정가 06:최유리지정가 10:지정가(IOC) 20:지정가(FOK)
            "OrdPrc": 1280.7,  # 주문가격 (int)
            "MdfyQty": 10,  # 정정수량 (int)
        },
    },
    label="선물옵션 정정주문",
)
print_response(resp, data)
