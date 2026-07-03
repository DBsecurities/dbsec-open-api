"""[실시간]해외주식 주문체결 조회 [IS2] — standalone WebSocket 예제.

그룹: 해외주식시세(실시간)
프로토콜: WebSocket (실시간)
가이드: https://openapi.dbsec.co.kr/apiservice?group_id=68dccbef-704a-4ebc-86ac-e44056c5687b&api_id=85fc552d-4bcd-45e5-8fd3-62eaf01b7e5c

해외주식 실시간 주문체결 API 입니다. 주문 체결시 내역이 출력됩니다.

토큰은 examples/dbsec_helper.py 가 자동 확보합니다.
필요한 외부 패키지: requests, pyyaml, websockets

실행:
    # examples/ 폴더에서 실행하는 경우:
    python ov_stock_realtime/ov_stock_realtime_order_execution.py
    # examples/ov_stock_realtime/ 폴더에서 실행하는 경우:
    python ov_stock_realtime_order_execution.py

── 응답 파라미터 (Out) ─ OUT_BEGIN ──────────────────────
  [TR IS2]
    Sordxctptncode  (문자)  주문체결유형코드 — 00: 해당없음 01: 주문 02: 정정 03: 취소 11: 체결 12: 정정확인 13: 취소확인 14: 거부
    Strancode  (문자)  서비스 코드
    Sorddt  (문자)  주문일자
    Sordno  (문자)  주문번호
    Sorgordno  (문자)  원주문번호
    Sastkisuno  (문자)  해외주식종목번호
    Ssymcode  (문자)  심볼코드
    Sastkisunm  (문자)  해외주식종목명
    Sastkmktcode  (문자)  해외주식시장코드
    Sastkmktnm  (문자)  해외주식시장명
    Sownsecode  (문자)  자체증권거래소코드
    Sastkbnstpcode  (문자)  해외주식매매구분코드 — 0: 전체 1: 매도 2: 매수
    Sastkbnstpnm  (문자)  해외주식매매구분명
    Sordtrdtpcode  (문자)  주문거래구분코드 — 0: 원주문 1: 정정주문 2: 취소주문
    Sastkordqty  (문자)  해외주식주문수량
    Sastkordprc  (문자)  해외주식주문가격
    Sastkordprcptncode  (문자)  해외주식호가유형코드 — 1: 지정가 2: 시장가
    Sastkordprcptnnm  (문자)  해외주식호가유형명
    Sastkordcnditpcode  (문자)  해외주식주문조건구분코드 — 1:FAS 2:IOC 3:FOK
    Sastkordcnditpnm  (문자)  해외주식주문조건구분명
    Scrcycode  (문자)  통화코드
    Sshtncntrysymcode  (문자)  단축국가심볼코드
    Sastkordstatnm  (문자)  해외주식주문상태명
    Sastkorddttm  (문자)  해외주식주문일시
    Sastklclorddttm  (문자)  해외주식현지주문일시
    Sastkexecqty  (문자)  체결수량
    Sastkexecprc  (문자)  체결가격
    Sastkacmexecqty  (문자)  누적체결수량
    Sastkexecavruprc  (문자)  체결평균단가
    Sastkunercqty  (문자)  미체결수량
    Sastkexecamt  (문자)  체결금액
    Sastkexecdttm  (문자)  외주식체결일시
    Sastklclexecdttm  (문자)  해외주식현지체결일시
    Smgntrncode  (문자)  신용거래코드
    Sloandt  (문자)  대출일자
    Sastkexecbaseqty  (문자)  해외주식체결기준수량
    Sastkordableqty  (문자)  해외주식주문가능수량
    Sastkbuyamt  (문자)  해외주식매수금액
    Sastkbuycmsn  (문자)  해외주식매수수수료
    Sthdayrlzpnlamt  (문자)  당일실현손익금액
    Sastkselllclcmsnrat  (문자)  해외주식매도현지수수료율
    Sastkbuylclcmsnrat  (문자)  해외주식매수현지수수료율
    Sacntno  (문자)  게좌번호

  공통: rsp_cd  응답코드  ·  rsp_msg  응답메시지
── OUT_END ──────────────────────────────────────────────
"""


import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from dbsec_helper import ws_subscribe, run_ws

# 주문 알림(IS2)은 계정 단위 — tr_key 불필요 (tr_type="3" 으로 계좌등록, 해제 메시지 없음)
run_ws(ws_subscribe(
    tr_type="3",  # 등록 종류 (1=시세구독 2=해제 3=계좌등록): 계좌등록
    tr_cd="IS2",  # 거래코드 (str) - TR코드입력: IS2
    tr_key="",  # 종목코드 (str) - 입력 X
    group_slug="ov_stock_realtime",
))
