"""해외주식 실현손익 조회 (CAZCQ00300) — standalone 예제.

그룹    : 해외주식주문
엔드포인트: POST /api/v1/trading/overseas-stock/inquiry/day-rlzpnl
TPS     : 2
가이드  : https://openapi.dbsec.co.kr/apiservice?group_id=e4726f55-cc3b-45af-a1b5-852628fe5960&api_id=2c20c615-d03a-4afc-92f6-b00aed42eaeb

해외주식 실현손익을 조회하는 API입니다. ※ 모의투자 계좌로 사용가능한 API입니다. ※ 원화환산은 가장 최근 최초고시환율을 기준으로 계산합니다. ※ 실현손익내역이 전부 표시되지 않는경우 연속키 조회를 통해 확인하실 수 있습니다.

토큰은 examples/dbsec_helper.py 가 자동 발급/캐싱합니다.

실행:
    # examples/ 폴더에서 실행하는 경우:
    python ov_stock_order/ov_stock_inquire_realized_pnl.py
    # examples/ov_stock_order/ 폴더에서 실행하는 경우:
    python ov_stock_inquire_realized_pnl.py

── 응답 파라미터 (Out) ─ OUT_BEGIN ──────────────────────
  [TR CAZCQ00300]
    Out2  (배열)  Out2
      AstkMktCode  (문자)  해외주식시장코드
      AstkMktNm  (문자)  해외주식시장명
      OrdDt  (문자)  주문일자
      CrcyCode  (문자)  통화코드
      AstkIsuNo  (문자)  해외주식종목번호
      AstkHanglIsuNm  (문자)  해외주식한글종목명
      SymCode  (문자)  심볼코드
      OwnSeCode  (문자)  자체증권거래소코드
      AstkSeNm  (문자)  해외주식증권거래소명
      ShtnCntrySymCode  (문자)  단축국가심볼코드
      AstkBuyExecQty  (숫자)  해외주식매수체결수량 — 사용안함
      AstkBuyExecAmt  (숫자)  해외주식매수체결금액 — 사용안함
      AstkAvrPchsPrc  (숫자)  해외주식평균매입가
      AstkBuyExecCmsn  (숫자)  해외주식매수체결수수료 — 사용안함
      AstkSellExecQty  (숫자)  해외주식매도체결수량
      AstkSellExecAmt  (숫자)  해외주식매도체결금액
      AstkSellAvrPrc  (숫자)  해외주식매도평균가
      AstkSellExecCmsn  (숫자)  해외주식매도체결수수료
      AstkExecBaseBuyAmt  (숫자)  해외주식체결기준매수금액
      AstkExecBaseBuyCost  (숫자)  해외주식체결기준매수비용
      AstkTaxAmt  (숫자)  해외주식세금금액
      AstkCmsn  (숫자)  해외주식수수료
      AstkCost  (숫자)  해외주식비용
      AstkBnsplAmt  (숫자)  해외주식매매손익금액
      PnlRat  (숫자)  손익율
      BnsplWonAmt  (숫자)  매매손익원화금액
      EvalXchrat  (숫자)  평가환율 — 매도체결 시점의 적용환율
      LoanDt  (문자)  대출일자
    Out3  (오브젝트)  Out3
      BnsplAmt  (숫자)  매매손익금액
      BnsAmt  (숫자)  매매금액
      SellAmt  (숫자)  매도금액
      BuyAmt  (숫자)  매수금액
      CostAmt  (숫자)  비용금액
      Cmsn  (숫자)  수수료
      TaxAmt  (숫자)  세금금액
      PnlRat  (숫자)  손익율

  공통: rsp_cd  응답코드  ·  rsp_msg  응답메시지
── OUT_END ──────────────────────────────────────────────
"""

import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from dbsec_helper import call_rest, print_response

resp, data = call_rest(
    url="/api/v1/trading/overseas-stock/inquiry/day-rlzpnl",
    body={
        "In": {
            "WonFcurrTpCode": "1",  # 원화외화구분코드 (str) - 1:원화 2:외화
            "TrxTpCode": "2",  # 처리구분코드 (str) - 1:국가별 및 일별국가별 실현손익 2:일별국가별종목별 실현손익
            "AstkIsuNo": "",  # 해외주식종목번호 (str) - 미국주식/ETF: "종목코드"
            "QrySrtDt": "20260101",  # 조회시작일자 (str) - YYYYMMDD EX.20240101
            "QryEndDt": "20260501",  # 조회종료일자 (str) - YYYYMMDD EX.20240105
            "EvrprcYn": "Y",  # 제비용여부 (str) - Y:예(기본) N:아니요
            "DpntBalTpCode": "0",  # 소수점잔고구분코드 (str) - 0: 전체 1: 일반 2: 소수점
        },
    },
    label="해외주식 실현손익 조회",
)
print_response(resp, data)
