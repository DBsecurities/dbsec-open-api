"""[실시간]잔고 [P] — standalone WebSocket 예제.

그룹: 해외선물옵션시세(실시간)
프로토콜: WebSocket (실시간)
가이드: https://openapi.dbsec.co.kr/apiservice?group_id=f1819725-95e6-4445-ad7f-aa1908b20b03&api_id=8c1c0e6a-a0cd-4eb8-a170-40832b8317c4

해외선물옵션 실시간 잔고 API 입니다. 주문 체결시 내역이 출력됩니다.

토큰은 examples/dbsec_helper.py 가 자동 확보합니다.
필요한 외부 패키지: requests, pyyaml, websockets

실행:
    # examples/ 폴더에서 실행하는 경우:
    python ov_futopt_realtime/ov_futopt_realtime_balance.py
    # examples/ov_futopt_realtime/ 폴더에서 실행하는 경우:
    python ov_futopt_realtime_balance.py

── 응답 파라미터 (Out) ─ OUT_BEGIN ──────────────────────
  [TR P]
    Curr  (문자)  현재가
    Code  (문자)  종목코드
    TickSize  (문자)  Tick Size
    TickValue  (문자)  Tick Value
    AdjustmentValue  (문자)  Adjust Value
    SellBuy  (문자)  매도매수구분 — 1:매수 2:매도
    NetPositionQty  (문자)  잔고수량
    AvailableQty  (문자)  청산가능수량
    PositionPrice  (문자)  평균단가
    EvaluatedPL  (문자)  평가손익
    GCurr  (문자)  통화코드
    PreNonePositionQty  (문자)  전일잔고수량
    PurchasePrice  (문자)  총매입금액 — 해당종목의 전체 매입금액

  공통: rsp_cd  응답코드  ·  rsp_msg  응답메시지
── OUT_END ──────────────────────────────────────────────
"""


import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from dbsec_helper import ws_subscribe, run_ws

run_ws(ws_subscribe(
    tr_type="3",  # 등록 종류 (1=시세구독 2=해제 3=계좌등록): 계좌등록
    tr_cd="P",  # 거래코드 (str) - 입력 X (계좌등록시 자동으로 출력)
    tr_key="",  # 종목코드 (str) - 입력 X
    group_slug="ov_futopt_realtime",
))
