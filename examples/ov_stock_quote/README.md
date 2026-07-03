# 해외주식시세 — 예제

group_slug: `ov_stock_quote`

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
| 1 | 해외주식종목 조회 | `FSTKCODES` | [`ov_stock_search_stocks.py`](ov_stock_search_stocks.py) |
| 2 | 해외주식 멀티현재가조회 | `FSTKMULTIPRICE` | [`ov_stock_inquire_price_multi.py`](ov_stock_inquire_price_multi.py) |
| 3 | 해외주식현재가조회 | `FSTKPRICE` | [`ov_stock_inquire_price.py`](ov_stock_inquire_price.py) |
| 4 | 해외주식호가조회 | `FSTKHOGA` | [`ov_stock_inquire_orderbook.py`](ov_stock_inquire_orderbook.py) |
| 5 | 해외주식시간대별체결조회 | `FSTKCONCLUSION` | [`ov_stock_inquire_time_execution.py`](ov_stock_inquire_time_execution.py) |
| 6 | 해외주식 틱차트조회 | `FSTKCHARTTICK` | [`ov_stock_chart_tick.py`](ov_stock_chart_tick.py) |
| 7 | 해외주식 분차트조회 | `FSTKCHARTMIN` | [`ov_stock_chart_min.py`](ov_stock_chart_min.py) |
| 8 | 해외주식 일차트조회 | `FSTKCHARTDAY` | [`ov_stock_chart_day.py`](ov_stock_chart_day.py) |
| 9 | 해외주식 주차트조회 | `FSTKCHARTWEEK` | [`ov_stock_chart_week.py`](ov_stock_chart_week.py) |
| 10 | 해외주식 월차트조회 | `FSTKCHARTMONTH` | [`ov_stock_chart_month.py`](ov_stock_chart_month.py) |
| 11 | 해외주식 상승하락조회 | `FSTKRANKLIST` | [`ov_stock_inquire_condition_rise_fall.py`](ov_stock_inquire_condition_rise_fall.py) |

## 연속조회(자동 페이징) 예제

`call_rest_paged()` 사용법을 보여주는 예시입니다. 시계열·차트처럼 응답이
여러 페이지로 쪼개지는 API 를 한 번 호출로 모두 받아옵니다.

| API 명 | 파일 | 설명 |
|---|---|---|
| 틱차트조회 (페이징) | [`ov_stock_chart_tick_paged.py`](ov_stock_chart_tick_paged.py) | ov_stock_chart_tick.py 와 같은 API 를 자동 페이징으로 호출 |


## 실행

```bash
python examples/ov_stock_quote/<method>.py
```
