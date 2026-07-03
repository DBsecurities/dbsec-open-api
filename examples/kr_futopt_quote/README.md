# 국내선물옵션시세 — 예제

group_slug: `kr_futopt_quote`

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
| 1 | 선물종목 조회 | `FCODES` | [`kr_futopt_search_futures.py`](kr_futopt_search_futures.py) |
| 2 | 옵션종목 조회 | `OCODES` | [`kr_futopt_search_options.py`](kr_futopt_search_options.py) |
| 3 | 국내선옵 멀티현재가 조회 | `FOMULTIPRICE` | [`kr_futopt_inquire_price_multi.py`](kr_futopt_inquire_price_multi.py) |
| 4 | 현재가조회 | `FOPRICE` | [`kr_futopt_inquire_price.py`](kr_futopt_inquire_price.py) |
| 5 | 호가조회 | `HOGA` | [`kr_futopt_inquire_orderbook.py`](kr_futopt_inquire_orderbook.py) |
| 6 | 일별체결조회 | `DAYTRADE` | [`kr_futopt_inquire_daily_executions.py`](kr_futopt_inquire_daily_executions.py) |
| 7 | 시간대별체결조회 | `CONCLUSION` | [`kr_futopt_inquire_time_execution.py`](kr_futopt_inquire_time_execution.py) |
| 8 | 옵션전광판 | `OSTOCK_CONDT` | [`kr_futopt_option_board.py`](kr_futopt_option_board.py) |

## 연속조회(자동 페이징) 예제

`call_rest_paged()` 사용법을 보여주는 예시입니다. 시계열·차트처럼 응답이
여러 페이지로 쪼개지는 API 를 한 번 호출로 모두 받아옵니다.

| API 명 | 파일 | 설명 |
|---|---|---|
| 옵션종목 조회 (페이징) | [`kr_futopt_search_options_paged.py`](kr_futopt_search_options_paged.py) | kr_futopt_search_options.py 와 같은 API 를 자동 페이징으로 호출 (가이드에서 연속키 조회 명시) |


## 실행

```bash
python examples/kr_futopt_quote/<method>.py
```
