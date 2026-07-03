"""섹터분류코드 조회 (SECTORCOND) — standalone 예제.

그룹    : 국내주식시세
엔드포인트: POST /api/v1/quote/kr-stock/inquiry/sector-cls
TPS     : 2
가이드  : https://openapi.dbsec.co.kr/apiservice?group_id=80005fb0-6feb-4b8b-904a-605c59e29b4f&api_id=5e9ee146-7a0b-4759-a6ef-d778e4d7bedd

국내주식 섹터 분류코드를 조회 할 수 있는 API입니다.

토큰은 examples/dbsec_helper.py 가 자동 발급/캐싱합니다.

실행:
    # examples/ 폴더에서 실행하는 경우:
    python kr_stock_quote/kr_stock_inquire_sector_codes.py
    # examples/kr_stock_quote/ 폴더에서 실행하는 경우:
    python kr_stock_inquire_sector_codes.py

── 응답 파라미터 (Out) ─ OUT_BEGIN ──────────────────────
  [TR SECTORCOND]
    Out  (배열)  Out
      SectorGroupCode  (문자)  섹터그룹코드
      SectorGroupName  (문자)  섹터그룹명

  공통: rsp_cd  응답코드  ·  rsp_msg  응답메시지
── OUT_END ──────────────────────────────────────────────
"""


import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from dbsec_helper import call_rest, print_response

resp, data = call_rest(
    url="/api/v1/quote/kr-stock/inquiry/sector-cls",
    body={
        "In": {
            "InputSectorGroupClsCode": "S",  # 입력섹터그룹구분코드 (str) - "S" 고정
        },
    },
    label="섹터분류코드 조회",
)
print_response(resp, data)
