"""업종구성종목 조회 (USTOCKCONDLIST) — standalone 예제.

그룹    : 국내주식시세
엔드포인트: POST /api/v1/quote/kr-stock/inquiry/industry-components
TPS     : 2
가이드  : https://openapi.dbsec.co.kr/apiservice?group_id=80005fb0-6feb-4b8b-904a-605c59e29b4f&api_id=e75a5938-c6bb-4bb4-b424-06a021f6f560

국내 업종구성종목을 조회 할 수 있는 API 입니다.

토큰은 examples/dbsec_helper.py 가 자동 발급/캐싱합니다.

실행:
    # examples/ 폴더에서 실행하는 경우:
    python kr_stock_quote/kr_stock_inquire_industry_components.py
    # examples/kr_stock_quote/ 폴더에서 실행하는 경우:
    python kr_stock_inquire_industry_components.py

── 응답 파라미터 (Out) ─ OUT_BEGIN ──────────────────────
  [TR USTOCKCONDLIST]
    Out  (배열)  Out
      Iscd  (문자)  종목코드
      KorIsnm  (문자)  한글종목명
      Avls  (문자)  시가총액 — 단위: 100만원
      AvlsRlim  (문자)  시가총액비중
      Prpr  (문자)  현재가
      PrdyVrssSign  (문자)  전일대비부호 — 2: 상승 3: 보합 5: 하락
      PrdyVrss  (문자)  전일대비
      PrdyCtrt  (문자)  전일대비율
      AcmlVol  (문자)  거래량
      AcmlTrPbmn  (문자)  거래대금

  공통: rsp_cd  응답코드  ·  rsp_msg  응답메시지
── OUT_END ──────────────────────────────────────────────
"""


import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from dbsec_helper import call_rest, print_response

resp, data = call_rest(
    url="/api/v1/quote/kr-stock/inquiry/industry-components",
    body={
        "In": {
            "InputBstpIscd": "1024",  # 입력업종코드 (str) - 업종분류코드조회 API에서 조회된 값 사용 ex. "1024"입력시 증권 업종 구성종목 조회
            "InputRankSortClsCode1": "2",  # 입력순위정렬구분코드 (str) - 2: 시가총액 DESC 4: 현재가 DESC 12: 등락율 DESC 13: 거래량 DESC 42: 거래대금 DESC
            "InputCondMrktDivCode": "UJ",  # 입력조건시장분류코드 (str) - "UJ" 고정
        },
    },
    label="업종구성종목 조회",
)
print_response(resp, data)
