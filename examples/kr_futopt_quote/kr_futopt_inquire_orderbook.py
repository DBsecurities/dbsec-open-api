"""호가조회 (HOGA) — standalone 예제.

그룹    : 국내선물옵션시세
엔드포인트: POST /api/v1/quote/kr-futureoption/inquiry/orderbook
TPS     : 5
가이드  : https://openapi.dbsec.co.kr/apiservice?group_id=80d95623-7135-481b-b109-d7370f1a261b&api_id=0ecec614-4830-4a7c-a0a0-7ba65cb54f3d

국내선물옵션 호가 조회 API입니다.

토큰은 examples/dbsec_helper.py 가 자동 발급/캐싱합니다.

실행:
    # examples/ 폴더에서 실행하는 경우:
    python kr_futopt_quote/kr_futopt_inquire_orderbook.py
    # examples/kr_futopt_quote/ 폴더에서 실행하는 경우:
    python kr_futopt_inquire_orderbook.py

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
    url="/api/v1/quote/kr-futureoption/inquiry/orderbook",
    body={
        "In": {
            "InputIscd1": "A0166000",  # 입력종목코드1 (str) - 종목코드 입력 ex. 005930
            "InputCondMrktDivCode": "F",  # 입력조건시장분류코드 (str) - F : 지수선물 JF : 주식선물 KF : 미니선물 CF : 상품선물 XF : 섹터선물 CM : 야간선물 O : 지수옵션 JO : 주식옵션 KO : 미니옵션 WO : K200위클리옵션 EU : 야간옵션 SO: 코스닥 150옵션
        },
    },
    label="호가조회",
)
print_response(resp, data)
