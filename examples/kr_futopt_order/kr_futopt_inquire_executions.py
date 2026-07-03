"""선물옵션 체결조회 (CFOAQ04000) — standalone 예제.

그룹    : 국내선물옵션주문
엔드포인트: POST /api/v1/trading/kr-futureoption/inquiry/transaction-history
TPS     : 2
가이드  : https://openapi.dbsec.co.kr/apiservice?group_id=44c4a04f-f55e-4c1c-b4e2-b48ec4869aee&api_id=73f68889-f613-4a16-bc1a-5e3cdaf75b0c

선물옵션 주문의 체결 여부 조회가 가능한 API 입니다. ※ 모의투자 계좌로 사용가능한 API입니다.

토큰은 examples/dbsec_helper.py 가 자동 발급/캐싱합니다.

실행:
    # examples/ 폴더에서 실행하는 경우:
    python kr_futopt_order/kr_futopt_inquire_executions.py
    # examples/kr_futopt_order/ 폴더에서 실행하는 경우:
    python kr_futopt_inquire_executions.py

── 응답 파라미터 (Out) ─ OUT_BEGIN ──────────────────────
  [TR CFOAQ04000]
    Out  (배열)  Out
      OrdNo  (숫자)  주문번호
      OrgOrdNo  (숫자)  원주문번호
      FnoIsuNo  (문자)  선물옵션종목번호
      IsuNm  (문자)  종목명
      FnoIsuPtnTpCode  (문자)  선물옵션종목유형구분 — F:선물 C:콜옵션 P:풋옵션 S:스프레드
      BnsTpCode  (문자)  매매구분코드 — 1:매도 2:매수
      MrcTpCode  (문자)  정정취소구분코드 — 0:정상 1:정정 2:취소
      FnoOrdprcPtnCode  (문자)  선물옵션호가유형코드 — 00:지정가 03:시장가 05:조건부지정가 06:최유리지정가
      OrdQty  (숫자)  주문수량
      OrdPrc  (숫자)  주문가격
      AllExecQty  (숫자)  전체체결수량
      AvrExecPrc  (숫자)  평균체결가
      UnercQty  (숫자)  미체결수량
      MrcQty  (숫자)  정정취소수량
      TrxTime  (문자)  처리시각
      OrdTrxStatCode  (문자)  주문처리상태코드 — 01:접수 02:거부 03:확인 04:일부체결 05:전량체결
      MdfyCnfQty  (숫자)  정정확인수량
      BnsplAmt  (숫자)  매매손익금액 — 해당주문에 대한 매매손익금액

  공통: rsp_cd  응답코드  ·  rsp_msg  응답메시지
── OUT_END ──────────────────────────────────────────────
"""

import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from dbsec_helper import call_rest, print_response

resp, data = call_rest(
    url="/api/v1/trading/kr-futureoption/inquiry/transaction-history",
    body={
        "In": {
            "ExecTpCode": "0",  # 체결구분코드 (str) - 0:전체 1:체결 2:미체결
            "BnsTpCode": "0",  # 매매구분코드 (str) - 0:전체 1:매도 2:매수
            "IsuTpCode": "",  # 종목구분코드 (str) - "": 전 종목조회 F:선물 C:콜옵션 P:풋옵션 S:스프레드
            "FnoIsuNo": "",  # 선물옵션종목번호 (str) - 공백 입력시 전 종목 조회 종목번호 입력시 해당 종목만 조회
        },
    },
    label="선물옵션 체결조회",
)
print_response(resp, data)
