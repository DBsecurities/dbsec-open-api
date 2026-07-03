"""선물옵션 체결조회 (야간) (CFOHQ04000) — standalone 예제.

그룹    : 국내선물옵션주문
엔드포인트: POST /api/v1/trading/night-futureoption/inquiry/cmedt
TPS     : 2
가이드  : https://openapi.dbsec.co.kr/apiservice?group_id=44c4a04f-f55e-4c1c-b4e2-b48ec4869aee&api_id=fc852deb-cbd0-451c-a66e-83aa282cede2

야간선물옵션 체결조회 API 입니다. ※ 체결내역이 전부 표시되지 않는경우 연속키 조회를 통해 확인하실 수 있습니다.

토큰은 examples/dbsec_helper.py 가 자동 발급/캐싱합니다.

실행:
    # examples/ 폴더에서 실행하는 경우:
    python kr_futopt_order/kr_futopt_inquire_executions_night.py
    # examples/kr_futopt_order/ 폴더에서 실행하는 경우:
    python kr_futopt_inquire_executions_night.py

── 응답 파라미터 (Out) ─ OUT_BEGIN ──────────────────────
  [TR CFOHQ04000]
    Out  (배열)  Out
      OrdNo  (숫자)  주문번호
      OrgOrdNo  (숫자)  원주문번호
      FnoIsuNo  (문자)  선물옵션종목번호
      IsuNm  (문자)  종목명
      PrdgrpClssCode  (문자)  상품군분류코드
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
    url="/api/v1/trading/night-futureoption/inquiry/cmedt",
    body={
        "In": {
            "IsuTpCode": "F",  # 종목구분코드 (str) - F:선물 C:콜옵션 P:풋옵션 S:스프레드
            "FnoIsuNo": "",  # 선물옵션종목번호 (str) - "": 전체 종목 조회 (종목번호 입력시 해당 종목만 조회)
            "ExecTpCode": "2",  # 체결구분코드 (str) - 0:전체 1:체결 2:미체결
            "BnsTpCode": "0",  # 매매구분코드 (str) - 0:전체 1:매도 2:매수
        },
    },
    label="선물옵션 체결조회 (야간)",
)
print_response(resp, data)
