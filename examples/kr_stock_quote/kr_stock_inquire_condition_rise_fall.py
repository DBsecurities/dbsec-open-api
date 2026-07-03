"""주식조건상승하락조회 (RANKLIST) — standalone 예제.

그룹    : 국내주식시세
엔드포인트: POST /api/v1/quote/kr-stock/inquiry/rank-list
TPS     : 3
가이드  : https://openapi.dbsec.co.kr/apiservice?group_id=80005fb0-6feb-4b8b-904a-605c59e29b4f&api_id=668de023-eb33-4f96-a687-51b5cc1b97ec

국내주식 주식조건상승하락 조회 API입니다. ※ 국내주식 상승/하락률을 조건에 맞는 종목을 제공합니다.

토큰은 examples/dbsec_helper.py 가 자동 발급/캐싱합니다.

실행:
    # examples/ 폴더에서 실행하는 경우:
    python kr_stock_quote/kr_stock_inquire_condition_rise_fall.py
    # examples/kr_stock_quote/ 폴더에서 실행하는 경우:
    python kr_stock_inquire_condition_rise_fall.py

── 응답 파라미터 (Out) ─ OUT_BEGIN ──────────────────────
  [TR RANKLIST]
    Out  (배열)  Out
      Iscd  (문자)  종목코드
      KorIsnm  (문자)  한글종목명
      DataRank  (문자)  순위
      Prpr  (문자)  현재가
      PrdyVrssSign  (문자)  전일대비부호
      PrdyVrss  (문자)  전일대비
      PrdyCtrt  (문자)  전일대비율

  공통: rsp_cd  응답코드  ·  rsp_msg  응답메시지
── OUT_END ──────────────────────────────────────────────
"""


import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from dbsec_helper import call_rest, print_response

resp, data = call_rest(
    url="/api/v1/quote/kr-stock/inquiry/rank-list",
    body={
        "In": {
            "InputDateClsCode": "1",  # 입력일자구분코드 (str) - 당일:0 전일:1 주간:2 월간:5
            "InputRankSortClsCode1": "12",  # 입력순위정렬구분코드1 (str) - 상승률:12 하락율:11
            "InputMrktClsCode": "A",  # 입력시장구분코드 (str) - 전체:A 코스피:K 코스닥:Q
            "InputBstpIscd": "",  # 입력업종코드 (str) - 입력시장구분코드 "A" 일시 입력 X 코스피:1001 코스닥:2001
        },
    },
    label="주식조건상승하락조회",
)
print_response(resp, data)
