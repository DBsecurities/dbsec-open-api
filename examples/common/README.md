# 공통 — 예제

group_slug: `common`

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
| 1 | 관심그룹 종목조회 | `MCJDD88841` | [`inquire_issue_groups.py`](inquire_issue_groups.py) |
| 2 | 관심종목 그룹조회 | `MCJDD88840` | [`inquire_group_list.py`](inquire_group_list.py) |

## 실행

```bash
python examples/common/<method>.py
```
