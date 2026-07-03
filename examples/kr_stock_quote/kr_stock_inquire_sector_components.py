"""섹터구성종목 조회 (SECTORCONDLIST) — standalone 예제.

그룹    : 국내주식시세
엔드포인트: POST /api/v1/quote/kr-stock/inquiry/sector-components
TPS     : 2
가이드  : https://openapi.dbsec.co.kr/apiservice?group_id=80005fb0-6feb-4b8b-904a-605c59e29b4f&api_id=d11dcc68-9e80-4e53-ac21-ea95172e7416

국내주식 섹터 구성종목을 조회 할 수 있는 API입니다.

토큰은 examples/dbsec_helper.py 가 자동 발급/캐싱합니다.

실행:
    # examples/ 폴더에서 실행하는 경우:
    python kr_stock_quote/kr_stock_inquire_sector_components.py
    # examples/kr_stock_quote/ 폴더에서 실행하는 경우:
    python kr_stock_inquire_sector_components.py

── 응답 파라미터 (Out) ─ OUT_BEGIN ──────────────────────
  [TR SECTORCONDLIST]
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
    url="/api/v1/quote/kr-stock/inquiry/sector-components",
    body={
        "In": {
            "InputSectorGroupClsCode": "S",  # 입력섹터그룹구분코드 (str) - "S" 고정
            "InputRankSortClsCode1": "2",  # 입력순위정렬구분코드 (str) - 2: 시가총액 DESC 4: 현재가 DESC 12: 등락율 DESC 13: 거래량 DESC 42: 거래대금 DESC
            "InputSectorGroupIscd": "9155",  # 입력섹터그룹코드 (str) - 섹터분류코드조회 API에서 조회된 값 사용 ex. "9155"입력시 반도체 대표주 섹터 구성종목 조회
        },
    },
    label="섹터구성종목 조회",
)
print_response(resp, data)
