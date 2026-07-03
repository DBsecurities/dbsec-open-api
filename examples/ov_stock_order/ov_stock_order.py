"""해외주식 주문 (CAZCT00100) — standalone 예제.

그룹    : 해외주식주문
엔드포인트: POST /api/v1/trading/overseas-stock/order
TPS     : 10
가이드  : https://openapi.dbsec.co.kr/apiservice?group_id=e4726f55-cc3b-45af-a1b5-852628fe5960&api_id=43bc0191-3745-4ba8-937e-7af51e65085c

해외주식(미국) 주문이 가능한 API입니다. ※ 모의투자 계좌로 사용가능한 API입니다. ※ 해외주식 거래신청 후 이용 가능합니다. - 신청방법 HTS : [7322] 해외주식 시작하기 MTS : 해외주식 > 서비스신청 > 해외주식 거래신청, 통합증거금 이용신청, 해외ETP(ETF,ETN) 거래신청 ※ 수수료 및 제세금 안내는 아래 링크 참고 부탁드립니다. https://www.dbsec.co.kr/custcenter/jobservice/cu_FeeTrading_viw10.do ※ 해외주식 양도소득세...

토큰은 examples/dbsec_helper.py 가 자동 발급/캐싱합니다.

실행:
    # examples/ 폴더에서 실행하는 경우:
    python ov_stock_order/ov_stock_order.py
    # examples/ov_stock_order/ 폴더에서 실행하는 경우:
    python ov_stock_order.py

── 응답 파라미터 (Out) ─ OUT_BEGIN ──────────────────────
  [TR CAZCT00100]
    Out  (오브젝트)  Out
      OrdNo  (숫자)  주문번호

  공통: rsp_cd  응답코드  ·  rsp_msg  응답메시지
── OUT_END ──────────────────────────────────────────────
"""

# ⚠️  경고: 실제 매매가 실행될 수 있는 주문 API입니다.
#        반드시 모의투자 환경(mode='demo')에서 먼저 테스트하세요.
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from dbsec_helper import call_rest, print_response

resp, data = call_rest(
    url="/api/v1/trading/overseas-stock/order",
    body={
        "In": {
            "AstkIsuNo": "SNDL",  # 해외주식종목번호 (str) - 미국주식/ETF: "종목코드"
            "AstkBnsTpCode": "2",  # 해외주식매매구분코드 (str) - 1:매도 2:매수
            "AstkOrdprcPtnCode": "2",  # 해외주식호가유형코드 (str) - 1: 지정가 2: 시장가 3: LOO 4: MOO (매도주문 시 사용가능) 5: LOC 6: MOC (매도주문 시 사용가능) 7: VWAP지정가 (매수/매도 주문 모두 사용가능) 8: TWAP지정가 (매수/매도 주문 모두 사용가능) 9: VWAP시장가 (매도주문시에만 사용가능) A: TWAP시장가 (매도주문시에만 사용가능)
            "AstkOrdCndiTpCode": "1",  # 해외주식주문조건구분코드 (str) - 1:FAS(일반) 2:IOC 3:FOK
            "AstkOrdQty": 1,  # 해외주식주문수량 (int)
            "AstkOrdPrc": 0,  # 해외주식주문가격 (int) - 시장가주문시: 0
            "OrdTrdTpCode": "0",  # 주문거래구분코드 (str) - 0:주문 1:정정주문 2:취소주문
            "OrgOrdNo": 0,  # 원주문번호 (int) - 정정주문, 취소주문시 원 주문번호 입력 매수/매도주문시: 0
        },
    },
    label="해외주식 주문",
)
print_response(resp, data)
