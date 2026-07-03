# 장내채권시세(실시간) — 예제

group_slug: `bond_realtime`

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
| 1 | [실시간]일반채권체결 | `B00` | [`bond_realtime_normal_execution.py`](bond_realtime_normal_execution.py) |
| 2 | [실시간]일반채권호가 | `B01` | [`bond_realtime_normal_orderbook.py`](bond_realtime_normal_orderbook.py) |
| 3 | [실시간]소액채권체결 | `B10` | [`bond_realtime_small_execution.py`](bond_realtime_small_execution.py) |
| 4 | [실시간]소액채권호가 | `B11` | [`bond_realtime_small_orderbook.py`](bond_realtime_small_orderbook.py) |

## 실행

```bash
python examples/bond_realtime/<method>.py
```
