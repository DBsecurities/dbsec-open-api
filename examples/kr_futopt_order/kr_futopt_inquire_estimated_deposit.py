"""선물옵션 가정산예탁금 상세 (CFOEQ11100) — standalone 예제.

그룹    : 국내선물옵션주문
엔드포인트: POST /api/v1/trading/kr-futureoption/inquiry/deposit-detail
TPS     : 1
가이드  : https://openapi.dbsec.co.kr/apiservice?group_id=44c4a04f-f55e-4c1c-b4e2-b48ec4869aee&api_id=58f71b7f-064c-4e44-8c8e-9a417bf366f2

선물옵션 계좌의 가정산예탁금 정보조회 API입니다. ※ 모의투자 계좌로 사용가능한 API입니다.

토큰은 examples/dbsec_helper.py 가 자동 발급/캐싱합니다.

실행:
    # examples/ 폴더에서 실행하는 경우:
    python kr_futopt_order/kr_futopt_inquire_estimated_deposit.py
    # examples/kr_futopt_order/ 폴더에서 실행하는 경우:
    python kr_futopt_inquire_estimated_deposit.py

── 응답 파라미터 (Out) ─ OUT_BEGIN ──────────────────────
  [TR CFOEQ11100]
    Out  (오브젝트)  Out
      AcntNm  (문자)  계좌명
      OpnmkDpsamtTotamt  (숫자)  개장시예탁금총액 — 개장시예수금현황.개장시예탁총액
      OpnmkDps  (숫자)  개장시예수금 — 개장시예수금현황.개장시예탁현금
      OpnmkMnyrclAmt  (숫자)  개장시현금미수금
      OpnmkSubstAmt  (숫자)  개장시대용금액 — 개장시예수금현황.개장시예탁대용
      TotAmt  (숫자)  총금액 — 예수금현황.예탁총액
      Dps  (숫자)  예수금 — 예수금현황.예탁현금
      MnyrclAmt  (숫자)  현금미수금액
      SubstDsgnAmt  (숫자)  대용지정금액 — 예수금현황.예탁대용
      CsgnMgn  (숫자)  위탁증거금액
      MnyCsgnMgn  (숫자)  현금위탁증거금액
      MaintMgn  (숫자)  유지증거금액
      MnyMaintMgn  (숫자)  현금유지증거금액
      OutAbleAmt  (숫자)  출금가능총액 — 예수금현황.인출가능총액
      MnyoutAbleAmt  (숫자)  출금가능금액 — 예수금현황.인출가능현금
      SubstOutAbleAmt  (숫자)  출금가능대용 — 예수금현황.인출가능대용
      OrdAbleAmt  (숫자)  주문가능금액 — 예수금현황.주문가능총액
      MnyOrdAbleAmt  (숫자)  현금주문가능금액 — 예수금현황.주문가능현금
      AddMgnOcrTpCode  (문자)  추가증거금구분 — 3.총액+현금발생 2.현금 1.총액 0.해소
      AddMgn  (숫자)  추가증거금액
      MnyAddMgn  (숫자)  현금추가증거금액
      NtdayTotAmt  (숫자)  익일예탁총액
      NtdayDps  (숫자)  익일예탁현금
      NtdayMnyrclAmt  (숫자)  익일미수금
      NtdaySubstAmt  (숫자)  익일예탁대용
      NtdayCsgnMgn  (숫자)  익일위탁증거금
      NtdayMnyCsgnMgn  (숫자)  익일위탁증거금현금
      NtdayMaintMgn  (숫자)  익일유지증거금
      NtdayMnyMaintMgn  (숫자)  익일유지증거금현금
      NtdayOutAbleAmt  (숫자)  익일인출가능금액
      NtdayMnyoutAbleAmt  (숫자)  익일인출가능금액
      NtdaySubstOutAbleAmt  (숫자)  익일인출가능대용
      NtdayOrdAbleAmt  (숫자)  익일주문가능금액
      NtdayMnyOrdAbleAmt  (숫자)  익일주문가능현금
      NtdayAddMgnTp  (문자)  익일추가증거금구분
      NtdayAddMgn  (숫자)  익일추가증거금
      NtdayMnyAddMgn  (숫자)  익일추가증거금현금
      NtdaySettAmt  (숫자)  익일결제금액
      EvalDpsamtTotamt  (숫자)  평가예탁금총액 — 익일예수금현황.추정예탁자산
      MnyEvalDpstgAmt  (숫자)  현금평가예탁금액 — 익일예수금현황.추정예탁현금
      DpsamtUtlfeeGivPrergAmt  (숫자)  예탁금이용료지급예정금액 — 결제예정내역.예탁금이용료
      TaxAmt  (숫자)  세금 — 결제예정내역.세금
      CsgnMgnrat  (숫자)  위탁증거금 비율
      CsgnMnyMgnrat  (숫자)  위탁증거금현금비율
      DpstgTotamtLackAmt  (숫자)  예탁총액부족금액(위탁증거금기준)
      DpstgMnyLackAmt  (숫자)  예탁현금부족금액(위탁증거금기준)
      RealInAmt  (숫자)  실입금액
      InAmt  (숫자)  입금액
      OutAmt  (숫자)  출금액
      FutsAdjstDfamt  (숫자)  선물정산차금
      FutsThdayDfamt  (숫자)  선물당일차금
      FutsUpdtDfamt  (숫자)  선물갱신차금
      FutsLastSettDfamt  (숫자)  선물최종결제차금
      OptSettDfamt  (숫자)  옵션결제차금
      OptBuyAmt  (숫자)  옵션매수금액
      OptSellAmt  (숫자)  옵션매도금액
      OptXrcDfamt  (숫자)  옵션행사차금
      OptAsgnDfamt  (숫자)  옵션배정차금
      RealGdsUndAmt  (숫자)  실물인수도금액
      RealGdsUndAsgnAmt  (숫자)  실물인수도배정대금
      RealGdsUndXrcAmt  (숫자)  실물인수도행사대금
      CmsnAmt  (숫자)  수수료
      FutsCmsn  (숫자)  선물수수료
      OptCmsn  (숫자)  옵션수수료
      FutsCtrctQty  (숫자)  선물약정수량
      FutsCtrctAmt  (숫자)  선물약정금액
      OptCtrctQty  (숫자)  옵션약정수량
      OptCtrctAmt  (숫자)  옵션약정금액
      FutsUnsttQty  (숫자)  선물미결제수량
      FutsUnsttAmt  (숫자)  선물미결제금액
      OptUnsttQty  (숫자)  옵션미결제수량
      OptUnsttAmt  (숫자)  옵션미결제금액
      FutsBuyUnsttQty  (숫자)  선물매수미결제수량
      FutsBuyUnsttAmt  (숫자)  선물매수미결제금액
      FutsSellUnsttQty  (숫자)  선물매도미결제수량
      FutsSellUnsttAmt  (숫자)  선물매도미결제금액
      OptBuyUnsttQty  (숫자)  옵션매수미결제수량
      OptBuyUnsttAmt  (숫자)  옵션매수미결제금액
      OptSellUnsttQty  (숫자)  옵션매도미결제수량
      OptSellUnsttAmt  (숫자)  옵션매도미결제금액
      FutsBuyctrQty  (숫자)  선물매수약정수량
      FutsBuyctrAmt  (숫자)  선물매수약정금액
      FutsSlctrQty  (숫자)  선물매도약정수량
      FutsSlctrAmt  (숫자)  선물매도약정금액
      OptBuyctrQty  (숫자)  옵션매수약정수량
      OptBuyctrAmt  (숫자)  옵션매수약정금액
      OptSlctrQty  (숫자)  옵션매도약정수량
      OptSlctrAmt  (숫자)  옵션매도약정금액
      FutsBnsplAmt  (숫자)  선물매매손익금액
      OptBnsplAmt  (숫자)  옵션매매손익금액
      FutsEvalPnlAmt  (숫자)  선물평가손익금액
      OptEvalPnlAmt  (숫자)  옵션평가손익금액
      FutsEvalAmt  (숫자)  선물평가금액
      OptEvalAmt  (숫자)  옵션평가금액 — 예수금현황.옵션잔고평가금
      MktEndAfMnyInAmt  (숫자)  장종료후현금입금금액
      MktEndAfMnyOutAmt  (숫자)  장종료후현금출금금액
      MktEndAfSubstDsgnAmt  (숫자)  장종료후대용지정금액
      MktEndAfSubstAbndAmt  (숫자)  장종료후대용해지금액

  공통: rsp_cd  응답코드  ·  rsp_msg  응답메시지
── OUT_END ──────────────────────────────────────────────
"""

import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from dbsec_helper import call_rest, print_response

resp, data = call_rest(
    url="/api/v1/trading/kr-futureoption/inquiry/deposit-detail",
    body={
        "In": {
            "BnsDt": "20240127",  # 매매일 (str)
        },
    },
    label="선물옵션 가정산예탁금 상세",
)
print_response(resp, data)
