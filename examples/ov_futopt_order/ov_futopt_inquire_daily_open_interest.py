"""일별 미결제 약정내역 (ph131101o) — standalone 예제.

그룹    : 해외선물옵션주문
엔드포인트: POST /api/v1/trading/overseas-futureoption/inquiry/daily-open-interest
TPS     : 2
가이드  : https://openapi.dbsec.co.kr/apiservice?group_id=344c4c78-ead3-448a-aeb8-0f6bce60efbc&api_id=6e5baafd-3cc6-43b2-a009-3f4b2c31f331

해외선물옵션 일별 미결제약정내역 조회 API 입니다.

토큰은 examples/dbsec_helper.py 가 자동 발급/캐싱합니다.

실행:
    # examples/ 폴더에서 실행하는 경우:
    python ov_futopt_order/ov_futopt_inquire_daily_open_interest.py
    # examples/ov_futopt_order/ 폴더에서 실행하는 경우:
    python ov_futopt_inquire_daily_open_interest.py

── 응답 파라미터 (Out) ─ OUT_BEGIN ──────────────────────
  [TR ph131101o]
    Out  (오브젝트)  Out
      Ikey  (문자)  키액션
      Sdir  (문자)  정렬방향
      Aflg  (문자)  추가위치
      Ckey  (문자)  연속키
      Nrow  (문자)  열 개수
      Kval  (문자)  다음 키값
    Out1  (오브젝트)  Out1
      Code  (문자)  종목코드
      Msmd  (문자)  매매구분
      Qtyx  (문자)  수량
      Avgp  (문자)  평균단가
      Pric  (문자)  현재가(정산가)
      Pson  (문자)  평가손익
      Hson  (문자)  평가손익증감
      Curr  (문자)  거래통화

  공통: rsp_cd  응답코드  ·  rsp_msg  응답메시지
── OUT_END ──────────────────────────────────────────────
"""

#        실거래 위험이 큰 만큼 소액·시뮬레이션으로 충분히 검증한 뒤 사용하세요.
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from dbsec_helper import call_rest, print_response

resp, data = call_rest(
    url="/api/v1/trading/overseas-futureoption/inquiry/daily-open-interest",
    body={
        "In": {
            "Date": "20260626",  # 조회일자 (str) - 조회하려는 날짜 입력 YYYYMMDD ex.20240101
        },
    },
    label="일별 미결제 약정내역",
)
print_response(resp, data)
