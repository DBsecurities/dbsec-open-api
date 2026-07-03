"""신용상환가능총수량조회 (CSPAQ09400) — standalone 예제.

그룹    : 국내주식주문
엔드포인트: POST /api/v1/trading/kr-stock/inquiry/able-crdrepayment
TPS     : 1
가이드  : https://openapi.dbsec.co.kr/apiservice?group_id=05ac28b8-624f-4115-8aed-cf55f24279dd&api_id=0caa0bba-7ac1-49f9-b859-5ddb305f6d71

종목에 대한 신용상황가능 수량을 조회할 수 있는 API입니다. ※ 신용 약정등록이 완료된 계좌만 사용가능합니다.

토큰은 examples/dbsec_helper.py 가 자동 발급/캐싱합니다.

실행:
    # examples/ 폴더에서 실행하는 경우:
    python kr_stock_order/kr_stock_inquire_credit_repayment.py
    # examples/kr_stock_order/ 폴더에서 실행하는 경우:
    python kr_stock_inquire_credit_repayment.py

── 응답 파라미터 (Out) ─ OUT_BEGIN ──────────────────────
  [TR CSPAQ09400]
    Out  (오브젝트)  Out
      OrdAbleQty  (숫자)  주문가능수량

  공통: rsp_cd  응답코드  ·  rsp_msg  응답메시지
── OUT_END ──────────────────────────────────────────────
"""

import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from dbsec_helper import call_rest, print_response

resp, data = call_rest(
    url="/api/v1/trading/kr-stock/inquiry/able-crdrepayment",
    body={
        "In": {
            "IsuNo": "A005930",  # 종목번호 (str) - 주식/ETF: 종목코드6자리 or "A"+"종목코드" ETN: Q + 종목코드 ELW: J + 종목코드
            "BnsTpCode": "1",  # 매매구분코드 (str) - 1:매도 2:매수
        },
    },
    label="신용상환가능총수량조회",
)
print_response(resp, data)
