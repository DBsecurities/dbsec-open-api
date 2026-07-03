# 해외선물옵션주문 — 예제

group_slug: `ov_futopt_order`

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
| 1 | 해외선옵 주문 | `ph700101o` | [`ov_futopt_order.py`](ov_futopt_order.py) |
| 2 | 해외선옵 정정/취소주문 | `ph700201o` | [`ov_futopt_order_cancel.py`](ov_futopt_order_cancel.py) |
| 3 | 주문가능수량조회 | `ph710201o` | [`ov_futopt_inquire_psbl_quantity.py`](ov_futopt_inquire_psbl_quantity.py) |
| 4 | 상품별증거금조회 | `ph800404o` | [`ov_futopt_inquire_margin_by_product.py`](ov_futopt_inquire_margin_by_product.py) |
| 5 | 주문내역조회 | `ph020101o` | [`ov_futopt_inquire_orders.py`](ov_futopt_inquire_orders.py) |
| 6 | 체결내역 조회 | `ph020301o` | [`ov_futopt_inquire_executions.py`](ov_futopt_inquire_executions.py) |
| 7 | 미체결내역 조회 | `ph020201o` | [`ov_futopt_inquire_unfilled.py`](ov_futopt_inquire_unfilled.py) |
| 8 | 미결제 약정 조회 | `ph020401o` | [`ov_futopt_inquire_open_interest.py`](ov_futopt_inquire_open_interest.py) |
| 9 | 일별 미결제 약정내역 | `ph131101o` | [`ov_futopt_inquire_daily_open_interest.py`](ov_futopt_inquire_daily_open_interest.py) |
| 10 | 예탁잔고현황 | `ph131601o` | [`ov_futopt_inquire_deposit_balance.py`](ov_futopt_inquire_deposit_balance.py) |
| 11 | 예탁자산현황 | `ph131501o` | [`ov_futopt_inquire_deposit_assets.py`](ov_futopt_inquire_deposit_assets.py) |
| 12 | 기간별 거래내역 조회 | `ph135102o` | [`ov_futopt_inquire_trading_history.py`](ov_futopt_inquire_trading_history.py) |

## 실행

```bash
python examples/ov_futopt_order/<method>.py
```

## 주의

- **실제 매매 주문이 실행됩니다.** 해외선옵은 모의투자 미지원이므로 demo 환경에서의 사전 검증이 불가능합니다 — 소액·수량 검증과 시간 외 호출(시세 닫힌 시간대) 등으로 충분히 사전 점검 후 사용하세요.
- TPS 제한 확인 후 호출 빈도를 조절하세요.
