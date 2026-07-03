"""기간별 거래내역 조회 (ph135102o) — standalone 예제.

그룹    : 해외선물옵션주문
엔드포인트: POST /api/v1/trading/overseas-futureoption/inquiry/term-trade-history
TPS     : 2
가이드  : https://openapi.dbsec.co.kr/apiservice?group_id=344c4c78-ead3-448a-aeb8-0f6bce60efbc&api_id=964af1f0-b701-453d-8327-c74c3831bebc

기간별 거래내역 조회 API 입니다.

토큰은 examples/dbsec_helper.py 가 자동 발급/캐싱합니다.

조회기간은 최대 31일로 제한됩니다. (ex. 20240101 ~ 20240131)

실행:
    # examples/ 폴더에서 실행하는 경우:
    python ov_futopt_order/ov_futopt_inquire_trading_history.py
    # examples/ov_futopt_order/ 폴더에서 실행하는 경우:
    python ov_futopt_inquire_trading_history.py

── 응답 파라미터 (Out) ─ OUT_BEGIN ──────────────────────
  [TR ph135102o]
    Out  (오브젝트)  Out
      Msqt  (문자)  매수수량 합계
      Mdqt  (문자)  매도수량 합계
      Cqty  (문자)  수량 합계
      Susu  (문자)  수수료 합계
    Out1  (오브젝트)  Out1
      Ikey  (문자)  조회구분
      Sdir  (문자)  정렬방식
      Aflg  (문자)  추가위치
      Ckey  (문자)  다음조회가능여부
      Nrow  (문자)  조회건수
      Kval  (문자)  다음키값
    Out2  (오브젝트)  Out2
      Date  (문자)  거래일자
      Jmno  (문자)  주문번호
      Ojno  (문자)  원주문번호
      Code  (문자)  종목코드
      Mdms  (문자)  매매구분
      Jqty  (문자)  주문수량
      Pric  (문자)  체결가격
      Cqty  (문자)  체결수량
      Susu  (문자)  수수료
      Ogub  (문자)  주문구분
      Time  (문자)  주문시간
      Curr  (문자)  통화코드
      Dltp  (문자)  거래유형코드

  공통: rsp_cd  응답코드  ·  rsp_msg  응답메시지
── OUT_END ──────────────────────────────────────────────
"""

#        실거래 위험이 큰 만큼 소액·시뮬레이션으로 충분히 검증한 뒤 사용하세요.
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from dbsec_helper import call_rest, print_response

resp, data = call_rest(
    url="/api/v1/trading/overseas-futureoption/inquiry/term-trade-history",
    body={
        "In": {
            "Frdt": "20260401",  # 조회일자 from (str) - YYYYMMDD ex.20240101
            "Todt": "20260501",  # 조회일자 to (str) - YYYYMMDD ex.20240115
            "Curr": "USD",  # 통화코드 (str) - "": 전체 "USD": 달러 "JPY": 엔 "HKD": 홍콩달러 "EUR":유로
        },
    },
    label="기간별 거래내역 조회",
)
print_response(resp, data)
