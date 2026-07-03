"""옵션종목 조회 (OCODES) — standalone 예제.

그룹    : 국내선물옵션시세
엔드포인트: POST /api/v1/quote/kr-futureoption/inquiry/option-ticker
TPS     : 10
가이드  : https://openapi.dbsec.co.kr/apiservice?group_id=80d95623-7135-481b-b109-d7370f1a261b&api_id=a51e61c7-a77f-408c-99bd-69f1ae4df730

국내옵션 종목조회 API입니다. ※ 연속키 조회를 통해 종목을 추가로 조회 할 수 있습니다.

토큰은 examples/dbsec_helper.py 가 자동 발급/캐싱합니다.

실행:
    # examples/ 폴더에서 실행하는 경우:
    python kr_futopt_quote/kr_futopt_search_options.py
    # examples/kr_futopt_quote/ 폴더에서 실행하는 경우:
    python kr_futopt_search_options.py

── 응답 파라미터 (Out) ─ OUT_BEGIN ──────────────────────
  [TR OCODES]
    Out  (배열)  Out
      Mxpr1st  (문자)  1단계상한가
      UnasIsnm  (문자)  기초자산명
      Mxpr2nd  (문자)  2단계상한가
      Mxpr3rd  (문자)  3단계상한가
      Llam1st  (문자)  1단계하한가
      Llam2nd  (문자)  2단계하한가
      Llam3rd  (문자)  3단계하한가
      Acpr  (문자)  행사가
      RmnnDynu  (문자)  잔존만기
      Iscd  (문자)  종목코드
      StndIscd  (문자)  표준종목코드
      KorIsnm  (문자)  한글종목명
      AtmClsCode  (문자)  ATM구분코드
      TrMltl  (문자)  거래승수

  공통: rsp_cd  응답코드  ·  rsp_msg  응답메시지
── OUT_END ──────────────────────────────────────────────
"""


import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from dbsec_helper import call_rest, print_response

resp, data = call_rest(
    url="/api/v1/quote/kr-futureoption/inquiry/option-ticker",
    body={
        "In": {
            "InputCondMrktDivCode": "O",  # 입력조건시장분류코드 (str) - O : 지수옵션 JO : 주식옵션 KO : 미니옵션 WO : K200위클리옵션 EU : 야간옵션 SO : 코스닥 150옵션 EQ : KOSDAQ150옵션(야간) EM : 미니옵션(야간) EW : 위클리옵션(야간)
        },
    },
    label="옵션종목 조회",
)
print_response(resp, data)
