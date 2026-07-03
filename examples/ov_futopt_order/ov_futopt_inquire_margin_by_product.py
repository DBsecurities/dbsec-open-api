"""상품별증거금조회 (ph800404o) — standalone 예제.

그룹    : 해외선물옵션주문
엔드포인트: POST /api/v1/trading/overseas-futureoption/inquiry/product-margin
TPS     : 2
가이드  : https://openapi.dbsec.co.kr/apiservice?group_id=344c4c78-ead3-448a-aeb8-0f6bce60efbc&api_id=f0e3ef2e-f895-444e-a51c-3fb825316428

해외선물옵션 상품별 증거금 조회 API 입니다.

토큰은 examples/dbsec_helper.py 가 자동 발급/캐싱합니다.

실행:
    # examples/ 폴더에서 실행하는 경우:
    python ov_futopt_order/ov_futopt_inquire_margin_by_product.py
    # examples/ov_futopt_order/ 폴더에서 실행하는 경우:
    python ov_futopt_inquire_margin_by_product.py

── 응답 파라미터 (Out) ─ OUT_BEGIN ──────────────────────
  [TR ph800404o]
    Out  (오브젝트)  Out
      Ikey  (문자)  조회구분
      Sdir  (문자)  정렬방식
      Aflg  (문자)  추가위치
      Ckey  (문자)  다음조회가능여부
      Nrow  (문자)  조회건수
      Kval  (문자)  다음키값
    Out1  (오브젝트)  Out1
      Code  (문자)  상품코드
      Cdnm  (문자)  상품명
      Mrg1  (문자)  위탁증거금구분
      Mrgn  (문자)  위탁증거금
      Mrg2  (문자)  유지증거금구분
      Urgn  (문자)  유지증거금

  공통: rsp_cd  응답코드  ·  rsp_msg  응답메시지
── OUT_END ──────────────────────────────────────────────
"""

#        실거래 위험이 큰 만큼 소액·시뮬레이션으로 충분히 검증한 뒤 사용하세요.
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from dbsec_helper import call_rest, print_response

resp, data = call_rest(
    url="/api/v1/trading/overseas-futureoption/inquiry/product-margin",
    body={
        "In": {
            "Code": "MNQ",  # 상품코드 (str)
        },
    },
    label="상품별증거금조회",
)
print_response(resp, data)
