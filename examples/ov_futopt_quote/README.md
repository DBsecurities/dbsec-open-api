# 해외선물옵션시세 — 예제

group_slug: `ov_futopt_quote`

> ⚠️ **운영(production) 전용 그룹** — DB증권 해외선물옵션은 시스템 차원에서 모의투자를 지원하지 않습니다.
> `config.yaml` 의 `environment.mode` 를 `"production"` 으로 두고 `prd_app_key`/`prd_app_secret` 를 사용해야 합니다.
> demo 모드에서 호출하면 `dbsec_helper` 가 명확한 에러로 차단합니다.

각 파일은 **standalone** 입니다. `examples/dbsec_helper.py` 의 공통 헬퍼만 사용합니다.
(토큰 발급·캐싱·응답코드 분류 등 boilerplate 는 헬퍼가 담당)

## 실행 전 준비

```bash
pip install requests pyyaml
cp config.yaml.example config.yaml      # mode: "production" + prd_app_key/prd_app_secret 입력
python examples/auth/token_issue.py     # 토큰을 루트 .dbsec_token.json 에 캐시
```

## API 목록

| # | API 명 | TR 코드 | 파일 |
|---:|---|---|---|
| 1 | 호가 & 현재가 조회 | `pibo7042` | [`ov_futopt_inquire_orderbook_price.py`](ov_futopt_inquire_orderbook_price.py) |
| 2 | 일자별 시세추이 | `pibo7044` | [`ov_futopt_daily_price_trend.py`](ov_futopt_daily_price_trend.py) |
| 3 | 해외선물 틱차트조회 | `pibg7301` | [`ov_futopt_future_chart_tick.py`](ov_futopt_future_chart_tick.py) |
| 4 | 해외선물 분차트조회 | `pibg7302` | [`ov_futopt_future_chart_min.py`](ov_futopt_future_chart_min.py) |
| 5 | 해외선물 일주월차트조회 | `pibg7303` | [`ov_futopt_future_chart_day_week_month.py`](ov_futopt_future_chart_day_week_month.py) |
| 6 | 해외옵션 틱차트조회 | `pibg7401` | [`ov_futopt_option_chart_tick.py`](ov_futopt_option_chart_tick.py) |
| 7 | 해외옵션 분차트조회 | `pibg7402` | [`ov_futopt_option_chart_min.py`](ov_futopt_option_chart_min.py) |
| 8 | 해외옵션 일주월차트조회 | `pibg7403` | [`ov_futopt_option_chart_day_week_month.py`](ov_futopt_option_chart_day_week_month.py) |

## 실행

```bash
python examples/ov_futopt_quote/<method>.py
```
