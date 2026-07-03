# 국내주식시세 — 예제

group_slug: `kr_stock_quote`

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
| 1 | 주식종목 조회 | `JCODES` | [`kr_stock_search_stocks.py`](kr_stock_search_stocks.py) |
| 2 | ELW 종목 조회 | `WCODES` | [`kr_stock_inquire_elw_stock.py`](kr_stock_inquire_elw_stock.py) |
| 3 | 국내주식 멀티현재가조회 | `MULTIPRICE` | [`kr_stock_inquire_price_multi.py`](kr_stock_inquire_price_multi.py) |
| 4 | 현재가조회 | `PRICE` | [`kr_stock_inquire_price.py`](kr_stock_inquire_price.py) |
| 5 | 호가조회 | `HOGA` | [`kr_stock_inquire_orderbook.py`](kr_stock_inquire_orderbook.py) |
| 6 | 시간대별체결조회 | `CONCLUSION` | [`kr_stock_inquire_time_execution.py`](kr_stock_inquire_time_execution.py) |
| 7 | 일별체결조회 | `DAYTRADE` | [`kr_stock_inquire_daily_executions.py`](kr_stock_inquire_daily_executions.py) |
| 8 | 주식조건상승하락조회 | `RANKLIST` | [`kr_stock_inquire_condition_rise_fall.py`](kr_stock_inquire_condition_rise_fall.py) |
| 9 | 일별업종별투자자조회 | `UPTJJDAY` | [`kr_stock_inquire_daily_industry_investor.py`](kr_stock_inquire_daily_industry_investor.py) |
| 10 | 일별종목별투자자조회 | `DAYSTOCKTJJ` | [`kr_stock_inquire_daily_issue_investor.py`](kr_stock_inquire_daily_issue_investor.py) |
| 11 | 국내 ETF/ETN 구성종목조회 | `ETFCOMPCODE` | [`kr_stock_inquire_etf_etn_stock.py`](kr_stock_inquire_etf_etn_stock.py) |
| 12 | 섹터분류코드 조회 | `SECTORCOND` | [`kr_stock_inquire_sector_codes.py`](kr_stock_inquire_sector_codes.py) |
| 13 | 섹터구성종목 조회 | `SECTORCONDLIST` | [`kr_stock_inquire_sector_components.py`](kr_stock_inquire_sector_components.py) |
| 14 | 업종분류코드 조회 | `USTOCKCOND` | [`kr_stock_inquire_industry_codes.py`](kr_stock_inquire_industry_codes.py) |
| 15 | 업종구성종목 조회 | `USTOCKCONDLIST` | [`kr_stock_inquire_industry_components.py`](kr_stock_inquire_industry_components.py) |

## 연속조회(자동 페이징) 예제

`call_rest_paged()` 사용법을 보여주는 예시입니다. 시계열·차트처럼 응답이
여러 페이지로 쪼개지는 API 를 한 번 호출로 모두 받아옵니다.

| API 명 | 파일 | 설명 |
|---|---|---|
| 시간대별체결조회 (페이징) | [`kr_stock_inquire_time_execution_paged.py`](kr_stock_inquire_time_execution_paged.py) | kr_stock_inquire_time_execution.py 와 같은 API 를 자동 페이징으로 호출 |


## 실행

```bash
python examples/kr_stock_quote/<method>.py
```
