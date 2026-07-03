"""당일매매손익 조회 (CSPAQ01800) — standalone 예제.

그룹    : 국내주식주문
엔드포인트: POST /api/v1/trading/kr-stock/inquiry/daily-ernrate
TPS     : 2
가이드  : https://openapi.dbsec.co.kr/apiservice?group_id=05ac28b8-624f-4115-8aed-cf55f24279dd&api_id=d159f8ec-a52d-40ec-bf05-99b6f8b68744

당일 실현손익을 조회 할 수 있는 API 입니다. 당일 실현손익을 실시간으로 조회 가능합니다. 기간별, 종목별 실현손익 확인이 필요하신 경우 "주식 실현손익조회" API 사용 부탁드립니다.

토큰은 examples/dbsec_helper.py 가 자동 발급/캐싱합니다.

실행:
    # examples/ 폴더에서 실행하는 경우:
    python kr_stock_order/kr_stock_inquire_daily_pnl.py
    # examples/kr_stock_order/ 폴더에서 실행하는 경우:
    python kr_stock_inquire_daily_pnl.py

── 응답 파라미터 (Out) ─ OUT_BEGIN ──────────────────────
  [TR CSPAQ01800]
    Out  (배열)  Out
      AcntNm  (문자)  계좌명
      CrdaySellExecAmt  (숫자)  금일매도체결금액
      SellExecQty  (숫자)  매도체결수량
      CrdayBuyExecAmt  (숫자)  금일매수체결금액
      BuyExecQty  (숫자)  매수체결수량
      AdjstAmt  (숫자)  정산금액
      DtTotPnlAmt  (숫자)  일총손익금액
      MnyOrdAbleAmt  (숫자)  현금주문가능금액
      MnyoutAbleAmt  (숫자)  출금가능금액
      Evrprc  (숫자)  제비용
      BalEvalAmt  (숫자)  잔고평가금액
      InvstPlAmt  (숫자)  투자손익금액
      InvstOrgAmt  (숫자)  투자원금
      PnlRat  (숫자)  손익율
    Out1  (배열)  Out1
      IsuNo  (문자)  종목번호
      IsuNm  (문자)  종목명
      FlctQty  (숫자)  변동수량
      CrdaySellExecQty  (숫자)  금일매도체결수량
      SellPrc  (숫자)  매도가
      CrdayBuyExecQty  (숫자)  금일매수체결수량
      BuyPrc  (숫자)  매수가
      NowPrc  (숫자)  현재가
      BalQty  (숫자)  잔고수량
      BalEvalPnlAmt  (숫자)  잔고평가손익금액
      SellPnlAmt  (숫자)  매도손익금액
      PnlRat  (숫자)  손익율
      SecBalPtnCode  (문자)  유가증권잔고유형코드
      SecBalPtnNm  (문자)  유가증권잔고유형명
      AvrUprc  (숫자)  평균단가
      CmsnAmt  (숫자)  수수료 — 수수료 단독
      BuyCmsn  (숫자)  매수수수료
      EvrTax  (숫자)  제세금
      Ernrat  (숫자)  수익률
      Cmsn0  (숫자)  수수료0 — 수수료+제세금
      LoanDt  (문자)  대출일자

  공통: rsp_cd  응답코드  ·  rsp_msg  응답메시지
── OUT_END ──────────────────────────────────────────────
"""

import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from dbsec_helper import call_rest, print_response

resp, data = call_rest(
    url="/api/v1/trading/kr-stock/inquiry/daily-ernrate",
    body={
        "In": {
            "QryTp": "2",  # 조회구분 (str) - "2" 고정입력
        },
    },
    label="당일매매손익 조회",
)
print_response(resp, data)
