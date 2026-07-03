"""선물옵션 잔고 조회 (CFOAQ02500) — standalone 예제.

그룹    : 국내선물옵션주문
엔드포인트: POST /api/v1/trading/kr-futureoption/inquiry/balance
TPS     : 2
가이드  : https://openapi.dbsec.co.kr/apiservice?group_id=44c4a04f-f55e-4c1c-b4e2-b48ec4869aee&api_id=0f2f94c7-27f3-4f42-8a8b-862224618d1b

선물옵션 잔고 조회 API 입니다. ※ 모의투자 계좌로 사용가능한 API입니다. ※ 잔고가 전부 표시되지 않는경우 연속키 조회를 통해 확인하실 수 있습니다. ※ Output 필드 중 "총매매금액, 총평가금액, 총평가손익금액, 총수익률, 당일 실현손익금액" 필드는 모의투자 계좌에서만 값이 제공 됩니다.

토큰은 examples/dbsec_helper.py 가 자동 발급/캐싱합니다.

실행:
    # examples/ 폴더에서 실행하는 경우:
    python kr_futopt_order/kr_futopt_inquire_balance.py
    # examples/kr_futopt_order/ 폴더에서 실행하는 경우:
    python kr_futopt_inquire_balance.py

── 응답 파라미터 (Out) ─ OUT_BEGIN ──────────────────────
  [TR CFOAQ02500]
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
    url="/api/v1/trading/kr-futureoption/inquiry/balance",
    body={
        "In": {
        },
    },
    label="선물옵션 잔고 조회",
)
print_response(resp, data)
