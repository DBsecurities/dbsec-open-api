# 장내채권주문 — 예제

group_slug: `bond_order`

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
| 1 | 채권주문 (매수/매도 통합) | `CSPAT02000` | [`bond_order.py`](bond_order.py) |
| 2 | 채권정정주문 | `CSPAT02100` | [`bond_order_modify.py`](bond_order_modify.py) |
| 3 | 채권취소주문 | `CSPAT02200` | [`bond_order_cancel.py`](bond_order_cancel.py) |
| 4 | 채권주문체결조회 | `CSPAQ05700` | [`bond_inquire_executions.py`](bond_inquire_executions.py) |
| 5 | 채권잔고조회 | `CSPAQ01200` | [`bond_inquire_balance.py`](bond_inquire_balance.py) |
| 6 | 채권잔고평가조회 | `CSPAQ07900` | [`bond_inquire_balance_eval.py`](bond_inquire_balance_eval.py) |

## 실행

```bash
python examples/bond_order/<method>.py
```

## 주의

- **실제 매매 주문이 실행됩니다.** 
- TPS 제한 확인 후 호출 빈도를 조절하세요.
