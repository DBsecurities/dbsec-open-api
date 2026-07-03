"""호가 & 현재가 조회 (pibo7042) — standalone 예제.

그룹    : 해외선물옵션시세
엔드포인트: POST /api/v1/quote/overseas-futureoption/inquiry/orderbook-price
TPS     : 2
가이드  : https://openapi.dbsec.co.kr/apiservice?group_id=e1035c5a-edb1-4b7d-8336-04e2ab76ed35&api_id=a1345aa1-aa24-4a98-bdc6-73d5120b7035

해외선물옵션 호가 & 현재가 조회 API 입니다. ※ 해외선물옵션 API시세 신청이 되어있지 않은 경우 시세를 수신 하실 수 없습니다. ※ API시세(유료) 신청방법 GTS(Happy+ Global) : [1761] API시세 신청

토큰은 examples/dbsec_helper.py 가 자동 발급/캐싱합니다.

실행:
    # examples/ 폴더에서 실행하는 경우:
    python ov_futopt_quote/ov_futopt_inquire_orderbook_price.py
    # examples/ov_futopt_quote/ 폴더에서 실행하는 경우:
    python ov_futopt_inquire_orderbook_price.py

── 응답 파라미터 (Out) ─ OUT_BEGIN ──────────────────────
  [TR pibo7042]
    Out  (오브젝트)  Out
      Code  (문자)  종목코드
      Last  (문자)  현재가
      Diff  (문자)  대비
      Rate  (문자)  대비율
      Open  (문자)  시가 — 당일 시가
      High  (문자)  고가 — 당일 고가
      Lowp  (문자)  저가 — 당일 저가
      Clos  (문자)  종가 — 전일 종가
      Tvol  (문자)  누적거래량
      Lvol  (문자)  직전체결량
      Htim  (문자)  현재시간
    Out1  (배열)  Out1
      Askp  (문자)  매수호가가격
      Askq  (문자)  매수호가수량
      Askn  (문자)  매수호가건수
    Out2  (배열)  Out2
      Bidp  (문자)  매도호가가격
      Bidq  (문자)  매도호가수량
      Bidn  (문자)  매도호가건수
    Out3  (오브젝트)  Out3
      Taskq  (문자)  누적매수호가수량
      Tbidq  (문자)  누적매도호가수량
      Taskn  (문자)  누적매수호가건수
      Tbidn  (문자)  누적매도호가건수
      Bday  (문자)  영업일

  공통: rsp_cd  응답코드  ·  rsp_msg  응답메시지
── OUT_END ──────────────────────────────────────────────
"""


import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from dbsec_helper import call_rest, print_response

resp, data = call_rest(
    url="/api/v1/quote/overseas-futureoption/inquiry/orderbook-price",
    body={
        "In": {
            "Code": "MESU26",  # 종목코드 (str) - 종목코드 입력
        },
    },
    label="호가 & 현재가 조회",
)
print_response(resp, data)
