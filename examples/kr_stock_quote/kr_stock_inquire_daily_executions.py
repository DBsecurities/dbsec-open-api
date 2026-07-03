"""일별체결조회 (DAYTRADE) — standalone 예제.

그룹    : 국내주식시세
엔드포인트: POST /api/v1/quote/kr-stock/inquiry/daily-price
TPS     : 3
가이드  : https://openapi.dbsec.co.kr/apiservice?group_id=80005fb0-6feb-4b8b-904a-605c59e29b4f&api_id=6738128a-9cc7-46ce-b59f-dda6162a12b8

국내주식 일별체결 조회 API입니다.

토큰은 examples/dbsec_helper.py 가 자동 발급/캐싱합니다.

실행:
    # examples/ 폴더에서 실행하는 경우:
    python kr_stock_quote/kr_stock_inquire_daily_executions.py
    # examples/kr_stock_quote/ 폴더에서 실행하는 경우:
    python kr_stock_inquire_daily_executions.py

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
    url="/api/v1/quote/kr-stock/inquiry/daily-price",
    body={
        "In": {
            "InputCondMrktDivCode": "J",  # 입력조건시장분류코드 (str) - 주식:J 주식(NXT): NJ 주식(통합): UJ ETN: EN ELW: W ※ ETF종목의 경우 J 코드를 사용해 조회 부탁드립니다.
            "InputIscd1": "005930",  # 입력종목코드1 (str) - 종목코드 입력 - J(KRX 주식): - NJ(NXT 주식): - UJ(통합): ※ NXT/통합시세로 종목 조회 시 반드시 종목 앞에 구분자 (N-, U-)를 붙여서 호출 부탁드리겠습니다.
            "InputHourClsCode": "4",  # 입력시간구분코드 (str) - 1: 시간외단일가체결 2: 장전+장중+장후 3: 장전+장후 4: 장중 5: 장전+장중+장후+장종료(예상포함) 6: 예상제외 모두 7: 장전+장중+장후+장종료(예상불포함) 8: 예상 9: 장전+장중+장후+장종료 (예상,대량, 바스켓, 정리매매 제외) 10: 시간외단일가 예상
        },
    },
    label="일별체결조회",
)
print_response(resp, data)
