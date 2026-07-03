"""시간대별체결조회 (CONCLUSION) — standalone 예제.

그룹    : 국내주식시세
엔드포인트: POST /api/v1/quote/kr-stock/inquiry/hour-price
TPS     : 3
가이드  : https://openapi.dbsec.co.kr/apiservice?group_id=80005fb0-6feb-4b8b-904a-605c59e29b4f&api_id=01b99bab-7f12-4098-97e1-99fdda029ca2

국내주식 시간대별 체결 조회 API입니다.

토큰은 examples/dbsec_helper.py 가 자동 발급/캐싱합니다.

실행:
    # examples/ 폴더에서 실행하는 경우:
    python kr_stock_quote/kr_stock_inquire_time_execution.py
    # examples/kr_stock_quote/ 폴더에서 실행하는 경우:
    python kr_stock_inquire_time_execution.py

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
    url="/api/v1/quote/kr-stock/inquiry/hour-price",
    body={
        "In": {
            "InputCondMrktDivCode": "J",  # 입력조건시장분류코드 (str) - 주식:J 주식(NXT): NJ 주식(통합): UJ ETN: EN ELW: W ※ ETF종목의 경우 J 코드를 사용해 조회 부탁드립니다.
            "InputIscd1": "005930",  # 입력종목코드1 (str) - 종목코드 입력 - J(KRX 주식): - NJ(NXT 주식): - UJ(통합): ※ NXT/통합시세로 종목 조회 시 반드시 종목 앞에 구분자 (N-, U-)를 붙여서 호출 부탁드리겠습니다.
        },
    },
    label="시간대별체결조회",
)
print_response(resp, data)
