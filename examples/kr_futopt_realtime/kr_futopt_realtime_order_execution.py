"""[실시간]선물옵션주문체결 [IF0] — standalone WebSocket 예제.

그룹: 국내선물옵션시세(실시간)
프로토콜: WebSocket (실시간)
가이드: https://openapi.dbsec.co.kr/apiservice?group_id=548b70a6-24cc-4d9d-a7c7-90eb84a497f4&api_id=99f558bf-e02f-40e7-a388-00ade0ddf5ce

국내선물옵션 실시간 주문체결 API 입니다. 주문 체결시 내역이 출력됩니다.

토큰은 examples/dbsec_helper.py 가 자동 확보합니다.
필요한 외부 패키지: requests, pyyaml, websockets

실행:
    # examples/ 폴더에서 실행하는 경우:
    python kr_futopt_realtime/kr_futopt_realtime_order_execution.py
    # examples/kr_futopt_realtime/ 폴더에서 실행하는 경우:
    python kr_futopt_realtime_order_execution.py

── 응답 파라미터 (Out) ─ OUT_BEGIN ──────────────────────
  [TR IF0]
    Trcode  (문자)  TR코드 — FO01: 신규주문 FO02: 정정주문 FO03: 취소주문 HO01: 확인(정정/취소, 신규확인은 없음) HO10: 차동취소(IOC/FOK) CH01 : 체결
    Strancode  (문자)  서비스코드
    Sordmktcode  (문자)  주문시장코드
    Juno  (문자)  주문번호
    Wonjuno  (문자)  원주문번호
    Mojuno  (문자)  모주문번호
    Sisuno  (문자)  종목번호
    Jgcode  (문자)  선물옵션종목번호
    Jgname  (문자)  선물옵션종목명
    Spdgrpcode  (문자)  상품군분류코드
    Dealgb  (문자)  선물옵션종목유형구분
    Jugb  (문자)  매매구분
    Canclegb  (문자)  정정취소구분
    Juqty  (문자)  주문수량
    Mmgb  (문자)  호가유형코드
    Sfnotrdptncode  (문자)  거래유형코드
    Juprc  (문자)  주문가격
    Micheqty  (문자)  미체결수량
    Dealamt  (문자)  선물옵션거래단위금액
    Time  (문자)  처리시각
    Sopdrtnno  (문자)  운영지시번호
    Reggb  (문자)  거래소거부코드
    Realaltgnty  (문자)  정정취소확인수량
    Wonmicheqty  (문자)  원주문미체결수량
    Wonjujjqty  (문자)  원주문정정취소수량(MrcQty)
    Sctrcttime  (문자)  약정시각(거래소체결시각)
    Yakno  (문자)  약정번호
    Cheprc  (문자)  체결가격
    Cheqty  (문자)  체결수량
    Snewqty  (문자)  신규체결수량
    Slqdtqty  (문자)  청산체결수량
    Slastqty  (문자)  최종결제수량
    Cheqtyall  (문자)  전체체결수량
    Cheprcall  (문자)  전체체결금액
    Sfnobalevaltp  (문자)  잔고평가구분
    Sbnsplamt  (문자)  매매손익금액(스프레드제외)
    Jgcode1  (문자)  선물옵션종목번호1
    Mmgb1  (문자)  매매구분1
    Chejisu1  (문자)  체결가1
    Snewqty1  (문자)  신규체결수량1
    Slqdtqty1  (문자)  청산체결수량1
    Cheprc1  (문자)  전체체결금액1
    Jgcode2  (문자)  선물옵션종목번호2
    Mmgb2  (문자)  매매구분2
    Chejisu2  (문자)  체결가2
    Snewqty2  (문자)  신규체결수량2
    Slqdtqty2  (문자)  청산체결수량2
    Cheprc2  (문자)  전체체결금액2
    Yetakcash  (문자)  예수금
    Yetakdae  (문자)  선물대용지정금액
    Smgn  (문자)  증거금
    Smnymgn  (문자)  증거금현금
    Jumuntot  (문자)  주문가능금액
    Jumuncash  (문자)  주문가능현금액
    Jgcode21  (문자)  잔고종목번호1
    Janmmgb1  (문자)  잔고매매구분1
    Openyak1  (문자)  미결제수량1
    Bettingvol1  (문자)  주문가능수량1
    Yakavgdan1  (문자)  평균가1
    Jgcode22  (문자)  잔고종목번호2
    Janmmgb2  (문자)  잔고매매구분2
    Openyak2  (문자)  미결제수량2
    Bettingvol2  (문자)  주문가능수량2
    Yakavgdan2  (문자)  평균가2
    Gejano  (문자)  게좌번호

  공통: rsp_cd  응답코드  ·  rsp_msg  응답메시지
── OUT_END ──────────────────────────────────────────────
"""


import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from dbsec_helper import ws_subscribe, run_ws

run_ws(ws_subscribe(
    tr_type="3",  # 등록 종류 (1=시세구독 2=해제 3=계좌등록): 계좌등록
    tr_cd="IF0",  # 거래코드 (str) - TR코드입력: IF0
    tr_key="",  # 종목코드 (str) - 입력 X
    group_slug="kr_futopt_realtime",
))
