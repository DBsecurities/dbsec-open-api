"""선물옵션 주문가능수량 (CFOAQ42400) — standalone 예제.

그룹    : 국내선물옵션주문
엔드포인트: POST /api/v1/trading/kr-futureoption/inquiry/able-orderqty
TPS     : 2
가이드  : https://openapi.dbsec.co.kr/apiservice?group_id=44c4a04f-f55e-4c1c-b4e2-b48ec4869aee&api_id=2c3c7308-2fc1-4a27-acef-5c9352036365

선물옵션 주문가능수량 조회 API 입니다. ※ 모의투자 계좌로 사용가능한 API입니다.

토큰은 examples/dbsec_helper.py 가 자동 발급/캐싱합니다.

실행:
    # examples/ 폴더에서 실행하는 경우:
    python kr_futopt_order/kr_futopt_inquire_psbl_quantity.py
    # examples/kr_futopt_order/ 폴더에서 실행하는 경우:
    python kr_futopt_inquire_psbl_quantity.py

── 응답 파라미터 (Out) ─ OUT_BEGIN ──────────────────────
  [TR CFOAQ42400]
    Out  (오브젝트)  Out
      QryDt  (문자)  조회일
      FnoLmtSetupTpCode  (문자)  선물옵션한도설정구분 — 0:제한없음 1:수량 2:금액 3:수량+금액
      FutsHldLmtQty  (숫자)  선물보유한도수량
      OptHldLmtQty  (숫자)  옵션보유한도수량
      EqoHldLmtQty  (숫자)  주식옵션보유한도수량
      FutsHldLmtAmt  (숫자)  선물보유한도금액
      OptHldLmtAmt  (숫자)  옵션보유한도금액
      EqoHldLmtAmt  (숫자)  주식옵션보유한도금액
      HldLmtOrdAbleQty  (숫자)  보유한도주문가능수량 — 보유한도에 의한 주문가능수량
      OrdPrc  (숫자)  주문가
      CurPrc  (숫자)  현재가
      NewOrdAbleQty  (숫자)  신규주문가능수량
      LqdtOrdAbleQty  (숫자)  청산주문가능수량
      OrdPrcOrdAbleQty  (숫자)  주문가격주문가능수량 — 주문가격에 의한 주문가능수량
      OptSellUnsttRestrcQty  (숫자)  옵션매도미결제제한수량
      OptSellRestrcOrdAbleQty  (숫자)  옵션매도제한주문가능수량 — 옵션매도보유제한에 의한 주문가능수량
      LastOrdAbleQty  (숫자)  최종주문가능수량

  공통: rsp_cd  응답코드  ·  rsp_msg  응답메시지
── OUT_END ──────────────────────────────────────────────
"""

import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from dbsec_helper import call_rest, print_response

resp, data = call_rest(
    url="/api/v1/trading/kr-futureoption/inquiry/able-orderqty",
    body={
        "In": {
            "FnoIsuNo": "A0566000",  # 선물옵션종목번호 (str) - 선물옵션 종목 코드 입력 선물 EX) 211V2060 옵션 EX) 201V2347
            "BnsTpCode": "2",  # 매매구분 (str) - 1:매도 2:매수
            "OrdPrc": 1201,  # 주문가 (int)
            "FnoOrdprcPtnCode": "00",  # 선물옵션호가유형코드 (str) - 00:지정가 03:시장가
        },
    },
    label="선물옵션 주문가능수량",
)
print_response(resp, data)
