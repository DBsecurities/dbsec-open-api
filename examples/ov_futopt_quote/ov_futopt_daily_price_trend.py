"""일자별 시세추이 (pibo7044) — standalone 예제.

그룹    : 해외선물옵션시세
엔드포인트: POST /api/v1/quote/overseas-futureoption/inquiry/daily-price
TPS     : 2
가이드  : https://openapi.dbsec.co.kr/apiservice?group_id=e1035c5a-edb1-4b7d-8336-04e2ab76ed35&api_id=5b43af78-1f7e-46e2-b96c-054512499a2c

해외선물옵션 일자별 시세추이 조회 API 입니다. ※ 해외선물옵션 API시세 신청이 되어있지 않은 경우 시세를 수신 하실 수 없습니다. ※ API시세(유료) 신청방법 GTS(Happy+ Global) : [1761] API시세 신청

토큰은 examples/dbsec_helper.py 가 자동 발급/캐싱합니다.

실행:
    # examples/ 폴더에서 실행하는 경우:
    python ov_futopt_quote/ov_futopt_daily_price_trend.py
    # examples/ov_futopt_quote/ 폴더에서 실행하는 경우:
    python ov_futopt_daily_price_trend.py

── 응답 파라미터 (Out) ─ OUT_BEGIN ──────────────────────
  [TR pibo7044]
    Out  (오브젝트)  Out
      Code  (문자)  종목코드
      Ikey  (문자)  조회구분
      Sdir  (문자)  정렬방식
      Aflg  (문자)  추가위치
      Ckey  (문자)  다음조회가능여부
      Nrow  (문자)  조회건수
      Kval  (문자)  다음키값
    Out1  (오브젝트)  Out1
      Date  (문자)  영업일자
      Open  (문자)  시가
      High  (문자)  고가
      Lowp  (문자)  저가
      Clos  (문자)  종가
      Diff  (문자)  대비
      Rate  (문자)  대비율
      Tvol  (문자)  누적거래량

  공통: rsp_cd  응답코드  ·  rsp_msg  응답메시지
── OUT_END ──────────────────────────────────────────────
"""


import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from dbsec_helper import call_rest, print_response

resp, data = call_rest(
    url="/api/v1/quote/overseas-futureoption/inquiry/daily-price",
    body={
        "In": {
            "Code": "MESU26",  # 종목코드 (str) - 종목코드 입력
        },
    },
    label="일자별 시세추이",
)
print_response(resp, data)
