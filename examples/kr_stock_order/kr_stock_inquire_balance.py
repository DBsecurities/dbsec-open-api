"""주식잔고조회 (CSPAQ03420) — standalone 예제.

그룹    : 국내주식주문
엔드포인트: POST /api/v1/trading/kr-stock/inquiry/balance
TPS     : 2
가이드  : https://openapi.dbsec.co.kr/apiservice?group_id=05ac28b8-624f-4115-8aed-cf55f24279dd&api_id=07a86b9a-0548-47cd-baa9-24395d4ea4bb

주식 잔고조회 API 입니다. 보유중인 주식 잔고에 대한 정보를 제공합니다. ※ 모의투자 계좌로 사용가능한 API입니다. ※ 잔고가 전부 표시되지 않는경우 연속키 조회를 통해 확인하실 수 있습니다.

토큰은 examples/dbsec_helper.py 가 자동 발급/캐싱합니다.

실행:
    # examples/ 폴더에서 실행하는 경우:
    python kr_stock_order/kr_stock_inquire_balance.py
    # examples/kr_stock_order/ 폴더에서 실행하는 경우:
    python kr_stock_inquire_balance.py

── 응답 파라미터 (Out) ─ OUT_BEGIN ──────────────────────
  [TR CSPAQ03420]
    Out  (오브젝트)  Out
      TotBuyAmt  (숫자)  총매수금액 — 체결기준 매수금액
      TotEvalAmt  (숫자)  총평가금액 — 체결기준 총평가금액
      TotEvalPnlAmt  (숫자)  총평가손익금액
      TotErnrat  (숫자)  총수익률
      ThdaySellAmt  (숫자)  당일매도금액
      ThdayBuyAmt  (숫자)  당일매수금액
      ThdayRlzPnlAmt  (숫자)  당일실현손익금액
      CrdtBnsAmt  (숫자)  신용매매금액
      DpsastAmt  (숫자)  예탁자산금액
      Dps2  (숫자)  예수금2 — D+2 예수금
    Out1  (배열)  Out1
      IsuNo  (문자)  종목번호
      IsuNm  (문자)  종목명
      BalQty  (숫자)  잔고수량 — 결제기준 잔고
      BalQty0  (숫자)  잔고수량0 — 체결기준 잔고 (T+2)
      AbleQty  (숫자)  가능수량
      ExecPrc  (숫자)  체결가
      EvalAmt  (숫자)  평가금액
      EvalPnlAmt  (숫자)  평가손익금액
      Ernrat  (숫자)  수익률
      MnyAmt  (숫자)  현금금액
      CrdtAmt  (숫자)  신용금액
      PchsAmt  (숫자)  매입금액
      LoanDt  (문자)  대출일자
      DueDt  (문자)  만기일자
      EvrTax  (숫자)  제세금
      BnsCmsn  (숫자)  매매수수료
      SellCmsn  (숫자)  매도수수료
      ThdayBuyQty  (숫자)  당일매수수량
      ThdaySellQty  (숫자)  당일매도수량
      BuyRat  (숫자)  매수비율
      EvalRat  (숫자)  평가비율
      NowPrc  (숫자)  현재가
      ThdaySellAmt  (숫자)  당일매도금액
      ThdayBuyAmt  (숫자)  당일매수금액
      ThdayRlzPnlAmt  (숫자)  당일실현손익금액

  공통: rsp_cd  응답코드  ·  rsp_msg  응답메시지
── OUT_END ──────────────────────────────────────────────
"""

import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from dbsec_helper import call_rest, print_response

resp, data = call_rest(
    url="/api/v1/trading/kr-stock/inquiry/balance",
    body={
        "In": {
            "QryTpCode0": "0",  # 조회구분코드0 (str) - 0:전체 1:비상장제외 2:비상장,코넥스,kotc 제외
        },
    },
    label="주식잔고조회",
)
print_response(resp, data)
