"""채권주문체결조회 (CSPAQ05700) — standalone 예제.

그룹    : 장내채권주문
엔드포인트: POST /api/v1/trading/krx-bond/inquiry/transaction-history
TPS     : 2
가이드  : https://openapi.dbsec.co.kr/apiservice?group_id=4a7257ed-b94a-462e-987d-132f064ed0d3&api_id=f0b45051-2960-4101-a4ad-352fc28d6383

채권주문체결 조회 API 입니다.

토큰은 examples/dbsec_helper.py 가 자동 발급/캐싱합니다.

실행:
    # examples/ 폴더에서 실행하는 경우:
    python bond_order/bond_inquire_executions.py
    # examples/bond_order/ 폴더에서 실행하는 경우:
    python bond_inquire_executions.py

── 응답 파라미터 (Out) ─ OUT_BEGIN ──────────────────────
  [TR CSPAQ05700]
    Out1  (배열)  Out1
      IsuNm  (문자)  종목명
      SmbndBnsTrdObjCode  (문자)  소액채권매매거래대상코드 — 00 : 일반채권 01 : 소액채권 02 : CB(전환사채)
      ThdayOrdNo  (숫자)  당일주문번호
      OrgOrdNo  (숫자)  원주문번호
      OrdQty  (숫자)  주문수량
      OrdPrc  (숫자)  주문가격
      TaxchrTpNm  (문자)  과세구분명
      OrdTrxPtnCode  (숫자)  주문처리유형코드 — 0:정상, 6:정정확인, 8:취소확인
      BuyDt  (문자)  매수일
      ExecQty  (숫자)  체결수량
      ExecPrc  (숫자)  체결가
      ErnRat  (숫자)  수익율
      BndIsuNo  (문자)  채권종목번호
      AllExecQty  (숫자)  전체체결수량
      MrcAbleQty  (숫자)  정정취소가능수량
      BnsTpCode  (문자)  매매구분 — 1:매도 2:매수
      OrdPtnCode  (문자)  주문유형코드 — 확인필요
      OrdTime  (문자)  주문시각
      ExecTime  (문자)  체결시각
    Out2  (오브젝트)  Out2
      SellExecQty  (숫자)  매도체결수량
      BuyExecQty  (숫자)  매수체결수량
      SellExecAmt  (숫자)  매도체결금액
      BuyExecAmt  (숫자)  매수체결금액

  공통: rsp_cd  응답코드  ·  rsp_msg  응답메시지
── OUT_END ──────────────────────────────────────────────
"""

import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from dbsec_helper import call_rest, print_response

resp, data = call_rest(
    url="/api/v1/trading/krx-bond/inquiry/transaction-history",
    body={
        "In": {
            "PrdtExecTpCode": "",  # 체결구분 (str) - 0. 전체 1. 체결 2. 미체결
            "BnsTpCode": "0",  # 매매구분 (str) - 1:매도 2:매수
            "BndIsuNo": "",  # 채권종목번호 (str)
            "OrdDt": "20240130",  # 주문일 (str)
        },
    },
    label="채권주문체결조회",
)
print_response(resp, data)
