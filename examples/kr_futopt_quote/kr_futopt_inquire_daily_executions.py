"""일별체결조회 (DAYTRADE) — standalone 예제.

그룹    : 국내선물옵션시세
엔드포인트: POST /api/v1/quote/kr-futureoption/inquiry/daily-price
TPS     : 2
가이드  : https://openapi.dbsec.co.kr/apiservice?group_id=80d95623-7135-481b-b109-d7370f1a261b&api_id=a6870035-beab-4c43-a0c2-86f102c330c7

국내선물옵션 일별 체결조회 API입니다.

토큰은 examples/dbsec_helper.py 가 자동 발급/캐싱합니다.

실행:
    # examples/ 폴더에서 실행하는 경우:
    python kr_futopt_quote/kr_futopt_inquire_daily_executions.py
    # examples/kr_futopt_quote/ 폴더에서 실행하는 경우:
    python kr_futopt_inquire_daily_executions.py

── 응답 파라미터 (Out) ─ OUT_BEGIN ──────────────────────
  [TR DAYTRADE]
    Out  (오브젝트)  Out
      Hour  (문자)  시간
      Prpr  (문자)  현재가
      PrdyVrssSign  (문자)  전일대비부호
      PrdyVrss  (문자)  전일대비
      ShnuCnqn  (문자)  매수체결량
      SelnCnqn  (문자)  매도체결량

  공통: rsp_cd  응답코드  ·  rsp_msg  응답메시지
── OUT_END ──────────────────────────────────────────────
"""


import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from dbsec_helper import call_rest, print_response

resp, data = call_rest(
    url="/api/v1/quote/kr-futureoption/inquiry/daily-price",
    body={
        "In": {
            "InputCondMrktDivCode": "F",  # 입력조건시장분류코드 (str) - F : 지수선물 JF : 주식선물 KF : 미니선물 CF : 상품선물 XF : 섹터선물 CM : 야간선물 O : 지수옵션 JO : 주식옵션 KO : 미니옵션 WO : K200위클리옵션 EU : 야간옵션 SO: 코스닥 150옵션
            "InputIscd1": "A0166000",  # 입력종목코드1 (str) - 선물 종목코드 입력 
            "InputHourClsCode": "5",  # 입력시간구분코드 (str) - 1: 시간외단일가체결 2: 장전+장중+장후 3: 장전+장후 4: 장중 5: 장전+장중+장후+장종료(예상포함) 6: 예상제외 모두 7: 장전+장중+장후+장종료(예상불포함) 8: 예상 9: 장전+장중+장후+장종료 (예상,대량, 바스켓, 정리매매 제외) 10: 시간외단일가 예상
        },
    },
    label="일별체결조회",
)
print_response(resp, data)
