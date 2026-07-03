"""선물종목 조회 (FCODES) — standalone 예제.

그룹    : 국내선물옵션시세
엔드포인트: POST /api/v1/quote/kr-futureoption/inquiry/future-ticker
TPS     : 3
가이드  : https://openapi.dbsec.co.kr/apiservice?group_id=80d95623-7135-481b-b109-d7370f1a261b&api_id=43e60397-77df-4926-8969-3eb18f9f48e3

국내선물 종목조회 API입니다. ※ 연속키 조회를 통해 종목을 추가로 조회 할 수 있습니다.

토큰은 examples/dbsec_helper.py 가 자동 발급/캐싱합니다.

실행:
    # examples/ 폴더에서 실행하는 경우:
    python kr_futopt_quote/kr_futopt_search_futures.py
    # examples/kr_futopt_quote/ 폴더에서 실행하는 경우:
    python kr_futopt_search_futures.py

── 응답 파라미터 (Out) ─ OUT_BEGIN ──────────────────────
  [TR FCODES]
    Out  (배열)  Out
      Mxpr1st  (문자)  1단계상한가
      UnasShrnIscd  (문자)  기초자산종목코드
      Llam3rd  (문자)  3단계하한가
      Llam2nd  (문자)  2단계하한가
      Llam1st  (문자)  1단계하한가
      Mxpr3rd  (문자)  3단계상한가
      Mxpr2nd  (문자)  2단계상한가
      Iscd  (문자)  종목코드
      StndIscd  (문자)  표준종목코드
      KorIsnm  (문자)  한글종목명
      Sdpr  (문자)  기준가

  공통: rsp_cd  응답코드  ·  rsp_msg  응답메시지
── OUT_END ──────────────────────────────────────────────
"""


import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from dbsec_helper import call_rest, print_response

resp, data = call_rest(
    url="/api/v1/quote/kr-futureoption/inquiry/future-ticker",
    body={
        "In": {
            "InputCondMrktDivCode": "F",  # 입력조건시장분류코드 (str) - F : 지수선물 JF : 주식선물 KF : 미니선물 CF : 상품선물 XF : 섹터선물 CM : 야간선물 EC : 야간상품선물 ES : KOSDAQ150선물 EK : 야간미니선물
        },
    },
    label="선물종목 조회",
)
print_response(resp, data)
