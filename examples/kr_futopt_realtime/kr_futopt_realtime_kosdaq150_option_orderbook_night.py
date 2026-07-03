"""[실시간]KOSDAQ150옵션호가(야간) [E21] — standalone WebSocket 예제.

그룹: 국내선물옵션시세(실시간)
프로토콜: WebSocket (실시간)
가이드: https://openapi.dbsec.co.kr/apiservice?group_id=548b70a6-24cc-4d9d-a7c7-90eb84a497f4&api_id=94a4a8ab-102e-4fd7-acd8-9032c1eab191

KOSDAQ150옵션호가(야간) API입니다.

토큰은 examples/dbsec_helper.py 가 자동 확보합니다.
필요한 외부 패키지: requests, pyyaml, websockets

실행:
    # examples/ 폴더에서 실행하는 경우:
    python kr_futopt_realtime/kr_futopt_realtime_kosdaq150_option_orderbook_night.py
    # examples/kr_futopt_realtime/ 폴더에서 실행하는 경우:
    python kr_futopt_realtime_kosdaq150_option_orderbook_night.py

── 응답 파라미터 (Out) ─ OUT_BEGIN ──────────────────────
  [TR E21]
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
    tr_cd="E21",  # 거래코드 (str) - TR코드입력: EQ
    tr_key="",  # 종목코드 (str) - KOSDAQ150옵션: EQ ※ 종목분류코드 + KOSDAQ150옵션 종목코드 입력
    group_slug="kr_futopt_realtime",
))
