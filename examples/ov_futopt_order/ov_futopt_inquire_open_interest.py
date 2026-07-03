"""미결제 약정 조회 (ph020401o) — standalone 예제.

그룹    : 해외선물옵션주문
엔드포인트: POST /api/v1/trading/overseas-futureoption/inquiry/open-interest
TPS     : 2
가이드  : https://openapi.dbsec.co.kr/apiservice?group_id=344c4c78-ead3-448a-aeb8-0f6bce60efbc&api_id=5025f940-6dea-44d0-aa3a-80872f14cce7

해외선물옵션 미결제 약정 조회 API 입니다. ※ 내역이 전부 표시되지 않는경우 연속키 조회를 통해 확인하실 수 있습니다.

토큰은 examples/dbsec_helper.py 가 자동 발급/캐싱합니다.

실행:
    # examples/ 폴더에서 실행하는 경우:
    python ov_futopt_order/ov_futopt_inquire_open_interest.py
    # examples/ov_futopt_order/ 폴더에서 실행하는 경우:
    python ov_futopt_inquire_open_interest.py

── 응답 파라미터 (Out) ─ OUT_BEGIN ──────────────────────
  [TR ph020401o]
    Out  (오브젝트)  Out
      Ikey  (문자)  조회구분
      Sdir  (문자)  정렬방식
      Aflg  (문자)  추가위치
      Ckey  (문자)  다음조회가능여부
      Nrow  (문자)  조회건수
      Kval  (문자)  다음키값
    Out1  (오브젝트)  Out1
      Code  (문자)  종목코드
      Curr  (문자)  통화코드
      Mdms  (문자)  매도/매수구분
      Pqty  (문자)  미결제수량
      Rqty  (문자)  전일미결제수량
      Avgc  (문자)  평균가
      Lprc  (문자)  현재가
      Pamt  (문자)  평가손익
      Cqty  (문자)  청산가능수량
      Tsiz  (문자)  TickSize
      Tval  (문자)  TickValue
      Aval  (문자)  가격조정계수
      Oprc  (문자)  미결제약정 수량X체결가 — 약정가(체결가) X 미결제 약정 수량 합산

  공통: rsp_cd  응답코드  ·  rsp_msg  응답메시지
── OUT_END ──────────────────────────────────────────────
"""

#        실거래 위험이 큰 만큼 소액·시뮬레이션으로 충분히 검증한 뒤 사용하세요.
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from dbsec_helper import call_rest, print_response

resp, data = call_rest(
    url="/api/v1/trading/overseas-futureoption/inquiry/open-interest",
    body={
        "In": {
            "Hsbg": "",  # 행사예약구분 (str) - "": 기본값 공백 Y: 옵션 주문 행사예약구분 Y인 경우 만 조회 N: 옵션 주문 행사예약구분 N인 경우 만 조회
        },
        "In1": {
            "Sdir": "2",  # 정렬방식 (str) - 1: 오름차순 정렬 2: 내림차순 정렬
        },
    },
    label="미결제 약정 조회",
)
print_response(resp, data)
