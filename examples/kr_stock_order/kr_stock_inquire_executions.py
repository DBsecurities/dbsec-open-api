"""체결/미체결조회 (CSPAQ04800) — standalone 예제.

그룹    : 국내주식주문
엔드포인트: POST /api/v1/trading/kr-stock/inquiry/transaction-history
TPS     : 2
가이드  : https://openapi.dbsec.co.kr/apiservice?group_id=05ac28b8-624f-4115-8aed-cf55f24279dd&api_id=815bbd65-8208-4428-b82a-18c32c13a092

국내주식 체결/미체결 내역을 확인하는 API입니다. ※ 모의투자 계좌로 사용가능한 API입니다.

토큰은 examples/dbsec_helper.py 가 자동 발급/캐싱합니다.

실행:
    # examples/ 폴더에서 실행하는 경우:
    python kr_stock_order/kr_stock_inquire_executions.py
    # examples/kr_stock_order/ 폴더에서 실행하는 경우:
    python kr_stock_inquire_executions.py

── 응답 파라미터 (Out) ─ OUT_BEGIN ──────────────────────
  [TR CSPAQ04800]
    Out1  (배열)  Out1
      TrdMktCode  (문자)  시장구분코드 — 1:KRX 2:NXT
      OrdNo  (숫자)  주문번호
      OrdSplitYn  (문자)  주문분할여부 — 0 : N 1 : Y KRX/NXT로 분할 되었는지 여부 (SOR주문여부가 아님에 유의)
      ConnOrdNo  (숫자)  연결주문번호 — SOR 로 분할된 주문의 연결고리가 되는 KEY ※ SOR로 KRX/NXT 분할된경우(주문분할여부 '1')에 값 셋팅 예정
      SorTpYn  (문자)  SOR구분여부 — 0 : N 1 : Y
      OrgOrdNo  (숫자)  원주문번호
      IsuNo  (문자)  종목번호
      OrdMktCode  (문자)  주문시장코드 — 00:전체 10:KSE 20:KOSDAQ 25:KONEX 30:OTCBB
      BnsTpCode  (문자)  매매구분 — 1:매도 2:매수
      OrdPtnCode  (문자)  주문유형코드 — 01:현금매도 02:현금매수 03:신용매도 04:신용매수 05:저축
      OrdprcPtnCode  (문자)  호가유형코드 — 00:지정가 03:시장가 05:조건부지정가 06:최유리지정가
      OrdQty  (숫자)  주문수량
      OrdPrc  (숫자)  주문가
      AllExecQty  (숫자)  전체체결수량
      MrcAbleQty  (숫자)  정정취소가능수량
      AvrExecPrc  (숫자)  평균체결가
      MrcQty  (숫자)  정정취소수량
      MgntrnCode  (문자)  신용거래코드 — 070:매도대금담보대출신규 182:예탁자산채권담보대출상환
      LoanDt  (문자)  대출일
      OrdTrxPtnCode  (숫자)  주문처리유형코드 — 0:정상 6:정정확인 8:취소확인 7:정정중 9:취소중
      TrxTime  (문자)  처리시각
      OrdCndiTpCode  (문자)  주문조건구분 — 0:없음 1:IOC 2:FOK
      MtiordSeqno  (숫자)  복수주문일련번호

  공통: rsp_cd  응답코드  ·  rsp_msg  응답메시지
── OUT_END ──────────────────────────────────────────────
"""

import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from dbsec_helper import call_rest, print_response

resp, data = call_rest(
    url="/api/v1/trading/kr-stock/inquiry/transaction-history",
    body={
        "In": {
            "ExecYn": "0",  # 체결여부 (str) - 0:전체 1:체결 2:미체결(정정취소가능)
            "BnsTpCode": "0",  # 매매구분 (str) - 0:전체 1:매도 2:매수
            "IsuTpCode": "0",  # 종목구분 (str) - 0:전체
            "QryTp": "0",  # 조회구분 (str) - 0:전체 1:ELW 2:ELW제외
            "TrdMktCode": "0",  # 거래시장코드 (str) - 0 : 전체 1 : KRX 2 : NXT
            "SorTpYn": "2",  # SOR구분여부 (str) - 0 : N 1 : Y 2 : 전체
        },
    },
    label="체결/미체결조회",
)
print_response(resp, data)
