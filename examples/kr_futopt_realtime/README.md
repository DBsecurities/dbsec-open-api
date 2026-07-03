# 국내선물옵션시세(실시간) — 예제

group_slug: `kr_futopt_realtime`

각 파일은 **standalone** 입니다. `examples/dbsec_helper.py` 의 공통 헬퍼만 사용합니다.
(토큰 발급·캐싱·응답코드 분류 등 boilerplate 는 헬퍼가 담당)

## 실행 전 준비

```bash
pip install requests pyyaml  websockets
cp config.yaml.example config.yaml      # 그리고 prd_app_key/vtl_app_key 입력
python examples/auth/token_issue.py     # 토큰을 루트 .dbsec_token.json 에 캐시
```

## API 목록

| # | API 명 | TR 코드 | 파일 |
|---:|---|---|---|
| 1 | [실시간]선물옵션주문체결 | `IF0` | [`kr_futopt_realtime_order_execution.py`](kr_futopt_realtime_order_execution.py) |
| 2 | [실시간]지수선물호가 | `F01` | [`kr_futopt_realtime_index_future_orderbook.py`](kr_futopt_realtime_index_future_orderbook.py) |
| 3 | [실시간]지수선물체결가 | `F00` | [`kr_futopt_realtime_index_future_execution_price.py`](kr_futopt_realtime_index_future_execution_price.py) |
| 4 | [실시간]미니지수선물호가 | `F91` | [`kr_futopt_realtime_mini_index_future_orderbook.py`](kr_futopt_realtime_mini_index_future_orderbook.py) |
| 5 | [실시간]미니지수선물체결가 | `F90` | [`kr_futopt_realtime_mini_index_future_execution_price.py`](kr_futopt_realtime_mini_index_future_execution_price.py) |
| 6 | [실시간]섹터지수선물호가 | `F71` | [`kr_futopt_realtime_sector_index_future_orderbook.py`](kr_futopt_realtime_sector_index_future_orderbook.py) |
| 7 | [실시간]섹터지수선물체결 | `F70` | [`kr_futopt_realtime_sector_index_future_execution.py`](kr_futopt_realtime_sector_index_future_execution.py) |
| 8 | [실시간]주식선물호가 | `F21` | [`kr_futopt_realtime_stock_future_orderbook.py`](kr_futopt_realtime_stock_future_orderbook.py) |
| 9 | [실시간]주식선물체결 | `F20` | [`kr_futopt_realtime_stock_future_execution.py`](kr_futopt_realtime_stock_future_execution.py) |
| 10 | [실시간]상품선물호가 | `F11` | [`kr_futopt_realtime_commodity_future_orderbook.py`](kr_futopt_realtime_commodity_future_orderbook.py) |
| 11 | [실시간]상품선물체결가 | `F10` | [`kr_futopt_realtime_commodity_future_execution_price.py`](kr_futopt_realtime_commodity_future_execution_price.py) |
| 12 | [실시간]지수옵션호가 | `O01` | [`kr_futopt_realtime_index_option_orderbook.py`](kr_futopt_realtime_index_option_orderbook.py) |
| 13 | [실시간]지수옵션체결 | `O00` | [`kr_futopt_realtime_index_option_execution.py`](kr_futopt_realtime_index_option_execution.py) |
| 14 | [실시간]주식옵션호가 | `O21` | [`kr_futopt_realtime_stock_option_orderbook.py`](kr_futopt_realtime_stock_option_orderbook.py) |
| 15 | [실시간]주식옵션체결가 | `O20` | [`kr_futopt_realtime_stock_option_execution_price.py`](kr_futopt_realtime_stock_option_execution_price.py) |
| 16 | [실시간]미니지수옵션호가 | `O91` | [`kr_futopt_realtime_mini_index_option_orderbook.py`](kr_futopt_realtime_mini_index_option_orderbook.py) |
| 17 | [실시간]미니지수옵션체결가 | `O90` | [`kr_futopt_realtime_mini_index_option_execution_price.py`](kr_futopt_realtime_mini_index_option_execution_price.py) |
| 18 | [실시간]K200지수위클리옵션호가 | `OB1` | [`kr_futopt_realtime_k200_weekly_option_orderbook.py`](kr_futopt_realtime_k200_weekly_option_orderbook.py) |
| 19 | [실시간]K200지수위클리옵션체결 | `OB0` | [`kr_futopt_realtime_k200_weekly_option_execution.py`](kr_futopt_realtime_k200_weekly_option_execution.py) |
| 20 | [실시간]KOSDAQ150옵션호가 | `OA1` | [`kr_futopt_realtime_kosdaq150_option_orderbook.py`](kr_futopt_realtime_kosdaq150_option_orderbook.py) |
| 21 | [실시간]KOSDAQ150옵션체결 | `OA0` | [`kr_futopt_realtime_kosdaq150_option_execution.py`](kr_futopt_realtime_kosdaq150_option_execution.py) |
| 22 | [실시간]선물체결(야간) | `F40` | [`kr_futopt_realtime_future_execution_night.py`](kr_futopt_realtime_future_execution_night.py) |
| 23 | [실시간]선물호가(야간) | `F41` | [`kr_futopt_realtime_future_orderbook_night.py`](kr_futopt_realtime_future_orderbook_night.py) |
| 24 | [실시간]옵션체결(야간) | `O30` | [`kr_futopt_realtime_option_execution_night.py`](kr_futopt_realtime_option_execution_night.py) |
| 25 | [실시간]옵션호가(야간) | `O31` | [`kr_futopt_realtime_option_orderbook_night.py`](kr_futopt_realtime_option_orderbook_night.py) |
| 26 | [실시간]미니옵션호가(야간) | `E11` | [`kr_futopt_realtime_mini_option_orderbook_night.py`](kr_futopt_realtime_mini_option_orderbook_night.py) |
| 27 | [실시간]미니옵션체결가(야간) | `E10` | [`kr_futopt_realtime_mini_option_execution_price_night.py`](kr_futopt_realtime_mini_option_execution_price_night.py) |
| 28 | [실시간]KOSDAQ150옵션체결가(야간) | `E20` | [`kr_futopt_realtime_kosdaq150_option_execution_price_night.py`](kr_futopt_realtime_kosdaq150_option_execution_price_night.py) |
| 29 | [실시간]KOSDAQ150옵션호가(야간) | `E21` | [`kr_futopt_realtime_kosdaq150_option_orderbook_night.py`](kr_futopt_realtime_kosdaq150_option_orderbook_night.py) |

## 실행

```bash
python examples/kr_futopt_realtime/<method>.py
```
