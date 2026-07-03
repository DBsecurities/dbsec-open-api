"""계좌예수금조회 (CDPCQ00100) — standalone 예제.

그룹    : 국내주식주문
엔드포인트: POST /api/v1/trading/kr-stock/inquiry/acnt-deposit
TPS     : 1
가이드  : https://openapi.dbsec.co.kr/apiservice?group_id=05ac28b8-624f-4115-8aed-cf55f24279dd&api_id=3876bc95-5981-4009-91ca-2408cd56cf6d

계좌의 예수금에대한 정보를 제공하는 API 입니다. ※ 모의투자 계좌로 사용가능한 API입니다. ※ CMA 계좌일 경우 전일, 당일 매매 존재 시 D+1, D+2 예수금은 (-) 금액으로 표시될 수 있습니다.

토큰은 examples/dbsec_helper.py 가 자동 발급/캐싱합니다.

실행:
    # examples/ 폴더에서 실행하는 경우:
    python kr_stock_order/kr_stock_inquire_deposit.py
    # examples/kr_stock_order/ 폴더에서 실행하는 경우:
    python kr_stock_inquire_deposit.py

── 응답 파라미터 (Out) ─ OUT_BEGIN ──────────────────────
  [TR CDPCQ00100]
    Out1  (오브젝트)  Out1
      DpsBalAmt  (숫자)  예수금잔고금액
      MgnMny  (숫자)  증거금현금
      PldgCurAmt  (숫자)  담보현금액
      AddCrdtPldgMny  (숫자)  추가신용담보현금
      RcvblEnsrAmt  (숫자)  미수확보금액
      SubstAmt  (숫자)  대용금액
      SubstMgn  (숫자)  대용증거금액
      PldgSubstAmt0  (숫자)  담보대용금액0
      AddCrdtPldgSubst  (숫자)  추가신용담보대용
      RgtsbAmt  (숫자)  권리대용금액
      ChckAmt  (숫자)  수표금액
      UnSettEtcChckAmt  (숫자)  미결제기타수표금액
      CrdtPldgRuseAmt  (숫자)  신용담보재사용금액
      Imreq  (숫자)  신용설정보증금
      DpslRestrcAmt  (숫자)  처분제한금액
      WthdwAbleAmt  (숫자)  인출가능금액
      SfaccMloanAmt  (숫자)  자기융자금액
      MktcplMloanAmt  (숫자)  유통융자금액
      MloanTotamt  (숫자)  융자총액
      SfaccSloanAmt  (숫자)  자기대주금액
      MktcplSloanAmt  (숫자)  유통대주금액
      SloanTotamt  (숫자)  대주총액
      MnyrclAmt  (숫자)  현금미수금액
      IntrstDlinqAmt  (숫자)  이자미납금액
      Etclnd  (숫자)  기타대여금
      OldUnRfundAmt  (숫자)  (구)미상환금액
      DpspdgLoanEvalAmt  (숫자)  예탁담보대출평가금액
      DpspdgLoanAbleLmt  (숫자)  예탁담보대출가능한도
      DpspdgLoanBal  (숫자)  예탁담보대출잔고
      DpspdgLoanAbleAmt  (숫자)  예탁담보대출가능금액
      DpspdgLoanIntdltAmt  (숫자)  예탁담보대출이자미납금
      PmLoanEvalAmt  (숫자)  매입자금대출평가금액
      PmLoanAbleLmt  (숫자)  매입자금대출가능한도
      PmLoanBal  (숫자)  매입자금대출잔고
      PmLoanAbleAmt  (숫자)  매입자금대출가능금액
      PmLoanIntdltAmt  (숫자)  매입자금대출이자미납금
      BuyAdjstAmtD1  (숫자)  매수정산금(D+1)
      SellAdjstAmtD1  (숫자)  매도정산금(D+1)
      RepayRqrdAmtD1  (숫자)  변제소요금(D+1)
      PrsmptDpsD1  (숫자)  추정예수금(D+1)
      PrsmptMnyoutAbleAmtD1  (숫자)  추정인출가능금(D+1)
      BuyAdjstAmtD2  (숫자)  매수정산금(D+2)
      SellAdjstAmtD2  (숫자)  매도정산금(D+2)
      RepayRqrdAmtD2  (숫자)  변제소요금(D+2)
      PrsmptDpsD2  (숫자)  추정예수금(D+2)
      PrsmptMnyoutAbleAmtD2  (숫자)  추정인출가능금(D+2)
      MnyRuseUseAmt  (숫자)  현금재사용사용금액
      MnyRuseUseAmt1  (숫자)  현금재사용사용금액1
      SubstRuseUseAmt  (숫자)  대용재사용사용금액
      SubstRuseUseAmt1  (숫자)  대용재사용사용금액1

  공통: rsp_cd  응답코드  ·  rsp_msg  응답메시지
── OUT_END ──────────────────────────────────────────────
"""

import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from dbsec_helper import call_rest, print_response

resp, data = call_rest(
    url="/api/v1/trading/kr-stock/inquiry/acnt-deposit",
    body={
        "In": {
        },
    },
    label="계좌예수금조회",
)
print_response(resp, data)
