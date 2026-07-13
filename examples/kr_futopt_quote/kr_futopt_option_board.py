"""옵션전광판 (OSTOCK_CONDT) — standalone 예제.

그룹    : 국내선물옵션시세
엔드포인트: POST /api/v1/quote/kr-futureoption/inquiry/option-board
TPS     : 1
가이드  : https://openapi.dbsec.co.kr/apiservice?group_id=80d95623-7135-481b-b109-d7370f1a261b&api_id=cc54c7e7-2e86-4688-b5cb-f5630fe48c60

당사 HTS [2501] - "선옵 만기월별시세" 화면과 유시한 기능을 제공하는 국내옵션 전광판 API입니다. ※ 행사가를 기준으로 콜옵션/풋옵션 각 50종목에 대한 정보를 제공 합니다.

토큰은 examples/dbsec_helper.py 가 자동 발급/캐싱합니다.

실행:
    # examples/ 폴더에서 실행하는 경우:
    python kr_futopt_quote/kr_futopt_option_board.py
    # examples/kr_futopt_quote/ 폴더에서 실행하는 경우:
    python kr_futopt_option_board.py

── 응답 파라미터 (Out) ─ OUT_BEGIN ──────────────────────
  [TR OSTOCK_CONDT]
    Out  (오브젝트)  Out
      OptnClsCode  (문자)  옵션구분코드 — 2 : 콜 3 : 풋
      Acpr  (문자)  행사가
      NearAtm  (문자)  ATM구분코드
      Iscd  (문자)  종목코드
      Prpr  (문자)  현재가
      PrdyVrss  (문자)  전일대비
      PrdyVrssSign  (문자)  전일대비부호
      PrdyCtrt  (문자)  전일대비율
      Askp1  (문자)  매도호가1
      Bidp1  (문자)  매수호가1
      CntgVol  (문자)  체결거래량
      TotalAskpCsnu  (문자)  총매도호가건수
      TotalBidpCsnu  (문자)  총매수호가건수
      TotalAskpRsqn  (문자)  총매도호가잔량
      TotalBidpRsqn  (문자)  총매수호가잔량
      AcmlNtbyQty  (문자)  누적순매수수량
      HtsOtstStplQty  (문자)  미결제약정수량
      Oprc  (문자)  시가
      Hprc  (문자)  고가
      Lprc  (문자)  저가
      AntcCnpr  (문자)  예상체결가
      AntcCntgVrss  (문자)  예상체결대비
      AntcCntgVrssSign  (문자)  예상체결대비부호
      AntcCntgPrdyCtrt  (문자)  예상체결전일대비율
      Thpr  (문자)  이론가
      Delta  (문자)  델타
      Gama  (문자)  감마
      Theta  (문자)  쎄타
      Vega  (문자)  베가
      Dprt  (문자)  괴리율
      PsntIntsVltl  (문자)  현재내재변동성
      Invl  (문자)  내재가치
      Tmvl  (문자)  시간가치
      RmnnDynu  (문자)  잔존일수

  공통: rsp_cd  응답코드  ·  rsp_msg  응답메시지
── OUT_END ──────────────────────────────────────────────
"""


import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from dbsec_helper import call_rest, print_response

resp, data = call_rest(
    url="/api/v1/quote/kr-futureoption/inquiry/option-board",
    body={
        "In": {
            "InputCondMrktDivCode1": "O",  # 입력조건시장분류코드1 (str) - O : 지수옵션 KO : 미니옵션 WO : 위클리옵션 EU : 야간옵션 SO : 코스닥 150옵션 EQ : 코스닥 150옵션(야간) EM : 미니옵션(야간) EW : 위클리옵션(야간)
            "InputMtrtYymm1": "202606",  # 입력입력만기년월1 (str) - 일반옵션 : YYYYMM 위클리옵션 : YYMMWW W뒤의 숫자는 주차를 의미
            "InputTrgtClsCode": "",  # 입력대상구분코드 (str) - 위클리 옵션 조회시에만 사용. 그 외 옵션 분류코드 사용시 "" 공백 입력 WKM : 코스피200 위클리 월 만기 WKI : 코스피200 위클리 목 만기 WQM : 코스닥150 위클리 월 만기 WQI : 코스닥150 위클리 목 만기
        },
    },
    label="옵션전광판",
)
print_response(resp, data)
