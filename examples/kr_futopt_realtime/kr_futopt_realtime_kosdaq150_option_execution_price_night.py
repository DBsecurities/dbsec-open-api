"""[실시간]KOSDAQ150옵션체결가(야간) [E20] — standalone WebSocket 예제.

그룹: 국내선물옵션시세(실시간)
프로토콜: WebSocket (실시간)
가이드: https://openapi.dbsec.co.kr/apiservice?group_id=548b70a6-24cc-4d9d-a7c7-90eb84a497f4&api_id=4d593338-5bdb-41f1-8b68-dfef0fd3cea6

KOSDAQ150옵션체결가(야간) API입니다.

토큰은 examples/dbsec_helper.py 가 자동 확보합니다.
필요한 외부 패키지: requests, pyyaml, websockets

실행:
    # examples/ 폴더에서 실행하는 경우:
    python kr_futopt_realtime/kr_futopt_realtime_kosdaq150_option_execution_price_night.py
    # examples/kr_futopt_realtime/ 폴더에서 실행하는 경우:
    python kr_futopt_realtime_kosdaq150_option_execution_price_night.py

── 응답 파라미터 (Out) ─ OUT_BEGIN ──────────────────────
  [TR E20]
    TotalBidprsqn  (문자)  총 매수호가 잔량
    TotalAskprsqn  (문자)  총 매도호가 잔량
    TotalBidpcsnu  (문자)  총 매수호가 건수
    TotalAskpcsnu  (문자)  총 매도호가 건수
    RgbfAntcctrtclr  (문자)  색참조(+상승, -하락)
    RgbfAntcctrt  (문자)  직전예상대비율
    RgbfAntcvrssclr  (문자)  색참조(+상승, -하락)
    RgbfAntcvrss  (문자)  직전예상대비
    RgbfAntcvrsssign  (문자)  직전예상대비부호
    RgbfAntcsdprclr  (문자)  색참조(+상승, -하락)
    RgbfAntcsdpr  (문자)  전예상기준가
    AsprRaisesign  (문자)  호가상향부호
    CntgPrgs  (문자)  체결틱추이
    DprtClr  (문자)  색참조(+상승, -하락)
    Dprt  (문자)  괴리율
    EsdgClr  (문자)  색참조(+상승, -하락)
    Esdg  (문자)  괴리도
    TimeWrth  (문자)  시간가치
    IntsWrth  (문자)  내재가치
    OtstStplqtyreficclr  (문자)  색참조(+상승, -하락)
    OtstStplqtyrefic  (문자)  미결제약정수량직전증감
    AntcNmixclscode  (문자)  예상지수구분코드
    DynmcLwlmtprc  (문자)  실시간하한
    DynmcUplmtprc  (문자)  실시간상한가
    OtstStplqtyicdcclr  (문자)  색참조(+상승, -하락)
    OtstStplqtyicdc  (문자)  미결제 약정 수량 증감
    IntsVltlbidp  (문자)  내재변동성_매수호가
    IntsVltlaskp  (문자)  내재변동성_매도호가
    IntsVltlprpr  (문자)  내재변동성_현재가
    Thpr  (문자)  이론가
    Rho  (문자)  로
    Theta  (문자)  세타
    Vega  (문자)  베가
    Gama  (문자)  감마
    Delta  (문자)  델타
    OtstStplqty  (문자)  미결제 약정 수량
    Bidp1Clr  (문자)  색참조(+상승, -하락)
    Bidp1  (문자)  매수호가1
    Askp1Clr  (문자)  색참조(+상승, -하락)
    Askp1  (문자)  매도호가1
    LwprClr  (문자)  색참조(+상승, -하락)
    Lwpr  (문자)  저가
    HgprClr  (문자)  색참조(+상승, -하락)
    Hgpr  (문자)  고가
    OprcClr  (문자)  색참조(+상승, -하락)
    Oprc  (문자)  시가
    AcmlTrpbmn  (문자)  누적 거래 대금
    AcmlVol  (문자)  누적 거래량
    CntgClscode  (문자)  체결 구분 코드
    CntgVolclr  (문자)  색참조(+상승, -하락)
    CntgVol  (문자)  체결 거래량
    PrdyCtrtclr  (문자)  색참조(+상승, -하락)
    PrdyCtrt  (문자)  전일 대비율
    PrdyVrssclr  (문자)  색참조(+상승, -하락)
    PrdyVrss  (문자)  전일 대비
    PrdyVrsssign  (문자)  전일 대비 부호
    PrprClr  (문자)  색참조(+상승, -하락)
    Prpr  (문자)  현재가
    BsopHour  (문자)  체결 시간
    BsopDate  (문자)  실시간일자
    ShrnIscd  (문자)  종목 코드

  공통: rsp_cd  응답코드  ·  rsp_msg  응답메시지
── OUT_END ──────────────────────────────────────────────
"""


import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from dbsec_helper import ws_subscribe, run_ws

run_ws(ws_subscribe(
    tr_type="1",  # 등록 종류 (1=시세구독 2=해제 3=계좌등록): 시세구독
    tr_cd="E20",  # 거래코드 (str) - TR코드입력: E20
    tr_key="",  # 종목코드 (str) - KOSDAQ150옵션(야간): EQ ※ 종목분류코드 + 지수옵션종목코드 입력
    group_slug="kr_futopt_realtime",
))
