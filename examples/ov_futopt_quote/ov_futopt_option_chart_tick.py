"""해외옵션 틱차트조회 (pibg7401) — standalone 예제.

그룹    : 해외선물옵션시세
엔드포인트: POST /api/v1/quote/overseas-futureoption/option-chart/tick
TPS     : 10
가이드  : https://openapi.dbsec.co.kr/apiservice?group_id=e1035c5a-edb1-4b7d-8336-04e2ab76ed35&api_id=32cc74fd-28c0-4756-a7ff-369b56c90df1

해외옵션 틱 차트 조회 API 입니다. ※ 해외선물옵션 API시세 신청이 되어있지 않은 경우 시세를 수신 하실 수 없습니다. ※ API시세(유료) 신청방법 GTS(Happy+ Global) : [1761] API시세 신청

토큰은 examples/dbsec_helper.py 가 자동 발급/캐싱합니다.

실행:
    # examples/ 폴더에서 실행하는 경우:
    python ov_futopt_quote/ov_futopt_option_chart_tick.py
    # examples/ov_futopt_quote/ 폴더에서 실행하는 경우:
    python ov_futopt_option_chart_tick.py

── 응답 파라미터 (Out) ─ OUT_BEGIN ──────────────────────
  [TR pibg7401]
    Out  (오브젝트)  Out
      Pind  (문자)  price indicator
      Nrec  (문자)  조회건수
      Ikey  (문자)  조회구분
      Sdir  (문자)  정렬방식
      Aflg  (문자)  추가위치
      Ckey  (문자)  다음조회가능여부
      Nrow  (문자)  조회건수
      Kval  (문자)  다음키값
    Out1  (오브젝트)  Out1
      Date  (문자)  체결일자
      Bday  (문자)  영업일자
      Time  (문자)  체결시간
      Clos  (문자)  종가
      Lvol  (문자)  체결량
      Open  (문자)  시가
      High  (문자)  고가
      Lowp  (문자)  저가

  공통: rsp_cd  응답코드  ·  rsp_msg  응답메시지
── OUT_END ──────────────────────────────────────────────
"""


import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from dbsec_helper import call_rest, print_response

resp, data = call_rest(
    url="/api/v1/quote/overseas-futureoption/option-chart/tick",
    body={
        "In": {
            "Code": "OESU26_C7400",  # 종목코드 (str) - 종목코드 입력
            "Tick": "900",  # N tick (str) - N틱 (최대 900틱)
            "Dcnt": "10",  # 조회건수 (str) - 요청 데이터건수 (최대400건)
            "Dedt": "99999999",  # 조회일자 (str) - 조회일자입력: YYYYMMDD 당일인 경우: 99999999
        },
    },
    label="해외옵션 틱차트조회",
)
print_response(resp, data)
