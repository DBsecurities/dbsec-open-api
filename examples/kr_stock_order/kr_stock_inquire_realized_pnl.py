"""주식 실현손익조회 (CSPAQ07800) — standalone 예제.

그룹    : 국내주식주문
엔드포인트: POST /api/v1/trading/kr-stock/inquiry/stock-ernrate
TPS     : 1
가이드  : https://openapi.dbsec.co.kr/apiservice?group_id=05ac28b8-624f-4115-8aed-cf55f24279dd&api_id=c2eb049b-d54b-4d60-9645-129552f15edf

종목&기간별 실현손익을 조회 할 수 있는 API 입니다. 당일 실현손익의 경우, 장 마감 후 확인 가능합니다. 실시간 당일 실현손익 확인이 필요하신 경우 "당일매매손익 조회" API 사용 부탁드립니다.

토큰은 examples/dbsec_helper.py 가 자동 발급/캐싱합니다.

실행:
    # examples/ 폴더에서 실행하는 경우:
    python kr_stock_order/kr_stock_inquire_realized_pnl.py
    # examples/kr_stock_order/ 폴더에서 실행하는 경우:
    python kr_stock_inquire_realized_pnl.py

── 응답 파라미터 (Out) ─ OUT_BEGIN ──────────────────────
  [TR CSPAQ07800]
    Out  (오브젝트)  Out
      BuyAmt  (숫자)  매수금액
      SellAmt  (숫자)  매도금액
      RlzPnlAmt  (숫자)  실현손익금액
      BuyCmsn  (숫자)  매수수수료
      SellCmsn  (숫자)  매도수수료
      TaxAmt  (숫자)  세금금액
      PnlRat  (숫자)  손익율
      AdjstAmt  (숫자)  정산금액
    Out1  (배열)  Out1
      BnsDt  (문자)  매매일자
      CodeNm  (문자)  코드명
      IsuNo  (문자)  종목번호
      IsuNm  (문자)  종목명
      SellPnlAmt  (숫자)  매도손익금액
      PnlRat0  (숫자)  손익율0 — 실현수익률
      CrdayBuyExecQty  (숫자)  금일매수체결수량
      BuyPrc  (숫자)  매수가
      BuyCmsn  (숫자)  매수수수료
      CrdaySellExecQty  (숫자)  금일매도체결수량
      SellPrc  (숫자)  매도가
      CmsnAmt  (숫자)  수수료
      Cmsn  (숫자)  수수료
      EvrTax  (숫자)  제세금
      NowPrc  (숫자)  현재가
      BalQty  (숫자)  잔고수량
      AvrUprc  (숫자)  평균단가
      BalEvalPnlAmt  (숫자)  잔고평가손익금액
      PnlRat  (숫자)  손익율 — 잔고수익률
      LoanDt  (문자)  대출일자

  공통: rsp_cd  응답코드  ·  rsp_msg  응답메시지
── OUT_END ──────────────────────────────────────────────
"""

import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from dbsec_helper import call_rest, print_response

resp, data = call_rest(
    url="/api/v1/trading/kr-stock/inquiry/stock-ernrate",
    body={
        "In": {
            "SrtDt": "20260101",  # 시작일자 (str) - YYYYMMDD 형식의 날짜 입력
            "EndDt": "20260526",  # 종료일자 (str) - YYYYMMDD 형식의 날짜 입력
            "IsuNo": "",  # 종목번호 (str) - 주식/ETF: 종목코드6자리 or "A"+"종목코드" "": 전체 종목 표시 (공백으로 설정 시 기간 내 거래된 모든 특정 종목이 아닌 모든 종목을 표시합니다) ETN: Q + 종목코드 ELW: J + 종목코드
            "CmsnAppTpCode": "1",  # 수수료적용구분코드 (str) - 0: 제비용 미포함, 1: 제비용 포함
        },
    },
    label="주식 실현손익조회",
)
print_response(resp, data)
