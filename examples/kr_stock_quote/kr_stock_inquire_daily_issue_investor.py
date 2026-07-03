"""일별종목별투자자조회 (DAYSTOCKTJJ) — standalone 예제.

그룹    : 국내주식시세
엔드포인트: POST /api/v1/quote/kr-stock/inquiry/daily-investor
TPS     : 2
가이드  : https://openapi.dbsec.co.kr/apiservice?group_id=80005fb0-6feb-4b8b-904a-605c59e29b4f&api_id=2a750d3d-5ea2-4bb6-b3d6-411956d42e75

국내 일별종목별투자자조회 API입니다.

토큰은 examples/dbsec_helper.py 가 자동 발급/캐싱합니다.

실행:
    # examples/ 폴더에서 실행하는 경우:
    python kr_stock_quote/kr_stock_inquire_daily_issue_investor.py
    # examples/kr_stock_quote/ 폴더에서 실행하는 경우:
    python kr_stock_inquire_daily_issue_investor.py

── 응답 파라미터 (Out) ─ OUT_BEGIN ──────────────────────
  [TR DAYSTOCKTJJ]
    Out  (오브젝트)  Out
      Date  (문자)  일자
      Prpr  (문자)  현재가
      PrdyVrssSign  (문자)  전일대비부호
      PrdyVrss  (문자)  전일대비
      PrdyCtrt  (문자)  전일대비율
      AcmlVol  (문자)  거래량
      AcmlTrPbmn  (문자)  거래대금
      OrgnShnuVol  (문자)  기관계매수수량
      OrgnSelnVol  (문자)  기관계매도수량
      OrgnShnuTrPbmn  (문자)  기관계매수금액
      OrgnSelnTrPbmn  (문자)  기관계매도금액
      FrgnRegShnuVol  (문자)  외국인매수수량
      FrgnRegSelnVol  (문자)  외국인매도수량
      FrgnRegShnuTrPbmn  (문자)  외국인매수금액
      FrgnRegSelnTrPbmn  (문자)  외국인매도금액
      PrsnShnuVol  (문자)  개인매수수량
      PrsnSelnVol  (문자)  개인매도수량
      PrsnShnuTrPbmn  (문자)  개인매수금액
      PrsnSelnTrPbmn  (문자)  개인매도금액

  공통: rsp_cd  응답코드  ·  rsp_msg  응답메시지
── OUT_END ──────────────────────────────────────────────
"""


import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from dbsec_helper import call_rest, print_response

resp, data = call_rest(
    url="/api/v1/quote/kr-stock/inquiry/daily-investor",
    body={
        "In": {
            "InputCondMrktDivCode": "J",  # 입력조건시장분류코드 (str) - 주식&ETF:J 주식(NXT): NJ 주식(통합): UJ ETN: EN ELW: W
            "InputIscd1": "005930",  # 입력종목코드1 (str) - 종목코드 입력 - J(KRX 주식): - NJ(NXT 주식): - UJ(통합): ※ NXT/통합시세로 종목 조회 시 반드시 종목 앞에 구분자 (N-, U-)를 붙여서 호출 부탁드리겠습니다.
            "InputDate1": "20250425",  # 입력날짜1 (str) - YYYYMMDD
            "InputDate2": "20250425",  # 입력날짜2 (str) - YYYYMMDD
        },
    },
    label="일별종목별투자자조회",
)
print_response(resp, data)
