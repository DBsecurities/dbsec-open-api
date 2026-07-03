"""[실시간]선물체결(야간) [F40] — standalone WebSocket 예제.

그룹: 국내선물옵션시세(실시간)
프로토콜: WebSocket (실시간)
가이드: https://openapi.dbsec.co.kr/apiservice?group_id=548b70a6-24cc-4d9d-a7c7-90eb84a497f4&api_id=bbf8d6a7-ddb3-43c7-bb42-f22a0ece2fa5

야간선물 실시간 체결가 API 입니다.

토큰은 examples/dbsec_helper.py 가 자동 확보합니다.
필요한 외부 패키지: requests, pyyaml, websockets

실행:
    # examples/ 폴더에서 실행하는 경우:
    python kr_futopt_realtime/kr_futopt_realtime_future_execution_night.py
    # examples/kr_futopt_realtime/ 폴더에서 실행하는 경우:
    python kr_futopt_realtime_future_execution_night.py

── 응답 파라미터 (Out) ─ OUT_BEGIN ──────────────────────
  [TR F40]
    BsopDate  (문자)  실시간일자
    BsopHour  (문자)  체결 시간
    ShrnIscd  (문자)  종목 코드
    prpr  (문자)  현재가
    PrprClr  (문자)  색참조(+상승, -하락)
    PrdyVrsssign  (문자)  전일 대비 부호
    PrdyVrss  (문자)  전일 대비
    PrdyVrssclr  (문자)  색참조(+상승, -하락)
    PrdyCtrt  (문자)  전일 대비율
    PrdyCtrtclr  (문자)  색참조(+상승, -하락)
    CntgVol  (문자)  체결량
    CntgVolclr  (문자)  색참조(+상승, -하락)
    AcmlVol  (문자)  누적 거래량
    AcmlTrpbmn  (문자)  누적 거래 대금
    oprc  (문자)  시가
    OprcClr  (문자)  색참조(+상승, -하락)
    hgpr  (문자)  고가
    HgprClr  (문자)  색참조(+상승, -하락)
    lwpr  (문자)  저가
    LwprClr  (문자)  색참조(+상승, -하락)
    OprcHour  (문자)  시가 시간
    OprcVrsssign  (문자)  시가 대비 부호
    OprcVrss  (문자)  시가 대비
    OprcVrssclr  (문자)  색참조(+상승, -하락)
    HgprHour  (문자)  고가 시간
    HgprVrsssign  (문자)  고가 대비 부호
    HgprVrss  (문자)  고가 대비
    HgprVrssclr  (문자)  색참조(+상승, -하락)
    LwprHour  (문자)  저가 시간
    LwprVrsssign  (문자)  저가 대비 부호
    LwprVrss  (문자)  저가 대비
    LwprVrssclr  (문자)  색참조(+상승, -하락)
    NmscFctnstplprc  (문자)  근월물 의제 약정가
    FmscFctnstplprc  (문자)  원월물 의제 약정가
    SpeadPrc  (문자)  스프레드
    OtstStplqty  (문자)  미결제 약정 수량
    OtstStplqtyicdc  (문자)  미결제 약정 수량 증감
    OtstStplqtyicdcclr  (문자)  색참조(+상승, -하락)
    OtstStplqtyrefic  (문자)  미결제 약정 직전 수량 증감
    OtstStplqtyreficclr  (문자)  색참조(+상승, -하락)
    thpr  (문자)  이론가
    ThprClr  (문자)  색참조(+상승, -하락)
    MrktBasis  (문자)  시장 BASIS
    MrktBasisclr  (문자)  색참조(+상승, -하락)
    TherBasis  (문자)  이론 BASIS
    TherBasisclr  (문자)  색참조(+상승, -하락)
    esdg  (문자)  괴리도
    EsdgClr  (문자)  색참조(+상승, -하락)
    dprt  (문자)  괴리율
    DprtClr  (문자)  색참조(+상승, -하락)
    ShnuRate  (문자)  매수비율
    ShnuRateclr  (문자)  색참조(+상승, -하락)
    cttr  (문자)  체결강도
    CttrClr  (문자)  색참조(+상승, -하락)
    askp1  (문자)  매도호가1
    Askp1Clr  (문자)  색참조(+상승, -하락)
    bidp1  (문자)  매수호가1
    Bidp1Clr  (문자)  색참조(+상승, -하락)
    AskpRsqn1  (문자)  매도호가 잔량
    BidpRsqn1  (문자)  매수호가 잔량
    SelnCntgcsnu  (문자)  매도 체결 건수
    ShnuCntgcsnu  (문자)  매수 체결 건수
    NtbyCntgcsnu  (문자)  순매수 체결 건수
    NtbyCntgcsnuclr  (문자)  색참조(+상승, -하락)
    SelnCntgsmtn  (문자)  매도 체결 합계
    ShnuCntgsmtn  (문자)  매수 체결 합계
    TotalAskprsqn  (문자)  총 매도호가 잔량
    TotalBidprsqn  (문자)  총 매수호가 잔량
    PrdyVrssvolrate  (문자)  전일 대비 거래량 비율
    PrdyVrssvolrateclr  (문자)  색참조(+상승, -하락)
    UnasPrc  (문자)  기초자산 가격
    UnasPrcclr  (문자)  색참조(+상승, -하락)
    UnasPrdyvrsssign  (문자)  기초자산 전일대비구분
    UnasPrdyvrss  (문자)  기초자산 전일 대비
    UnasPrdyvrssclr  (문자)  색참조(+상승, -하락)
    UnasPrdyctrt  (문자)  기초자산 전일 대비율
    UnasPrdyctrtclr  (문자)  색참조(+상승, -하락)
    CntgPrgs  (문자)  체결틱추이
    CntgClscode  (문자)  체결 구분 코드
    DynmcUplmtPrc  (문자)  실시간상한가
    DynmcLwlmtPrc  (문자)  실시간하한가
    AntcNmixClsCode  (문자)  예상체결구분코드

  공통: rsp_cd  응답코드  ·  rsp_msg  응답메시지
── OUT_END ──────────────────────────────────────────────
"""


import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from dbsec_helper import ws_subscribe, run_ws

run_ws(ws_subscribe(
    tr_type="1",  # 등록 종류 (1=시세구독 2=해제 3=계좌등록): 시세구독
    tr_cd="F40",  # 거래코드 (str) - TR코드입력: F40
    tr_key="",  # 종목코드 (str) - 야간선물: CM ※ 종목분류코드 + 야간선물종목코드 입력
    group_slug="kr_futopt_realtime",
))
