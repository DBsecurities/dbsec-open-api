"""해외주식 매매내역 조회 (CAZCQ00200) — standalone 예제.

그룹    : 해외주식주문
엔드포인트: POST /api/v1/trading/overseas-stock/inquiry/trading-history
TPS     : 2
가이드  : https://openapi.dbsec.co.kr/apiservice?group_id=e4726f55-cc3b-45af-a1b5-852628fe5960&api_id=f70342e8-2f36-4e6f-9a60-807da4fd0522

해외주식 매매내역을 조회하는 API입니다. ※ 모의투자 계좌로 사용가능한 API입니다. ※ 원화환산은 가장 최근 최초고시환율을 기준으로 계산합니다. ※ 매매내역이 전부 표시되지 않는경우 연속키 조회를 통해 확인하실 수 있습니다.

토큰은 examples/dbsec_helper.py 가 자동 발급/캐싱합니다.

실행:
    # examples/ 폴더에서 실행하는 경우:
    python ov_stock_order/ov_stock_inquire_trade_history.py
    # examples/ov_stock_order/ 폴더에서 실행하는 경우:
    python ov_stock_inquire_trade_history.py

── 응답 파라미터 (Out) ─ OUT_BEGIN ──────────────────────
  [TR CAZCQ00200]
    Out  (배열)  Out
      OrdDt  (문자)  주문일자
      OrdNo  (숫자)  주문번호
      AstkMktCode  (문자)  해외주식시장코드
      AstkMktNm  (문자)  해외주식시장명
      AstkIsuNo  (문자)  해외주식종목번호
      AstkHanglIsuNm  (문자)  해외주식한글종목명
      SymCode  (문자)  심볼코드
      OwnSeCode  (문자)  자체증권거래소코드
      AstkSeNm  (문자)  해외주식증권거래소명
      ShtnCntrySymCode  (문자)  단축국가심볼코드
      AstkBnsTpCode  (문자)  해외주식매매구분코드
      BnsTpNm  (문자)  매매구분명
      AstkExecQty  (숫자)  해외주식체결수량
      AstkExecPrc  (숫자)  해외주식체결가격
      AstkExecAmt  (숫자)  해외주식체결금액
      AstkExecCmsn  (숫자)  해외주식체결수수료
      AstkExecLclCmsn  (숫자)  해외주식체결현지수수료
      AstkSettAmt  (숫자)  해외주식결제금액
      CrcyCode  (문자)  통화코드
      SettDt  (문자)  결제일자 — 매도시 유가증권결제일자 매수시 현금결제일자
      MnySettDt  (문자)  현금결제일자
      SecSettDt  (문자)  유가증권결제일자
      RsvOrdDt  (문자)  예약주문일자
      RsvOrdNo  (숫자)  예약주문번호
      AstkRsvOrdPtnCode  (문자)  해외주식예약주문유형코드
      OtptItemNm  (문자)  출력항목명
      LoanDt  (문자)  대출일자
      DpntBalTpNm  (문자)  소수점잔고구분명
    Out1  (오브젝트)  Out1
      AdjstAmt  (숫자)  정산금액
      ExecAmt  (숫자)  체결금액
      Cmsn  (숫자)  수수료
      TaxAmt  (숫자)  세금금액

  공통: rsp_cd  응답코드  ·  rsp_msg  응답메시지
── OUT_END ──────────────────────────────────────────────
"""

import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from dbsec_helper import call_rest, print_response

resp, data = call_rest(
    url="/api/v1/trading/overseas-stock/inquiry/trading-history",
    body={
        "In": {
            "QrySrtDt": "20260101",  # 조회시작일자 (str) - YYYYMMDD EX.20240101
            "QryEndDt": "20260501",  # 조회종료일자 (str) - YYYYMMDD EX.20240105
            "AstkIsuNo": "",  # 해외주식종목번호 (str) - 미국주식/ETF: "종목코드" "" 공백 입력시 전체 종목 조회
            "AstkBnsTpCode": "0",  # 해외주식매매구분코드 (str) - 0:전체 1:매도 2:매수
            "StnlnTpCode": "0",  # 정렬구분코드 (str) - 0:역순 1:정순
            "QryTpCode": "1",  # 조회구분코드 (str) - 0:합산별 1:건별
            "WonFcurrTpCode": "2",  # 원화외화구분코드 (str) - 1:원화 2:외화
            "BaseDdTpCode": "1",  # 기준일구분코드 (str) - 1:매매일 2:결제일
            "DpntBalTpCode": "1",  # 소수점잔고구분코드 (str) - 0:전체 1:일반 2:소수점
        },
    },
    label="해외주식 매매내역 조회",
)
print_response(resp, data)
