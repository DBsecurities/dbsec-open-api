"""주식종합주문 (CSPAT00600) — standalone 예제.

그룹    : 국내주식주문
엔드포인트: POST /api/v1/trading/kr-stock/order
TPS     : 10
가이드  : https://openapi.dbsec.co.kr/apiservice?group_id=05ac28b8-624f-4115-8aed-cf55f24279dd&api_id=c047bef4-020c-4ecb-9f6f-1597ee410a89

국내주식주문(현금&신용) API 입니다. ※ 모의투자 계좌로 사용가능한 API입니다. 
※ 모의투자 주문 시 "지정가, 시장가, 최유리지정가, 최우선지정가" 주문 유형만 입력 가능합니다. 
※ 수수료 및 제세금 안내는 아래 링크 참고 부탁드립니다. https://www.dbsec.co.kr/custcenter/jobservice/cu_FeeTrading_viw10.do 
※ 신용주문은 신용약정등록 계좌만 가능합니다. 
※ 주식매매 거래제도 안내는 아래 링크 참고 부탁드립니다. https://www.dbsec.co.kr/custcenter/jobservice/cu_TradeStock_viw.do

토큰은 examples/dbsec_helper.py 가 자동 발급/캐싱합니다.

실행:
    # examples/ 폴더에서 실행하는 경우:
    python kr_stock_order/kr_stock_order.py
    # examples/kr_stock_order/ 폴더에서 실행하는 경우:
    python kr_stock_order.py

── 응답 파라미터 (Out) ─ OUT_BEGIN ──────────────────────
  [TR CSPAT00600]
    Out  (오브젝트)  Out
      OrdSplitYn  (문자)  주문분할여부 — 0 : N 1 : Y KRX/NXT로 분할 되었는지 여부 (SOR주문여부가 아님에 유의) (추후 SOR 지원시 사용)
      ConnOrdNo  (숫자)  연결주문번호 — 신규필드 SOR 로 분할된 주문의 연결고리가 되는 KEY ※ SOR로 KRX/NXT 분할된경우(주문분할여부 '1')에 값 셋팅 예정 (추후 SOR 지원시 사용)
      NxtOrdNo  (숫자)  NXT주문번호 — NXT 주문번호 (추후 SOR 지원시 사용)
      OrdNo  (숫자)  주문번호 — 주문시 DB증권 거래시스템에서 채번된 주문번호
      OrdTime  (문자)  주문시각 — 주문시각(HHMMSSSSS - 시분초)
      ShtnIsuNo  (문자)  단축종목번호
      SpotOrdQty  (숫자)  실물주문수량
      MnyOrdAmt  (숫자)  현금주문금액 — 주문시 사용된 주문금액 시장가 주문시 "0" 으로 표시
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
    url="/api/v1/trading/kr-stock/order",
    body={
        "In": {
            "IsuNo": "A016610",  # 종목번호 (str) - 주식/ETF: 종목코드6자리 or "A"+"종목코드" ETN: Q + 종목코드 ELW: J + 종목코드
            "OrdQty": 1,  # 주문수량 (int) - 주식 주문수량
            "OrdPrc": 0,  # 주문가 (int) - * 지정가주문 이외의 주문 (시장가, 시간외 등)은 주문가를 0 으로 입력하는것을 권고
            "BnsTpCode": "2",  # 매매구분 (str) - 1:매도 2:매수
            "OrdprcPtnCode": "03",  # 호가유형코드 (str) - 00:지정가 03:시장가 05:조건부지정가 06:최유리지정가 07:최우선지정가 14: 중간가호가 61:장개시전시간외 81:시간외종가 82:시간외단일가
            "MgntrnCode": "000",  # 신용거래코드 (str) - 000:보통 (일반주문시 사용 신용주문X) 101:유통융자상환 103:자기융자상환 105:유통대주상환 107:자기대주상환 180:예탁담보대출상환(신용)
            "LoanDt": "00000000",  # 대출일 (str) - 일반 주문시: '00000000' 신용매수시: 오늘날짜 (YYYYMMDD) 입력 신용매도시: 매도할 종목의 결제일자(YYYYMMDD)입력 (대출일자X)
            "OrdCndiTpCode": "0",  # 주문조건구분 (str) - 0:없음 1:IOC 2:FOK
            "TrchNo": 1,  # 트렌치번호 (int) - 주문시 거래소 구분용도로 사용 1 : KRX ※ 1로 고정하셔서 사용 부탁드립니다. (SOR 주문 구분은 추후 제공 예정)
        },
    },
    label="주식종합주문",
)
print_response(resp, data)
 