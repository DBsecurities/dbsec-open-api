"""[실시간]섹터지수선물체결 [F70] — standalone WebSocket 예제.

그룹: 국내선물옵션시세(실시간)
프로토콜: WebSocket (실시간)
가이드: https://openapi.dbsec.co.kr/apiservice?group_id=548b70a6-24cc-4d9d-a7c7-90eb84a497f4&api_id=e0dea90d-2247-4e92-843c-0d27592a7a93

섹터지수선물 실시간 체결가 API 입니다.

토큰은 examples/dbsec_helper.py 가 자동 확보합니다.
필요한 외부 패키지: requests, pyyaml, websockets

실행:
    # examples/ 폴더에서 실행하는 경우:
    python kr_futopt_realtime/kr_futopt_realtime_sector_index_future_execution.py
    # examples/kr_futopt_realtime/ 폴더에서 실행하는 경우:
    python kr_futopt_realtime_sector_index_future_execution.py

── 응답 파라미터 (Out) ─ OUT_BEGIN ──────────────────────
  [TR F70]
    ShrnIscd  (문자)  종목 코드
    BsopDate  (문자)  일자
    BsopHour  (문자)  체결 시간
    Prpr  (문자)  현재가
    PrprClr  (문자)  색참조(+상승, -하락)
    PrdyVrsssign  (문자)  전일 대비 부호
    PrdyVrss  (문자)  전일 대비
    PrdyVrssclr  (문자)  색참조(+상승, -하락)
    PrdyCtrt  (문자)  전일 대비율
    PrdyCtrtclr  (문자)  색참조(+상승, -하락)
    CntgVol  (문자)  체결량
    CntgVolclr  (문자)  색참조(+상승, -하락)
    CntgClscode  (문자)  체결 구분 코드
    AcmlVol  (문자)  누적 거래량
    AcmlTrpbmn  (문자)  누적 거래 대금
    Oprc  (문자)  시가
    OprcClr  (문자)  색참조(+상승, -하락)
    Hgpr  (문자)  고가
    HgprClr  (문자)  색참조(+상승, -하락)
    Lwpr  (문자)  저가
    LwprClr  (문자)  색참조(+상승, -하락)
    Askp1  (문자)  매도호가1
    Askp1Clr  (문자)  색참조(+상승, -하락)
    Bidp1  (문자)  매수호가1
    Bidp1Clr  (문자)  색참조(+상승, -하락)
    OtstStplqty  (문자)  미결제 약정 수량
    NmscFctnstplprc  (문자)  근월물 의제 약정가
    FmscFctnstplprc  (문자)  원월물 의제 약정가
    FctnStplprc  (문자)  의제 약정가
    NmscAcmlstplqty  (문자)  근월물 누적 약정 수량
    NmscAcmlstplpbmn  (문자)  근월물 누적 약정 대금
    FmscAcmlstplqty  (문자)  원월물 누적 약정 수량
    FmscAcmlstplpbmn  (문자)  원월물 누적 약정 대금
    MrktBasis  (문자)  시장 BASIS
    MrktBasisclr  (문자)  색참조(+상승, -하락)
    Thpr  (문자)  이론가
    OtstStplqtyicdc  (문자)  미결제 약정 수량 증감
    OtstStplqtyicdcclr  (문자)  색참조(+상승, -하락)
    DynmcUplmtprc  (문자)  실시간상한가
    DynmcLwlmtprc  (문자)  실시간하한가
    AntcNmixclscode  (문자)  예상체결구분코드
    OtstStplqtyrefic  (문자)  미결제약정수량직전증감
    OtstStplqtyreficclr  (문자)  색참조(+상승, -하락)
    TherBasis  (문자)  이론BASIS
    TherBasisclr  (문자)  색참조(+상승, -하락)
    Esdg  (문자)  괴리도
    EsdgClr  (문자)  색참조(+상승, -하락)
    Dprt  (문자)  괴리율
    DprtClr  (문자)  색참조(+상승, -하락)
    CntgPrgs  (문자)  체결틱추이
    AsprRaisesign  (문자)  호가상향부호
    RgbfAntcsdpr  (문자)  전예상기준가
    RgbfAntcsdprclr  (문자)  색참조(+상승, -하락)
    RgbfAntcvrsssign  (문자)  직전예상대비부호
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
    tr_cd="F70",  # 거래코드 (str) - TR코드입력: F70
    tr_key="",  # 종목코드 (str) - 섹터지수선물: XF ※ 종목분류코드 + 섹터지수선물종목코드 입력
    group_slug="kr_futopt_realtime",
))
