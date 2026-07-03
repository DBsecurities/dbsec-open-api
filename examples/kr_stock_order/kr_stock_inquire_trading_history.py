"""계좌거래내역 조회 (CDPCQ04700) — standalone 예제.

그룹    : 국내주식주문
엔드포인트: POST /api/v1/trading/kr-stock/inquiry/trading-history
TPS     : 2
가이드  : https://openapi.dbsec.co.kr/apiservice?group_id=05ac28b8-624f-4115-8aed-cf55f24279dd&api_id=1a4fcb20-874c-40a7-bd7a-1b099289de0f

국내주식 거래내역을 확인하는 API입니다. ※ 모의투자 계좌로 사용가능한 API입니다.

토큰은 examples/dbsec_helper.py 가 자동 발급/캐싱합니다.

실행:
    # examples/ 폴더에서 실행하는 경우:
    python kr_stock_order/kr_stock_inquire_trading_history.py
    # examples/kr_stock_order/ 폴더에서 실행하는 경우:
    python kr_stock_inquire_trading_history.py

── 응답 파라미터 (Out) ─ OUT_BEGIN ──────────────────────
  [TR CDPCQ04700]
    Out  (오브젝트)  Out
      AcntNm  (문자)  계좌명
    Out1  (오브젝트)  Out1
      AcntNo  (문자)  계좌번호
      TrdDt  (문자)  거래일자
      TrdNo  (숫자)  거래번호
      TpCodeNm  (문자)  구분코드명
      SmryNo  (문자)  적요번호
      SmryNm  (문자)  적요명
      CancTpNm  (문자)  취소구분 — 0:정상 1:취소
      TrdQty  (숫자)  거래수량
      Trtax  (숫자)  거래세
      AdjstAmt  (숫자)  정산금액
      OvdSum  (숫자)  연체합
      DpsBfbalAmt  (숫자)  예수금전잔금액
      SellPldgRfundAmt  (숫자)  매도담보상환금
      DpspdgLoanBfbalAmt  (숫자)  예탁담보대출전잔금액
      OrgTrdNo  (숫자)  원거래번호
      IsuNm  (문자)  종목명
      TrdUprc  (숫자)  거래단가
      CmsnAmt  (숫자)  수수료
      RfundDiffAmt  (숫자)  상환차이금액
      RepayAmtSum  (숫자)  변제금합계
      SecCrbalQty  (숫자)  유가증권금잔수량
      CslLoanRfundIntrstAmt  (숫자)  매도대금담보대출상환이자금액
      DpspdgLoanCrbalAmt  (숫자)  예탁담보대출금잔금액
      TrxTime  (문자)  처리시각
      Inouno  (숫자)  출납번호
      IsuNo  (문자)  종목번호
      TrdAmt  (숫자)  거래금액
      TaxSumAmt  (숫자)  세금합계금액
      IntrstUtlfee  (숫자)  이자이용료
      MnyDvdAmt  (숫자)  배당금액
      RcvblOcrAmt  (숫자)  미수발생금액
      DpspdgLoanAmt  (숫자)  예탁담보대출금액
      DpspdgLoanRfundAmt  (숫자)  예탁담보대출상환금액
      BasePrc  (숫자)  기준가
      DpsCrbalAmt  (숫자)  예수금금잔금액
      BoaAmt  (숫자)  과표
      MnyoutAbleAmt  (숫자)  출금가능금액
      BcrLoanOcrAmt  (숫자)  수익증권담보대출발생금
      BcrLoanBfbalAmt  (숫자)  수익증권담보대출전잔금
      BnsBasePrc  (숫자)  매매기준가
      TaxchrBasePrc  (숫자)  과세기준가
      거래좌수  (숫자)  TrdUnit
      BalUnit  (숫자)  잔고좌수
      EvrTax  (숫자)  제세금
      EvalAmt  (숫자)  평가금액
      BcrLoanRfundAmt  (숫자)  수익증권담보대출상환금
      BcrLoanCrbalAmt  (숫자)  수익증권담보대출금잔금
      AddMgnOcrTotamt  (숫자)  추가증거금발생총액
      AddMnyMgnOcrAmt  (숫자)  추가현금증거금발생금액
      AddMgnDfryTotamt  (숫자)  추가증거금납부총액
      AddMnyMgnDfryAmt  (숫자)  추가현금증거금납부금액
      BnsplAmt  (숫자)  매매손익금액
      Ictax  (숫자)  소득세
      Ihtax  (숫자)  주민세
      LoanDt  (문자)  대출일
      CrcyCode  (문자)  통화코드
      FcurrAmt  (숫자)  외화금액
      FcurrTrdAmt  (숫자)  외화거래금액
      FcurrDps  (숫자)  외화예수금
      OppAcntNm  (문자)  상대계좌명
      OppAcntNo  (문자)  상대계좌번호
      LoanRfundAmt  (숫자)  대출상환금액
      LoanIntrstAmt  (숫자)  대출이자금액
      AskpsnNm  (문자)  의뢰인명
      BkeepIttNm  (문자)  대체기관명
    Out2  (오브젝트)  Out2
      PnlSumAmt  (문자)  손익합계금액
      CtrctAsm  (문자)  약정누계
      CmsnAmtSumAmt  (문자)  수수료합계금액
    Out3  (오브젝트)  Out3
      MnyinAmt  (문자)  입금금액
      SecinAmt  (문자)  입고금액
      MnyoutAmt  (문자)  출금금액
      SecoutAmt  (문자)  출고금액
      DiffAmt  (문자)  차이금액
      DiffAmt0  (문자)  차이금액0

  공통: rsp_cd  응답코드  ·  rsp_msg  응답메시지
── OUT_END ──────────────────────────────────────────────
"""

import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from dbsec_helper import call_rest, print_response

resp, data = call_rest(
    url="/api/v1/trading/kr-stock/inquiry/trading-history",
    body={
        "In": {
            "QryTp": "0",  # 조회구분 (str) - 0:전체 1:입출금 2:입출고 3:매매 4.이체/대체
            "QrySrtDt": "20260101",  # 조회시작일 (str)
            "QryEndDt": "20260526",  # 조회종료일 (str) - 조회기간 최대 12개월(선물옵션계좌의 경우 6개월)
            "SrtNo": 0,  # 시작번호 (int) - 기본값: 0 조회구분 "0.전체"인 경우 CMA매매내역 생략시 1 입력
            "IsuNo": "",  # 종목번호 (str) - "" : 공백 입력시 전체 종목 조회 "A+종목번호" 입력시 특정 종목 내역 조회 ex. "A016610" 설정시 DB증권 종목 내역만 확인
        },
    },
    label="계좌거래내역 조회",
)
print_response(resp, data)
