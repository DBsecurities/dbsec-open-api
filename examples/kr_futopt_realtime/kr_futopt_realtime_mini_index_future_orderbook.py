"""[실시간]미니지수선물호가 [F91] — standalone WebSocket 예제.

그룹: 국내선물옵션시세(실시간)
프로토콜: WebSocket (실시간)
가이드: https://openapi.dbsec.co.kr/apiservice?group_id=548b70a6-24cc-4d9d-a7c7-90eb84a497f4&api_id=777b955c-17b2-4700-94cd-46735463cffe

국내 미니지수선물 실시간 호가 API 입니다.

토큰은 examples/dbsec_helper.py 가 자동 확보합니다.
필요한 외부 패키지: requests, pyyaml, websockets

실행:
    # examples/ 폴더에서 실행하는 경우:
    python kr_futopt_realtime/kr_futopt_realtime_mini_index_future_orderbook.py
    # examples/kr_futopt_realtime/ 폴더에서 실행하는 경우:
    python kr_futopt_realtime_mini_index_future_orderbook.py

── 응답 파라미터 (Out) ─ OUT_BEGIN ──────────────────────
  [TR F91]
    BsopHour  (문자)  호가시간
    ShrnIscd  (문자)  종목코드
    askp1  (문자)  1매도호가
    Askp1Clr  (문자)  색참조(+상승, -하락)
    askp2  (문자)  2매도호가
    Askp2Clr  (문자)  색참조(+상승, -하락)
    askp3  (문자)  3매도호가
    Askp3Clr  (문자)  색참조(+상승, -하락)
    askp4  (문자)  4매도호가
    Askp4Clr  (문자)  색참조(+상승, -하락)
    askp5  (문자)  5매도호가
    Askp5Clr  (문자)  색참조(+상승, -하락)
    bidp1  (문자)  1매수호가
    Bidp1Clr  (문자)  색참조(+상승, -하락)
    bidp2  (문자)  2매수호가
    Bidp2Clr  (문자)  색참조(+상승, -하락)
    bidp3  (문자)  3매수호가
    Bidp3Clr  (문자)  색참조(+상승, -하락)
    bidp4  (문자)  4매수호가
    Bidp4Clr  (문자)  색참조(+상승, -하락)
    bidp5  (문자)  5매수호가
    Bidp5Clr  (문자)  색참조(+상승, -하락)
    AskpCsnu1  (문자)  1매도호가 건수
    AskpCsnu2  (문자)  2매도호가 건수
    AskpCsnu3  (문자)  3매도호가 건수
    AskpCsnu4  (문자)  4매도호가 건수
    AskpCsnu5  (문자)  5매도호가 건수
    BidpCsnu1  (문자)  1매수호가 건수
    BidpCsnu2  (문자)  2매수호가 건수
    BidpCsnu3  (문자)  3매수호가 건수
    BidpCsnu4  (문자)  4매수호가 건수
    BidpCsnu5  (문자)  5매수호가 건수
    AskpRsqn1  (문자)  1매도호가 잔량
    AskpRsqn2  (문자)  2매도호가 잔량
    AskpRsqn3  (문자)  3매도호가 잔량
    AskpRsqn4  (문자)  4매도호가 잔량
    AskpRsqn5  (문자)  5매도호가 잔량
    BidpRsqn1  (문자)  1매수호가 잔량
    BidpRsqn2  (문자)  2매수호가 잔량
    BidpRsqn3  (문자)  3매수호가 잔량
    BidpRsqn4  (문자)  4매수호가 잔량
    BidpRsqn5  (문자)  5매수호가 잔량
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
    tr_cd="F91",  # 거래코드 (str) - TR코드입력: F91
    tr_key="",  # 종목코드 (str) - 미니지수선물: KF ※ 종목분류코드 + 미니지수선물종목코드 입력
    group_slug="kr_futopt_realtime",
))
