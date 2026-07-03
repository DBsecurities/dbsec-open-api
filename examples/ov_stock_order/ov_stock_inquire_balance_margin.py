"""해외주식 잔고/증거금 조회 (CAZCQ00400) — standalone 예제.

그룹    : 해외주식주문
엔드포인트: POST /api/v1/trading/overseas-stock/inquiry/balance-margin
TPS     : 3
가이드  : https://openapi.dbsec.co.kr/apiservice?group_id=e4726f55-cc3b-45af-a1b5-852628fe5960&api_id=8b7f35a4-1d2c-4e56-921d-c0be4611d1ee

해외주식 잔고조회 API 입니다. 보유중인 주식/증거금 잔고에 대한 정보를 제공합니다. ※ 모의투자 계좌로 사용가능한 API입니다. ※ 잔고가 전부 표시되지 않는경우 연속키 조회를 통해 확인하실 수 있습니다. ※ 원화환산은 가장 최근 최초고시환율을 기준으로 계산합니다. ※ 예수금, 잔고평가, 출금가능 등의 금액은 추정치로 실제와 차이가 있을 수 있습니다.

토큰은 examples/dbsec_helper.py 가 자동 발급/캐싱합니다.

실행:
    # examples/ 폴더에서 실행하는 경우:
    python ov_stock_order/ov_stock_inquire_balance_margin.py
    # examples/ov_stock_order/ 폴더에서 실행하는 경우:
    python ov_stock_inquire_balance_margin.py

── 응답 파라미터 (Out) ─ OUT_BEGIN ──────────────────────
  [TR CAZCQ00400]
    Out  (오브젝트)  Out
      Dps  (숫자)  예수금
      OrdAbleAmt  (숫자)  주문가능금액
      MnyoutAbleAmt  (숫자)  출금가능금액
      BalEvalAmt  (숫자)  잔고평가금액
      EvalPnlAmt  (숫자)  평가손익금액
      ErnRat  (숫자)  수익율
      PchsAmt  (숫자)  매입금액
      Cmsn  (숫자)  수수료
      TaxAmt  (숫자)  세금금액
      ThdayRlzPnlAmt  (숫자)  당일실현손익금액
      AssetAmtTotamt  (숫자)  자산금액총액
      UnsttAmt  (숫자)  미결제금액
    Out1  (배열)  Out1
      CrcyCode  (문자)  통화코드
      CrcyCodeNm  (문자)  통화코드명
      FcurrDps  (숫자)  외화예수금
      AstkEstiDps  (숫자)  해외주식추정예수금
      AstkMgn  (숫자)  해외주식증거금
      AstkReBuyAbleAmt  (숫자)  해외주식재매수가능금액
      AstkOrdAbleAmt  (숫자)  해외주식주문가능금액
      AstkMnyoutAbleAmt  (숫자)  해외주식출금가능금액
      AstkUnsttSellAmt  (숫자)  해외주식미결제매도금액
      AstkUnsttBuyAmt  (숫자)  해외주식미결제매수금액
      AstkEvalAmt  (숫자)  해외주식평가금액
      AstkAssetEvalAmt  (숫자)  해외주식자산평가금액
      WonEvalAmt  (숫자)  원화평가금액
      AvrXchrat  (숫자)  평균환율
      Xchrat  (숫자)  환율
      FcurrRcvblAmt  (숫자)  외화미수금액
      AstkOrdAbleAmt0  (숫자)  해외주식주문가능금액0 — 통합증거금주문가능금액
      FcurrOthrCrcyMgn  (숫자)  외화타통화증거금
      OthrCrcyMgnWtAmt  (숫자)  타통화증거금원화환산금액
    Out2  (배열)  Out2
      AstkIsuNo  (문자)  해외주식종목번호
      AstkHanglIsuNm  (문자)  해외주식한글종목명
      SymCode  (문자)  심볼코드
      OwnSeCode  (문자)  자체증권거래소코드
      AstkSeNm  (문자)  해외주식증권거래소명
      ShtnCntrySymCode  (문자)  단축국가심볼코드
      CntryNm  (문자)  국가명
      CrcyCode  (문자)  통화코드
      AstkMktCode  (문자)  해외주식시장코드
      AstkMktNm  (문자)  해외주식시장명
      AstkExecBaseQty  (숫자)  해외주식체결기준수량
      AstkSettBaseQty  (숫자)  해외주식결제기준수량
      AstkRopSetupQty  (숫자)  해외주식질권설정수량
      AstkOrdAbleQty  (숫자)  해외주식주문가능수량
      AstkAvrPchsPrc  (숫자)  해외주식평균매입가
      WonAmt1  (숫자)  원화금액1 — 원화환산평균매입가
      AstkNowPrc  (숫자)  해외주식현재가
      WonAmt2  (숫자)  원화금액2 — 원화환산현재가
      AstkBuyAmt  (숫자)  해외주식매수금액
      WonAmt3  (숫자)  원화금액3 — 원화환산매수금액
      AstkEvalAmt  (숫자)  해외주식평가금액
      WonAmt4  (숫자)  원화금액4 — 원화환산평가금액
      AstkEvalPnlAmt  (숫자)  해외주식평가손익금액
      WonAmt5  (숫자)  원화금액5 — 원화환산평가손익
      EvalPnlRat  (숫자)  평가손익율
      EvalPnlRat0  (숫자)  평가손익율0 — 원화환산손익율
      AstkCmsn  (숫자)  해외주식수수료
      WonAmt6  (숫자)  원화금액6 — 원화환산수수료
      AstkTaxAmt  (숫자)  해외주식세금금액
      WonAmt7  (숫자)  원화금액7 — 원화환산세금금액
      AstkPrdayCmpPrc  (숫자)  해외주식전일대비가격
      WonAmt8  (숫자)  원화금액8 — 원화환산전일대비가격
      AstkUpdnRat  (숫자)  해외주식등락율
      HldWeght  (숫자)  보유비중
      TpVal  (문자)  구분값 — 현금/대출
      DueDt  (문자)  만기일자
      LoanDt  (문자)  대출일자
      LoanAmt  (숫자)  대출금액
      AstkBuyCmsn  (숫자)  해외주식매수수수료
      WonAmt9  (숫자)  원화금액9 — 원화환산매수수수료
      AstkSellCmsn  (숫자)  해외주식매도수수료
      WonAmt0  (숫자)  원화금액0 — 원화환산매도수수료
      AstkCmsnRat  (숫자)  해외주식수수료율 — 고객수수료율
      AstkCmsnRat0  (숫자)  해외주식수수료율0 — 현지매도수수료율
      ThdayRlzPnlAmt  (숫자)  당일실현손익금액
      AstkSellExecQty  (숫자)  해외주식매도체결수량 — 당일매도수량
      AstkSellExecAmt  (숫자)  해외주식매도체결금액 — 당일매도금액
      AstkExecBaseBuyCost  (숫자)  해외주식체결기준매수비용 — 당일매수수수료
      AstkCmsnRat1  (숫자)  해외주식수수료율1 — 현지매수수수료율
    Out3  (배열)  Out3
      ShtnCntrySymCode  (문자)  단축국가심볼코드
      CntryNm  (문자)  국가명
      CrcyCode  (문자)  통화코드
      AstkBuyAmt  (숫자)  해외주식매수금액
      WonAmt1  (숫자)  원화금액1 — 원화환산매수금액
      AstkEvalAmt  (숫자)  해외주식평가금액
      WonAmt2  (숫자)  원화금액2 — 원화환산평가금액
      AstkEvalPnlAmt  (숫자)  해외주식평가손익금액
      WonAmt3  (숫자)  원화금액3 — 원화환산평가손익금액
      EvalPnlRat  (숫자)  평가손익율
      EvalPnlRat0  (숫자)  평가손익율0
      AstkCmsn  (숫자)  해외주식수수료
      WonAmt4  (숫자)  원화금액4 — 원화환산수수료
      AstkTaxAmt  (숫자)  해외주식세금금액
      WonAmt5  (숫자)  원화금액5 — 원화환산세금금액
      AstkBuyCmsn  (숫자)  해외주식매수수수료
      WonAmt6  (숫자)  원화금액6 — 원화환산매수수수료
      AstkSellCmsn  (숫자)  해외주식매도수수료
      WonAmt7  (숫자)  원화금액7 — 원화환산매도수수료

  공통: rsp_cd  응답코드  ·  rsp_msg  응답메시지
── OUT_END ──────────────────────────────────────────────
"""

import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from dbsec_helper import call_rest, print_response

resp, data = call_rest(
    url="/api/v1/trading/overseas-stock/inquiry/balance-margin",
    body={
        "In": {
            "WonFcurrTpCode": "2",  # 원화외화구분코드 (str) - 1:원화 2:외화
            "TrxTpCode": "2",  # 처리구분코드 (str) - 1:외화잔고 2:주식잔고상세 3:주식잔고(국가별) 9:당일실현손익
            "CmsnTpCode": "2",  # 수수료구분코드 (str) - 0:전부 미포함 1:매수제비용만 포함 2:매수제비용+매도제비용
            "DpntBalTpCode": "1",  # 소수점잔고구분코드 (str) - 0: 전체 1: 일반 2: 소수점
        },
    },
    label="해외주식 잔고/증거금 조회",
)
print_response(resp, data)
