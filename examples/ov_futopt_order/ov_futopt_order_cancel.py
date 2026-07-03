"""해외선옵 정정/취소주문 (ph700201o) — standalone 예제.

그룹    : 해외선물옵션주문
엔드포인트: POST /api/v1/trading/overseas-futureoption/order-revision
TPS     : 5
가이드  : https://openapi.dbsec.co.kr/apiservice?group_id=344c4c78-ead3-448a-aeb8-0f6bce60efbc&api_id=4bf364e6-1a5d-4a74-887f-be98de14bc60

해외선물옵션 정정/취소 API입니다. ※ 이미 체결완료된 주문은 정정 및 취소주문이 불가능합니다.

토큰은 examples/dbsec_helper.py 가 자동 발급/캐싱합니다.

실행:
    # examples/ 폴더에서 실행하는 경우:
    python ov_futopt_order/ov_futopt_order_cancel.py
    # examples/ov_futopt_order/ 폴더에서 실행하는 경우:
    python ov_futopt_order_cancel.py

── 응답 파라미터 (Out) ─ OUT_BEGIN ──────────────────────
  [TR ph700201o]
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
    url="/api/v1/trading/overseas-futureoption/order-revision",
    body={
        "In": {
            "Jcgb": "3",  # 정정/취소 구분 (str) - 2:정정 3:취소
            "Ojno": "3781468",  # 원주문번호 (str) - 정정/취소를 진행할 주문 번호
            "Code": "MESU26",  # 종목코드 (str) - 원 주문에서 사용한 종목코드
            "Mdms": "",  # 매수/매도 구분 (str) - 취소주문시 "" (공백) 설정 1:매수 2:매도
            "Jtyp": "",  # 주문유형 구분 (str) - 취소주문시 "" (공백) 설정 1:시장가 2:지정가 3:STOP 4:STOP LIMIT
            "Jqty": "",  # 주문수량 (str) - 취소주문시 "" (공백) 설정
            "Jprc": "",  # 주문가격 (str) - 취소주문시 "" (공백) 설정
            "Sprc": "",  # STOP-LIMIT 가격 (str) - 취소주문시 "" (공백) 설정
            "Hsbg": "",  # 행사예약 (str) - 옵션 주문시 사용 Y: 행사예약 O N: 행사예약 X
        },
    },
    label="해외선옵 정정/취소주문",
)
print_response(resp, data)
