# 국내선물옵션주문 — 예제

group_slug: `kr_futopt_order`

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
| 1 | 선물옵션 주문 | `CFOAT00100` | [`kr_futopt_order.py`](kr_futopt_order.py) |
| 2 | 선물옵션 정정주문 | `CFOAT00200` | [`kr_futopt_order_modify.py`](kr_futopt_order_modify.py) |
| 3 | 선물옵션 취소주문 | `CFOAT00300` | [`kr_futopt_order_cancel.py`](kr_futopt_order_cancel.py) |
| 4 | 선물옵션 체결조회 | `CFOAQ04000` | [`kr_futopt_inquire_executions.py`](kr_futopt_inquire_executions.py) |
| 5 | 선물옵션 주문가능수량 | `CFOAQ42400` | [`kr_futopt_inquire_psbl_quantity.py`](kr_futopt_inquire_psbl_quantity.py) |
| 6 | 선물옵션 잔고 조회 | `CFOAQ02500` | [`kr_futopt_inquire_balance.py`](kr_futopt_inquire_balance.py) |
| 7 | 선물옵션 잔고_평가현황조회 | `CFOAQ50100` | [`kr_futopt_inquire_balance_eval.py`](kr_futopt_inquire_balance_eval.py) |
| 8 | 선물옵션 당일실현손익 | `CFOAQ02600` | [`kr_futopt_inquire_realized_pnl.py`](kr_futopt_inquire_realized_pnl.py) |
| 9 | 선물옵션 가정산예탁금 상세 | `CFOEQ11100` | [`kr_futopt_inquire_estimated_deposit.py`](kr_futopt_inquire_estimated_deposit.py) |
| 10 | 선물옵션 주문 (야간) | `CFOHT00100` | [`kr_futopt_order_night.py`](kr_futopt_order_night.py) |
| 11 | 선물옵션 정정주문 (야간) | `CFOHT00200` | [`kr_futopt_order_modify_night.py`](kr_futopt_order_modify_night.py) |
| 12 | 선물옵션 취소주문 (야간) | `CFOHT00300` | [`kr_futopt_order_cancel_night.py`](kr_futopt_order_cancel_night.py) |
| 13 | 선물옵션 체결조회 (야간) | `CFOHQ04000` | [`kr_futopt_inquire_executions_night.py`](kr_futopt_inquire_executions_night.py) |
| 14 | 선물옵션 잔고조회 (야간) | `CFOHQ02500` | [`kr_futopt_inquire_balance_night.py`](kr_futopt_inquire_balance_night.py) |

## 실행

```bash
python examples/kr_futopt_order/<method>.py
```

## 주의

- **실제 매매 주문이 실행됩니다.** 반드시 모의투자(`mode: demo`)에서 먼저 테스트하세요.
- TPS 제한 확인 후 호출 빈도를 조절하세요.
