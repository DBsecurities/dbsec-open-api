"""해외주식 상승하락조회 (FSTKRANKLIST) — standalone 예제.

그룹    : 해외주식시세
엔드포인트: POST /api/v1/quote/overseas-stock/inquiry/rank-list
TPS     : 2
가이드  : https://openapi.dbsec.co.kr/apiservice?group_id=a804e311-cb53-499b-9d8a-a4d838f0a484&api_id=28acef41-26f3-4d3d-bc55-8aca7587a576

해외주식 조건상승하락 조회 API입니다. ※ 해외주식 상승/하락률 조건에 맞는 종목을 제공합니다.

토큰은 examples/dbsec_helper.py 가 자동 발급/캐싱합니다.

실행:
    # examples/ 폴더에서 실행하는 경우:
    python ov_stock_quote/ov_stock_inquire_condition_rise_fall.py
    # examples/ov_stock_quote/ 폴더에서 실행하는 경우:
    python ov_stock_inquire_condition_rise_fall.py

── 응답 파라미터 (Out) ─ OUT_BEGIN ──────────────────────
  [TR FSTKRANKLIST]
    Out  (오브젝트)  Out
      AcmlTrPbmn  (문자)  거래대금
      AcmlVol  (문자)  거래량
      PrdyClpr  (문자)  전일종가
      PrdyCtrt  (문자)  전일대비율
      PrdyVrss  (문자)  전일대비
      PrdyVrssSign  (문자)  전일대비부호
      Prpr  (문자)  현재가
      KorIsnm  (문자)  한글종목명
      Iscd  (문자)  종목코드
      MrktClsName  (문자)  시장구분명

  공통: rsp_cd  응답코드  ·  rsp_msg  응답메시지
── OUT_END ──────────────────────────────────────────────
"""

import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from dbsec_helper import call_rest, print_response

resp, data = call_rest(
    url="/api/v1/quote/overseas-stock/inquiry/rank-list",
    body={
        "In": {
            "InputRealDelayClsCode": "1",  # 지연실시간구분코드 (str) - 0: 지연 1: 실시간
            "InputDataCode": "US",  # 입력해외증시구분코드 (str) - NY: 뉴욕 NA: 나스닥 AM: 아멕스 US:미국
            "InputDateClsCode": "0",  # 입력일자구분코드 (str) - 0: 당일 1: 전일
            "InputRankSortClsCode1": "249",  # 입력순위정렬구분코드1 (str) - 249: 상승율 250: 하락율
            "InputVolClsCode": "9",  # 입력거래량구분코드 (str) - 7: 10만주이상 8: 50만주이상 9: 100만주이상 10:500만주이상 11:1000만주이상 12:5000만주이상
            "InputTrPbmn1": "",  # 거래대금최소값 (str)
            "InputDprice1": "",  # 가격최소값 (str)
            "InputDprice2": "",  # 가격최대값 (str)
        },
    },
    label="해외주식 상승하락조회",
)
print_response(resp, data)
