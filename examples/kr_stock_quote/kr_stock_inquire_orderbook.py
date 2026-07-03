"""호가조회 (HOGA) — standalone 예제.

그룹    : 국내주식시세
엔드포인트: POST /api/v1/quote/kr-stock/inquiry/orderbook
TPS     : 3
가이드  : https://openapi.dbsec.co.kr/apiservice?group_id=80005fb0-6feb-4b8b-904a-605c59e29b4f&api_id=14be0244-5a65-4219-9639-f32d6ec3f374

국내주식 호가 조회 API입니다.

토큰은 examples/dbsec_helper.py 가 자동 발급/캐싱합니다.

실행:
    # examples/ 폴더에서 실행하는 경우:
    python kr_stock_quote/kr_stock_inquire_orderbook.py
    # examples/kr_stock_quote/ 폴더에서 실행하는 경우:
    python kr_stock_inquire_orderbook.py

── 응답 파라미터 (Out) ─ OUT_BEGIN ──────────────────────
  [TR HOGA]
    Out  (오브젝트)  Out
      Askp1  (문자)  매도호가1
      Askp2  (문자)  매도호가2
      Askp3  (문자)  매도호가3
      Askp4  (문자)  매도호가4
      Askp5  (문자)  매도호가5
      Bidp1  (문자)  매수호가1
      Bidp2  (문자)  매수호가2
      Bidp3  (문자)  매수호가3
      Bidp4  (문자)  매수호가4
      Bidp5  (문자)  매수호가5
      AskpRsqn1  (문자)  매도호가잔량1
      AskpRsqn2  (문자)  매도호가잔량2
      AskpRsqn3  (문자)  매도호가잔량3
      AskpRsqn4  (문자)  매도호가잔량4
      AskpRsqn5  (문자)  매도호가잔량5
      BidpRsqn1  (문자)  매수호가잔량1
      BidpRsqn2  (문자)  매수호가잔량2
      BidpRsqn3  (문자)  매수호가잔량3
      BidpRsqn4  (문자)  매수호가잔량4
      BidpRsqn5  (문자)  매수호가잔량5
      AskpRsqnIcdc1  (문자)  매도호가잔량증감1
      AskpRsqnIcdc2  (문자)  매도호가잔량증감2
      AskpRsqnIcdc3  (문자)  매도호가잔량증감3
      AskpRsqnIcdc4  (문자)  매도호가잔량증감4
      AskpRsqnIcdc5  (문자)  매도호가잔량증감5
      BidpRsqnIcdc1  (문자)  매수호가잔량증감1
      BidpRsqnIcdc2  (문자)  매수호가잔량증감2
      BidpRsqnIcdc3  (문자)  매수호가잔량증감3
      BidpRsqnIcdc4  (문자)  매수호가잔량증감4
      BidpRsqnIcdc5  (문자)  매수호가잔량증감5

  공통: rsp_cd  응답코드  ·  rsp_msg  응답메시지
── OUT_END ──────────────────────────────────────────────
"""


import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from dbsec_helper import call_rest, print_response

resp, data = call_rest(
    url="/api/v1/quote/kr-stock/inquiry/orderbook",
    body={
        "In": {
            "InputIscd1": "005930",  # 입력종목코드1 (str) - 종목코드 입력 - J(KRX 주식): - NJ(NXT 주식): - UJ(통합): ※ NXT/통합시세로 종목 조회 시 반드시 종목 앞에 구분자 (N-, U-)를 붙여서 호출 부탁드리겠습니다.
            "InputCondMrktDivCode": "J",  # 입력조건시장분류코드 (str) - 주식:J 주식(NXT): NJ 주식(통합): UJ ETN: EN ELW: W ※ ETF종목의 경우 J 코드를 사용해 조회 부탁드립니다.
        },
    },
    label="호가조회",
)
print_response(resp, data)
