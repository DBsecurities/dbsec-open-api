"""계좌별신용한도조회 (CSPAQ00600) — standalone 예제.

그룹    : 국내주식주문
엔드포인트: POST /api/v1/trading/kr-stock/inquiry/able-crdlimit
TPS     : 1
가이드  : https://openapi.dbsec.co.kr/apiservice?group_id=05ac28b8-624f-4115-8aed-cf55f24279dd&api_id=485bffdb-5d83-4ab0-8707-e115602e6280

종목에 대한 신용 한도를 조회할 수 있는 API 입니다. ※ 모의투자 계좌로 사용가능한 API입니다. ※ 신용 약정등록이 완료된 계좌만 사용가능합니다.

토큰은 examples/dbsec_helper.py 가 자동 발급/캐싱합니다.

실행:
    # examples/ 폴더에서 실행하는 경우:
    python kr_stock_order/kr_stock_inquire_credit_limit.py
    # examples/kr_stock_order/ 폴더에서 실행하는 경우:
    python kr_stock_inquire_credit_limit.py

── 응답 파라미터 (Out) ─ OUT_BEGIN ──────────────────────
  [TR CSPAQ00600]
    Out  (오브젝트)  Out
      OrdPrc  (숫자)  주문가
      SloanLmtAmt  (숫자)  대주한도
      SloanAmtSum  (숫자)  대주금액합계
      SloanNewAmt  (숫자)  대주신규금액
      SloanRfundAmt  (숫자)  대주상환금액
      MktcplMloanLmtAmt  (숫자)  유통융자한도금액
      MktcplMloanAmtSum  (숫자)  유통융자금액합계
      MktcplMloanNewAmt  (숫자)  유통융자신규금액
      MktcplMloanRfundAmt  (숫자)  유통융자상환금액
      SfaccMloanLmtAmt  (숫자)  자기융자한도금액
      SfaccMloanAmtSum  (숫자)  자기융자금액합계
      SfaccMloanNewAmt  (숫자)  자기융자신규금액
      SfaccMloanRfundAmt  (숫자)  자기융자상환금액
      BrnMktcplMloanLmtAmt  (숫자)  지점유통융자한도금액 — 내용확인필요
      BrnMktcplMloanNewAmt  (숫자)  지점유통융자신규금액
      BrnMktcplMloanRfundAmt  (숫자)  지점유통융자상환금액
      BrnMktcplMloanUseAmt  (숫자)  지점유통융자사용금액
      BrnSfaccMloanLmtAmt  (숫자)  지점자기융자한도금액
      BrnSfaccMloanNewAmt  (숫자)  지점자기융자신규금액
      BrnSfaccMloanRfundAmt  (숫자)  지점자기융자상환금액
      BrnSfaccMloanUseAmt  (숫자)  지점자기융자사용금액
      FirmMloanLmtMgmtYn  (문자)  이용사융자한도관리여부
      FirmCrdtIsuRestrcTp  (문자)  이용사신용종목제한구분
      PldgMaintRat  (숫자)  담보유지비율
      FirmNm  (문자)  이용사명
      PldgRat  (숫자)  담보비율
      DpsastSum  (숫자)  예탁자산합계
      LmtChgAbleAmt  (숫자)  한도변경가능금액
      OrdAbleAmt  (숫자)  주문가능금액
      OrdAbleQty  (숫자)  주문가능수량
      RcvblUablOrdAbleQty  (숫자)  미수불가주문가능수량

  공통: rsp_cd  응답코드  ·  rsp_msg  응답메시지
── OUT_END ──────────────────────────────────────────────
"""

import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from dbsec_helper import call_rest, print_response

resp, data = call_rest(
    url="/api/v1/trading/kr-stock/inquiry/able-crdlimit",
    body={
        "In": {
            "LoanDtlClssCode": "01",  # 대출상세분류코드 (str) - 01 : 유통융자 03 : 자기융자 05 : 유통대주 07 : 자기대주
            "IsuNo": "A005930",  # 종목번호 (str) - 주식/ETF: 종목코드6자리 or "A"+"종목코드" ETN: Q + 종목코드 ELW: J + 종목코드
            "OrdPrc": 78000,  # 주문가 (int)
        },
    },
    label="계좌별신용한도조회",
)
print_response(resp, data)
