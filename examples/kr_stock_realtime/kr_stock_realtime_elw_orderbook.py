"""[실시간]ELW호가 [W01] — standalone WebSocket 예제.

그룹: 국내주식시세(실시간)
프로토콜: WebSocket (실시간)
가이드: https://openapi.dbsec.co.kr/apiservice?group_id=94b5fddc-b819-451b-9619-13ee42468798&api_id=f6d79404-3c1e-4f7f-b176-49b542477bf4

ELW 실시간 호가 API 입니다.

토큰은 examples/dbsec_helper.py 가 자동 확보합니다.
필요한 외부 패키지: requests, pyyaml, websockets

실행:
    # examples/ 폴더에서 실행하는 경우:
    python kr_stock_realtime/kr_stock_realtime_elw_orderbook.py
    # examples/kr_stock_realtime/ 폴더에서 실행하는 경우:
    python kr_stock_realtime_elw_orderbook.py

── 응답 파라미터 (Out) ─ OUT_BEGIN ──────────────────────
  [TR W01]
    ShrnIscd  (문자)  종목코드
    BsopHour  (문자)  호가시간
    HourClscode  (문자)  시간구분
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
    AskpRsqnicdc1  (문자)  1매도호가 잔량 증감
    AskpRsqnicdc1clr  (문자)  색참조(+상승, -하락)
    AskpRsqnicdc2  (문자)  2매도호가 잔량 증감
    AskpRsqnicdc2clr  (문자)  색참조(+상승, -하락)
    AskpRsqnicdc3  (문자)  3매도호가 잔량 증감
    AskpRsqnicdc3clr  (문자)  색참조(+상승, -하락)
    AskpRsqnicdc4  (문자)  4매도호가 잔량 증감
    AskpRsqnicdc4clr  (문자)  색참조(+상승, -하락)
    AskpRsqnicdc5  (문자)  5매도호가 잔량 증감
    AskpRsqnicdc5clr  (문자)  색참조(+상승, -하락)
    AskpRsqnicdc6  (문자)  6매도호가 잔량 증감
    AskpRsqnicdc6clr  (문자)  색참조(+상승, -하락)
    AskpRsqnicdc7  (문자)  7매도호가 잔량 증감
    AskpRsqnicdc7clr  (문자)  색참조(+상승, -하락)
    AskpRsqnicdc8  (문자)  8매도호가 잔량 증감
    AskpRsqnicdc8clr  (문자)  색참조(+상승, -하락)
    AskpRsqnicdc9  (문자)  9매도호가 잔량 증감
    AskpRsqnicdc9clr  (문자)  색참조(+상승, -하락)
    AskpRsqnicdc10  (문자)  10매도호가 잔량 증감
    AskpRsqnicdc10clr  (문자)  색참조(+상승, -하락)
    BidpRsqnicdc1  (문자)  1매수호가 잔량 증감
    BidpRsqnicdc1clr  (문자)  색참조(+상승, -하락)
    BidpRsqnicdc2  (문자)  2매수호가 잔량 증감
    BidpRsqnicdc2clr  (문자)  색참조(+상승, -하락)
    BidpRsqnicdc3  (문자)  3매수호가 잔량 증감
    BidpRsqnicdc3clr  (문자)  색참조(+상승, -하락)
    BidpRsqnicdc4  (문자)  4매수호가 잔량 증감
    BidpRsqnicdc4clr  (문자)  색참조(+상승, -하락)
    BidpRsqnicdc5  (문자)  5매수호가 잔량 증감
    BidpRsqnicdc5clr  (문자)  색참조(+상승, -하락)
    BidpRsqnicdc6  (문자)  6매수호가 잔량 증감
    BidpRsqnicdc6clr  (문자)  색참조(+상승, -하락)
    BidpRsqnicdc7  (문자)  7매수호가 잔량 증감
    BidpRsqnicdc7clr  (문자)  색참조(+상승, -하락)
    BidpRsqnicdc8  (문자)  8매수호가 잔량 증감
    BidpRsqnicdc8clr  (문자)  색참조(+상승, -하락)
    BidpRsqnicdc9  (문자)  9매수호가 잔량 증감
    BidpRsqnicdc9clr  (문자)  색참조(+상승, -하락)
    BidpRsqnicdc10  (문자)  10매수호가 잔량 증감
    BidpRsqnicdc10clr  (문자)  색참조(+상승, -하락)
    LpAskprsqn1  (문자)  LP 매도호가 잔량1
    LpAskprsqn2  (문자)  LP 매도호가 잔량2
    LpAskprsqn3  (문자)  LP 매도호가 잔량3
    LpAskprsqn4  (문자)  LP 매도호가 잔량4
    LpAskprsqn5  (문자)  LP 매도호가 잔량5
    LpAskprsqn6  (문자)  LP 매도호가 잔량6
    LpAskprsqn7  (문자)  LP 매도호가 잔량7
    LpAskprsqn8  (문자)  LP 매도호가 잔량8
    LpAskprsqn9  (문자)  LP 매도호가 잔량9
    LpAskprsqn10  (문자)  LP 매도호가 잔량10
    LpBidprsqn1  (문자)  LP 매수호가 잔량1
    LpBidprsqn2  (문자)  LP 매수호가 잔량2
    LpBidprsqn3  (문자)  LP 매수호가 잔량3
    LpBidprsqn4  (문자)  LP 매수호가 잔량4
    LpBidprsqn5  (문자)  LP 매수호가 잔량5
    LpBidprsqn6  (문자)  LP 매수호가 잔량6
    LpBidprsqn7  (문자)  LP 매수호가 잔량7
    LpBidprsqn8  (문자)  LP 매수호가 잔량8
    LpBidprsqn9  (문자)  LP 매수호가 잔량9
    LpBidprsqn10  (문자)  LP 매수호가 잔량10
    LpAskprsqnicdc1  (문자)  LP 매도호가 잔량 증감1
    LpAskprsqnicdc1clr  (문자)  색참조(+상승, -하락)
    LpAskprsqnicdc2  (문자)  LP 매도호가 잔량 증감2
    LpAskprsqnicdc2clr  (문자)  색참조(+상승, -하락)
    LpAskprsqnicdc3  (문자)  LP 매도호가 잔량 증감3
    LpAskprsqnicdc3clr  (문자)  색참조(+상승, -하락)
    LpAskprsqnicdc4  (문자)  LP 매도호가 잔량 증감4
    LpAskprsqnicdc4clr  (문자)  색참조(+상승, -하락)
    LpAskprsqnicdc5  (문자)  LP 매도호가 잔량 증감5
    LpAskprsqnicdc5clr  (문자)  색참조(+상승, -하락)
    LpAskprsqnicdc6  (문자)  LP 매도호가 잔량 증감6
    LpAskprsqnicdc6clr  (문자)  색참조(+상승, -하락)
    LpAskprsqnicdc7  (문자)  LP 매도호가 잔량 증감7
    LpAskprsqnicdc7clr  (문자)  색참조(+상승, -하락)
    LpAskprsqnicdc8  (문자)  LP 매도호가 잔량 증감8
    LpAskprsqnicdc8clr  (문자)  색참조(+상승, -하락)
    LpAskprsqnicdc9  (문자)  LP 매도호가 잔량 증감9
    LpAskprsqnicdc9clr  (문자)  색참조(+상승, -하락)
    LpAskprsqnicdc10  (문자)  LP 매도호가 잔량 증감10
    LpAskprsqnicdc10clr  (문자)  색참조(+상승, -하락)
    LpBidprsqnicdc1  (문자)  LP 매수호가 잔량 증감1
    LpBidprsqnicdc1clr  (문자)  색참조(+상승, -하락)
    LpBidprsqnicdc2  (문자)  LP 매수호가 잔량 증감2
    LpBidprsqnicdc2clr  (문자)  색참조(+상승, -하락)
    LpBidprsqnicdc3  (문자)  LP 매수호가 잔량 증감3
    LpBidprsqnicdc3clr  (문자)  색참조(+상승, -하락)
    LpBidprsqnicdc4  (문자)  LP 매수호가 잔량 증감4
    LpBidprsqnicdc4clr  (문자)  색참조(+상승, -하락)
    LpBidprsqnicdc5  (문자)  LP 매수호가 잔량 증감5
    LpBidprsqnicdc5clr  (문자)  색참조(+상승, -하락)
    LpBidprsqnicdc6  (문자)  LP 매수호가 잔량 증감6
    LpBidprsqnicdc6clr  (문자)  색참조(+상승, -하락)
    LpBidprsqnicdc7  (문자)  LP 매수호가 잔량 증감7
    LpBidprsqnicdc7clr  (문자)  색참조(+상승, -하락)
    LpBidprsqnicdc8  (문자)  LP 매수호가 잔량 증감8
    LpBidprsqnicdc8clr  (문자)  색참조(+상승, -하락)
    LpBidprsqnicdc9  (문자)  LP 매수호가 잔량 증감9
    LpBidprsqnicdc9clr  (문자)  색참조(+상승, -하락)
    LpBidprsqnicdc10  (문자)  LP 매수호가 잔량 증감10
    LpBidprsqnicdc10clr  (문자)  색참조(+상승, -하락)
    TotalAskprsqn  (문자)  총 매도호가 잔량
    TotalBidprsqn  (문자)  총 매수호가 잔량
    TotalAskprsqnicdc  (문자)  총 매도호가 잔량 증감
    TotalAskprsqnicdcclr  (문자)  색참조(+상승, -하락)
    TotalBidprsqnicdc  (문자)  총 매수호가 잔량 증감
    TotalBidprsqnicdcclr  (문자)  색참조(+상승, -하락)
    LpTotalaskprsqn  (문자)  LP 총 매도호가 잔량
    LpTotalbidprsqn  (문자)  LP 총 매수호가 잔량
    LpTotalaskrsqnicdc  (문자)  LP 총 매도호가 잔량 증감
    LpTotalaskrsqnicdcclr  (문자)  색참조(+상승, -하락)
    LpTotalbidrsqnicdc  (문자)  LP 총 매수호가 잔량 증감
    LpTotalbidrsqnicdcclr  (문자)  색참조(+상승, -하락)
    CnccAsprclscode  (문자)  동시 호가 구분 코드
    AntcCnpr  (문자)  예상 체결가
    AntcCnprclr  (문자)  색참조(+상승, -하락)
    AntcCnqn  (문자)  예상 체결량
    AcmlVol  (문자)  누적 거래량
    NewMkopclscode  (문자)  신장운영구분코드
    AntcIssyn  (문자)  예상활성여부

  공통: rsp_cd  응답코드  ·  rsp_msg  응답메시지
── OUT_END ──────────────────────────────────────────────
"""


import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from dbsec_helper import ws_subscribe, run_ws

run_ws(ws_subscribe(
    tr_type="1",  # 등록 종류 (1=시세구독 2=해제 3=계좌등록): 시세구독
    tr_cd="W01",  # 거래코드 (str) - TR코드입력: W01
    tr_key="",  # 종목코드 (str) - ELW: W ※ 종목분류코드 + 주식종목코드 입력 ※ 종목분류코드는 두자리 입력이 필요하므로, W + " " (공백) 문자를 넣어 2바이트를 맞춰 입력 부탁드리겠습니다.
    group_slug="kr_stock_realtime",
))
