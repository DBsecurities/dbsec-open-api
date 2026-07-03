"""해외주식현재가조회 (FSTKPRICE) — standalone 예제.

그룹    : 해외주식시세
엔드포인트: POST /api/v1/quote/overseas-stock/inquiry/price
TPS     : 2
가이드  : https://openapi.dbsec.co.kr/apiservice?group_id=a804e311-cb53-499b-9d8a-a4d838f0a484&api_id=1c4d54aa-9f0f-4036-bb76-202c7116398d

해외주식 현재가 조회 API 입니다.

토큰은 examples/dbsec_helper.py 가 자동 발급/캐싱합니다.

실행:
    # examples/ 폴더에서 실행하는 경우:
    python ov_stock_quote/ov_stock_inquire_price.py
    # examples/ov_stock_quote/ 폴더에서 실행하는 경우:
    python ov_stock_inquire_price.py

── 응답 파라미터 (Out) ─ OUT_BEGIN ──────────────────────
  [TR FSTKPRICE]
    Out  (오브젝트)  Out
      Sdpr  (문자)  기준가
      prdyVol  (문자)  전일거래량
      AcmlVol  (문자)  거래량
      AcmlTrPbmn  (문자)  거래대금
      Per  (문자)  PER
      PrdyCtrt  (문자)  전일대비율
      PrdyVrss  (문자)  전일대비
      askp1  (문자)  매도호가
      bidp1  (문자)  매수호가
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

  공통: rsp_cd  응답코드  ·  rsp_msg  응답메시지
── OUT_END ──────────────────────────────────────────────
"""


import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from dbsec_helper import call_rest, print_response

resp, data = call_rest(
    url="/api/v1/quote/overseas-stock/inquiry/price",
    body={
        "In": {
            "InputIscd1": "TSLA",  # 입력종목코드1 (str) - 해외주식 종목코드
            "InputCondMrktDivCode": "FN",  # 입력조건시장분류코드 (str) - FY:뉴욕 FN:나스닥 FA:아멕스
        },
    },
    label="해외주식현재가조회",
)
print_response(resp, data)
