"""해외주식 거래내역 조회 (CAZCQ01600) — standalone 예제.

그룹    : 해외주식주문
엔드포인트: POST /api/v1/trading/overseas-stock/inquiry/trade-history
TPS     : 2
가이드  : https://openapi.dbsec.co.kr/apiservice?group_id=e4726f55-cc3b-45af-a1b5-852628fe5960&api_id=141f22b1-b905-4f65-a462-6a0a744f3075

해외주식 계좌의 거래내역을 조회하는 API입니다. ※ 모의투자 계좌로 사용가능한 API입니다. ※ 거래내역이 전부 표시되지 않는경우 연속키 조회를 통해 확인하실 수 있습니다.

토큰은 examples/dbsec_helper.py 가 자동 발급/캐싱합니다.

실행:
    # examples/ 폴더에서 실행하는 경우:
    python ov_stock_order/ov_stock_inquire_trading_history.py
    # examples/ov_stock_order/ 폴더에서 실행하는 경우:
    python ov_stock_inquire_trading_history.py

── 응답 파라미터 (Out) ─ OUT_BEGIN ──────────────────────
  [TR CAZCQ01600]
    Out  (배열)  Out
      TrdDt  (문자)  거래일자
      TrdTime  (문자)  거래시각
      SmryNm  (문자)  적요명
      AstkIsuNo  (문자)  해외주식종목번호
      AstkEngIsuNm  (문자)  해외주식영문종목명
      AstkHanglIsuNm  (문자)  해외주식한글종목명
      AstkMktCode  (문자)  해외주식시장코드
      SymCode  (문자)  심볼코드
      OwnSeCode  (문자)  자체증권거래소코드
      AstkSeNm  (문자)  해외주식증권거래소명
      CrcyCode  (문자)  통화코드
      AstkTrdQty  (숫자)  해외주식거래수량
      AstkBnsAmt  (숫자)  해외주식매매금액
      AstkTrdUprc  (숫자)  해외주식거래단가
      AstkCmsn  (숫자)  해외주식수수료
      AstkTaxAmt  (숫자)  해외주식세금금액
      AstkCrbalQty  (숫자)  해외주식금잔수량
      AstkAppXchrat  (숫자)  해외주식적용환율
      FcurrTrdAmt  (숫자)  외화거래금액
      FcurrDpsCrbalAmt  (숫자)  외화예수금금잔금액
      TrdAmt  (숫자)  거래금액
      DpsCrbalAmt  (숫자)  예수금금잔금액
      FcurrRcvblRepayAmt  (숫자)  외화미수변제금액
      FcurrRcvblOcrAmt  (숫자)  외화미수발생금액
      FcurrRcvblAmt  (숫자)  외화미수금액
      FcurrOdpnt  (숫자)  외화연체료
      OppAcntNo  (문자)  상대계좌번호
      OppAcntNm  (문자)  상대계좌명
      OthbkpOppCoNo  (문자)  타사대체상대회사번호
      BkeepIttNm  (문자)  대체기관명

  공통: rsp_cd  응답코드  ·  rsp_msg  응답메시지
── OUT_END ──────────────────────────────────────────────
"""

import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from dbsec_helper import call_rest, print_response

resp, data = call_rest(
    url="/api/v1/trading/overseas-stock/inquiry/trade-history",
    body={
        "In": {
            "QryTpCode": "0",  # 조회구분코드 (str) - 0:전체 1:입출금 2:입출고 3:매매
            "StnlnTpCode": "1",  # 정렬구분코드 (str) - 0:역순 1:정순
            "AstkIsuNo": "",  # 해외주식종목번호 (str) - 미국주식/ETF: "종목코드"
            "QrySrtDt": "20260101",  # 조회시작일자 (str) - YYYYMMDD EX.20240101
            "QryEndDt": "20260501",  # 조회종료일자 (str) - YYYYMMDD EX.20240110
            "DpntBalTpCode": "0",  # 소수점잔고구분코드 (str) - 0: 전체 1: 일반 2: 소수점
        },
    },
    label="해외주식 거래내역 조회",
)
print_response(resp, data)
