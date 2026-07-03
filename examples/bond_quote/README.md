# 장내채권시세 — 예제

group_slug: `bond_quote`

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
| 1 | 장내채권 상세검색 | `BO_SEARCH` | [`bond_search_detail.py`](bond_search_detail.py) |
| 2 | 장내채권 현재가조회 | `BO_SISE` | [`bond_inquire_price.py`](bond_inquire_price.py) |
| 3 | 장내채권 호가 조회 | `BO_HOGA` | [`bond_inquire_orderbook.py`](bond_inquire_orderbook.py) |

## 실행

```bash
python examples/bond_quote/<method>.py
```
