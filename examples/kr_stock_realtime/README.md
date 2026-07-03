# 국내주식시세(실시간) — 예제

group_slug: `kr_stock_realtime`

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
| 1 | [실시간]주식주문체결 조회 | `IS1` | [`kr_stock_realtime_order_execution.py`](kr_stock_realtime_order_execution.py) |
| 2 | [실시간]주식주문접수 조회 | `IS0` | [`kr_stock_realtime_order_accept.py`](kr_stock_realtime_order_accept.py) |
| 3 | [실시간]주식호가 | `S01` | [`kr_stock_realtime_orderbook.py`](kr_stock_realtime_orderbook.py) |
| 4 | [실시간]주식체결가 | `S00` | [`kr_stock_realtime_execution_price.py`](kr_stock_realtime_execution_price.py) |
| 5 | [실시간]ELW호가 | `W01` | [`kr_stock_realtime_elw_orderbook.py`](kr_stock_realtime_elw_orderbook.py) |
| 6 | [실시간]ELW체결 | `W00` | [`kr_stock_realtime_elw_execution.py`](kr_stock_realtime_elw_execution.py) |
| 7 | [실시간]업종지수체결가 | `U00` | [`kr_stock_realtime_industry_index_execution_price.py`](kr_stock_realtime_industry_index_execution_price.py) |
| 8 | [실시간]업종지수등락 | `U03` | [`kr_stock_realtime_industry_index_change.py`](kr_stock_realtime_industry_index_change.py) |
| 9 | [실시간]업종별투자자 | `U05` | [`kr_stock_realtime_industry_investor.py`](kr_stock_realtime_industry_investor.py) |

## 실행

```bash
python examples/kr_stock_realtime/<method>.py
```
