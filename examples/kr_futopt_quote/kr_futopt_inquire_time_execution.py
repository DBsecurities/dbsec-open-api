"""시간대별체결조회 (CONCLUSION) — standalone 예제.

그룹    : 국내선물옵션시세
엔드포인트: POST /api/v1/quote/kr-futureoption/inquiry/hour-price
TPS     : 2
가이드  : https://openapi.dbsec.co.kr/apiservice?group_id=80d95623-7135-481b-b109-d7370f1a261b&api_id=587bb0f9-55bd-428e-b8e2-d5ab92c1eb5c

국내선물옵션 시간대별 체결조회 API입니다.

토큰은 examples/dbsec_helper.py 가 자동 발급/캐싱합니다.

실행:
    # examples/ 폴더에서 실행하는 경우:
    python kr_futopt_quote/kr_futopt_inquire_time_execution.py
    # examples/kr_futopt_quote/ 폴더에서 실행하는 경우:
    python kr_futopt_inquire_time_execution.py

── 응답 파라미터 (Out) ─ OUT_BEGIN ──────────────────────
  [TR CONCLUSION]
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
    url="/api/v1/quote/kr-futureoption/inquiry/hour-price",
    body={
        "In": {
            "InputCondMrktDivCode": "F",  # 입력조건시장분류코드 (str) - F : 지수선물 JF : 주식선물 KF : 미니선물 CF : 상품선물 XF : 섹터선물 CM : 야간선물 O : 지수옵션 JO : 주식옵션 KO : 미니옵션 WO : K200위클리옵션 EU : 야간옵션 SO: 코스닥 150옵션
            "InputIscd1": "A0166000",  # 입력종목코드1 (str) - 종목코드 입력 ex. 005930
        },
    },
    label="시간대별체결조회",
)
print_response(resp, data)
