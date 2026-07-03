"""선물옵션 잔고조회 (야간) (CFOHQ02500) — standalone 예제.

그룹    : 국내선물옵션주문
엔드포인트: POST /api/v1/trading/night-futureoption/inquiry/balance
TPS     : 2
가이드  : https://openapi.dbsec.co.kr/apiservice?group_id=44c4a04f-f55e-4c1c-b4e2-b48ec4869aee&api_id=1bee0db4-d037-4983-95f2-08bc5fa8b876

야간선물옵션 잔고조회 API 입니다. ※ 잔고가 전부 표시되지 않는경우 연속키 조회를 통해 확인하실 수 있습니다.

토큰은 examples/dbsec_helper.py 가 자동 발급/캐싱합니다.

실행:
    # examples/ 폴더에서 실행하는 경우:
    python kr_futopt_order/kr_futopt_inquire_balance_night.py
    # examples/kr_futopt_order/ 폴더에서 실행하는 경우:
    python kr_futopt_inquire_balance_night.py

── 응답 파라미터 (Out) ─ OUT_BEGIN ──────────────────────
  [TR CFOHQ02500]
    Out  (오브젝트)  Out
      TotBnsAmt  (숫자)  총매매금액
      TotEvalAmt  (숫자)  총평가금액
      TotEvalPnlAmt  (숫자)  총평가손익금액
      TotErnrat  (숫자)  총수익률
      ThdayRlzPnlAmt  (숫자)  당일실현손익금액
      EvalDpstgTotamt  (숫자)  평가예탁총액
      OrdAbleAmt  (숫자)  주문가능금액
      CmsnAmt  (숫자)  수수료금액
    Out1  (배열)  Out1
      FnoIsuNo  (문자)  선물옵션종목번호
      IsuNm  (문자)  종목명
      BnsTpCode  (문자)  매매구분
      LqdtOrdAbleQty  (숫자)  청산주문가능수량
      PrdayUnsttQty  (숫자)  전일미결제수량
      IncdecQty  (숫자)  증감수량
      UnsttQty  (숫자)  미결제수량
      UnercQty  (숫자)  미체결수량
      BnsUprc  (숫자)  매매단가
      Curprc  (숫자)  현재가
      EvalPnlAmt  (숫자)  평가손익금액
      Ernrat  (숫자)  수익률
      FnoEvalAmt  (숫자)  선물옵션평가금액
      BnsAmt  (숫자)  매매금액
      PchsAmt  (숫자)  매입금액
      FnoTrdUnitAmt  (숫자)  선물옵션거래단위금액
      ThdayBnsAmt  (숫자)  당일매매금액
      BnsAmt0  (숫자)  매매금액0

  공통: rsp_cd  응답코드  ·  rsp_msg  응답메시지
── OUT_END ──────────────────────────────────────────────
"""

import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from dbsec_helper import call_rest, print_response

resp, data = call_rest(
    url="/api/v1/trading/night-futureoption/inquiry/balance",
    body={
        "In": {
            "QryTpCode": "0",  # 조회구분코드 (str) - 0:전체조회 1:개별조회 합산 2:개별조회 그리드
        },
    },
    label="선물옵션 잔고조회 (야간)",
)
print_response(resp, data)
