# 해외주식시세(실시간) — 예제

group_slug: `ov_stock_realtime`

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
| 1 | [실시간]해외주식 주문체결 조회 | `IS2` | [`ov_stock_realtime_order_execution.py`](ov_stock_realtime_order_execution.py) |
| 2 | [실시간]해외주식 체결가 | `V60` | [`ov_stock_realtime_execution_price.py`](ov_stock_realtime_execution_price.py) |
| 3 | [실시간]해외주식 호가 | `V61` | [`ov_stock_realtime_orderbook.py`](ov_stock_realtime_orderbook.py) |
| 4 | [실시간]해외주식 지연체결가 | `V10` | [`ov_stock_realtime_delayed_execution_price.py`](ov_stock_realtime_delayed_execution_price.py) |
| 5 | [실시간]해외주식 지연호가 | `V11` | [`ov_stock_realtime_delayed_orderbook.py`](ov_stock_realtime_delayed_orderbook.py) |

## 실행

```bash
python examples/ov_stock_realtime/<method>.py
```
