"""해외주식 체결내역조회 (CAZCQ00100) — standalone 예제.

그룹    : 해외주식주문
엔드포인트: POST /api/v1/trading/overseas-stock/inquiry/transaction-history
TPS     : 2
가이드  : https://openapi.dbsec.co.kr/apiservice?group_id=e4726f55-cc3b-45af-a1b5-852628fe5960&api_id=6aca1814-eea1-4e5c-94da-828143c343f2

해외주식 체결/미체결 내역을 조회하는 API입니다. ※ 모의투자 계좌로 사용가능한 API입니다. ※ 원화환산은 가장 최근 최초고시환율을 기준으로 계산합니다. ※ 체결내역이 전부 표시되지 않는경우 연속키 조회를 통해 확인하실 수 있습니다.

토큰은 examples/dbsec_helper.py 가 자동 발급/캐싱합니다.

실행:
    # examples/ 폴더에서 실행하는 경우:
    python ov_stock_order/ov_stock_inquire_executions.py
    # examples/ov_stock_order/ 폴더에서 실행하는 경우:
    python ov_stock_inquire_executions.py

── 응답 파라미터 (Out) ─ OUT_BEGIN ──────────────────────
  [TR CAZCQ00100]
    Out  (배열)  Out
      OrdDt  (문자)  주문일자
      OrdNo  (숫자)  주문번호
      ExecNo  (숫자)  체결번호
      OrgOrdNo  (숫자)  원주문번호
      AstkIsuNo  (문자)  해외주식종목번호
      AstkHanglIsuNm  (문자)  해외주식한글종목명
      SymCode  (문자)  심볼코드
      OwnSeCode  (문자)  자체증권거래소코드
      AstkSeNm  (문자)  해외주식증권거래소명
      ShtnCntrySymCode  (문자)  단축국가심볼코드
      CntryNm  (문자)  국가명
      AstkBnsTpCode  (문자)  해외주식매매구분코드
      OtptItemNm1  (문자)  출력항목명1
      AstkOrdQty  (숫자)  해외주식주문수량
      AstkOrdPrc  (숫자)  해외주식주문가격
      AstkExecQty  (숫자)  해외주식체결수량
      AstkExecPrc  (숫자)  해외주식체결가격
      AstkOrdRmqty  (숫자)  해외주식주문잔량
      AstkExecAmt  (숫자)  해외주식체결금액
      AstkOrdStatCode  (문자)  해외주식주문상태코드
      AstkBnsMdfyCode  (문자)  해외주식매매정정코드
      OtptItemNm2  (문자)  출력항목명2
      OrdTrdTpCode  (문자)  주문거래구분코드
      OtptItemNm3  (문자)  출력항목명3
      AstkOrdDttm  (문자)  해외주식주문일시
      AstkLclOrdDttm  (문자)  해외주식현지주문일시
      AstkExecDttm  (문자)  해외주식체결일시
      AstkLclExecDttm  (문자)  해외주식현지체결일시
      AstkOrdprcPtnCode  (문자)  해외주식호가유형코드
      OtptItemNm4  (문자)  출력항목명4
      AstkOrdCndiTpCode  (문자)  해외주식주문조건구분코드
      OtptItemNm5  (문자)  출력항목명5
      AstkMktCode  (문자)  해외주식시장코드
      AstkMktNm  (문자)  해외주식시장명
      CrcyCode  (문자)  통화코드
      AstkRjtCode  (문자)  해외주식거부코드
      AstkRjtRsnCnts  (문자)  해외주식거부사유내용
      RsvOrdYn  (문자)  예약주문여부
      RsvOrdDt  (문자)  예약주문일자
      RsvOrdNo  (숫자)  예약주문번호
      AstkRsvOrdPtnCode  (문자)  해외주식예약주문유형코드
      OtptItemNm6  (문자)  출력항목명6
      LoanDt  (문자)  대출일자
      LoanSeqno  (숫자)  대출일련번호
      WonAmt1  (숫자)  원화금액1 — 원화환산 주문가격
      WonAmt2  (숫자)  원화금액2 — 원화환산 체결가격
      WonAmt3  (숫자)  원화금액3 — 원화환산 체결금액
    Out1  (배열)  Out1
      ShtnCntrySymCode  (문자)  단축국가심볼코드
      CntryNm  (문자)  국가명
      CrcyCode  (문자)  통화코드
      AstkSellOrdQty  (숫자)  해외주식매도주문수량
      AstkBuyOrdQty  (숫자)  해외주식매수주문수량
      AstkSellExecQty  (숫자)  해외주식매도체결수량
      AstkBuyExecQty  (숫자)  해외주식매수체결수량

  공통: rsp_cd  응답코드  ·  rsp_msg  응답메시지
── OUT_END ──────────────────────────────────────────────
"""

import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from dbsec_helper import call_rest, print_response

resp, data = call_rest(
    url="/api/v1/trading/overseas-stock/inquiry/transaction-history",
    body={
        "In": {
            "QrySrtDt": "20260210",  # 조회시작일자 (str) - "": 당일조회 기간조회시 YYYYMMDD 형식의 날짜 입력
            "QryEndDt": "20260701",  # 조회종료일자 (str) - "": 당일조회 기간조회시 YYYYMMDD 형식의 날짜 입력
            "AstkIsuNo": "GOOGL",  # 해외주식종목번호 (str) - 미국주식/ETF: "종목코드" 종목코드 미입력시 전체 종목 조회
            "AstkBnsTpCode": "2",  # 해외주식매매구분코드 (str) - 0.전체 1.매도 2.매수
            "OrdxctTpCode": "0",  # 주문체결구분코드 (str) - 0:전체 1:체결 2:미체결
            "StnlnTpCode": "1",  # 정렬구분코드 (str) - 0:역순 1:정순
            "QryTpCode": "1",  # 조회구분코드 (str) - 0:합산별 1:건별
            "OnlineYn": "0",  # 온라인여부 (str) - 0:전체 Y:온라인 N:오프라인
            "WonFcurrTpCode": "1",  # 원화외화구분코드 (str) - 1:원화 2:외화
            "CvrgOrdYn": "N",  # 반대매매주문여부 (str) - 0:전체 Y:반대매매 N:일반주문
        },
    },
    label="해외주식 체결내역조회",
)
print_response(resp, data)
