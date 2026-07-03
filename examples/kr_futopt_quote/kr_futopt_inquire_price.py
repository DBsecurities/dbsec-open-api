"""현재가조회 (FOPRICE) — standalone 예제.

그룹    : 국내선물옵션시세
엔드포인트: POST /api/v1/quote/kr-futureoption/inquiry/price
TPS     : 5
가이드  : https://openapi.dbsec.co.kr/apiservice?group_id=80d95623-7135-481b-b109-d7370f1a261b&api_id=18f56401-9d9e-49c6-8e6b-3b226c1dc222

국내선물옵션 현재가 조회 API입니다.

토큰은 examples/dbsec_helper.py 가 자동 발급/캐싱합니다.

실행:
    # examples/ 폴더에서 실행하는 경우:
    python kr_futopt_quote/kr_futopt_inquire_price.py
    # examples/kr_futopt_quote/ 폴더에서 실행하는 경우:
    python kr_futopt_inquire_price.py

── 응답 파라미터 (Out) ─ OUT_BEGIN ──────────────────────
  [TR FOPRICE]
    Out  (오브젝트)  Out
      Thrr  (문자)  이론가
      AcmlTrPbmn  (문자)  거래대금
      AcmlVol  (문자)  거래량
      PrdyVol  (문자)  전일거래량
      Bidp1  (문자)  매수호가
      Askp1  (문자)  매도호가
      HtsOtstStplQty  (문자)  미결제약정수량
      OtstStplQtyIcdc  (문자)  미결제증감
      Dprt  (문자)  괴리율
      PrdyVrss  (문자)  전일대비
      PrdyCtrt  (문자)  전일대비율
      MrktBasis  (문자)  시장베이시스
      Prpr  (문자)  현재가
      Mxpr  (문자)  상한가
      Llam  (문자)  하한가
      Oprc  (문자)  시가
      SdprVrssMrktRate  (문자)  기준가대비시가비율
      PrprVrssOprcRate  (문자)  현재가대비시가비율
      Hprc  (문자)  고가
      SdprVrssHgprRate  (문자)  기준가대비고가비율
      Lprc  (문자)  저가
      SdprVrssLwprRate  (문자)  기준가대비저가비율
      PrprVrssLwprRate  (문자)  현재가대비저가비율

  공통: rsp_cd  응답코드  ·  rsp_msg  응답메시지
── OUT_END ──────────────────────────────────────────────
"""


import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from dbsec_helper import call_rest, print_response

resp, data = call_rest(
    url="/api/v1/quote/kr-futureoption/inquiry/price",
    body={
        "In": {
            "InputCondMrktDivCode": "F",  # 입력조건시장분류코드 (str) - F : 지수선물 JF : 주식선물 KF : 미니선물 CF : 상품선물 XF : 섹터선물 CM : 야간선물 EK : 야간미니선물 O : 지수옵션 JO : 주식옵션 KO : 미니옵션 WO : K200위클리옵션 EU : 야간옵션 EW : 위클리옵션(야간) SO: 코스닥 150옵션
            "InputIscd1": "A0166000",  # 입력종목코드1 (str) - 종목코드 입력 ex. 101VC000
        },
    },
    label="현재가조회",
)
print_response(resp, data)
