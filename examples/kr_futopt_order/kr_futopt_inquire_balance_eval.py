"""선물옵션 잔고_평가현황조회 (CFOAQ50100) — standalone 예제.

그룹    : 국내선물옵션주문
엔드포인트: POST /api/v1/trading/kr-futureoption/inquiry/balance-evalstatus
TPS     : 2
가이드  : https://openapi.dbsec.co.kr/apiservice?group_id=44c4a04f-f55e-4c1c-b4e2-b48ec4869aee&api_id=af116c58-19a5-4bbe-8abf-5632829f327b

선물옵션 잔고/평가현황 조회 API 입니다. ※ 모의투자 계좌로 사용가능한 API입니다. ※ 잔고가 전부 표시되지 않는경우 연속키 조회를 통해 확인하실 수 있습니다.

토큰은 examples/dbsec_helper.py 가 자동 발급/캐싱합니다.

실행:
    # examples/ 폴더에서 실행하는 경우:
    python kr_futopt_order/kr_futopt_inquire_balance_eval.py
    # examples/kr_futopt_order/ 폴더에서 실행하는 경우:
    python kr_futopt_inquire_balance_eval.py

── 응답 파라미터 (Out) ─ OUT_BEGIN ──────────────────────
  [TR CFOAQ50100]
    Out  (오브젝트)  Out
      EvalDpsamtTotamt  (숫자)  평가예탁금총액
      MnyEvalDpstgAmt  (숫자)  현금평가예탁금액
      DpsamtTotamt  (숫자)  예탁금총액
      DpstgMny  (숫자)  예탁현금
      DpstgSubst  (숫자)  예탁대용
      PsnOutAbleTotAmt  (숫자)  인출가능총금액
      PsnOutAbleCurAmt  (숫자)  인출가능현금액
      PsnOutAbleSubstAmt  (숫자)  인출가능대용금액
      OrdAbleTotAmt  (숫자)  주문가능총금액
      MnyOrdAbleAmt  (숫자)  현금주문가능금액
      CsgnMgnTotamt  (숫자)  위탁증거금총액
      MnyCsgnMgn  (숫자)  현금위탁증거금액
      MtmgnTotamt  (숫자)  유지증거금총액
      MnyMaintMgn  (숫자)  현금유지증거금액
      EvalAmtSum  (숫자)  평가금액합계
      RcvblOdpnt  (숫자)  미수연체료
      AddMgnTotamt  (숫자)  추가증거금총액
      EvalPnlSum  (숫자)  평가손익합계
      RcvblAmt  (숫자)  미수금액
      MnyAddMgn  (숫자)  현금추가증거금액
    Out1  (배열)  Out1
      FnoIsuNo  (문자)  선물옵션종목번호
      IsuNm  (문자)  종목명
      BnsTpCode  (문자)  매매구분 — 1:매도 2:매수
      BnsTpNm  (문자)  매매구분 — '매도' '매수'
      UnsttQty  (숫자)  미결제수량
      FnoAvrPrc  (숫자)  평균가
      NowPrc  (숫자)  현재가
      CmpPrc  (숫자)  대비가
      EvalPnl  (숫자)  평가손익
      PnlRat  (숫자)  손익률
      FnoTrdUnitAmt  (숫자)  선물옵션거래단위금액
      EvalAmt  (숫자)  평가금액
      EvalRat  (숫자)  평가비율
      BnsplAmt  (숫자)  매매손익금액

  공통: rsp_cd  응답코드  ·  rsp_msg  응답메시지
── OUT_END ──────────────────────────────────────────────
"""

import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from dbsec_helper import call_rest, print_response

resp, data = call_rest(
    url="/api/v1/trading/kr-futureoption/inquiry/balance-evalstatus",
    body={
        "In": {
            "OrdDt": "00000000",  # 주문일 (str) - 일자를 '00000000'로 전송시 당일기준으로 산출함
            "BalEvalTp": "0",  # 잔고평가구분 (str) - 0:기본설정 1:이동평균법 2:선입선출법
            "FutsPrcEvalTp": "2",  # 선물가격평가구분 (str) - 1:당초가 2:전일종가
        },
    },
    label="선물옵션 잔고_평가현황조회",
)
print_response(resp, data)
