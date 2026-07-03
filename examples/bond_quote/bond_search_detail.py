"""장내채권 상세검색 (BO_SEARCH) — standalone 예제.

그룹    : 장내채권시세
엔드포인트: POST /api/v1/quote/krx-bond/search
TPS     : 2
가이드  : https://openapi.dbsec.co.kr/apiservice?group_id=b86989c1-9666-42d2-a446-492376f71f1b&api_id=ed6b9416-bd89-4c99-9a8a-7599f0e14474

장내채권 상세검색 API 입니다.

토큰은 examples/dbsec_helper.py 가 자동 발급/캐싱합니다.

실행:
    # examples/ 폴더에서 실행하는 경우:
    python bond_quote/bond_search_detail.py
    # examples/bond_quote/ 폴더에서 실행하는 경우:
    python bond_search_detail.py

── 응답 파라미터 (Out) ─ OUT_BEGIN ──────────────────────
  [TR BO_SEARCH]
    Out  (배열)  Out
      StndIscd  (문자)  표준종목코드
      KorIsnm  (문자)  한글종목명
      BondClsName  (문자)  채권구분명
      CrdtVltnGrad1  (문자)  신용평가등급1
      IntKindName  (문자)  이자지급방법
      Prpr  (문자)  현재가
      PrdyVrss  (문자)  전일대비
      PrdyVrssSign  (문자)  전일대비부호
      BondCntgErt  (문자)  체결수익률
      RdmpDate  (문자)  상환일
      SrfcMnrt  (문자)  표면금리

  공통: rsp_cd  응답코드  ·  rsp_msg  응답메시지
── OUT_END ──────────────────────────────────────────────
"""


import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from dbsec_helper import call_rest, print_response

resp, data = call_rest(
    url="/api/v1/quote/krx-bond/search",
    body={
        "In": {
            "InputSerhName": "국고",  # 입력검색명 (str) - 기본값: "" 종목명으로 검색 가능 EX. 국고
            "InputBondStndIscd": "0",  # 입력채권구분코드 (str) - 0:채권종류(전체) 1:국채 2:지방채 3:회사채 4:특수채 5:금융채 6:일반사채 7:주식관련사채
            "InputCrdtClsCode": "0",  # 입력신용구분코드 (str) - 0:신용등급(전체) 1:AAA+ ~ AAA- 2:AA+ ~ AA- 3:A+ ~ A- 4:BBB+ ~ BBB- 5:BBB- 미만 6:없음
            "InputDivClsCode": "0",  # 입력분류구분코드 (str) - 0:이자종류(전체) 1:할인채 2:복리채 3:단리채 4:이표채
            "InputRmnnDynu1": "0",  # 입력잔존일수1 (str) - 0:잔존기간(전체) 1:6개월 내 2:6개월~1년 3:1년~2년 4:2년~3년
            "InputCompDiviType": "0",  # 입력비교구분코드 (str) - 0: 수익률조건 전체 1:이상 2:이하
            "InputCntgErt1": "3",  # 입력수익률1 (str) - 수익률 입력 (정수만 입력가능) EX. 3
        },
    },
    label="장내채권 상세검색",
)
print_response(resp, data)
