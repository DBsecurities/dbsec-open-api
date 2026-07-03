"""[실시간]주식주문접수 조회 [IS0] — standalone WebSocket 예제.

그룹: 국내주식시세(실시간)
프로토콜: WebSocket (실시간)
가이드: https://openapi.dbsec.co.kr/apiservice?group_id=94b5fddc-b819-451b-9619-13ee42468798&api_id=24ae5513-5186-4e7e-a4eb-66bfe10a0d8a

국내주식 실시간 주문접수 API 입니다. 주문 접수시 내역이 출력됩니다.

토큰은 examples/dbsec_helper.py 가 자동 확보합니다.
필요한 외부 패키지: requests, pyyaml, websockets

실행:
    # examples/ 폴더에서 실행하는 경우:
    python kr_stock_realtime/kr_stock_realtime_order_accept.py
    # examples/kr_stock_realtime/ 폴더에서 실행하는 경우:
    python kr_stock_realtime_order_accept.py

── 응답 파라미터 (Out) ─ OUT_BEGIN ──────────────────────
  [TR IS0]
    Sordxctptncode  (문자)  주문체결유형코드
    Sordmktcode  (문자)  주문시장코드
    Strancode  (문자)  서비스코드
    Sordptncode  (문자)  주문유형코드
    Sorgordno  (문자)  원주문번호
    Sisuno  (문자)  종목번호
    Sshtnisuno  (문자)  단축종목번호
    Sisunm  (문자)  종목명
    Sordqty  (문자)  주문수량
    Sordprc  (문자)  주문가
    Sordcndi  (문자)  주문조건
    Sordprcptncode  (문자)  호가유형코드
    Sprgmordprcptncode  (문자)  프로그램호가유형코드
    Smgntrncode  (문자)  신용거래코드
    Sloandt  (문자)  대출일
    Scvrgordtp  (문자)  반대매매주문구분
    Sordno  (문자)  주문번호
    Sordtm  (문자)  주문시각
    Sprntordno  (문자)  모주문번호
    Sorgordunercqty  (문자)  원주문미체결수량
    Sorgordmdfyqty  (문자)  원주문정정수량
    Sorgordcancqty  (문자)  원주문취소수량
    Sordamt  (문자)  주문금액
    Sbnstp  (문자)  매매구분
    Sspotordqty  (문자)  실물주문수량
    Sordruseqty  (문자)  재사용주문수량
    Smnyordamt  (문자)  현금주문금액
    Sordsubstamt  (문자)  주문대용금액
    Sruseordamt  (문자)  재사용주문금액
    Sordcmsnamt  (문자)  수수료주문금액
    Susecrdtpldgruseamt  (문자)  사용신용담보재사용금
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

# 주문 알림(IS0)은 계정 단위 — tr_key 불필요 (tr_type="3" 으로 계좌등록, 해제 메시지 없음)
run_ws(ws_subscribe(
    tr_type="3",  # 등록 종류 (1=시세구독 2=해제 3=계좌등록): 계좌등록
    tr_cd="IS0",  # 거래코드 (str) - TR코드입력: IS0
    tr_key="",  # 종목코드 (str) - 입력 X
    group_slug="kr_stock_realtime",
))
