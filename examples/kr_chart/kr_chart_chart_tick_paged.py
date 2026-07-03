"""틱차트조회 — 자동 페이징(연속조회) standalone 예제.

그룹    : 국내주식/선물차트
엔드포인트: POST /api/v1/quote/kr-chart/tick
TPS     : 4
가이드  : https://openapi.dbsec.co.kr/apiservice?group_id=0bc09824-e8c2-491a-8c9d-b99e64b4b907&api_id=efe731f7-0f2a-45d1-81da-335ebeacd552

같은 API 의 단건 호출 예제: kr_chart_chart_tick.py
이 파일은 같은 API 를 "자동 페이징" 으로 호출하는 예시입니다.

────────────────────────────────────────────────────────────
1. 연속조회(Pagination) 가 뭐고 왜 필요한가?
────────────────────────────────────────────────────────────
틱차트는 1초보다 짧은 단위의 모든 체결을 시간 순으로 내려주기 때문에
하루치만 해도 수만 건이 나옵니다. DB증권 API 는 이를 한 번에 통째로
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
                  본 API 는 4 TPS 라 0.5 면 충분히 안전.
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
    python kr_chart/kr_chart_chart_tick_paged.py
    # examples/kr_chart/ 폴더에서 실행하는 경우:
    python kr_chart_chart_tick_paged.py

── 응답 파라미터 (Out) ─ OUT_BEGIN ──────────────────────
  [TR CHARTTICK]
    Out  (배열)  Out
      Hour  (문자)  시간
      Date  (문자)  일자
      Prpr  (문자)  현재가
      Oprc  (문자)  시가
      Hprc  (문자)  고가
      Lprc  (문자)  저가
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
# 틱은 거래가 일어날 때마다 한 건씩 쌓이므로 하루치만 해도 데이터가 매우 많음.
# 한 페이지에 못 담겨 서버가 cont_yn=Y 로 "다음 페이지 있음" 을 알려주는
# 전형적인 케이스. call_rest_paged 가 cont_yn=Y 인 동안 자동으로 이어 받습니다.
pages = call_rest_paged(
    url="/api/v1/quote/kr-chart/tick",
    body={
        "In": {
            "dataCnt": "",  # 호출건수 (str) - 입력범위: "1" ~ "2000" ""(공백입력) 또는 "0" 입력시 기본개수(400개)조회
            "InputOrgAdjPrc": "1",  # 수정주가사용여부 (str) - 0:수정주가 미사용 1: 수정주가 사용
            "InputCondMrktDivCode": "J",  # 입력조건시장분류코드 (str) - 주식:J 주식(NXT): NJ 주식(통합): UJ EN : ETN W: ELW F : 지수선물 JF : 주식선물 KF : 미니선물 CF : 상품선물 XF : 섹터선물 CM : 야간선물 O : 지수옵션 JO : 주식옵션 KO : 미니옵션 WO : K200위클리옵션 EU : 야간옵션 SO: 코스닥 150옵션 업종&지수: U ※ ETF종목의 경우 J 코드를 사용해 조회 부탁드립니다.
            "InputIscd1": "005930",  # 입력종목코드1 (str) - 주식(J, NJ, UJ) 선택시 주식종목코드 입력 - J(KRX 주식): - NJ(NXT 주식): - UJ(통합): ※ NXT/통합시세로 종목 조회 시 반드시 종목 앞에 구분자 (N-, U-)를 붙여서 호출 부탁드리겠습니다. 업종(U) 선택시 지수코드: 1001: KOSPI 2001: KOSDAQ 3001: KOSPI200 1002: 코스피(대형주) 1004: 코스피(소형주) 1053: KOSPI50종합지수 1054: KOSPI100종합지수 1163: 코스피고배당50 2002: 코스닥(대형주) 2004: 코스닥(소형주) 2203: 코스닥 150 3903: KP200레버리지지수 3907: 변동성지수 0100: KRX100 0600: KTOP 30 K001: KOVIXI00
            "InputDate1": "20260526",  # 입력날짜1 (str) - 조회 시작일을 YYYYMMDD 형식으로 입력 ex. 20241204
            "InputDivXtick": "100",  # 틱분틱일별구분코드 (str) - N Tick 입력 ex. 100
        },
    },
    label="틱차트조회 (페이징)",
    page_sleep=0.5,    # 4 TPS API → 0.5초로 충분
    max_pages="10",    # "" 공백 입력시 전체 페이지 조회, 페이지 수(예: 3) 입력시 해당 페이지만큼만 호출
    # 진행 표시: 기본(progress=True)으로 페이지마다 한 줄 요약이 출력됩니다.
    # verbose=True 면 본문 전체 출력.
)


# ─────────────────────────────────────────
# 모든 페이지 데이터 합치기 예시
# ─────────────────────────────────────────
# pages 는 [(resp, data), ...] 형태이고, data 는 페이지별 응답 본문.
# 틱처럼 각 페이지에 list 가 들어 있으면 이어 붙여서 분석에 사용합니다.
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
