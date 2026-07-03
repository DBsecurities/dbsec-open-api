"""옵션종목 조회 — 자동 페이징(연속조회) standalone 예제.

그룹    : 국내선물옵션시세
엔드포인트: POST /api/v1/quote/kr-futureoption/inquiry/option-ticker
TPS     : 10
가이드  : https://openapi.dbsec.co.kr/apiservice?group_id=80d95623-7135-481b-b109-d7370f1a261b&api_id=a51e61c7-a77f-408c-99bd-69f1ae4df730

같은 API 의 단건 호출 예제: kr_futopt_search_options.py
이 파일은 같은 API 를 "자동 페이징" 으로 호출하는 예시입니다.

이 API 는 가이드에서도 명시적으로 "연속키 조회를 통해 종목을 추가로 조회 할 수
있습니다" 라고 안내하는 케이스 — 옵션 종목 마스터가 한 페이지에 다 담기지 않음.

────────────────────────────────────────────────────────────
1. 연속조회(Pagination) 가 뭐고 왜 필요한가?
────────────────────────────────────────────────────────────
옵션은 행사가·만기별로 종목 수가 매우 많아 한 번 호출에 결과 전체를
통째로 내려주지 않고, 양이 많으면 여러 "페이지" 로 나눠서 응답합니다.
응답 헤더의 cont_yn / cont_key 가 다음 페이지 위치를 가리킵니다.

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
                  본 API 는 10 TPS 라 0.5 면 매우 여유 있음.
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
    python kr_futopt_quote/kr_futopt_search_options_paged.py
    # examples/kr_futopt_quote/ 폴더에서 실행하는 경우:
    python kr_futopt_search_options_paged.py

── 응답 파라미터 (Out) ─ OUT_BEGIN ──────────────────────
  [TR OCODES]
    Out  (배열)  Out
      Mxpr1st  (문자)  1단계상한가
      UnasIsnm  (문자)  기초자산명
      Mxpr2nd  (문자)  2단계상한가
      Mxpr3rd  (문자)  3단계상한가
      Llam1st  (문자)  1단계하한가
      Llam2nd  (문자)  2단계하한가
      Llam3rd  (문자)  3단계하한가
      Acpr  (문자)  행사가
      RmnnDynu  (문자)  잔존만기
      Iscd  (문자)  종목코드
      StndIscd  (문자)  표준종목코드
      KorIsnm  (문자)  한글종목명
      AtmClsCode  (문자)  ATM구분코드
      TrMltl  (문자)  거래승수

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
# 옵션 종목 수가 많아 첫 호출에 모두 받지 못하고 서버가 cont_yn=Y 로
# "다음 페이지 있음" 을 알려주는 대표적인 페이징 케이스.
# call_rest_paged 가 cont_yn=Y 인 동안 자동으로 다음 페이지를 이어 받습니다.
pages = call_rest_paged(
    url="/api/v1/quote/kr-futureoption/inquiry/option-ticker",
    body={
        "In": {
            "InputCondMrktDivCode": "O",  # 입력조건시장분류코드 (str) - O : 지수옵션 JO : 주식옵션 KO : 미니옵션 WO : K200위클리옵션 EU : 야간옵션 SO : 코스닥 150옵션 EQ : KOSDAQ150옵션(야간) EM : 미니옵션(야간) EW : 위클리옵션(야간)
        },
    },
    label="옵션종목 조회 (페이징)",
    page_sleep=0.5,    # 10 TPS API → 0.5초로 매우 안전
    max_pages="10",    # "" 공백 입력시 전체 페이지 조회, 페이지 수(예: 3) 입력시 해당 페이지만큼만 호출
    # 진행 표시: 기본(progress=True)으로 페이지마다 한 줄 요약이 출력됩니다.
    # verbose=True 면 본문 전체 출력.
)


# ─────────────────────────────────────────
# 모든 페이지 데이터 합치기 예시
# ─────────────────────────────────────────
# pages 는 [(resp, data), ...] 형태이고, data 는 페이지별 응답 본문.
# 옵션 종목처럼 각 페이지에 list 가 들어 있으면 이어 붙여서 분석에 사용합니다.
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
