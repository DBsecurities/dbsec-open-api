"""예탁자산현황 (ph131501o) — standalone 예제.

그룹    : 해외선물옵션주문
엔드포인트: POST /api/v1/trading/overseas-futureoption/inquiry/deposit
TPS     : 2
가이드  : https://openapi.dbsec.co.kr/apiservice?group_id=344c4c78-ead3-448a-aeb8-0f6bce60efbc&api_id=875bd9a7-4d03-499b-a721-6cf9adcda634

계좌의 예탁 자산현황 조회 API 입니다.

토큰은 examples/dbsec_helper.py 가 자동 발급/캐싱합니다.

실행:
    # examples/ 폴더에서 실행하는 경우:
    python ov_futopt_order/ov_futopt_inquire_deposit_assets.py
    # examples/ov_futopt_order/ 폴더에서 실행하는 경우:
    python ov_futopt_inquire_deposit_assets.py

── 응답 파라미터 (Out) ─ OUT_BEGIN ──────────────────────
  [TR ph131501o]
    Out  (오브젝트)  Out
      Date  (문자)  조회일자
      Pamt  (문자)  전일예탁금잔액
      Tamt  (문자)  당일예탁금잔액
      Camt  (문자)  입출금액
      Clpl  (문자)  선물청산손익
      Feea  (문자)  수수료
      Inpl  (문자)  선물평가손익
      Bamt  (문자)  옵션매매대금
      Opta  (문자)  옵션시장가치
      Appa  (문자)  예탁자산평가액
      Outa  (문자)  인출가능금액
      Orda  (문자)  주문가능금액
      Uncl  (문자)  미수금
      Daly  (문자)  연체료
      Omrg  (문자)  위탁증거금
      Umrg  (문자)  유지증거금
      Amrg  (문자)  추가증거금필요액
    Out1  (오브젝트)  Out1
      Ikey  (문자)  조회구분
      Sdir  (문자)  정렬방식
      Aflg  (문자)  추가위치
      Ckey  (문자)  다음조회가능여부
      Nrow  (문자)  조회건수
      Kval  (문자)  다음키값
    Out2  (오브젝트)  Out2
      Curr  (문자)  통화코드
      Pamt  (문자)  전일예탁금잔액
      Tamt  (문자)  당일예탁금잔액
      Camt  (문자)  입출금액
      Clpl  (문자)  청산손익
      Feea  (문자)  수수료
      Inpl  (문자)  평가손익
      Bamt  (문자)  옵션매매대금
      Opta  (문자)  옵션시장가치
      Appa  (문자)  예탁자산평가액
      Outa  (문자)  인출가능금액
      Orda  (문자)  주문가능금액
      Uncl  (문자)  미수금
      Daly  (문자)  연체료
      Omrg  (문자)  위탁증거금
      Umrg  (문자)  유지증거금
      Amrg  (문자)  추가증거금필요액

  공통: rsp_cd  응답코드  ·  rsp_msg  응답메시지
── OUT_END ──────────────────────────────────────────────
"""

#        실거래 위험이 큰 만큼 소액·시뮬레이션으로 충분히 검증한 뒤 사용하세요.
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from dbsec_helper import call_rest, print_response

resp, data = call_rest(
    url="/api/v1/trading/overseas-futureoption/inquiry/deposit",
    body={
        "In": {
            "Date": "99999999",  # 조회일자 (str) - YYYYMMDD 형식의 날짜 입력 "99999999": 입력시 당일 날짜로 조회
        },
    },
    label="예탁자산현황",
)
print_response(resp, data)
