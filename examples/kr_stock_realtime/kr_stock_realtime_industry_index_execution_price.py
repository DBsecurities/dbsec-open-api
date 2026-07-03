"""[실시간]업종지수체결가 [U00] — standalone WebSocket 예제.

그룹: 국내주식시세(실시간)
프로토콜: WebSocket (실시간)
가이드: https://openapi.dbsec.co.kr/apiservice?group_id=94b5fddc-b819-451b-9619-13ee42468798&api_id=831d29dc-d607-474a-b85a-5dd4fe1ab74d

업종지수 체결가 조회 API 입니다.

토큰은 examples/dbsec_helper.py 가 자동 확보합니다.
필요한 외부 패키지: requests, pyyaml, websockets

실행:
    # examples/ 폴더에서 실행하는 경우:
    python kr_stock_realtime/kr_stock_realtime_industry_index_execution_price.py
    # examples/kr_stock_realtime/ 폴더에서 실행하는 경우:
    python kr_stock_realtime_industry_index_execution_price.py

── 응답 파라미터 (Out) ─ OUT_BEGIN ──────────────────────
  [TR U00]
    AntcNmixclscode  (문자)  예상지수 구분코드 — 0:예상 1:정규
    BstpClscode  (문자)  업종 구분 코드
    BsopDate  (문자)  실시간일자
    BsopHour  (문자)  시간
    PrprNmix  (문자)  지수
    PrprNmixclr  (문자)  색참조(+상승, -하락)
    PrdyVrsssign  (문자)  전일 대비 부호
    BstpNmixprdyvrss  (문자)  전일 대비
    BstpNmixprdyvrssclr  (문자)  색참조(+상승, -하락)
    PrdyCtrt  (문자)  등락율
    PrdyCtrtclr  (문자)  색참조(+상승, -하락)
    AcmlVol  (문자)  누적 거래량
    AcmlTrpbmn  (문자)  누적 거래 대금
    OprcNmix  (문자)  시가
    OprcNmixclr  (문자)  색참조(+상승, -하락)
    NmixHgpr  (문자)  고가
    NmixHgprclr  (문자)  색참조(+상승, -하락)
    NmixLwpr  (문자)  저가
    NmixLwprclr  (문자)  색참조(+상승, -하락)
    CntgVol  (문자)  체결 거래량
    CntgPrgs  (문자)  체결틱추이
    AntcClscode  (문자)  예상지수구분코드 — 0: 정규장 B: 장전 A: 장후

  공통: rsp_cd  응답코드  ·  rsp_msg  응답메시지
── OUT_END ──────────────────────────────────────────────
"""


import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from dbsec_helper import ws_subscribe, run_ws

run_ws(ws_subscribe(
    tr_type="1",  # 등록 종류 (1=시세구독 2=해제 3=계좌등록): 시세구독
    tr_cd="U00",  # 거래코드 (str) - TR코드입력: U00
    tr_key="",  # 종목코드 (str) - 1001: KOSPI 2001: KOSDAQ 3001: KOSPI200 1002: 코스피(대형주) 1004: 코스피(소형주) 1053: KOSPI50종합지수 1054: KOSPI100종합지수 1163: 코스피고배당50 2002: 코스닥(대형주) 2004: 코스닥(소형주) 2203: 코스닥 150 3903: KP200레버리지지수 3907: 변동성지수 0100: KRX100 0600: KTOP 30 K001: KOVIXI00
    group_slug="kr_stock_realtime",
))
