# 해외선물옵션시세(실시간) — 예제

group_slug: `ov_futopt_realtime`

> ⚠️ **운영(production) 전용 그룹** — DB증권 해외선물옵션은 시스템 차원에서 모의투자를 지원하지 않습니다.
> `config.yaml` 의 `environment.mode` 를 `"production"` 으로 두고 `prd_app_key`/`prd_app_secret` 를 사용해야 합니다.
> WebSocket 포트도 운영 전용(`wss://openapi.dbsec.co.kr:7071/websocket`)입니다.
> demo 모드에서 호출하면 `dbsec_helper` 가 명확한 에러로 차단합니다.

각 파일은 **standalone** 입니다. `examples/dbsec_helper.py` 의 공통 헬퍼만 사용합니다.
(토큰 발급·캐싱·응답코드 분류 등 boilerplate 는 헬퍼가 담당)

## 실행 전 준비

```bash
pip install requests pyyaml  websockets
cp config.yaml.example config.yaml      # mode: "production" + prd_app_key/prd_app_secret 입력
python examples/auth/token_issue.py     # 토큰을 루트 .dbsec_token.json 에 캐시
```

## API 목록

| # | API 명 | TR 코드 | 파일 |
|---:|---|---|---|
| 1 | [실시간]주문체결 | `O` | [`ov_futopt_realtime_order_execution.py`](ov_futopt_realtime_order_execution.py) |
| 2 | [실시간]잔고 | `P` | [`ov_futopt_realtime_balance.py`](ov_futopt_realtime_balance.py) |
| 3 | [실시간]해외선물호가 | `L01` | [`ov_futopt_realtime_future_orderbook.py`](ov_futopt_realtime_future_orderbook.py) |
| 4 | [실시간]해외선물시세 | `K01` | [`ov_futopt_realtime_future_quote.py`](ov_futopt_realtime_future_quote.py) |
| 5 | [실시간]해외옵션시세 | `K02` | [`ov_futopt_realtime_option_quote.py`](ov_futopt_realtime_option_quote.py) |
| 6 | [실시간]해외옵션호가 | `L02` | [`ov_futopt_realtime_option_orderbook.py`](ov_futopt_realtime_option_orderbook.py) |

## 실행

```bash
python examples/ov_futopt_realtime/<method>.py
```
