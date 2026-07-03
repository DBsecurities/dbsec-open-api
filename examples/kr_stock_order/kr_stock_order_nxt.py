"""주식종합주문- NXT거래소 (CSPAT00610) — standalone 예제.

그룹    : 국내주식주문
엔드포인트: POST /api/v1/trading/kr-stock/order-nxt
TPS     : 10
가이드  : https://openapi.dbsec.co.kr/apiservice?group_id=05ac28b8-624f-4115-8aed-cf55f24279dd&api_id=13143c06-cf97-4ea5-a9b9-3d30fe6b1fec

NXT거래소 전용 국내주식 주문 API 입니다. 
※ 주문 전 MTS/HTS등 당사 매체를 통해 최선집행의무 동의를 하셔야 주문이 가능하십니다. 
※ 수수료 및 제세금 안내는 아래 링크 참고 부탁드립니다. https://www.dbsec.co.kr/custcenter/jobservice/cu_FeeTrading_viw10.do 
※ 주식매매 거래제도 안내는 아래 링크 참고 부탁드립니다. https://www.dbsec.co.kr/custcenter/jobservice/cu_TradeStock_viw.do

토큰은 examples/dbsec_helper.py 가 자동 발급/캐싱합니다.

실행:
    # examples/ 폴더에서 실행하는 경우:
    python kr_stock_order/kr_stock_order_nxt.py
    # examples/kr_stock_order/ 폴더에서 실행하는 경우:
    python kr_stock_order_nxt.py

── 응답 파라미터 (Out) ─ OUT_BEGIN ──────────────────────
  [TR CSPAT00610]
    Out  (오브젝트)  Out
      OrdNo  (숫자)  주문번호 — 주문시 DB증권 거래시스템에서 채번된 주문번호
      OrdTime  (문자)  주문시각 — 주문시각(HHMMSSSSS - 시분초)
      ShtnIsuNo  (문자)  단축종목번호
      SpotOrdQty  (숫자)  실물주문수량
      MnyOrdAmt  (숫자)  현금주문금액
      IsuNm  (문자)  종목명 — 주문 종목의 한글명

  공통: rsp_cd  응답코드  ·  rsp_msg  응답메시지
── OUT_END ──────────────────────────────────────────────
"""

# ⚠️  경고: 실제 매매가 실행될 수 있는 주문 API입니다.
#        반드시 모의투자 환경(mode='demo')에서 먼저 테스트하세요.
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from dbsec_helper import call_rest, print_response

resp, data = call_rest(
    url="/api/v1/trading/kr-stock/order-nxt",
    body={
        "In": {
            "IsuNo": "003620",  # 종목번호 (str) - 주식/ETF: 종목코드6자리 or "A"+"종목코드" ETN: Q + 종목코드 ELW: J + 종목코드
            "OrdQty": 20,  # 주문수량 (int) - 주식 주문수량
            "OrdPrc": 3010,  # 주문가 (int) - * 지정가주문 이외의 주문 (시장가, 시간외 등)은 주문가를 0 으로 입력하는것을 권고
            "BnsTpCode": "2",  # 매매구분 (str) - 1:매도 2:매수
            "OrdprcPtnCode": "00",  # 호가유형코드 (str) - 00:지정가 03:시장가 05:조건부지정가 06:최유리지정가 07:최우선지정가 14: 중간가호가 61:장개시전시간외 81:시간외종가 82:시간외단일가
            "MgntrnCode": "000",  # 신용거래코드 (str) - 000:보통 (일반주문시 사용 신용주문X) 101:유통융자상환 103:자기융자상환 105:유통대주상환 107:자기대주상환 180:예탁담보대출상환(신용)
            "LoanDt": "00000000",  # 대출일 (str) - 일반 주문시: '00000000' 신용매수시: 오늘날짜 (YYYYMMDD) 입력 신용매도시: 매도할 종목의 결제일자(YYYYMMDD)입력 (대출일자X)
            "OrdCndiTpCode": "0",  # 주문조건구분 (str) - 0:없음 1:IOC 2:FOK
        },
    },
    label="주식종합주문- NXT거래소",
)
print_response(resp, data)
