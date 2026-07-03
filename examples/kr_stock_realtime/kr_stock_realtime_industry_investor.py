"""[실시간]업종별투자자 [U05] — standalone WebSocket 예제.

그룹: 국내주식시세(실시간)
프로토콜: WebSocket (실시간)
가이드: https://openapi.dbsec.co.kr/apiservice?group_id=94b5fddc-b819-451b-9619-13ee42468798&api_id=73819a0e-7df0-4f15-b9f5-e8e3c945caf8

업종별 투자자 조회 API 입니다.

토큰은 examples/dbsec_helper.py 가 자동 확보합니다.
필요한 외부 패키지: requests, pyyaml, websockets

실행:
    # examples/ 폴더에서 실행하는 경우:
    python kr_stock_realtime/kr_stock_realtime_industry_investor.py
    # examples/kr_stock_realtime/ 폴더에서 실행하는 경우:
    python kr_stock_realtime_industry_investor.py

── 응답 파라미터 (Out) ─ OUT_BEGIN ──────────────────────
  [TR U05]
    BsopHour  (문자)  영업 시간
    BstpInvrcode  (문자)  업종 투자자 코드_업종3상품3
    PrsnSelnvol  (문자)  개인 매도 거래량
    PrsnShnuvol  (문자)  개인 매수 거래량
    PrsnSelntrpbmn  (문자)  개인 매도 거래대금
    PrsnShnutrpbmn  (문자)  개인 매수 거래대금
    FrgnRegselnvol  (문자)  등록외국인 매도 거래량
    FrgnRegshnuvol  (문자)  등록외국인 매수 거래량
    FrgnRegselntrpb  (문자)  등록외국인 매도 거래대금
    FrgnRegshnutrpb  (문자)  등록외국인 매수 거래대금
    FrgnNregselnvol  (문자)  비등록외국인 매도 거래량
    FrgnNregshnuvol  (문자)  비등록외국인 매수 거래량
    FrgnNregselntrpb  (문자)  비등록외국인 매도 거래대금
    FrgnNregshnutrpb  (문자)  비등록외국인 매수 거래대금
    FrgnSelnvol  (문자)  외국인 매도 거래량
    FrgnShnuvol  (문자)  외국인 매수 거래량
    FrgnSelntrpbmn  (문자)  외국인 매도 거래대금
    FrgnShnutrpbmn  (문자)  외국인 매수 거래대금
    OrgnSelnvol  (문자)  기관계 매도 거래량
    OrgnShnuvol  (문자)  기관계 매수 거래량
    OrgnSelntrpbmn  (문자)  기관계 매도 거래대금
    OrgnShnutrpbmn  (문자)  기관계 매수 거래대금
    ScrtSelnvol  (문자)  증권 매도 거래량
    ScrtShnuvol  (문자)  증권 매수 거래량
    ScrtSelntrpbmn  (문자)  증권 매도 거래대금
    ScrtShnutrpbmn  (문자)  증권 매수 거래대금
    IvtrSelnvol  (문자)  투신 매도 거래량
    IvtrShnuvol  (문자)  투신 매수 거래량
    IvtrSelntrpbmn  (문자)  투신 매도 거래대금
    IvtrShnutrpbmn  (문자)  투신 매수 거래대금
    BankSelnvol  (문자)  은행 매도 거래량
    BankShnuvol  (문자)  은행 매수 거래량
    BankSelntrpbmn  (문자)  은행 매도 거래대금
    BankShnutrpbmn  (문자)  은행 매수 거래대금
    InsuSelnvol  (문자)  보험 매도 거래량
    InsuShnuvol  (문자)  보험 매수 거래량
    InsuSelntrpbmn  (문자)  보험 매도 거래대금
    InsuShnutrpbmn  (문자)  보험 매수 거래대금
    MrbnSelnvol  (문자)  종금 매도 거래량
    MrbnShnuvol  (문자)  종금 매수 거래량
    MrbnSelntrpbmn  (문자)  종금 매도 거래대금
    MrbnShnutrpbmn  (문자)  종금 매수 거래대금
    FundSelnvol  (문자)  기금 매도 거래량
    FundShnuvol  (문자)  기금 매수 거래량
    FundSelntrpbmn  (문자)  기금 매도 거래대금
    FundShnutrpbmn  (문자)  기금 매수 거래대금
    PeFundselnvol  (문자)  사모펀드 매도 거래량
    PeFundshnuvol  (문자)  사모펀드 매수 거래량
    PeFundselntrpb  (문자)  사모펀드 매도 거래대금
    PeFundshnutrpb  (문자)  사모펀드 매수 거래대금
    EtcOrgtselnvol  (문자)  국가지방 매도거래량
    EtcOrgtshnuvol  (문자)  국가지방 매수거래량
    EtcOrgtselntrpb  (문자)  국가지방 매도 거래대금
    EtcOrgtshnutrpb  (문자)  국가지방 매수거래대금
    EtcCorpselnvol  (문자)  기타법인 매도 거래량
    EtcCorpshnuvol  (문자)  기타법인 매수 거래량
    EtcCorpselntrpb  (문자)  기타법인 매도 거래대금
    EtcCorpshnutrpb  (문자)  기타법인 매수 거래대금
    WholSelnvol  (문자)  전체 매도 거래량
    WholShnuvol  (문자)  전체 매수 거래량
    WholSelntrpbmn  (문자)  전체 매도 거래대금
    WholShnutrpbmn  (문자)  전체 매수 거래대금
    PrsnNtbyvol  (문자)  개인 순매수 거래량
    PrsnNtbyvolclr  (문자)  색참조(+상승, -하락)
    PrsnNtbytrpb  (문자)  개인 순매수 거래대금
    PrsnNtbytrpbclr  (문자)  색참조(+상승, -하락)
    FrgnRegntbyvol  (문자)  등록외국인 순매수 거래량
    FrgnRegntbyvolclr  (문자)  색참조(+상승, -하락)
    FrgnRegntbytrpb  (문자)  등록외국인 순매수 거래대금
    FrgnRegntbytrpbclr  (문자)  색참조(+상승, -하락)
    FrgnNregntbyvol  (문자)  비등록외국인 순매수 거래량
    FrgnNregntbyvolclr  (문자)  색참조(+상승, -하락)
    FrgnNregntbytrpb  (문자)  비등록외국인 순매수 거래대금
    FrgnNregntbytrpbclr  (문자)  색참조(+상승, -하락)
    FrgnNtbyvol  (문자)  외국인 순매수 거래량
    FrgnNtbyvolclr  (문자)  색참조(+상승, -하락)
    FrgnNtbytrpbmn  (문자)  외국인 순매수 거래대금
    FrgnNtbytrpbmnclr  (문자)  색참조(+상승, -하락)
    OrgnNtbyvol  (문자)  기관계 순매수 거래량
    OrgnNtbyvolclr  (문자)  색참조(+상승, -하락)
    OrgnNtbytrpbmn  (문자)  기관계 순매수 거래대금
    OrgnNtbytrpbmnclr  (문자)  색참조(+상승, -하락)
    ScrtNtbyvol  (문자)  증권 순매수 거래량
    ScrtNtbyvolclr  (문자)  색참조(+상승, -하락)
    ScrtNtbytrpbmn  (문자)  증권 순매수 거래대금
    ScrtNtbytrpbmnclr  (문자)  색참조(+상승, -하락)
    IvtrNtbyvol  (문자)  투신 순매수 거래량
    IvtrNtbyvolclr  (문자)  색참조(+상승, -하락)
    IvtrNtbytrpbmn  (문자)  투신 순매수 거래대금
    IvtrNtbytrpbmnclr  (문자)  색참조(+상승, -하락)
    BankNtbyvol  (문자)  은행 순매수 거래량
    BankNtbyvolclr  (문자)  색참조(+상승, -하락)
    BankNtbytrpbmn  (문자)  은행 순매수 거래대금
    BankNtbytrpbmnclr  (문자)  색참조(+상승, -하락)
    InsuNtbyvol  (문자)  보험 순매수 거래량
    InsuNtbyvolclr  (문자)  색참조(+상승, -하락)
    InsuNtbytrpbmn  (문자)  보험 순매수 거래대금
    InsuNtbytrpbmnclr  (문자)  색참조(+상승, -하락)
    MrbnNtbyvol  (문자)  종금 순매수 거래량
    MrbnNtbyvolclr  (문자)  색참조(+상승, -하락)
    MrbnNtbytrpbmn  (문자)  종금 순매수 거래대금
    MrbnNtbytrpbmnclr  (문자)  색참조(+상승, -하락)
    FundNtbyvol  (문자)  기금 순매수 거래량
    FundNtbyvolclr  (문자)  색참조(+상승, -하락)
    FundNtbytrpbmn  (문자)  기금 순매수 거래대금
    FundNtbytrpbmnclr  (문자)  색참조(+상승, -하락)
    PeFundntbyvol  (문자)  사모펀드 순매수 거래량
    PeFundntbyvolclr  (문자)  색참조(+상승, -하락)
    PeFundntbytrpbmn  (문자)  사모펀드 순매수 거래대금
    PeFundntbytrpbmnclr  (문자)  색참조(+상승, -하락)
    EtcOrgtntbyvol  (문자)  국가지방 순매수 거래량
    EtcOrgtntbyvolclr  (문자)  색참조(+상승, -하락)
    EtcOrgtntbytrpb  (문자)  국가지방 순매수 거래대금
    EtcOrgtntbytrpbclr  (문자)  색참조(+상승, -하락)
    EtcCorpntbyvol  (문자)  기타법인 순매수 거래량
    EtcCorpntbyvolclr  (문자)  색참조(+상승, -하락)
    EtcCorpntbytrpb  (문자)  기타법인 순매수 거래대금
    EtcCorpntbytrpbclr  (문자)  색참조(+상승, -하락)
    WholNtbyvol  (문자)  전체 순매수 거래량
    WholNtbyvolclr  (문자)  색참조(+상승, -하락)
    WholNtbytrpbmn  (문자)  전체 순매수 거래대금
    WholNtbytrpbmnclr  (문자)  색참조(+상승, -하락)

  공통: rsp_cd  응답코드  ·  rsp_msg  응답메시지
── OUT_END ──────────────────────────────────────────────
"""


import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from dbsec_helper import ws_subscribe, run_ws

run_ws(ws_subscribe(
    tr_type="1",  # 등록 종류 (1=시세구독 2=해제 3=계좌등록): 시세구독
    tr_cd="U05",  # 거래코드 (str) - TR코드입력: U05
    tr_key="",  # 종목코드 (str) - 1001KSP: KOSPI 2001KSQ: KOSDAQ 1001NXP: KOSPI (NXT) 2001NXQ: KOSDAQ (NXT) 1001UNP: KOSPI (통합) 2001UNQ: KOSDAQ (통합) 3001KSP: KOSPI200 F001K2I: 선물 OC01K2I: 콜옵션 OP01K2I: 풋옵션 S001999: 주식선물 미니선물: F009MKI 미니콜옵션: MC01MKI 미니풋옵션: MP01MKI F004VKI: 변동성 F002KQI: 코스닥150선물 WC01WKM: 위클리 (월) 콜 WP01WKM: 위클리 (월) 풋 WC01WKI: 위클리 (목) 콜 WP01WKI: 위클리 (목) 풋 F004VKI: 변동성 F005XA0: 에너지화학 F006XA1: 정보기술 F007XA2: 금융 F008XA3: 경기소비재
    group_slug="kr_stock_realtime",
))
