"""장내채권 호가 조회 (BO_HOGA) — standalone 예제.

그룹    : 장내채권시세
엔드포인트: POST /api/v1/quote/krx-bond/inquiry/orderbook
TPS     : 2
가이드  : https://openapi.dbsec.co.kr/apiservice?group_id=b86989c1-9666-42d2-a446-492376f71f1b&api_id=1bf5ef83-606b-4b5d-a129-8a35e503aeee

장내채권 호가조회 API 입니다.

토큰은 examples/dbsec_helper.py 가 자동 발급/캐싱합니다.

실행:
    # examples/ 폴더에서 실행하는 경우:
    python bond_quote/bond_inquire_orderbook.py
    # examples/bond_quote/ 폴더에서 실행하는 경우:
    python bond_inquire_orderbook.py

── 응답 파라미터 (Out) ─ OUT_BEGIN ──────────────────────
  [TR BO_HOGA]
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
      BondSelnErt1  (문자)  매도호가수익률1
      AskpRsqnIcdc1  (문자)  매도호가잔량증감1
      AskpRsqnIcdc2  (문자)  매도호가잔량증감2
      AskpRsqnIcdc3  (문자)  매도호가잔량증감3
      AskpRsqnIcdc4  (문자)  매도호가잔량증감4
      AskpRsqnIcdc5  (문자)  매도호가잔량증감5
      BondShnuErt1  (문자)  매수호가수익률1
      BidpRsqnIcdc1  (문자)  매수호가잔량증감1
      BidpRsqnIcdc2  (문자)  매수호가잔량증감2
      BidpRsqnIcdc3  (문자)  매수호가잔량증감3
      BidpRsqnIcdc4  (문자)  매수호가잔량증감4
      BidpRsqnIcdc5  (문자)  매수호가잔량증감5
      TotalAskpRsqn  (문자)  총매도호가잔량
      TotalBidpRsqn  (문자)  총매수호가잔량
      Oprc  (문자)  시가
      Hprc  (문자)  고가
      Lprc  (문자)  저가
      Prpr  (문자)  현재가
      PrdyClpr  (문자)  전일종가

  공통: rsp_cd  응답코드  ·  rsp_msg  응답메시지
── OUT_END ──────────────────────────────────────────────
"""


import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from dbsec_helper import call_rest, print_response

resp, data = call_rest(
    url="/api/v1/quote/krx-bond/inquiry/orderbook",
    body={
        "In": {
            "InputIscd1": "KR101501DDC7",  # 입력종목코드1 (str) - 채권 종목코드 입력
            "InputCondMrktDivCode": "B",  # 입력조건시장분류코드 (str) - 소액:SB 일반:B
        },
    },
    label="장내채권 호가 조회",
)
print_response(resp, data)
