"""선물옵션 주문 (야간) (CFOHT00100) — standalone 예제.

그룹    : 국내선물옵션주문
엔드포인트: POST /api/v1/trading/night-futureoption/order
TPS     : 10
가이드  : https://openapi.dbsec.co.kr/apiservice?group_id=44c4a04f-f55e-4c1c-b4e2-b48ec4869aee&api_id=a8e66f9f-5fda-437e-adfc-a130a5c66437

야간 선물옵션 주문이 가능한 API입니다. ※ 야간선물옵선 거래신청이 완료된 계좌만 야간선물옵션 거래가 가능합니다. 
※ 신청방법 HTS : [2300]야간선물옵션참여신청 MTS : 선물옵션 > 야간시장 > 야간선옵거래신청 
※ 수수료 및 제세금 안내는 아래 링크 참고 부탁드립니다. https://www.dbsec.co.kr/custcenter/jobservice/cu_FeeTrading_viw10.do 
※ 거래제도
   거래일: 월요일 야간 ~ 토요일 오전
   거래시간: 18:00 ~ 익일 05:00 (동시호가 17:30 ~ 18:00)
   ☆ 유럽 Summer time 적용시 18:00 ~ 04:00
※ 야간선물옵션 거래제도 상세안내는 아래 링크 참고 부탁드립니다. https://www.dbsec.co.kr/custcenter/jobservice/cu_TradeKrx_viw.do

토큰은 examples/dbsec_helper.py 가 자동 발급/캐싱합니다.

실행:
    # examples/ 폴더에서 실행하는 경우:
    python kr_futopt_order/kr_futopt_order_night.py
    # examples/kr_futopt_order/ 폴더에서 실행하는 경우:
    python kr_futopt_order_night.py

── 응답 파라미터 (Out) ─ OUT_BEGIN ──────────────────────
  [TR CFOHT00100]
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
    url="/api/v1/trading/night-futureoption/order",
    body={
        "In": {
            "FnoIsuNo": "175V2000",  # 선물옵션종목번호 (str) - 선물옵션 종목 코드 입력 선물 EX) 211V2060 옵션 EX) 201V2347
            "BnsTpCode": "2",  # 매매구분 (str) - 1:매도 2:매수
            "FnoOrdprcPtnCode": "00",  # 선물옵션호가유형코드 (str) - 00:지정가 10:지정가(IOC)
            "OrdPrc": 1340.7,  # 주문가격 (int)
            "OrdQty": 10,  # 주문수량 (int)
        },
    },
    label="선물옵션 주문 (야간)",
)
print_response(resp, data)
