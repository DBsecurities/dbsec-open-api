"""일자별매매내역 (CSPEQ00400) — standalone 예제.

그룹    : 국내주식주문
엔드포인트: POST /api/v1/trading/kr-stock/inquiry/daliy-trade-report
TPS     : 1
가이드  : https://openapi.dbsec.co.kr/apiservice?group_id=05ac28b8-624f-4115-8aed-cf55f24279dd&api_id=97c0b3a7-e28b-4317-83bd-cbb7ee6bac48

일자별 매매내역을 확인 할 수 있는 API 입니다. ※ 모의투자 계좌로 사용가능한 API입니다. ※ 종목코드 미입력시, 해당일에 매매된 모든 종목이 출력됩니다.

토큰은 examples/dbsec_helper.py 가 자동 발급/캐싱합니다.

실행:
    # examples/ 폴더에서 실행하는 경우:
    python kr_stock_order/kr_stock_inquire_daily_trade.py
    # examples/kr_stock_order/ 폴더에서 실행하는 경우:
    python kr_stock_inquire_daily_trade.py

── 응답 파라미터 (Out) ─ OUT_BEGIN ──────────────────────
  [TR CSPEQ00400]
    Out  (오브젝트)  Out
      SellQty  (숫자)  매도수량
      BuyQty  (숫자)  매수수량
      SellAdjstAmt  (숫자)  매도정산금액
      BuyAdjstAmt  (숫자)  매수정산금액
      BnsDt  (문자)  매매일
      SettDt  (문자)  결제일
      QryDt  (문자)  조회일
    Out1  (배열)  Out1
      IsuNo  (문자)  종목번호
      IsuNm  (문자)  종목명
      IsuSeqno  (숫자)  일련번호
      SettRnkCode  (문자)  결제순위코드 — 10.프리보드 20.코스닥 30.거래소
      OrdTrdPtnCode  (문자)  주문거래유형코드 — 00.위탁 01.신용 02.저축 03.상품 04.선물대용
      TrdTpNm  (문자)  거래구분
      TrdTpNm1  (문자)  거래구분명1
      BnsTpNm  (문자)  매매구분
      BnsTpCode  (문자)  매매구분 — 1:매도 2:매수
      IsuKindCodeNm  (문자)  종목종류코드명
      ExecQty  (숫자)  체결수량
      ExecUprc  (숫자)  체결단가
      CmsnRat  (숫자)  수수료율
      CmsnAmt  (숫자)  수수료
      Trtax  (숫자)  거래세
      Fstax  (숫자)  농특세
      Ictax  (숫자)  소득세
      Ihtax  (숫자)  주민세
      CtrctAmt  (숫자)  약정금액
      AdjstAmt  (숫자)  정산금액
      LoanDt  (문자)  대출일
      CrdtDays  (숫자)  신용일수
      DueDt  (문자)  만기일
      CrdtTpNm  (문자)  신용구분
      BnsMdfyCode  (문자)  매매정정코드 — 00. 정상 01. 익일일부말소 02. 익일전부말소 03. 익일추가 11. 당일일부말소 12. 당일전부말소 13. 당일추가
      MdfyTpNm  (문자)  정정구분명
      FrgrUnqno  (문자)  외국인고유번호
      CrdtBnsAmt  (숫자)  신용매매금액
      AlrdyLevyIntrstAmt  (숫자)  기징수이자금액
      IntrstUtlfee  (숫자)  이자이용료
      OvdDays  (숫자)  연체일수
      IntrstOdpnt  (숫자)  이자연체료
      MnyMgn  (숫자)  현금증거금액
      SubstMgn  (숫자)  대용증거금액
      PldgSubstAmt  (숫자)  담보대용금액
      PldgMnyAmt  (숫자)  담보현금금액
      SavCmsnMgn  (숫자)  저축수수료증거금액
      LoanIntrat  (숫자)  대출이자율
      StslExecQty  (숫자)  공매도체결수량
      ErsQty  (숫자)  말소수량
      TpCodeNm  (문자)  구분자값 한글명

  공통: rsp_cd  응답코드  ·  rsp_msg  응답메시지
── OUT_END ──────────────────────────────────────────────
"""

import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from dbsec_helper import call_rest, print_response

resp, data = call_rest(
    url="/api/v1/trading/kr-stock/inquiry/daliy-trade-report",
    body={
        "In": {
            "IsuNo": "",  # 종목번호 (str) - "": 공백 설정 시 전 종목 조회 주식/ETF: 종목코드6자리 or "A"+"종목코드" ETN: Q + 종목코드 ELW: J + 종목코드
            "BnsDt": "20260527",  # 매매일 (str) - YYYYMMDD 형식의 날짜 입력
        },
    },
    label="일자별매매내역",
)
print_response(resp, data)
