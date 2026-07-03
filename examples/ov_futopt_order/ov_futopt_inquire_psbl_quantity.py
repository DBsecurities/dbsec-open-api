"""주문가능수량조회 (ph710201o) — standalone 예제.

그룹    : 해외선물옵션주문
엔드포인트: POST /api/v1/trading/overseas-futureoption/inquiry/able-orderqty
TPS     : 2
가이드  : https://openapi.dbsec.co.kr/apiservice?group_id=344c4c78-ead3-448a-aeb8-0f6bce60efbc&api_id=f29b1de6-cdba-42c0-91be-af8638f5abda

해외선물옵션 주문가능수량 조회 API 입니다.

토큰은 examples/dbsec_helper.py 가 자동 발급/캐싱합니다.

실행:
    # examples/ 폴더에서 실행하는 경우:
    python ov_futopt_order/ov_futopt_inquire_psbl_quantity.py
    # examples/ov_futopt_order/ 폴더에서 실행하는 경우:
    python ov_futopt_inquire_psbl_quantity.py

── 응답 파라미터 (Out) ─ OUT_BEGIN ──────────────────────
  [TR ph710201o]
    Out  (오브젝트)  Out
      Jqty  (문자)  주문가능수량
      Cqty  (문자)  청산가능수량

  공통: rsp_cd  응답코드  ·  rsp_msg  응답메시지
── OUT_END ──────────────────────────────────────────────
"""

#        실거래 위험이 큰 만큼 소액·시뮬레이션으로 충분히 검증한 뒤 사용하세요.
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from dbsec_helper import call_rest, print_response

resp, data = call_rest(
    url="/api/v1/trading/overseas-futureoption/inquiry/able-orderqty",
    body={
        "In": {
            "Code": "MESU26",  # 종목코드 (str)
            "Mdms": "1",  # 매도매수구분 (str) - 1:매수 2:매도
            "Jtyp": "1",  # 주문유형구분 (str) - 1:시장가 2:지정가 3:STOP 4:STOP LIMIT
            "Jprc": "",  # 주문가격 (str) - "1:시장가" 선택시 "" (공백) 입력
            "Sprc": "",  # STOP-LIMIT 가격 (str)
            "Hsbg": "N",  # 행사예약 (str) - Y/N
        },
    },
    label="주문가능수량조회",
)
print_response(resp, data)
