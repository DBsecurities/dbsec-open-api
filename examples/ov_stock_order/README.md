# 해외주식주문 — 예제

group_slug: `ov_stock_order`

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
| 1 | 해외주식 주문 | `CAZCT00100` | [`ov_stock_order.py`](ov_stock_order.py) |
| 2 | 해외주식 체결내역조회 | `CAZCQ00100` | [`ov_stock_inquire_executions.py`](ov_stock_inquire_executions.py) |
| 3 | 해외주식 잔고/증거금 조회 | `CAZCQ00400` | [`ov_stock_inquire_balance_margin.py`](ov_stock_inquire_balance_margin.py) |
| 4 | 해외주식 매매내역 조회 | `CAZCQ00200` | [`ov_stock_inquire_trade_history.py`](ov_stock_inquire_trade_history.py) |
| 5 | 해외주식 거래내역 조회 | `CAZCQ01600` | [`ov_stock_inquire_trading_history.py`](ov_stock_inquire_trading_history.py) |
| 6 | 해외주식 주문가능금액조회 | `CAZCQ01300` | [`ov_stock_inquire_psbl_amount.py`](ov_stock_inquire_psbl_amount.py) |
| 7 | 해외주식 실현손익 조회 | `CAZCQ00300` | [`ov_stock_inquire_realized_pnl.py`](ov_stock_inquire_realized_pnl.py) |
| 8 | 해외주식 예수금상세 | `CAZCQ01400` | [`ov_stock_inquire_deposit_detail.py`](ov_stock_inquire_deposit_detail.py) |
| 9 | 해외주식 평균매입단가 조회 | `CAZCQ03400` | [`ov_stock_inquire_avg_buy_price.py`](ov_stock_inquire_avg_buy_price.py) |

## 실행

```bash
python examples/ov_stock_order/<method>.py
```

## 주의

- **실제 매매 주문이 실행됩니다.** 반드시 모의투자(`mode: demo`)에서 먼저 테스트하세요.
- TPS 제한 확인 후 호출 빈도를 조절하세요.
