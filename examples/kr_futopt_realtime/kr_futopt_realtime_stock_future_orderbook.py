"""[실시간]주식선물호가 [F21] — standalone WebSocket 예제.

그룹: 국내선물옵션시세(실시간)
프로토콜: WebSocket (실시간)
가이드: https://openapi.dbsec.co.kr/apiservice?group_id=548b70a6-24cc-4d9d-a7c7-90eb84a497f4&api_id=74f2800a-fbd1-4b2d-98c6-bcc86c84e334

주식선물 실시간 호가 API 입니다.

토큰은 examples/dbsec_helper.py 가 자동 확보합니다.
필요한 외부 패키지: requests, pyyaml, websockets

실행:
    # examples/ 폴더에서 실행하는 경우:
    python kr_futopt_realtime/kr_futopt_realtime_stock_future_orderbook.py
    # examples/kr_futopt_realtime/ 폴더에서 실행하는 경우:
    python kr_futopt_realtime_stock_future_orderbook.py

── 응답 파라미터 (Out) ─ OUT_BEGIN ──────────────────────
  [TR F21]
    ShrnIscd  (문자)  종목코드
    BsopHour  (문자)  호가시간
    Askp1  (문자)  1매도호가
    Askp1Clr  (문자)  색참조(+상승, -하락)
    Askp2  (문자)  2매도호가
    Askp2Clr  (문자)  색참조(+상승, -하락)
    Askp3  (문자)  3매도호가
    Askp3Clr  (문자)  색참조(+상승, -하락)
    Askp4  (문자)  4매도호가
    Askp4Clr  (문자)  색참조(+상승, -하락)
    Askp5  (문자)  5매도호가
    Askp5Clr  (문자)  색참조(+상승, -하락)
    Askp6  (문자)  6매도호가
    Askp6Clr  (문자)  색참조(+상승, -하락)
    Askp7  (문자)  7매도호가
    Askp7Clr  (문자)  색참조(+상승, -하락)
    Askp8  (문자)  8매도호가
    Askp8Clr  (문자)  색참조(+상승, -하락)
    Askp9  (문자)  9매도호가
    Askp9Clr  (문자)  색참조(+상승, -하락)
    Askp10  (문자)  10매도호가
    Askp10Clr  (문자)  색참조(+상승, -하락)
    Bidp1  (문자)  1매수호가
    Bidp1Clr  (문자)  색참조(+상승, -하락)
    Bidp2  (문자)  2매수호가
    Bidp2Clr  (문자)  색참조(+상승, -하락)
    Bidp3  (문자)  3매수호가
    Bidp3Clr  (문자)  색참조(+상승, -하락)
    Bidp4  (문자)  4매수호가
    Bidp4Clr  (문자)  색참조(+상승, -하락)
    Bidp5  (문자)  5매수호가
    Bidp5Clr  (문자)  색참조(+상승, -하락)
    Bidp6  (문자)  6매수호가
    Bidp6Clr  (문자)  색참조(+상승, -하락)
    Bidp7  (문자)  7매수호가
    Bidp7Clr  (문자)  색참조(+상승, -하락)
    Bidp8  (문자)  8매수호가
    Bidp8Clr  (문자)  색참조(+상승, -하락)
    Bidp9  (문자)  9매수호가
    Bidp9Clr  (문자)  색참조(+상승, -하락)
    Bidp10  (문자)  10매수호가
    Bidp10Clr  (문자)  색참조(+상승, -하락)
    AskpRsqn1  (문자)  1매도호가 잔량
    AskpRsqn2  (문자)  2매도호가 잔량
    AskpRsqn3  (문자)  3매도호가 잔량
    AskpRsqn4  (문자)  4매도호가 잔량
    AskpRsqn5  (문자)  5매도호가 잔량
    AskpRsqn6  (문자)  6매도호가 잔량
    AskpRsqn7  (문자)  7매도호가 잔량
    AskpRsqn8  (문자)  8매도호가 잔량
    AskpRsqn9  (문자)  9매도호가 잔량
    AskpRsqn10  (문자)  10매도호가 잔량
    BidpRsqn1  (문자)  1매수호가 잔량
    BidpRsqn2  (문자)  2매수호가 잔량
    BidpRsqn3  (문자)  3매수호가 잔량
    BidpRsqn4  (문자)  4매수호가 잔량
    BidpRsqn5  (문자)  5매수호가 잔량
    BidpRsqn6  (문자)  6매수호가 잔량
    BidpRsqn7  (문자)  7매수호가 잔량
    BidpRsqn8  (문자)  8매수호가 잔량
    BidpRsqn9  (문자)  9매수호가 잔량
    BidpRsqn10  (문자)  10매수호가 잔량
    AskpCsnu1  (문자)  1매도호가 건수
    AskpCsnu2  (문자)  2매도호가 건수
    AskpCsnu3  (문자)  3매도호가 건수
    AskpCsnu4  (문자)  4매도호가 건수
    AskpCsnu5  (문자)  5매도호가 건수
    AskpCsnu6  (문자)  6매도호가 건수
    AskpCsnu7  (문자)  7매도호가 건수
    AskpCsnu8  (문자)  8매도호가 건수
    AskpCsnu9  (문자)  9매도호가 건수
    AskpCsnu10  (문자)  10매도호가 건수
    BidpCsnu1  (문자)  1매수호가 건수
    BidpCsnu2  (문자)  2매수호가 건수
    BidpCsnu3  (문자)  3매수호가 건수
    BidpCsnu4  (문자)  4매수호가 건수
    BidpCsnu5  (문자)  5매수호가 건수
    BidpCsnu6  (문자)  6매수호가 건수
    BidpCsnu7  (문자)  7매수호가 건수
    BidpCsnu8  (문자)  8매수호가 건수
    BidpCsnu9  (문자)  9매수호가 건수
    BidpCsnu10  (문자)  10매수호가 건수
    TotalAskpcsnu  (문자)  총 매도호가 건수
    TotalBidpcsnu  (문자)  총 매수호가 건수
    TotalAskprsqn  (문자)  총 매도호가 잔량
    TotalBidprsqn  (문자)  총 매수호가 잔량
    AntcCnpr  (문자)  예상 체결 가격
    AntcCnprclr  (문자)  색참조(+상승, -하락)
    AntcClscode  (문자)  예상구분코드

  공통: rsp_cd  응답코드  ·  rsp_msg  응답메시지
── OUT_END ──────────────────────────────────────────────
"""


import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from dbsec_helper import ws_subscribe, run_ws

run_ws(ws_subscribe(
    tr_type="1",  # 등록 종류 (1=시세구독 2=해제 3=계좌등록): 시세구독
    tr_cd="F21",  # 거래코드 (str) - TR코드입력: F21
    tr_key="",  # 종목코드 (str) - 주식선물: JF ※ 종목분류코드 + 주식선물종목코드 입력
    group_slug="kr_futopt_realtime",
))
