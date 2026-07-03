"""현재가조회 (PRICE) — standalone 예제.

그룹    : 국내주식시세
엔드포인트: POST /api/v1/quote/kr-stock/inquiry/price
TPS     : 5
가이드  : https://openapi.dbsec.co.kr/apiservice?group_id=80005fb0-6feb-4b8b-904a-605c59e29b4f&api_id=d7f6a691-8fe6-4733-901f-c2535417dc46

국내주식 현재가 조회 API입니다.

토큰은 examples/dbsec_helper.py 가 자동 발급/캐싱합니다.

실행:
    # examples/ 폴더에서 실행하는 경우:
    python kr_stock_quote/kr_stock_inquire_price.py
    # examples/kr_stock_quote/ 폴더에서 실행하는 경우:
    python kr_stock_inquire_price.py

── 응답 파라미터 (Out) ─ OUT_BEGIN ──────────────────────
  [TR PRICE]
    Out  (오브젝트)  Out
      PrdyVrss  (문자)  전일대비
      Pbr  (문자)  PBR
      OtstStplQtyIcdc  (문자)  미결제증감
      HtsOtstStplQty  (문자)  미결제약정수량
      Askp1  (문자)  매도호가
      Bidp1  (문자)  매수호가
      PrdyVol  (문자)  전일거래량
      AcmlVol  (문자)  거래량
      AcmlTrPbmn  (문자)  거래대금
      Per  (문자)  PER
      PrdyCtrt  (문자)  전일대비율
      Sdpr  (문자)  기준가
      Prpr  (문자)  현재가
      Mxpr  (문자)  상한가
      Llam  (문자)  하한가
      Oprc  (문자)  시가
      SdprVrssMrktRate  (문자)  기준가대비시가비율
      PrprVrssOprcRate  (문자)  현재가대비시가비율
      Hprc  (문자)  고가
      SdprVrssHgprRate  (문자)  기준가대비고가비율
      Lprc  (문자)  저가
      SdprVrssLwprRate  (문자)  기준가대비저가비율
      PrprVrssLwprRate  (문자)  현재가대비저가비율

  공통: rsp_cd  응답코드  ·  rsp_msg  응답메시지
── OUT_END ──────────────────────────────────────────────
"""


import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from dbsec_helper import call_rest, print_response

resp, data = call_rest(
    url="/api/v1/quote/kr-stock/inquiry/price",
    body={
        "In": {
            "InputIscd1": "005930",  # 입력종목코드1 (str) - 주식(J, NJ, UJ) 선택시 주식종목코드 입력 - J(KRX 주식): - NJ(NXT 주식): - UJ(통합): ※ NXT/통합시세로 종목 조회 시 반드시 종목 앞에 구분자 (N-, U-)를 붙여서 호출 부탁드리겠습니다. 업종(U) 선택시 지수코드: 1001: KOSPI 2001: KOSDAQ 3001: KOSPI200 1002: 코스피(대형주) 1004: 코스피(소형주) 1053: KOSPI50종합지수 1054: KOSPI100종합지수 1163: 코스피고배당50 2002: 코스닥(대형주) 2004: 코스닥(소형주) 2203: 코스닥 150 3903: KP200레버리지지수 3907: 변동성지수 0100: KRX100 0600: KTOP 30 K001: KOVIXI00
            "InputCondMrktDivCode": "J",  # 입력조건시장분류코드 (str) - 주식:J 주식(NXT): NJ 주식(통합): UJ ETN: EN ELW: W 업종&지수: U ※ ETF종목의 경우 J 코드를 사용해 조회 부탁드립니다.
        },
    },
    label="현재가조회",
)
print_response(resp, data)
