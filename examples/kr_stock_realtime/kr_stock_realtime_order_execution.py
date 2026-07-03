"""[실시간]주식주문체결 조회 [IS1] — standalone WebSocket 예제.

그룹: 국내주식시세(실시간)
프로토콜: WebSocket (실시간)
가이드: https://openapi.dbsec.co.kr/apiservice?group_id=94b5fddc-b819-451b-9619-13ee42468798&api_id=a3a93ec3-2ccc-4fa5-8096-b45616b785e4

국내주식 실시간 주문체결 API 입니다. 주문 체결시 내역이 출력됩니다.

토큰은 examples/dbsec_helper.py 가 자동 확보합니다.
필요한 외부 패키지: requests, pyyaml, websockets

실행:
    # examples/ 폴더에서 실행하는 경우:
    python kr_stock_realtime/kr_stock_realtime_order_execution.py
    # examples/kr_stock_realtime/ 폴더에서 실행하는 경우:
    python kr_stock_realtime_order_execution.py

── 응답 파라미터 (Out) ─ OUT_BEGIN ──────────────────────
  [TR IS1]
    Sordxctptncode  (문자)  주문체결유형코드
    Strancode  (문자)  서비스코드
    Sordmktcode  (문자)  주문시장코드
    Sordptncode  (문자)  주문유형코드
    Sisuno  (문자)  종목번호
    Sisunm  (문자)  종목명
    Sordno  (문자)  주문번호
    Sorgordno  (문자)  원주문번호
    Sexecno  (문자)  체결번호
    Sordqty  (문자)  주문수량
    Sordprc  (문자)  주문가격
    Sexecqty  (문자)  체결수량
    Sexecprc  (문자)  체결가격
    Smdfycnfqty  (문자)  정정확인수량
    Smdfycnfprc  (문자)  정정확인가격
    Scanccnfqty  (문자)  취소확인수량
    Srjtqty  (문자)  거부수량
    Sordtrxptncode  (문자)  주문처리유형코드
    Sordcndi  (문자)  주문조건
    Sordprcptncode  (문자)  호가유형코드
    Snsavtrdqty  (문자)  비저축체결수량
    Sshtnisuno  (문자)  단축종목번호
    Sopdrtnno  (문자)  운용지시번호
    Scvrgordtp  (문자)  반대매매주문구분
    Sunercqty  (문자)  미체결수량(주문)
    Sorgordunercqty  (문자)  원주문미체결수량
    Sorgordmdfyqty  (문자)  원주문정정수량
    Sorgordcancqty  (문자)  원주문취소수량
    Sordavrexecprc  (문자)  주문평균체결가격
    Sordamt  (문자)  주문금액
    Sstdisuno  (문자)  표준종목번호
    Sbnstp  (문자)  매매구분
    Sordtrdptncode  (문자)  주문거래유형코드
    Smgntrncode  (문자)  신용거래코드
    Sadduptp  (문자)  수수료합산코드
    Sloandt  (문자)  대출일
    Sagrgbrnno  (문자)  집계지점번호
    Sregmktcode  (문자)  등록시장코드
    Smnymgnrat  (문자)  현금증거금률
    Ssubstmgnrat  (문자)  대용증거금률
    Smnyexecamt  (문자)  현금체결금액
    Ssubstexecamt  (문자)  대용체결금액
    Scmsnamtexecamt  (문자)  수수료체결금액
    Scrdtpldgexecamt  (문자)  신용담보체결금액
    Scrdtexecamt  (문자)  신용체결금액
    Sprdayruseexecval  (문자)  전일재사용체결금액
    Scrdayruseexecval  (문자)  금일재사용체결금액
    Sspotexecqty  (문자)  실물체결수량
    Sorduserid  (문자)  주문자ID
    Sfrgrunqno  (문자)  외국인고유번호
    Sexectime  (문자)  체결시각
    Srcptexectime  (문자)  거래소수신체결시각
    Srmndloanamt  (문자)  잔여대출금액
    Ssecbalqty  (문자)  *주식잔고-잔고수량
    Sspotordableqty  (문자)  *주식잔고-실물가능수량
    Sordableruseqty  (문자)  *주식잔고-재사용가능수량(매도)
    Sflctqty  (문자)  *주식잔고-변동수량
    Ssecbalqtyd2  (문자)  *주식잔고-잔고수량(D2)
    Ssellableqty  (문자)  *주식잔고-매도주문가능수량
    Sunercsellordqty  (문자)  *주식잔고-미체결매도주문수량
    Savrpchsprc  (문자)  *주식잔고-평균매입가
    Spchsamt  (문자)  *주식잔고-매입금액
    Sdeposit  (문자)  *예수금잔고-예수금
    Ssubstamt  (문자)  *예수금잔고-대용금
    Scsgnmnymgn  (문자)  *예수금잔고-위탁증거금현금
    Scsgnsubstmgn  (문자)  *예수금잔고-위탁증거금대용
    Scrdtpldgruseamt  (문자)  *예수금잔고-신용담보재사용금
    Sordablemny  (문자)  *예수금잔고-주문가능현금
    Sordablesubstamt  (문자)  *예수금잔고-주문가능대용
    Sruseableamt  (문자)  *예수금잔고-재사용가능금액
    Sacntno  (문자)  계좌번호

  공통: rsp_cd  응답코드  ·  rsp_msg  응답메시지
── OUT_END ──────────────────────────────────────────────
"""


import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from dbsec_helper import ws_subscribe, run_ws

# 주문 알림(IS1)은 계정 단위 — tr_key 불필요 (tr_type="3" 으로 계좌등록, 해제 메시지 없음)
run_ws(ws_subscribe(
    tr_type="3",  # 등록 종류 (1=시세구독 2=해제 3=계좌등록): 계좌등록
    tr_cd="IS1",  # 거래코드 (str) - TR코드입력: IS1
    tr_key="",  # 종목코드 (str) - 입력 X
    group_slug="kr_stock_realtime",
))
