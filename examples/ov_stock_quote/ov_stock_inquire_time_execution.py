"""해외주식시간대별체결조회 (FSTKCONCLUSION) — standalone 예제.

그룹    : 해외주식시세
엔드포인트: POST /api/v1/quote/overseas-stock/inquiry/hour-price
TPS     : 2
가이드  : https://openapi.dbsec.co.kr/apiservice?group_id=a804e311-cb53-499b-9d8a-a4d838f0a484&api_id=e4c85422-9d4a-4e46-917c-ef7988fba8c8

해외주식 시간대별 체결조회 API입니다.

토큰은 examples/dbsec_helper.py 가 자동 발급/캐싱합니다.

실행:
    # examples/ 폴더에서 실행하는 경우:
    python ov_stock_quote/ov_stock_inquire_time_execution.py
    # examples/ov_stock_quote/ 폴더에서 실행하는 경우:
    python ov_stock_inquire_time_execution.py

── 응답 파라미터 (Out) ─ OUT_BEGIN ──────────────────────
  [TR FSTKCONCLUSION]
    Out  (오브젝트)  Out
      Hour  (문자)  시간
      Prpr  (문자)  현재가
      PrdyVrssSign  (문자)  전일대비부호
      PrdyCtrt  (문자)  전일대비율
      CntgVol  (문자)  체결거래량

  공통: rsp_cd  응답코드  ·  rsp_msg  응답메시지
── OUT_END ──────────────────────────────────────────────
"""


import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from dbsec_helper import call_rest, print_response

resp, data = call_rest(
    url="/api/v1/quote/overseas-stock/inquiry/hour-price",
    body={
        "In": {
            "InputCondMrktDivCode": "FN",  # 입력조건시장분류코드 (str) - FY:뉴욕 FN:나스닥 FA:아멕스
            "InputIscd1": "TSLA",  # 입력종목코드1 (str) - 해외주식 종목코드 입력
            "InputHourClsCode": "2",  # 입력시간구분코드 (str) - 0: 전체 1: 장전 2: 장중 3: 장후 4: 장전+장중 5: 장전+장후
            "InputDivXtick": "600",  # 입력X틱분틱일별구분코드 (str) - 30: 30초 60: 1분 600: 10분 3600: 60분 [60*N: N분]
            "InputSctnClsCode": "2",  # 입력구간구분코드 (str) - 0:default 1:당일 2:전일
        },
    },
    label="해외주식시간대별체결조회",
)
print_response(resp, data)
