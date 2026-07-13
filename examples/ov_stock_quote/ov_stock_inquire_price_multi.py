"""해외주식 멀티현재가조회 (FSTKMULTIPRICE) — standalone 예제.

그룹    : 해외주식시세
엔드포인트: POST /api/v1/quote/overseas-stock/inquiry/multiprice
TPS     : 2
가이드  : https://openapi.dbsec.co.kr/apiservice?group_id=a804e311-cb53-499b-9d8a-a4d838f0a484&api_id=729276aa-9913-444e-b637-8efc316de84e

해외주식시세 멀티 현재가 조회 API입니다. ※ 1회 호출에 최대 50종목의 시세를 확인 가능합니다. ※ "dataCnt" 필드에 요청할 데이터의 개수를 입력하여 호출이 가능 합니다. (1~50) ※ "dataCnt" 필드의 값과 입력 데이터의 개수가 일치하지 않으면 호출이 불가합니다. ※ 아래와 같이시장구분필드와 종목코드가 1:1 쌍을 이뤄야 호출이 정상적으로 이뤄집니다. - InputIscd1:J (시장구분필드), - InputCondMrktDivCode1:005930 (종목코드) ※ [Inp...

토큰은 examples/dbsec_helper.py 가 자동 발급/캐싱합니다.

실행:
    # examples/ 폴더에서 실행하는 경우:
    python ov_stock_quote/ov_stock_inquire_price_multi.py
    # examples/ov_stock_quote/ 폴더에서 실행하는 경우:
    python ov_stock_inquire_price_multi.py

── 응답 파라미터 (Out) ─ OUT_BEGIN ──────────────────────
  [TR FSTKMULTIPRICE]
    Out  (배열)  Out
      Iscd  (문자)  종목코드
      KorIsnm  (문자)  한글종목명
      Sdpr  (문자)  기준가
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

  공통: rsp_cd  응답코드  ·  rsp_msg  응답메시지
── OUT_END ──────────────────────────────────────────────
"""


import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from dbsec_helper import call_rest, print_response

resp, data = call_rest(
    url="/api/v1/quote/overseas-stock/inquiry/multiprice",
    body={
        "In": {
            "dataCnt": 5,  # 호출건수 (str) - 1~50사이의 값 입력
            "InputCondMrktDivCode1": "FN",  # 입력조건시장분류코드1 (str) - FY:뉴욕 FN:나스닥 FA:아멕스
            "InputIscd1": "TSLA",  # 입력종목코드1 (str) - 해외주식 종목코드
            "InputCondMrktDivCode2": "FN",
            "InputIscd2": "AAPL",
            "InputCondMrktDivCode3": "FN",
            "InputIscd3": "GOOG",
            "InputCondMrktDivCode4": "FN",
            "InputIscd4": "NVDA",
            "InputCondMrktDivCode5": "FN",
            "InputIscd5": "META",
        },
    },
    label="해외주식 멀티현재가조회",
)
print_response(resp, data)
