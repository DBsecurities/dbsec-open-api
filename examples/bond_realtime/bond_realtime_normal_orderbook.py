"""[실시간]일반채권호가 [B01] — standalone WebSocket 예제.

그룹: 장내채권시세(실시간)
프로토콜: WebSocket (실시간)
가이드: https://openapi.dbsec.co.kr/apiservice?group_id=9d49d2cf-5ec2-49f4-b032-e5ea0bdb50d6&api_id=ec62334a-6150-4a29-89b0-193a2d8e35f4

일반채권 실시간 호가 API 입니다.

토큰은 examples/dbsec_helper.py 가 자동 확보합니다.
필요한 외부 패키지: requests, pyyaml, websockets

실행:
    # examples/ 폴더에서 실행하는 경우:
    python bond_realtime/bond_realtime_normal_orderbook.py
    # examples/bond_realtime/ 폴더에서 실행하는 경우:
    python bond_realtime_normal_orderbook.py

── 응답 파라미터 (Out) ─ OUT_BEGIN ──────────────────────
  [TR B01]
    CntgHour  (문자)  체결 시간
    StndIscd  (문자)  표준 종목코드
    askp1  (문자)  매도호가1
    Askp1Clr  (문자)  색참조(+상승, -하락)
    askp2  (문자)  매도호가2
    Askp2Clr  (문자)  색참조(+상승, -하락)
    askp3  (문자)  매도호가3
    Askp3Clr  (문자)  색참조(+상승, -하락)
    askp4  (문자)  매도호가4
    Askp4Clr  (문자)  색참조(+상승, -하락)
    askp5  (문자)  매도호가5
    Askp5Clr  (문자)  색참조(+상승, -하락)
    bidp1  (문자)  매수호가1
    Bidp1Clr  (문자)  색참조(+상승, -하락)
    bidp2  (문자)  매수호가2
    Bidp2Clr  (문자)  색참조(+상승, -하락)
    bidp3  (문자)  매수호가3
    Bidp3Clr  (문자)  색참조(+상승, -하락)
    bidp4  (문자)  매수호가4
    Bidp4Clr  (문자)  색참조(+상승, -하락)
    bidp5  (문자)  매수호가5
    Bidp5Clr  (문자)  색참조(+상승, -하락)
    AskpErt1  (문자)  매도호가 수익률1
    AskpErt2  (문자)  매도호가 수익률2
    AskpErt3  (문자)  매도호가 수익률3
    AskpErt4  (문자)  매도호가 수익률4
    AskpErt5  (문자)  매도호가 수익률5
    BidpErt1  (문자)  매수호가 수익률1
    BidpErt2  (문자)  매수호가 수익률2
    BidpErt3  (문자)  매수호가 수익률3
    BidpErt4  (문자)  매수호가 수익률4
    BidpErt5  (문자)  매수호가 수익률5
    AskpRsqn1  (문자)  매도호가 잔량1
    AskpRsqn2  (문자)  매도호가 잔량2
    AskpRsqn3  (문자)  매도호가 잔량3
    AskpRsqn4  (문자)  매도호가 잔량4
    AskpRsqn5  (문자)  매도호가 잔량5
    BidpRsqn1  (문자)  매수호가 잔량1
    BidpRsqn2  (문자)  매수호가 잔량2
    BidpRsqn3  (문자)  매수호가 잔량3
    BidpRsqn4  (문자)  매수호가 잔량4
    BidpRsqn5  (문자)  매수호가 잔량5
    TotalAskprsqn  (문자)  총 매도호가 잔량
    TotalBidprsqn  (문자)  총 매수호가 잔량
    SmamMrktinvlyn  (문자)  소액시장 참여 여부

  공통: rsp_cd  응답코드  ·  rsp_msg  응답메시지
── OUT_END ──────────────────────────────────────────────
"""


import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from dbsec_helper import ws_subscribe, run_ws

run_ws(ws_subscribe(
    tr_type="1",  # 등록 종류 (1=시세구독 2=해제 3=계좌등록): 시세구독
    tr_cd="B01",  # 거래코드 (str) - TR코드입력: B01
    tr_key="",  # 종목코드 (str) - 채권 종목코드 입력 일반채권: "B " + "채권종목코드" 소액채권: "SB + "채권종목코드" ex. "B KR6095231F25"
    group_slug="bond_realtime",
))
