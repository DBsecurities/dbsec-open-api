# 국내주식/선물차트 — 예제

group_slug: `kr_chart`

각 파일은 **standalone** 입니다. `examples/dbsec_helper.py` 의 공통 헬퍼만 사용합니다.
(토큰 발급·캐싱·응답코드 분류 등 boilerplate 는 헬퍼가 담당)

## 실행 전 준비

```bash
pip install requests pyyaml
cp config.yaml.example config.yaml      # 그리고 prd_app_key/vtl_app_key 입력
python examples/auth/token_issue.py     # 토큰을 루트 .dbsec_token.json 에 캐시
```

## API 목록

| # | API 명 | TR 코드 | 파일 |
|---:|---|---|---|
| 1 | 틱차트조회 | `CHARTTICK` | [`kr_chart_chart_tick.py`](kr_chart_chart_tick.py) |
| 2 | 분차트조회 | `CHARTMIN` | [`kr_chart_chart_min.py`](kr_chart_chart_min.py) |
| 3 | 일차트조회 | `CHARTDAY` | [`kr_chart_chart_day.py`](kr_chart_chart_day.py) |
| 4 | 주차트조회 | `CHARTWEEK` | [`kr_chart_chart_week.py`](kr_chart_chart_week.py) |
| 5 | 월차트조회 | `CHARTMONTH` | [`kr_chart_chart_month.py`](kr_chart_chart_month.py) |

## 연속조회(자동 페이징) 예제

`call_rest_paged()` 사용법을 보여주는 예시입니다. 시계열·차트처럼 응답이
여러 페이지로 쪼개지는 API 를 한 번 호출로 모두 받아옵니다.

| API 명 | 파일 | 설명 |
|---|---|---|
| 틱차트조회 (페이징) | [`kr_chart_chart_tick_paged.py`](kr_chart_chart_tick_paged.py) | kr_chart_chart_tick.py 와 같은 API 를 자동 페이징으로 호출 |


## 실행

```bash
python examples/kr_chart/<method>.py
```

## 공통 입력 필드 참고

차트 API 들이 공유하는 입력 필드 중 자주 헷갈리거나 빈 문자열의 의미가 비직관적인 항목입니다. 전체 필드 명세는 각 API 의 [DB증권 OpenAPI 가이드](https://openapi.dbsec.co.kr/apiservice) 페이지를 확인하세요.

### `dataCnt` — 호출 건수 (틱차트·분차트)

| 항목 | 내용 |
|---|---|
| 타입 | String (최대 4자리) |
| 필수 | Y |
| 입력 범위 | `"1"` ~ `"2000"` |
| 빈 값/0 처리 | `""` (공백) 또는 `"0"` 입력 시 **기본개수 400개** 조회 |
| 적용 API | `kr_chart_chart_tick`, `kr_chart_chart_min`, `kr_chart_chart_tick_paged` |

예시:

```python
"dataCnt": "5"      # 5건만 조회
"dataCnt": ""       # 기본 400건 조회 (= "0" 과 동일)
"dataCnt": "2000"   # 최대치
```

> 일/주/월차트(`day`, `week`, `month`)는 `dataCnt` 대신 `InputDate1`/`InputDate2` 로 조회 구간을 지정합니다.
