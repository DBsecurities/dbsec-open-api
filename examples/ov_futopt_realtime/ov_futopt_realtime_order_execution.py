"""[실시간]주문체결 [O] — standalone WebSocket 예제.

그룹: 해외선물옵션시세(실시간)
프로토콜: WebSocket (실시간)
가이드: https://openapi.dbsec.co.kr/apiservice?group_id=f1819725-95e6-4445-ad7f-aa1908b20b03&api_id=227bff3a-ef1f-41b5-aee7-13c034f1e1f8

해외선물옵션 실시간 주문체결 API 입니다. 주문 체결시 내역이 출력됩니다.

토큰은 examples/dbsec_helper.py 가 자동 확보합니다.
필요한 외부 패키지: requests, pyyaml, websockets

실행:
    # examples/ 폴더에서 실행하는 경우:
    python ov_futopt_realtime/ov_futopt_realtime_order_execution.py
    # examples/ov_futopt_realtime/ 폴더에서 실행하는 경우:
    python ov_futopt_realtime_order_execution.py

── 응답 파라미터 (Out) ─ OUT_BEGIN ──────────────────────
  [TR O]
    OrderNo  (문자)  주문번호
    code  (문자)  종목코드
    OrderDate  (문자)  주문일자
    OrgOrderNo  (문자)  원주문번호
    OrgOrderDate  (문자)  원주문일자
    SellBuy  (문자)  매도매수구분 — 1:매수 2:매도
    OrderType  (문자)  주문유형
    OrderDurationType  (문자)  주문구분
    OrderDurationDate  (문자)  유효일자
    OrderQty  (문자)  주문수량
    OrderPrice  (문자)  주문가격
    WorkingQty  (문자)  주문잔량
    CancelQty  (문자)  취소수량
    ReplaceOrCancelQty  (문자)  정정취소수량
    OrderPlacedTime  (문자)  주문시간 — YYYYMMDDHHMISS
    CumulativelyFilledQty  (문자)  누적체결량
    RejectMessage  (문자)  주문거부메세지
    DealID  (문자)  체결번호
    ExecutedTime  (문자)  체결시간
    DealPrice  (문자)  체결가격
    DealQty  (문자)  체결수량
    ServerOrderFee  (문자)  수수료
    ServerOrderPl  (문자)  청산손익
    OrderStatusCode  (문자)  주문상태코드 — 10 : 주문대기 11 : 주문 20 : 정정대기 21 : 정정 30 : 취소대기 31 : 취소

  공통: rsp_cd  응답코드  ·  rsp_msg  응답메시지
── OUT_END ──────────────────────────────────────────────
"""


import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from dbsec_helper import ws_subscribe, run_ws

run_ws(ws_subscribe(
    tr_type="3",  # 등록 종류 (1=시세구독 2=해제 3=계좌등록): 계좌등록
    tr_cd="O",  # 거래코드 (str) - 입력 X (계좌등록시 자동으로 출력)
    tr_key="",  # 종목코드 (str) - 입력 X
    group_slug="ov_futopt_realtime",
))
