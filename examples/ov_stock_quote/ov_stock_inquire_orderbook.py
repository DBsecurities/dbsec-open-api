"""해외주식호가조회 (FSTKHOGA) — standalone 예제.

그룹    : 해외주식시세
엔드포인트: POST /api/v1/quote/overseas-stock/inquiry/orderbook
TPS     : 2
가이드  : https://openapi.dbsec.co.kr/apiservice?group_id=a804e311-cb53-499b-9d8a-a4d838f0a484&api_id=70caf020-96aa-4ffb-8637-aae4ec54cb39

해외주식 호가 조회 API 입니다.

토큰은 examples/dbsec_helper.py 가 자동 발급/캐싱합니다.

실행:
    # examples/ 폴더에서 실행하는 경우:
    python ov_stock_quote/ov_stock_inquire_orderbook.py
    # examples/ov_stock_quote/ 폴더에서 실행하는 경우:
    python ov_stock_inquire_orderbook.py

── 응답 파라미터 (Out) ─ OUT_BEGIN ──────────────────────
  [TR FSTKHOGA]
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
    url="/api/v1/quote/overseas-stock/inquiry/orderbook",
    body={
        "In": {
            "InputIscd1": "TSLA",  # 입력종목코드1 (str) - 해외주식 종목코드
            "InputCondMrktDivCode": "FN",  # 입력조건시장분류코드 (str) - FY:뉴욕 FN:나스닥 FA:아멕스
        },
    },
    label="해외주식호가조회",
)
print_response(resp, data)
