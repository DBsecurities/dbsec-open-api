"""[실시간]일반채권체결 [B00] — standalone WebSocket 예제.

그룹: 장내채권시세(실시간)
프로토콜: WebSocket (실시간)
가이드: https://openapi.dbsec.co.kr/apiservice?group_id=9d49d2cf-5ec2-49f4-b032-e5ea0bdb50d6&api_id=06f92550-04ce-4574-8278-90389ea1fa84

일반채권 실시간 체결가 API 입니다.

토큰은 examples/dbsec_helper.py 가 자동 확보합니다.
필요한 외부 패키지: requests, pyyaml, websockets

실행:
    # examples/ 폴더에서 실행하는 경우:
    python bond_realtime/bond_realtime_normal_execution.py
    # examples/bond_realtime/ 폴더에서 실행하는 경우:
    python bond_realtime_normal_execution.py

── 응답 파라미터 (Out) ─ OUT_BEGIN ──────────────────────
  [TR B00]
    BondIsnm  (문자)  채권 종목명
    StndIscd  (문자)  표준 종목코드
    BsopDate  (문자)  실시간일자
    CntgHour  (문자)  체결 시간
    prpr  (문자)  현재가
    PrprClr  (문자)  색참조(+상승, -하락)
    PrdyVrsssign  (문자)  전일 대비 부호
    PrdyVrss  (문자)  전일 대비
    PrdyVrssclr  (문자)  색참조(+상승, -하락)
    PrdyCtrt  (문자)  전일 대비율
    PrdyCtrtclr  (문자)  색참조(+상승, -하락)
    CntgVol  (문자)  체결 수량
    AcmlVol  (문자)  누적 거래량
    AcmlTrpbmn  (문자)  누적거래대금
    oprc  (문자)  시가
    OprcClr  (문자)  색참조(+상승, -하락)
    hgpr  (문자)  최고가
    HgprClr  (문자)  색참조(+상승, -하락)
    lwpr  (문자)  최저가
    LwprClr  (문자)  색참조(+상승, -하락)
    BondCntgert  (문자)  채권 체결 수익률
    OprcErt  (문자)  시가 수익률
    HgprErt  (문자)  최고가 수익률
    LwprErt  (문자)  최저가 수익률
    CntgTypeclscode  (문자)  체결 유형 코드
    askp1  (문자)  매도호가1
    Askp1Clr  (문자)  색참조(+상승, -하락)
    bidp1  (문자)  매수호가1
    Bidp1Clr  (문자)  색참조(+상승, -하락)

  공통: rsp_cd  응답코드  ·  rsp_msg  응답메시지
── OUT_END ──────────────────────────────────────────────
"""


import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from dbsec_helper import ws_subscribe, run_ws

run_ws(ws_subscribe(
    tr_type="1",  # 등록 종류 (1=시세구독 2=해제 3=계좌등록): 시세구독
    tr_cd="B00",  # 거래코드 (str) - TR코드입력: B00
    tr_key="",  # 종목코드 (str) - 채권 종목코드 입력 일반채권: "B " + "채권종목코드" 소액채권: "SB + "채권종목코드" ex. "B KR6095231F25"
    group_slug="bond_realtime",
))
