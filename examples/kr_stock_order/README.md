# 국내주식주문 — 예제

group_slug: `kr_stock_order`

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
| 1 | 주식종합주문 | `CSPAT00600` | [`kr_stock_order.py`](kr_stock_order.py) |
| 2 | 주식정정주문 | `CSPAT00700` | [`kr_stock_order_modify.py`](kr_stock_order_modify.py) |
| 3 | 주식취소주문 | `CSPAT00800` | [`kr_stock_order_cancel.py`](kr_stock_order_cancel.py) |
| 4 | 주식종합주문- NXT거래소 | `CSPAT00610` | [`kr_stock_order_nxt.py`](kr_stock_order_nxt.py) |
| 5 | 주식정정주문- NXT거래소 | `CSPAT00710` | [`kr_stock_order_modify_nxt.py`](kr_stock_order_modify_nxt.py) |
| 6 | 주식취소주문- NXT거래소 | `CSPAT00810` | [`kr_stock_order_cancel_nxt.py`](kr_stock_order_cancel_nxt.py) |
| 7 | 체결/미체결조회 | `CSPAQ04800` | [`kr_stock_inquire_executions.py`](kr_stock_inquire_executions.py) |
| 8 | 주식주문가능수량조회 | `CSPBQ00100` | [`kr_stock_inquire_psbl_quantity.py`](kr_stock_inquire_psbl_quantity.py) |
| 9 | 주식잔고조회 | `CSPAQ03420` | [`kr_stock_inquire_balance.py`](kr_stock_inquire_balance.py) |
| 10 | 당일매매손익 조회 | `CSPAQ01800` | [`kr_stock_inquire_daily_pnl.py`](kr_stock_inquire_daily_pnl.py) |
| 11 | 계좌예수금조회 | `CDPCQ00100` | [`kr_stock_inquire_deposit.py`](kr_stock_inquire_deposit.py) |
| 12 | 일자별매매내역 | `CSPEQ00400` | [`kr_stock_inquire_daily_trade.py`](kr_stock_inquire_daily_trade.py) |
| 13 | 임의기간수익률집계 | `FOCCQ10800` | [`kr_stock_inquire_period_returns.py`](kr_stock_inquire_period_returns.py) |
| 14 | 주식 실현손익조회 | `CSPAQ07800` | [`kr_stock_inquire_realized_pnl.py`](kr_stock_inquire_realized_pnl.py) |
| 15 | 계좌별신용한도조회 | `CSPAQ00600` | [`kr_stock_inquire_credit_limit.py`](kr_stock_inquire_credit_limit.py) |
| 16 | 신용상환가능총수량조회 | `CSPAQ09400` | [`kr_stock_inquire_credit_repayment.py`](kr_stock_inquire_credit_repayment.py) |
| 17 | 계좌거래내역 조회 | `CDPCQ04700` | [`kr_stock_inquire_trading_history.py`](kr_stock_inquire_trading_history.py) |

## 실행

```bash
python examples/kr_stock_order/<method>.py
```

## 주의

- **실제 매매 주문이 실행됩니다.** 반드시 모의투자(`mode: demo`)에서 먼저 테스트하세요.
- TPS 제한 확인 후 호출 빈도를 조절하세요.
