"""선물옵션 주문 (CFOAT00100) — standalone 예제.

그룹    : 국내선물옵션주문
엔드포인트: POST /api/v1/trading/kr-futureoption/order
TPS     : 10
가이드  : https://openapi.dbsec.co.kr/apiservice?group_id=44c4a04f-f55e-4c1c-b4e2-b48ec4869aee&api_id=5ca0a623-4424-4515-a9b9-1e736ea2be92

국내선물옵션 주문이 가능한 API입니다. 
※ 모의투자 계좌로 사용가능한 API입니다. 
※ 모의투자 주문 시 "지정가, 시장가, 최유리지정가" 주문 유형만 입력 가능합니다. 
※ 수수료 및 제세금 안내는 아래 링크 참고 부탁드립니다. https://www.dbsec.co.kr/custcenter/jobservice/cu_FeeTrading_viw10.do 
※ 선물옵션 거래제도 안내는 아래 링크 참고 부탁드립니다. https://www.dbsec.co.kr/custcenter/jobservice/cu_TradeFuture_viw.do

토큰은 examples/dbsec_helper.py 가 자동 발급/캐싱합니다.

실행:
    # examples/ 폴더에서 실행하는 경우:
    python kr_futopt_order/kr_futopt_order.py
    # examples/kr_futopt_order/ 폴더에서 실행하는 경우:
    python kr_futopt_order.py
    
── 응답 파라미터 (Out) ─ OUT_BEGIN ──────────────────────
  [TR CFOAT00100]
    Out  (오브젝트)  Out
      OrdNo  (숫자)  주문번호
      IsuNm  (문자)  종목명

  공통: rsp_cd  응답코드  ·  rsp_msg  응답메시지
── OUT_END ──────────────────────────────────────────────
"""

# ⚠️  경고: 실제 매매가 실행될 수 있는 주문 API입니다.
#        반드시 모의투자 환경(mode='demo')에서 먼저 테스트하세요.
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from dbsec_helper import call_rest, print_response

resp, data = call_rest(
    url="/api/v1/trading/kr-futureoption/order",
    body={
        "In": {
            "FnoIsuNo": "A0566000",  # 선물옵션종목번호 (str) - 선물옵션 종목 코드 입력 선물 EX) 211V2060 옵션 EX) 201V2347
            "BnsTpCode": "1",  # 매매구분 (str) - 1:매도 2:매수
            "OrdPrc": 1280,  # 주문가격 (int)
            "FnoOrdprcPtnCode": "03",  # 선물옵션호가유형코드 (str) - 00: 지정가 03: 시장가 10: 지정가(IOC)
            "OrdQty": 1,  # 주문수량 (int)
        },
    },
    label="선물옵션 주문",
)
print_response(resp, data)
