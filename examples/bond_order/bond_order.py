"""채권주문 (CSPAT02000) — standalone 예제.

그룹    : 장내채권주문
엔드포인트: POST /api/v1/trading/krx-bond/order
TPS     : 5
가이드  : https://openapi.dbsec.co.kr/apiservice?group_id=4a7257ed-b94a-462e-987d-132f064ed0d3&api_id=d3b2475e-2825-45ba-86de-16bbaa9745e5

장내채권 주문 API입니다. ※ 매매시간 : 장내 (09:00 ~ 15:00) ※ 채권은 '금액(원)' 단위로 매매 됩니다. 주식의 매매단위인 '주' 와 구분됩니다. (예시) DB금융투자 주식 10주 매수 -> DB금융투자 채권 10만원 매수 ※ 최소 '주문수량' 단위는 1000원 입니다.

토큰은 examples/dbsec_helper.py 가 자동 발급/캐싱합니다.

실행:
    # examples/ 폴더에서 실행하는 경우:
    python bond_order/bond_order.py
    # examples/bond_order/ 폴더에서 실행하는 경우:
    python bond_order.py

── 응답 파라미터 (Out) ─ OUT_BEGIN ──────────────────────
  [TR CSPAT02000]
    Out  (오브젝트)  Out
      OrdNo  (숫자)  주문번호
      IsuNm  (문자)  종목명
      BnsTpCode  (문자)  매매구분 — 매매구분

  공통: rsp_cd  응답코드  ·  rsp_msg  응답메시지
── OUT_END ──────────────────────────────────────────────
"""

# ⚠️  경고: 실제 매매가 실행될 수 있는 주문 API입니다.
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from dbsec_helper import call_rest, print_response

resp, data = call_rest(
    url="/api/v1/trading/krx-bond/order",
    body={
        "In": {
            "IsuNo": "KR2044022C80",  # 종목번호 (str)
            "OrdQty": 1000,  # 주문수량 (int)
            "OrdPrc": 10000,  # 주문가격 (int)
            "BnsTpCode": "2",  # 매매구분 (str) - 1:매도 2:매수
            "BndBuyDt": "20220928",  # 채권매수일 (str) - 채권매수일(매도주문시 입력), 매수시 " " 입력
            "TaxchrTpCode": "1",  # 과세집계구분 (str) - 매수주문시: "" 입력 매도주문시 1:종합과세 2:분리과세
            "SmbndEsmtnBnsTpCode": "0",  # 소액채권종료동시매매구분 (str) - 0:해당없음 1:소액시장참여
            "SmbndMktPtcnTpCode": "0",  # 소액채권시장참여구분 (str) - 0:일반 1:소액
            "LoanDt": "",  # 대출일자 (str) - 신용구분코드 1 일시 예탁담보대출시 매도주문일자 기본: ""
        },
    },
    label="채권매수주문",
)
print_response(resp, data)
