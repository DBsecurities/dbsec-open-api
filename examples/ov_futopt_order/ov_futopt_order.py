"""해외선옵 주문 (ph700101o) — standalone 예제.

그룹    : 해외선물옵션주문
엔드포인트: POST /api/v1/trading/overseas-futureoption/order
TPS     : 10
가이드  : https://openapi.dbsec.co.kr/apiservice?group_id=344c4c78-ead3-448a-aeb8-0f6bce60efbc&api_id=4ee438c9-16dd-4648-935e-e91ccbe599bd

해외선물옵션 주문 API입니다. ※ 수수료 및 제세금 안내는 아래 링크 참고 부탁드립니다. https://www.dbsec.co.kr/custcenter/jobservice/cu_FeeTrading_viw10.do ※ 매수/매도 진입으로 양방향 거래가 가능하여 API를 이용한 반복주문시, 예기치 못한 손실이 발생 할 수 있습니다. 옵션 상품을 포함한 특정 종목의 경우 유동성이 부족으로 인해 불리한 체결 가격으로 손실이 발생할 수 있으니 프로그램 작성에 반드시 주의 바랍니다. ※ 추가증거금 미납 또는 ...

토큰은 examples/dbsec_helper.py 가 자동 발급/캐싱합니다.

실행:
    # examples/ 폴더에서 실행하는 경우:
    python ov_futopt_order/ov_futopt_order.py
    # examples/ov_futopt_order/ 폴더에서 실행하는 경우:
    python ov_futopt_order.py

── 응답 파라미터 (Out) ─ OUT_BEGIN ──────────────────────
  [TR ph700101o]
    Out  (오브젝트)  Out
      Jmno  (문자)  주문번호

  공통: rsp_cd  응답코드  ·  rsp_msg  응답메시지
── OUT_END ──────────────────────────────────────────────
"""

# ⚠️  경고: 실제 매매가 실행될 수 있는 주문 API입니다.
#        해외선물옵션은 모의투자 미지원 — 운영(mode='production') 환경에서만 동작합니다.
#        실거래 위험이 큰 만큼 소액·시뮬레이션으로 충분히 검증한 뒤 사용하세요.
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from dbsec_helper import call_rest, print_response

resp, data = call_rest(
    url="/api/v1/trading/overseas-futureoption/order",
    body={
        "In": {
            "Code": "MESU26",  # 종목코드 (str) - 선물옵션 종목코드 입력
            "Mdms": "1",  # 매수/매도 구분 (str) - 1:매수 2:매도
            "Jtyp": "2",  # 주문유형 구분 (str) - 1:시장가 2:지정가 3:STOP 4:STOP LIMIT
            "Jmgb": "0",  # 주문구분 (str) - 0: DAY(당일) 1: GTC 6: GTD
            "Jqty": "1",  # 주문수량 (str)
            "Jprc": "7380",  # 주문가격 (str) - 시장가 주문시 "0" 입력
            "Sprc": "",  # STOP-LIMIT 가격 (str)
            "Date": "",  # 유효일자 (str) - YYYYMMDD ex.20240101
            "Hsbg": "B",  # 행사예약 (str) - Y/N
        },
    },
    label="해외선옵 주문",
)
print_response(resp, data)
