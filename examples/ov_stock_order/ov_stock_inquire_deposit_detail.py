"""해외주식 예수금상세 (CAZCQ01400) — standalone 예제.

그룹    : 해외주식주문
엔드포인트: POST /api/v1/trading/overseas-stock/inquiry/deposit-detail
TPS     : 2
가이드  : https://openapi.dbsec.co.kr/apiservice?group_id=e4726f55-cc3b-45af-a1b5-852628fe5960&api_id=44fd2ef3-756b-4715-a271-570397b33936

해외주식 상세 예수금을 조회하는 API입니다. ※ 모의투자 계좌로 사용가능한 API입니다. ※ 원화환산은 가장 최근 최초고시환율을 기준으로 계산합니다. ※ 예수금, 주문가능, 출금가능, 평가자산총액 등의 금액은 추정치로 실제와 차이가 있을 수 있습니다.

토큰은 examples/dbsec_helper.py 가 자동 발급/캐싱합니다.

실행:
    # examples/ 폴더에서 실행하는 경우:
    python ov_stock_order/ov_stock_inquire_deposit_detail.py
    # examples/ov_stock_order/ 폴더에서 실행하는 경우:
    python ov_stock_inquire_deposit_detail.py

── 응답 파라미터 (Out) ─ OUT_BEGIN ──────────────────────
  [TR CAZCQ01400]
    Out  (오브젝트)  Out
      OtptItemNm  (문자)  출력항목명
      DpsBaseDt0  (문자)  예수금기준일자0 — 당일기준
      DpsBaseDt1  (문자)  예수금기준일자1 — D+1
      DpsBaseDt2  (문자)  예수금기준일자2 — D+2
      DpsBaseDt3  (문자)  예수금기준일자3 — D+3
      DpsBaseDt4  (문자)  예수금기준일자4 — D+4
    Out1  (배열)  Out1
      CrcyCode  (문자)  통화코드
      CrcyCodeNm  (문자)  통화코드명
      OtptItemNm0  (문자)  출력항목명0
      OtptItemNm1  (문자)  출력항목명1
      OtptItemNm2  (문자)  출력항목명2
      OtptItemNm3  (문자)  출력항목명3
      AstkDps0  (숫자)  해외주식예수금0
      AstkBnsAmt0  (숫자)  해외주식매매금액0
      AstkUnsttBuyAmt0  (숫자)  해외주식미결제매수금액0
      AstkUnsttSellAmt0  (숫자)  해외주식미결제매도금액0
      AstkDps1  (숫자)  해외주식예수금1
      AstkBnsAmt1  (숫자)  해외주식매매금액1
      AstkUnsttBuyAmt1  (숫자)  해외주식미결제매수금액1
      AstkUnsttSellAmt1  (숫자)  해외주식미결제매도금액1
      AstkDps2  (숫자)  해외주식예수금2
      AstkBnsAmt2  (숫자)  해외주식매매금액2
      AstkUnsttBuyAmt2  (숫자)  해외주식미결제매수금액2
      AstkUnsttSellAmt2  (숫자)  해외주식미결제매도금액2
      AstkDps3  (숫자)  해외주식예수금3
      AstkBnsAmt3  (숫자)  해외주식매매금액3
      AstkUnsttBuyAmt3  (숫자)  해외주식미결제매수금액3
      AstkUnsttSellAmt3  (숫자)  해외주식미결제매도금액3
      AstkDps4  (숫자)  해외주식예수금4
      AstkBnsAmt4  (숫자)  해외주식매매금액4
      AstkUnsttBuyAmt4  (숫자)  해외주식미결제매수금액4
      AstkUnsttSellAmt4  (숫자)  해외주식미결제매도금액4

  공통: rsp_cd  응답코드  ·  rsp_msg  응답메시지
── OUT_END ──────────────────────────────────────────────
"""

import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from dbsec_helper import call_rest, print_response

resp, data = call_rest(
    url="/api/v1/trading/overseas-stock/inquiry/deposit-detail",
    body={
        "In": {
        },
    },
    label="해외주식 예수금상세",
)
print_response(resp, data)
