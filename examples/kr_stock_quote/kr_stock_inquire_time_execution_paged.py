"""국내주식 시간대별체결조회 — 자동 페이징(연속조회) standalone 예제.

그룹    : 국내주식시세
엔드포인트: POST /api/v1/quote/kr-stock/inquiry/hour-price
TPS     : 3
가이드  : https://openapi.dbsec.co.kr/apiservice?group_id=80005fb0-6feb-4b8b-904a-605c59e29b4f&api_id=01b99bab-7f12-4098-97e1-99fdda029ca2

같은 API 의 단건 호출 예제: kr_stock_inquire_time_execution.py
이 파일은 같은 API 를 "자동 페이징" 으로 호출하는 예시입니다.

────────────────────────────────────────────────────────────
1. 연속조회(Pagination) 가 뭐고 왜 필요한가?
────────────────────────────────────────────────────────────
시간대별 체결은 장중 체결 한 건 한 건이 시간 순으로 쌓이는 데이터라
하루치만 해도 양이 매우 많습니다. DB증권 API 는 이를 한 번에 통째로
주지 않고 여러 "페이지" 로 나눠서 응답합니다. 응답 헤더의
cont_yn / cont_key 가 다음 페이지 위치를 가리킵니다.

요청 헤더              →  응답 헤더                       의미
─────────────────────     ──────────────────────────────   ───────────────────────
cont_yn=N, cont_key=""    cont_yn=Y, cont_key="K1"         더 있음. 다음엔 K1로 호출
cont_yn=Y, cont_key="K1"  cont_yn=Y, cont_key="K2"         또 있음
cont_yn=Y, cont_key="K2"  cont_yn=N                        끝 (= 마지막 페이지)

이 cont_yn / cont_key 흐름을 사용자가 직접 다루지 않도록 도와주는 함수가
call_rest_paged 입니다. 호출 한 번이면 모든 페이지를 알아서 받아옵니다.

────────────────────────────────────────────────────────────
2. call_rest_paged 의 주요 인자
────────────────────────────────────────────────────────────
  url         : API 엔드포인트 (단건과 동일)
  body        : 요청 body. 페이지마다 동일하게 재사용됨 (cont_key 는 헤더로만 변함)
  page_sleep  : 페이지 사이 대기 시간(초). TPS 한도 초과 방지
                  · 2 TPS API → 0.5 (기본)
                  · 1 TPS API → 1.0 권장
                  본 API 는 3 TPS 라 0.5 면 안전.
  max_pages   : 받을 페이지 수 상한. "" (공백) 입력시 전체 페이지 조회,
                  페이지 수(예: 3) 입력시 해당 페이지만큼만 호출.
  verbose     : True 면 페이지마다 본문 전체 출력 (기본 False — 진행 한 줄 요약은 progress=True 가 담당)
                  데이터는 어차피 반환 list 에 그대로 보존되므로
                  페이지가 많을 땐 False 가 콘솔 보기 편합니다.
  cont_key    : 비우면 처음부터. 값을 주면 그 키부터 이어받기 (이전 세션 재개용)

────────────────────────────────────────────────────────────
3. 반환값
────────────────────────────────────────────────────────────
list[(resp, data), (resp, data), ...] — 페이지 수만큼 (resp, data) 쌍이 담긴 list.
모든 페이지의 데이터를 합쳐서 후처리하는 예시는 파일 하단 참고.

토큰은 examples/dbsec_helper.py 가 자동 발급/캐싱합니다.

실행:
    # examples/ 폴더에서 실행하는 경우:
    python kr_stock_quote/kr_stock_inquire_time_execution_paged.py
    # examples/kr_stock_quote/ 폴더에서 실행하는 경우:
    python kr_stock_inquire_time_execution_paged.py

── 응답 파라미터 (Out) ─ OUT_BEGIN ──────────────────────
  [TR CONCLUSION]
    Out  (오브젝트)  Out
      Hour  (문자)  시간
      Prpr  (문자)  현재가
      PrdyVrssSign  (문자)  전일대비부호
      PrdyCtrt  (문자)  전일대비율
      CntgVol  (문자)  체결거래량

  공통: rsp_cd  응답코드  ·  rsp_msg  응답메시지
── OUT_END ──────────────────────────────────────────────
"""

import json
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from dbsec_helper import call_rest_paged


# ─────────────────────────────────────────
# 자동 페이징 호출
# ─────────────────────────────────────────
# 시간대별 체결은 장중 체결 한 건씩 시간 순으로 쌓이는 데이터라 양이 매우 많아
# 첫 호출에 모두 받지 못하고 서버가 cont_yn=Y 로 "다음 페이지 있음" 을
# 알려주는 전형적인 케이스. call_rest_paged 가 자동으로 이어 받습니다.
pages = call_rest_paged(
    url="/api/v1/quote/kr-stock/inquiry/hour-price",
    body={
        "In": {
            "InputCondMrktDivCode": "J",  # 입력조건시장분류코드 (str) - 주식:J 주식(NXT): NJ 주식(통합): UJ ETN: EN ELW: W ※ ETF종목의 경우 J 코드를 사용해 조회 부탁드립니다.
            "InputIscd1": "005930",  # 입력종목코드1 (str) - 종목코드 입력 - J(KRX 주식): - NJ(NXT 주식): - UJ(통합): ※ NXT/통합시세로 종목 조회 시 반드시 종목 앞에 구분자 (N-, U-)를 붙여서 호출 부탁드리겠습니다.
        },
    },
    label="국내주식 시간대별체결조회 (페이징)",
    page_sleep=0.5,    # 3 TPS API → 0.5초로 충분
    max_pages="10",    # "" 공백 입력시 전체 페이지 조회, 페이지 수(예: 3) 입력시 해당 페이지만큼만 호출
    # 진행 표시: 기본(progress=True)으로 페이지마다 한 줄 요약이 출력됩니다.
    # verbose=True 면 본문 전체 출력.
)


# ─────────────────────────────────────────
# 모든 페이지 데이터 합치기 예시
# ─────────────────────────────────────────
# pages 는 [(resp, data), ...] 형태이고, data 는 페이지별 응답 본문.
# 시간대별 체결처럼 각 페이지에 list 가 들어 있으면 이어 붙여서 분석에 사용합니다.
print()
print("━" * 72)
print(f"수신한 페이지 수: {len(pages)}")
print("━" * 72)

merged = []
for page_no, (resp, data) in enumerate(pages, 1):
    # 응답 본문에서 첫 번째 list 필드를 찾아 누적 (필드명은 API 마다 다름; Out1 / Out2 등)
    for key, value in data.items():
        if isinstance(value, list):
            merged.extend(value)
            print(f"  page {page_no}: {key} = {len(value)} 건")
            break

print(f"\n총 누적 레코드: {len(merged)} 건")
if merged:
    print("첫 레코드 sample:")
    print(json.dumps(merged[0], ensure_ascii=False, indent=2))
