"""채권잔고평가조회 (CSPAQ07900) — standalone 예제.

그룹    : 장내채권주문
엔드포인트: POST /api/v1/trading/krx-bond/inquiry/balance-evalstatus
TPS     : 2
가이드  : https://openapi.dbsec.co.kr/apiservice?group_id=4a7257ed-b94a-462e-987d-132f064ed0d3&api_id=a0b85223-af82-4b88-a31e-9762c003eaac

채권 잔고평가조회 API입니다.

토큰은 examples/dbsec_helper.py 가 자동 발급/캐싱합니다.

실행:
    # examples/ 폴더에서 실행하는 경우:
    python bond_order/bond_inquire_balance_eval.py
    # examples/bond_order/ 폴더에서 실행하는 경우:
    python bond_inquire_balance_eval.py

── 응답 파라미터 (Out) ─ OUT_BEGIN ──────────────────────
  [TR CSPAQ07900]
    Out  (배열)  Out
      IsuNo  (문자)  종목번호
      IsuNm  (문자)  종목명
      RegMktCode  (문자)  등록시장코드 — 00:비상장 10:유가증권 20:코스닥 30:프리보드
      BalQty  (숫자)  잔고수량
      EvalAmt  (숫자)  평가금액
      BnsBaseBalQty  (숫자)  매매기준잔고수량
      SecBalPtnCode  (문자)  유가증권잔고유형코드 — 00:보통 01:채권 02:코스피선물대용 03:코스닥선물대용 04:주식옵션선물대용 05:CD/CP 10:채권
      SecBalPtnNm  (문자)  유가증권잔고유형명
      CrdayBuyExecQty  (숫자)  금일매수체결수량
      CrdaySellExecQty  (숫자)  금일매도체결수량
      SellPrc  (숫자)  매도가
      BuyPrc  (숫자)  매수가
      SellPnlAmt  (숫자)  매도손익금액
      PnlRat  (숫자)  손익률
      NowPrc  (숫자)  현재가
      CrdtAmt  (숫자)  신용금액
      DueDt  (문자)  만기일
      EvalPnl  (숫자)  평가손익
      PrdaySellExecPrc  (숫자)  전일매도체결가
      PrdaySellQty  (숫자)  전일매도수량
      PrdayBuyExecPrc  (숫자)  전일매수체결가
      PrdayBuyQty  (숫자)  전일매수수량
      LoanDt  (문자)  대출일
      AvrUprc  (숫자)  평균단가
      SellAbleQty  (숫자)  매도가능수량
      SellOrdQty  (숫자)  매도주문수량
      CrdayBuyExecAmt  (숫자)  금일매수체결금액
      CrdaySellExecAmt  (숫자)  금일매도체결금액
      PrdayBuyExecAmt  (숫자)  전일매수체결금액
      PrdaySellExecAmt  (숫자)  전일매도체결금액
      PchsAmt  (숫자)  매입금액

  공통: rsp_cd  응답코드  ·  rsp_msg  응답메시지
── OUT_END ──────────────────────────────────────────────
"""

import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from dbsec_helper import call_rest, print_response

resp, data = call_rest(
    url="/api/v1/trading/krx-bond/inquiry/balance-evalstatus",
    body={
        "In": {
            "D2balBaseQryTp": "0",  # D+2잔고기준조회구분 (str) - 0:전부조회 1:D+2잔고 0이상만 조회
            "OtptPtnTpCode": "0",  # 출력유형구분 (str) - 0:상장폐지종목 출력 1:상장페지종목 제외
        },
    },
    label="채권잔고평가조회",
)
print_response(resp, data)
