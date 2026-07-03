"""[실시간]ELW체결 [W00] — standalone WebSocket 예제.

그룹: 국내주식시세(실시간)
프로토콜: WebSocket (실시간)
가이드: https://openapi.dbsec.co.kr/apiservice?group_id=94b5fddc-b819-451b-9619-13ee42468798&api_id=cd318c5d-5bd3-4998-99a5-c74002e9caba

ELW 실시간 체결가 API 입니다.

토큰은 examples/dbsec_helper.py 가 자동 확보합니다.
필요한 외부 패키지: requests, pyyaml, websockets

실행:
    # examples/ 폴더에서 실행하는 경우:
    python kr_stock_realtime/kr_stock_realtime_elw_execution.py
    # examples/kr_stock_realtime/ 폴더에서 실행하는 경우:
    python kr_stock_realtime_elw_execution.py

── 응답 파라미터 (Out) ─ OUT_BEGIN ──────────────────────
  [TR W00]
    ShrnIscd  (문자)  종목 코드
    BsopDate  (문자)  실시간일자
    StckCntghour  (문자)  체결 시간
    HourClscode  (문자)  시간 구분 코드
    AntcNmixclscode  (문자)  예상 지수 구분 코드
    StckPrpr  (문자)  현재가
    StckPrprclr  (문자)  색참조(+상승, -하락)
    PrdyVrsssign  (문자)  전일 대비 부호
    PrdyVrss  (문자)  전일 대비
    PrdyVrssclr  (문자)  색참조(+상승, -하락)
    PrdyCtrt  (문자)  전일 대비율
    PrdyCtrtclr  (문자)  색참조(+상승, -하락)
    StckOprc  (문자)  시가
    StckOprcclr  (문자)  색참조(+상승, -하락)
    StckHgpr  (문자)  고가
    StckHgprclr  (문자)  색참조(+상승, -하락)
    StckLwpr  (문자)  저가
    StckLwprclr  (문자)  색참조(+상승, -하락)
    CntgClscode  (문자)  체결 구분 코드
    CntgVol  (문자)  채결 거래량
    CntgVolclr  (문자)  색참조(+상승, -하락)
    AcmlVol  (문자)  누적 거래량
    AcmlTrpbmn  (문자)  누적 거래 대금
    Askp1  (문자)  매도호가
    Askp1Clr  (문자)  색참조(+상승, -하락)
    Bidp1  (문자)  매수호가
    Bidp1Clr  (문자)  색참조(+상승, -하락)
    AskpRsqn1  (문자)  매도호가 잔량
    BidpRsqn1  (문자)  매수호가 잔량
    TotalAskprsqn  (문자)  총 매도호가 잔량
    TotalBidprsqn  (문자)  총 매수호가 잔량
    Tmvl  (문자)  시간가치
    Invl  (문자)  내재가치
    Prmm  (문자)  프리미엄 값
    PrmmRate  (문자)  프리미엄 비율
    Prit  (문자)  패리티
    Gear  (문자)  기어링
    PrlsQryrrate  (문자)  순익 분기율
    IntsVltl  (문자)  내재 변동성
    Cfp  (문자)  자본지지점
    Lvrg  (문자)  레버리지
    Delta  (문자)  델타
    Gama  (문자)  감마
    Vega  (문자)  베가
    Theta  (문자)  세타
    Rho  (문자)  로
    Thpr  (문자)  이론가
    LpAskprsqn1  (문자)  LP 매도호가 잔량1
    LpBidprsqn1  (문자)  LP 매수호가 잔량1
    LpTotalaskprsqn  (문자)  LP 총 매도호가 잔량
    LpTotalbidprsqn  (문자)  LP 총 매수호가 잔량
    LpHvol  (문자)  LP 보유량
    LpHvolclr  (문자)  색참조(+상승, -하락)
    LpHldnrate  (문자)  LP 보유 비율
    LpHldnrateclr  (문자)  색참조(+상승, -하락)
    NewMkopclscode  (문자)  신 장운영 구분코드
    Rltv  (문자)  체결강도
    RltvClr  (문자)  색참조(+상승, -하락)
    WghnAvrgprpr  (문자)  가중평균가격
    CntgPrgs  (문자)  체결틱추이
    RgbfAntcsdpr  (문자)  직전예상기준가(현재가)
    RgbfAntcsdprclr  (문자)  색참조(+상승, -하락)
    RgbfAntcvrsssign  (문자)  직전예상부호
    RgbfAntcvrss  (문자)  직전예상대비
    RgbfAntcvrssclr  (문자)  색참조(+상승, -하락)
    RgbfAntcctrt  (문자)  직전예상대비율
    RgbfAntcctrtclr  (문자)  색참조(+상승, -하락)

  공통: rsp_cd  응답코드  ·  rsp_msg  응답메시지
── OUT_END ──────────────────────────────────────────────
"""


import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from dbsec_helper import ws_subscribe, run_ws

run_ws(ws_subscribe(
    tr_type="1",  # 등록 종류 (1=시세구독 2=해제 3=계좌등록): 시세구독
    tr_cd="W00",  # 거래코드 (str) - TR코드입력: W00
    tr_key="",  # 종목코드 (str) - ELW: W ※ 종목분류코드 + 주식종목코드 입력 ※ 종목분류코드는 두자리 입력이 필요하므로, W + " " (공백) 문자를 넣어 2바이트를 맞춰 입력 부탁드리겠습니다.
    group_slug="kr_stock_realtime",
))
