"""임의기간수익률집계 (FOCCQ10800) — standalone 예제.

그룹    : 국내주식주문
엔드포인트: POST /api/v1/trading/kr-stock/inquiry/rdterm-ernrate
TPS     : 1
가이드  : https://openapi.dbsec.co.kr/apiservice?group_id=05ac28b8-624f-4115-8aed-cf55f24279dd&api_id=533bd6bd-8ab9-4673-83f3-4146041d871d

설정한 기간동안의 수익률을 집계할 수 있는 API 입니다. ※ 수익률은 전일 체결분까지 반영됩니다.

토큰은 examples/dbsec_helper.py 가 자동 발급/캐싱합니다.

실행:
    # examples/ 폴더에서 실행하는 경우:
    python kr_stock_order/kr_stock_inquire_period_returns.py
    # examples/kr_stock_order/ 폴더에서 실행하는 경우:
    python kr_stock_inquire_period_returns.py

── 응답 파라미터 (Out) ─ OUT_BEGIN ──────────────────────
  [TR FOCCQ10800]
    Out  (배열)  Out
      BaseDt  (문자)  기준일자
      FdEvalAmt  (숫자)  기초평가금액
      EotEvalAmt  (숫자)  기말평가금액
      TermAvrbalAmt  (숫자)  기간평잔금액
      InvstPrftAmt  (숫자)  투자이익금액
      TrstCmsnAmt  (숫자)  수탁수수료금액
      EvrTax  (숫자)  제세금
      InAmt  (숫자)  입금액
      SecinAmt  (숫자)  입고금액
      OutAmt  (숫자)  출금액
      SecoutAmt  (숫자)  출고금액
      MnyinCmpErnRat  (숫자)  입금대비수익율
      TblnBaseErnRat  (숫자)  잔액기준수익율
      AvrbalErnRat  (숫자)  평잔수익율

  공통: rsp_cd  응답코드  ·  rsp_msg  응답메시지
── OUT_END ──────────────────────────────────────────────
"""

import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from dbsec_helper import call_rest, print_response

resp, data = call_rest(
    url="/api/v1/trading/kr-stock/inquiry/rdterm-ernrate",
    body={
        "In": {
            "TermTpCode": "1",  # 기간구분코드 (str) - 1:일별 2:월별
            "QrySrtDt": "20260301",  # 조회시작일자 (str) - YYYYMMDD 형식의 날짤 입력
            "QryEndDt": "20260526",  # 조회종료일자 (str) - YYYYMMDD 형식의 날짤 입력
        },
    },
    label="임의기간수익률집계",
)
print_response(resp, data)
