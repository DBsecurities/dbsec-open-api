"""해외주식 주문가능금액조회 (CAZCQ01300) — standalone 예제.

그룹    : 해외주식주문
엔드포인트: POST /api/v1/trading/overseas-stock/inquiry/able-orderqty
TPS     : 2
가이드  : https://openapi.dbsec.co.kr/apiservice?group_id=e4726f55-cc3b-45af-a1b5-852628fe5960&api_id=0793f887-f97d-48f6-8808-630217c93022

해외주식 주문가능금액조회 API입니다. ※ 모의투자 계좌로 사용가능한 API입니다.

토큰은 examples/dbsec_helper.py 가 자동 발급/캐싱합니다.

실행:
    # examples/ 폴더에서 실행하는 경우:
    python ov_stock_order/ov_stock_inquire_psbl_amount.py
    # examples/ov_stock_order/ 폴더에서 실행하는 경우:
    python ov_stock_inquire_psbl_amount.py

── 응답 파라미터 (Out) ─ OUT_BEGIN ──────────────────────
  [TR CAZCQ01300]
    Out  (오브젝트)  Out
      AstkOrdAbleAmt  (숫자)  해외주식주문가능금액 — 해당통화 기준
      AstkOrdAbleQty  (숫자)  해외주식주문가능수량 — 해당통화 기준
      AstkOrdAbleAmt0  (숫자)  해외주식주문가능금액0 — 통함증거금 기준
      AstkOrdAbleQty0  (숫자)  해외주식주문가능수량0 — 통함증거금 기준
      AstkOrdAbleAmt1  (숫자)  해외주식주문가능금액1 — 미수금포함 기준
      AstkOrdAbleQty1  (숫자)  해외주식주문가능수량1 — 미수금포함 기준
      CsldtMgnUseYn  (문자)  통합증거금사용여부 — (Y/N)
      OtptItemNm0  (문자)  출력항목명0 — 통합증거금사용여부 (Y/N)
      Mgnrt  (숫자)  증거금율 — 종목증거금률
      OtptItemNm1  (문자)  출력항목명1 — 계좌증거금률
      Mgnrt0  (숫자)  증거금율0 — 적용증거금률

  공통: rsp_cd  응답코드  ·  rsp_msg  응답메시지
── OUT_END ──────────────────────────────────────────────
"""

import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from dbsec_helper import call_rest, print_response

resp, data = call_rest(
    url="/api/v1/trading/overseas-stock/inquiry/able-orderqty",
    body={
        "In": {
            "TrxTpCode": "2",  # 처리구분코드 (str) - 1:매도 2:매수
            "AstkIsuNo": "METU",  # 해외주식종목번호 (str) - 미국주식/ETF: "종목코드"
            "AstkOrdPrc": 26,  # 해외주식주문가격 (int)
            "WonFcurrTpCode": "2",  # 원화외화구분코드 (str) - 1: 원화 2: 외화
        },
    },
    label="해외주식 주문가능금액조회",
)
print_response(resp, data)
