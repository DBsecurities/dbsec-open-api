"""국내선옵 멀티현재가 조회 (FOMULTIPRICE) — standalone 예제.

그룹    : 국내선물옵션시세
엔드포인트: POST /api/v1/quote/kr-futureoption/inquiry/multiprice
TPS     : 2
가이드  : https://openapi.dbsec.co.kr/apiservice?group_id=80d95623-7135-481b-b109-d7370f1a261b&api_id=0d013d41-68cb-4ccb-92e6-893e27048217

국내선물옵션 멀티 현재가 조회 API입니다. ※ 1회 호출에 최대 50종목의 시세를 확인 가능합니다. ※ "dataCnt" 필드에 요청할 데이터의 개수를 입력하여 호출이 가능 합니다. (1~50) ※ "dataCnt" 필드의 값과 입력 데이터의 개수가 일치하지 않으면 호출이 불가합니다. ※ 아래와 같이시장구분필드와 종목코드가 1:1 쌍을 이뤄야 호출이 정상적으로 이뤄집니다. - InputIscd1:F (시장구분필드), - InputCondMrktDivCode1:A0166000 (종목코드) ※ [I...

토큰은 examples/dbsec_helper.py 가 자동 발급/캐싱합니다.

실행:
    # examples/ 폴더에서 실행하는 경우:
    python kr_futopt_quote/kr_futopt_inquire_price_multi.py
    # examples/kr_futopt_quote/ 폴더에서 실행하는 경우:
    python kr_futopt_inquire_price_multi.py

── 응답 파라미터 (Out) ─ OUT_BEGIN ──────────────────────
  [TR FOMULTIPRICE]
    Out  (배열)  Out
      Iscd  (문자)  종목코드
      Prpr  (문자)  현재가
      Mxpr  (문자)  상한가
      Llam  (문자)  하한가
      Oprc  (문자)  시가
      SdprVrssMrktRate  (문자)  기준가대비시가비율
      PrprVrssOprcRate  (문자)  현재가대비시가비율
      Hprc  (문자)  고가
      SdprVrssHgprRate  (문자)  기준가대비고가비율
      PrprVrssHgprRate  (문자)  현재가대비고가비율
      Lprc  (문자)  저가
      SdprVrssLwprRate  (문자)  기준가대비저가비율
      PrprVrssLwprRate  (문자)  현재가대비저가비율
      PrdyVrss  (문자)  전일대비
      PrdyCtrt  (문자)  전일대비율
      AcmlTrPbmn  (문자)  거래대금
      AcmlVol  (문자)  거래량
      PrdyVol  (문자)  전일거래량
      Bidp1  (문자)  매수호가
      Askp1  (문자)  매도호가
      HtsOtstStplQty  (문자)  미결제약정수량
      OtstStplQtyIcdc  (문자)  미결제증감
      Thrr  (문자)  이론가
      Dprt  (문자)  괴리율
      MrktBasis  (문자)  시장베이시스

  공통: rsp_cd  응답코드  ·  rsp_msg  응답메시지
── OUT_END ──────────────────────────────────────────────
"""


import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from dbsec_helper import call_rest, print_response

resp, data = call_rest(
    url="/api/v1/quote/kr-futureoption/inquiry/multiprice",
    body={
        "In": {
            "dataCnt": 5,  # 호출건수 (str) - 1~50사이의 값 입력
            "InputCondMrktDivCode1": "O",  # 입력조건시장분류코드1 (지수옵션) - F : 지수선물 JF : 주식선물 KF : 미니선물 CF : 상품선물 XF : 섹터선물 CM : 야간선물 EK : 야간미니선물 O : 지수옵션 JO : 주식옵션 KO : 미니옵션 WO : K200위클리옵션 EU : 야간옵션 EW : 위클리옵션(야간) SO: 코스닥 150옵션
            "InputIscd1": "B0166180",  # K200 C 202606 180.0
            "InputCondMrktDivCode2": "F",   # 지수선물
            "InputIscd2": "A0166000",  # K200 F 202606
            "InputCondMrktDivCode3": "CF",  # 상품선물
            "InputIscd3": "A6566000",  # 3년국채 F 202606
            "InputCondMrktDivCode4": "WO",  # K200위클리옵션
            "InputIscd4": "B09F1A03",  # 코스피위클리 T C 2605W4 1005.0
            "InputCondMrktDivCode5": "JO",  # 주식옵션
            "InputIscd5": "B0Z66001",  # 한미반도체 C 202606 190,000
        },
    },
    label="국내선옵 멀티현재가 조회",
)
print_response(resp, data)
