"""주식주문가능수량조회 (CSPBQ00100) — standalone 예제.

그룹    : 국내주식주문
엔드포인트: POST /api/v1/trading/kr-stock/inquiry/able-orderqty
TPS     : 2
가이드  : https://openapi.dbsec.co.kr/apiservice?group_id=05ac28b8-624f-4115-8aed-cf55f24279dd&api_id=4634714a-1ebb-481f-830d-a053524acc97

국내주식 주문가능수량 조회 API 입니다. ※ 모의투자 계좌로 사용가능한 API입니다.

토큰은 examples/dbsec_helper.py 가 자동 발급/캐싱합니다.

실행:
    # examples/ 폴더에서 실행하는 경우:
    python kr_stock_order/kr_stock_inquire_psbl_quantity.py
    # examples/kr_stock_order/ 폴더에서 실행하는 경우:
    python kr_stock_inquire_psbl_quantity.py

── 응답 파라미터 (Out) ─ OUT_BEGIN ──────────────────────
  [TR CSPBQ00100]
    Out  (오브젝트)  Out
      IsuNm  (문자)  종목명
      BnsTpNm  (문자)  매매구분 — 1:매도 2:매수
      Dps  (숫자)  예수금
      SubstAmt  (숫자)  대용금액
      MnyMgn  (숫자)  현금증거금액
      SubstMgn  (숫자)  대용증거금액
      MnyOrdAbleAmt  (숫자)  현금주문가능금액
      SubstOrdAbleAmt  (숫자)  대용주문가능금액
      CrdtPldgRuseAmt  (숫자)  신용담보재사용금액
      AbleAmt  (숫자)  가능금액
      MgnRat100pctOrdAbleAmt  (숫자)  증거금률100퍼센트주문가능금액
      MgnRat100OrdAbleQty  (숫자)  증거금률100퍼센트주문가능수량
      LoanPldgRat  (숫자)  대출담보율
      PldgMaintRat  (숫자)  담보유지비율
      OrdAbleQty  (숫자)  주문가능수량
      UnercBuyOrdAmt  (숫자)  미체결매수주문금액
      BalQty  (숫자)  잔고수량
      HtsOrdAbleAmt  (숫자)  HTS주문가능금액
      D1Dps  (숫자)  D+1예수금
      D2Dps  (숫자)  D+2예수금
      PrdayRuseOrdAbleQty  (숫자)  전일재사용주문가능수량
      CrdayRuseOrdAbleQty  (숫자)  금일재사용주문가능수량
      CrdtOrdAbleAmt  (숫자)  신용주문가능금액

  공통: rsp_cd  응답코드  ·  rsp_msg  응답메시지
── OUT_END ──────────────────────────────────────────────
"""

import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from dbsec_helper import call_rest, print_response

resp, data = call_rest(
    url="/api/v1/trading/kr-stock/inquiry/able-orderqty",
    body={
        "In": {
            "BnsTpCode": "2",  # 매매구분 (str) - 1:매도 2:매수
            "IsuNo": "A016610",  # 종목번호 (str) - 주식/ETF: 종목코드6자리 or "A"+"종목코드" ETN: Q + 종목코드 ELW: J + 종목코드
            "OrdPrc": 20000,  # 주문가격 (int) - 매매구분 "매도" 선택시 0 입력 "매수" 선택시 입력된 주문가격으로 주문가능수량 산정 (가격 0 으로 설정시 금일 종가가 존재하는경우 금일종가 기준, 없을경우 상한가 기준으로 산정)
        },
    },
    label="주식주문가능수량조회",
)
print_response(resp, data)
