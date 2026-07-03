"""[실시간]주식체결가 [S00] — standalone WebSocket 예제.

그룹: 국내주식시세(실시간)
프로토콜: WebSocket (실시간)
가이드: https://openapi.dbsec.co.kr/apiservice?group_id=94b5fddc-b819-451b-9619-13ee42468798&api_id=7c257cdc-5807-46ca-8d86-666a2bfd6798

국내주식 실시간 체결가 API 입니다.

토큰은 examples/dbsec_helper.py 가 자동 확보합니다.
필요한 외부 패키지: requests, pyyaml, websockets

실행:
    # examples/ 폴더에서 실행하는 경우:
    python kr_stock_realtime/kr_stock_realtime_execution_price.py
    # examples/kr_stock_realtime/ 폴더에서 실행하는 경우:
    python kr_stock_realtime_execution_price.py

── 응답 파라미터 (Out) ─ OUT_BEGIN ──────────────────────
  [TR S00]
    BsopDate  (문자)  실시간일자
    ShrnIscd  (문자)  종목코드
    StckCntghour  (문자)  체결시간
    HourClscode  (문자)  시간구분코드
    AntcNmixclscode  (문자)  예상지수구분코드 — 0:예상 1:정규
    StckPrpr  (문자)  현재가
    StckPrprclr  (문자)  색참조(+상승, -하락)
    PrdyVrsssign  (문자)  전일대비부호
    PrdyVrss  (문자)  전일대비
    PrdyVrssclr  (문자)  색참조(+상승, -하락)
    PrdyCtrt  (문자)  전일대비율
    PrdyCtrtclr  (문자)  색참조(+상승, -하락)
    StckOprc  (문자)  시가
    StckOprcclr  (문자)  색참조(+상승, -하락)
    StckHgpr  (문자)  고가
    StckHgprclr  (문자)  색참조(+상승, -하락)
    StckLwpr  (문자)  저가
    StckLwprclr  (문자)  색참조(+상승, -하락)
    StckSdpr  (문자)  기준가
    StckMxpr  (문자)  상한가
    StckMxprclr  (문자)  색참조(+상승, -하락)
    StckLlam  (문자)  하한가
    StckLlamclr  (문자)  색참조(+상승, -하락)
    CntgClscode  (문자)  체결구분코드
    CntgVol  (문자)  체결거래량
    CntgVolclr  (문자)  색참조(+상승, -하락)
    AcmlVol  (문자)  누적거래량
    AcmlTrpbmn  (문자)  누적거래대금
    askp1  (문자)  매도호가
    Askp1Clr  (문자)  색참조(+상승, -하락)
    bidp1  (문자)  매수호가
    Bidp1Clr  (문자)  색참조(+상승, -하락)
    AskpRsqn1  (문자)  매도호가잔량
    BidpRsqn1  (문자)  매수호가잔량
    TotalAskprsqn  (문자)  총매도호가잔량
    TotalBidprsqn  (문자)  총매수호가잔량
    TrhtYn  (문자)  거래정지 여부
    MangIssuyn  (문자)  관리종목 여부
    PrstClscode  (문자)  우선주 구분 코드
    WarnYn  (문자)  투자주의 여부
    NewMkopclscode  (문자)  신장운영구분코드
    RgbfCntgclscode  (문자)  직전체결구분코드
    rltv  (문자)  체결강도
    RltvClr  (문자)  색참조(+상승, -하락)
    SelnCntgcsnu  (문자)  매도체결건수
    ShnuCntgcsnu  (문자)  매수체결건수
    WghnAvrgprpr  (문자)  가중평균가격
    SelnCntgsmtn  (문자)  매도체결합계
    ShnuCntgsmtn  (문자)  매수체결합계
    CntgPrgs  (문자)  체결틱추이
    RgbfAntcsdpr  (문자)  직전예상기준가(현재가)
    RgbfAntcsdprclr  (문자)  색참조(+상승, -하락)
    RgbfAntcvrsssign  (문자)  직전예상부호
    RgbfAntcvrss  (문자)  직전예상대비
    RgbfAntcvrssclr  (문자)  색참조(+상승, -하락)
    RgbfAntcctrt  (문자)  직전예상대비율
    RgbfAntcctrtclr  (문자)  색참조(+상승, -하락)
    PrprCntgclscode  (문자)  현재가비교방식 체결구분코드
    PrprSelncntgsmtn  (문자)  현재가비교방식 매도체결합계
    PrprShnucntgsmtn  (문자)  현재가비교방식 매수체결합계
    PrprCttr  (문자)  현재가비교방식 체결강도
    PrprCttrclr  (문자)  색참조(+상승, -하락)
    ExmrClsCode  (문자)  거래소구분코드 — 1: KRX, 통합시세 2: NXT 거래소

  공통: rsp_cd  응답코드  ·  rsp_msg  응답메시지
── OUT_END ──────────────────────────────────────────────
"""


import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from dbsec_helper import ws_subscribe, run_ws

run_ws(ws_subscribe(
    tr_type="1",  # 등록 종류 (1=시세구독 2=해제 3=계좌등록): 시세구독
    tr_cd="S00",  # 거래코드 (str) - TR코드입력: S00
    tr_key="",  # 종목코드 (str) - [KRX] 주식&ETF:J ETN: EN ※ 종목분류코드 + 주식종목코드 입력 ※ 종목분류코드는 두자리 입력이 필요하므로, J + " " (공백) 문자를 넣어 2바이트를 맞춰 입력 부탁드리겠습니다. [NXT] NXT주식: NJ+ 종목코드 [통합시세] 통합시세 주식: UJ+ 종목코드 ※ KRX거래소 단독 상장 종목의 경우, 통합시세 코드가아닌 KRX 거래소 코드(J) 사용부탁드립니다
    group_slug="kr_stock_realtime",
))
