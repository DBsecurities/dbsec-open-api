"""국내주식 멀티현재가조회 (MULTIPRICE) — standalone 예제.

그룹    : 국내주식시세
엔드포인트: POST /api/v1/quote/kr-stock/inquiry/multiprice
TPS     : 2
가이드  : https://openapi.dbsec.co.kr/apiservice?group_id=80005fb0-6feb-4b8b-904a-605c59e29b4f&api_id=3abd4f11-4a92-48f3-bc3e-726a97a47905

국내시세 멀티 현재가 조회 API입니다. ※ 1회 호출에 최대 50종목의 시세를 확인 가능합니다. ※ "dataCnt" 필드에 요청할 데이터의 개수를 입력하여 호출이 가능 합니다. (1~50) ※ "dataCnt" 필드의 값과 입력 데이터의 개수가 일치하지 않으면 호출이 불가합니다. ※ 아래와 같이시장구분필드와 종목코드가 1:1 쌍을 이뤄야 호출이 정상적으로 이뤄집니다. - InputCondMrktDivCode1:J (시장구분필드), - InputIscd1:005930 (종목코드) ※ [Input...

토큰은 examples/dbsec_helper.py 가 자동 발급/캐싱합니다.

실행:
    # examples/ 폴더에서 실행하는 경우:
    python kr_stock_quote/kr_stock_inquire_price_multi.py
    # examples/kr_stock_quote/ 폴더에서 실행하는 경우:
    python kr_stock_inquire_price_multi.py

── 응답 파라미터 (Out) ─ OUT_BEGIN ──────────────────────
  [TR MULTIPRICE]
    Out  (배열)  Out
      Iscd  (문자)  종목코드
      KorIsnm  (문자)  한글종목명
      Sdpr  (문자)  기준가
      Prpr  (문자)  현재가
      Mxpr  (문자)  상한가
      Llam  (문자)  하한가
      Oprc  (문자)  시가
      SdprVrssMrktRate  (문자)  기준가대비시가비율
      PrprVrssOprcRate  (문자)  현재가대비시가비율
      Hprc  (문자)  고가
      SdprVrssHgprRate  (문자)  기준가대비고가비율
      PrprVrssHgprRate  (문자)  현재가대비고가비율
      Lprc  (문자)  저가
      SdprVrssLwprRate  (문자)  기준가대비저가비율
      PrprVrssLwprRate  (문자)  현재가대비저가비율
      PrdyVrss  (문자)  전일대비
      PrdyCtrt  (문자)  전일대비율

  공통: rsp_cd  응답코드  ·  rsp_msg  응답메시지
── OUT_END ──────────────────────────────────────────────
"""


import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from dbsec_helper import call_rest, print_response

resp, data = call_rest(
    url="/api/v1/quote/kr-stock/inquiry/multiprice",
    body={
        "In": {
            "dataCnt": 5,  # 호출건수 (str) - 1~50사이의 값 입력
            "InputCondMrktDivCode1": "F",  # 입력조건시장분류코드1 (str) - 주식:J 주식(NXT): NJ 주식(통합): UJ ETN: EN ELW: W 업종&지수: U F : 지수선물 JF : 주식선물 KF : 미니선물 CF : 상품선물 XF : 섹터선물 CM : 야간선물 O : 지수옵션 JO : 주식옵션 KO : 미니옵션 WO : K200위클리옵션 EU : 야간옵션 SO: 코스닥 150옵션 ※ ETF종목의 경우 J 코드를 사용해 조회 부탁드립니다.
            "InputIscd1": "101VC000",  # 입력종목코드1 (str) - 주식(J, NJ, UJ) 선택시 주식종목코드 입력 - J(KRX 주식): - NJ(NXT 주식): - UJ(통합): ※ NXT/통합시세로 종목 조회 시 반드시 종목 앞에 구분자 (N-, U-)를 붙여서 호출 부탁드리겠습니다. 업종(U) 선택시 지수코드: 1001: KOSPI 2001: KOSDAQ 3001: KOSPI200 1002: 코스피(대형주) 1004: 코스피(소형주) 1053: KOSPI50종합지수 1054: KOSPI100종합지수 1163: 코스피고배당50 2002: 코스닥(대형주) 2004: 코스닥(소형주) 2203: 코스닥 150 3903: KP200레버리지지수 3907: 변동성지수 0100: KRX100 0600: KTOP 30 K001: KOVIXI00
            "InputCondMrktDivCode2": "JO",
            "InputIscd2": "211VA038",
            "InputCondMrktDivCode3": "J",
            "InputIscd3": "000660",
            "InputCondMrktDivCode4": "J",
            "InputIscd4": "005930",
            "InputCondMrktDivCode5": "U",
            "InputIscd5": "1001",
        },
    },
    label="국내주식 멀티현재가조회",
)
print_response(resp, data)
