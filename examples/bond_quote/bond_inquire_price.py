"""장내채권 현재가조회 (BO_SISE) — standalone 예제.

그룹    : 장내채권시세
엔드포인트: POST /api/v1/quote/krx-bond/inquiry/price
TPS     : 2
가이드  : https://openapi.dbsec.co.kr/apiservice?group_id=b86989c1-9666-42d2-a446-492376f71f1b&api_id=106586fa-701b-49f8-9d21-eefe8b81e1a6



토큰은 examples/dbsec_helper.py 가 자동 발급/캐싱합니다.

실행:
    # examples/ 폴더에서 실행하는 경우:
    python bond_quote/bond_inquire_price.py
    # examples/bond_quote/ 폴더에서 실행하는 경우:
    python bond_inquire_price.py

── 응답 파라미터 (Out) ─ OUT_BEGIN ──────────────────────
  [TR BO_SISE]
    Out  (오브젝트)  Out
      Prpr  (문자)  현재가
      PrdyVrss  (문자)  전일대비
      PrdyVrssSign  (문자)  전일대비부호
      PrdyCtrt  (문자)  전일대비율
      AcmlVol  (문자)  누적거래량
      PrdyErt  (문자)  전일수익률
      Mxpr  (문자)  상한가
      Llam  (문자)  하한가
      PrdyClpr  (문자)  전일종가

  공통: rsp_cd  응답코드  ·  rsp_msg  응답메시지
── OUT_END ──────────────────────────────────────────────
"""


import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from dbsec_helper import call_rest, print_response

resp, data = call_rest(
    url="/api/v1/quote/krx-bond/inquiry/price",
    body={
        "In": {
            "InputIscd1": "KR101501DDC7",  # 입력종목코드1 (str) - 채권 종목코드 입력
            "InputCondMrktDivCode": "B",  # 입력조건시장분류코드 (str) - 소액:SB 일반:B
        },
    },
    label="장내채권 현재가조회",
)
print_response(resp, data)
