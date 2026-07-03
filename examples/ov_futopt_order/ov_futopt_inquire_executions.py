"""체결내역 조회 (ph020301o) — standalone 예제.

그룹    : 해외선물옵션주문
엔드포인트: POST /api/v1/trading/overseas-futureoption/inquiry/transaction-history
TPS     : 2
가이드  : https://openapi.dbsec.co.kr/apiservice?group_id=344c4c78-ead3-448a-aeb8-0f6bce60efbc&api_id=5e24f62a-802a-4f80-a86a-102a066bde58

해외선물옵션 체결내역 조회 API 입니다. ※ 내역이 전부 표시되지 않는경우 연속키 조회를 통해 확인하실 수 있습니다.

토큰은 examples/dbsec_helper.py 가 자동 발급/캐싱합니다.

실행:
    # examples/ 폴더에서 실행하는 경우:
    python ov_futopt_order/ov_futopt_inquire_executions.py
    # examples/ov_futopt_order/ 폴더에서 실행하는 경우:
    python ov_futopt_inquire_executions.py

── 응답 파라미터 (Out) ─ OUT_BEGIN ──────────────────────
  [TR ph020301o]
    Out  (오브젝트)  Out
      Ikey  (문자)  조회구분
      Sdir  (문자)  정렬방식
      Aflg  (문자)  추가위치
      Ckey  (문자)  다음조회가능여부
      Nrow  (문자)  조회건수
      Kval  (문자)  다음키값
    Out1  (오브젝트)  Out1
      Jmno  (문자)  주문번호
      Code  (문자)  종목코드
      Mdms  (문자)  매도/매수구분
      Cprc  (문자)  체결가
      Cqty  (문자)  체결수량
      Mqty  (문자)  미체결량
      Ctim  (문자)  체결시간

  공통: rsp_cd  응답코드  ·  rsp_msg  응답메시지
── OUT_END ──────────────────────────────────────────────
"""

#        실거래 위험이 큰 만큼 소액·시뮬레이션으로 충분히 검증한 뒤 사용하세요.
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from dbsec_helper import call_rest, print_response

resp, data = call_rest(
    url="/api/v1/trading/overseas-futureoption/inquiry/transaction-history",
    body={
        "In": {
            "Code": "",  # 종목코드 (str) - "": 기본값(공백) 전체 체결내역 조회 "종목코드": 입력한 종목코드의 체결내역 조회
        },
        "In1": {
            "Sdir": "2",  # 정렬방식 (str) - 1: 오름차순 정렬 2: 내림차순 정렬
        },
    },
    label="체결내역 조회",
)
print_response(resp, data)
