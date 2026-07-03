"""[실시간]업종지수등락 [U03] — standalone WebSocket 예제.

그룹: 국내주식시세(실시간)
프로토콜: WebSocket (실시간)
가이드: https://openapi.dbsec.co.kr/apiservice?group_id=94b5fddc-b819-451b-9619-13ee42468798&api_id=017147ee-baef-41de-8826-d0208a780be7

업종지수 등락 조회 API 입니다.

토큰은 examples/dbsec_helper.py 가 자동 확보합니다.
필요한 외부 패키지: requests, pyyaml, websockets

실행:
    # examples/ 폴더에서 실행하는 경우:
    python kr_stock_realtime/kr_stock_realtime_industry_index_change.py
    # examples/kr_stock_realtime/ 폴더에서 실행하는 경우:
    python kr_stock_realtime_industry_index_change.py

── 응답 파라미터 (Out) ─ OUT_BEGIN ──────────────────────
  [TR U03]
    AntcNmixclscode  (문자)  예상지수 구분코드
    BstpClscode  (문자)  업종코드
    BsopHour  (문자)  시간
    UplmIssucnt  (문자)  상한종목수
    AscnIssucnt  (문자)  상승종목수
    StnrIssucnt  (문자)  보합종목수
    DownIssucnt  (문자)  하락종목수
    LslmIssucnt  (문자)  하한종목수
    QtqtAscnissucnt  (문자)  기세상승종목수
    QtqtDownissucnt  (문자)  기세하락종목수

  공통: rsp_cd  응답코드  ·  rsp_msg  응답메시지
── OUT_END ──────────────────────────────────────────────
"""


import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from dbsec_helper import ws_subscribe, run_ws

run_ws(ws_subscribe(
    tr_type="1",  # 등록 종류 (1=시세구독 2=해제 3=계좌등록): 시세구독
    tr_cd="U03",  # 거래코드 (str) - TR코드입력: U03
    tr_key="",  # 종목코드 (str) - 1001: KOSPI 2001: KOSDAQ 3001: KOSPI200 1002: 코스피(대형주) 1004: 코스피(소형주) 1053: KOSPI50종합지수 1054: KOSPI100종합지수 1163: 코스피고배당50 2002: 코스닥(대형주) 2004: 코스닥(소형주) 2203: 코스닥 150 3903: KP200레버리지지수 3907: 변동성지수 0100: KRX100 0600: KTOP 30 K001: KOVIXI00
    group_slug="kr_stock_realtime",
))
