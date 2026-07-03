"""주문내역조회 (ph020101o) — standalone 예제.

그룹    : 해외선물옵션주문
엔드포인트: POST /api/v1/trading/overseas-futureoption/inquiry/order-history
TPS     : 2
가이드  : https://openapi.dbsec.co.kr/apiservice?group_id=344c4c78-ead3-448a-aeb8-0f6bce60efbc&api_id=e12c05bb-9ee8-4cce-966a-4b29ac67f742

해외선물옵션 주문내역 조회 API 입니다. ※ 주문내역이 전부 표시되지 않는경우 연속키 조회를 통해 확인하실 수 있습니다.

토큰은 examples/dbsec_helper.py 가 자동 발급/캐싱합니다.

실행:
    # examples/ 폴더에서 실행하는 경우:
    python ov_futopt_order/ov_futopt_inquire_orders.py
    # examples/ov_futopt_order/ 폴더에서 실행하는 경우:
    python ov_futopt_inquire_orders.py

── 응답 파라미터 (Out) ─ OUT_BEGIN ──────────────────────
  [TR ph020101o]
    Out  (오브젝트)  Out
      Ikey  (문자)  조회구분
      Sdir  (문자)  정렬방식
      Aflg  (문자)  추가위치
      Ckey  (문자)  다음조회가능여부
      Nrow  (문자)  조회건수
      Kval  (문자)  다음키값
    Out1  (오브젝트)  Out1
      Jmno  (문자)  주문번호
      Ojno  (문자)  원주문번호
      Stat  (문자)  처리상태 — 상태값: 주문대기 주문 정정대기 정정 취소대기 취소 거부
      Mtst  (문자)  전략유형 — 확인필요
      Code  (문자)  종목코드
      Mdms  (문자)  매도/매수구분 — 1:매수 2:매도
      Jqty  (문자)  주문수량
      Cqty  (문자)  체결수량
      Mqty  (문자)  미체결량
      Type  (문자)  주문유형 — 1:시장가 2:지정가 3:STOP 4:STOP LIMIT
      Jprc  (문자)  주문가격
      Sprc  (문자)  STOP가격
      Time  (문자)  주문시간
      Jmgb  (문자)  체결조건 — 0: DAY(당일) 1: GTC 6: GTD
      Date  (문자)  유효일자
      Hsbg  (문자)  행사예약 구분

  공통: rsp_cd  응답코드  ·  rsp_msg  응답메시지
── OUT_END ──────────────────────────────────────────────
"""

#        실거래 위험이 큰 만큼 소액·시뮬레이션으로 충분히 검증한 뒤 사용하세요.
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from dbsec_helper import call_rest, print_response

resp, data = call_rest(
    url="/api/v1/trading/overseas-futureoption/inquiry/order-history",
    body={
        "In": {
        },
    },
    label="주문내역조회",
)
print_response(resp, data)
