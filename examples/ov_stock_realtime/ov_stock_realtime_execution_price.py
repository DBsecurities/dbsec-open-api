"""[실시간]해외주식 체결가 [V60] — standalone WebSocket 예제.

그룹: 해외주식시세(실시간)
프로토콜: WebSocket (실시간)
가이드: https://openapi.dbsec.co.kr/apiservice?group_id=68dccbef-704a-4ebc-86ac-e44056c5687b&api_id=bb2ec432-194d-49dc-819b-763244cc6efa

해외주식(미국) 실시간 체결가 API 입니다. ※ 해외주식(미국) 무료실시간시세 신청을 하지 않을 경우 실시간 시세를 수신 하실 수 없습니다. (V10,V11 지연시세는 별도 신청없이 사용 가능하십니다.) ※ 실시간무료시세(0분) 신청방법 HTS : [7325] 해외주식 실시간 시세 신청 MTS : 해외주식 > 서비스신청 > 실시간시세신청 ※ 무료 실시간 시세는 전체 시세에 비해 50% 수준의 체결 데이터를 제공합니다. ※ 무료 실시간 시세 자동결제 신청 시 당월 거래가 없거나 말일에 보유한 미국...

토큰은 examples/dbsec_helper.py 가 자동 확보합니다.
필요한 외부 패키지: requests, pyyaml, websockets

실행:
    # examples/ 폴더에서 실행하는 경우:
    python ov_stock_realtime/ov_stock_realtime_execution_price.py
    # examples/ov_stock_realtime/ 폴더에서 실행하는 경우:
    python ov_stock_realtime_execution_price.py

── 응답 파라미터 (Out) ─ OUT_BEGIN ──────────────────────
  [TR V60]
    RealYn  (문자)  실시간여부(0:지연, 1:실시간)
    symbol  (문자)  거래소구분(2)+종목코드(16)
    busidate  (문자)  현지영업일자
    locdate  (문자)  현지일자
    loctime  (문자)  현지시간
    kordate  (문자)  한국일자
    kortime  (문자)  한국시간
    open  (문자)  시가
    OpenClr  (문자)  색참조(+상승, -하락)
    high  (문자)  고가
    HighClr  (문자)  색참조(+상승, -하락)
    low  (문자)  저가
    LowClr  (문자)  색참조(+상승, -하락)
    last  (문자)  현재가
    LastClr  (문자)  색참조(+상승, -하락)
    sign  (문자)  대비부호
    diff  (문자)  전일대비
    DiffClr  (문자)  색참조(+상승, -하락)
    rate  (문자)  등락율
    RateClr  (문자)  색참조(+상승, -하락)
    bid  (문자)  매수호가
    BidClr  (문자)  색참조(+상승, -하락)
    bidsize  (문자)  매수잔량
    ask  (문자)  매도호가
    AskClr  (문자)  색참조(+상승, -하락)
    asksize  (문자)  매도잔량
    exevol  (문자)  체결량
    ExevolClr  (문자)  색참조(+상승, -하락)
    volume  (문자)  누적거래량
    amount  (문자)  누적거래대금
    SessionId  (문자)  장구분 (0:장중
    BidExevolsum  (문자)  매수누적체결량
    AskExevolsum  (문자)  매도누적체결량
    rltv  (문자)  체결강도
    RltvClr  (문자)  색참조(+상승, -하락)
    clos  (문자)  기준가

  공통: rsp_cd  응답코드  ·  rsp_msg  응답메시지
── OUT_END ──────────────────────────────────────────────
"""


import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from dbsec_helper import ws_subscribe, run_ws

run_ws(ws_subscribe(
    tr_type="1",  # 등록 종류 (1=시세구독 2=해제 3=계좌등록): 시세구독
    tr_cd="V60",  # 거래코드 (str) - TR코드입력: V60
    tr_key="",  # 종목코드 (str) - 뉴욕거래소 주식/ETF: "FY" + "종목코드" 나스닥거래소 주식/ETF: "FN + "종목코드" 아멕스거래소 주식/ETF: "FA" + "종목코드"
    group_slug="ov_stock_realtime",
))
