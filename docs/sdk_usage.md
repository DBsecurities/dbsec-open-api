# dbsec_sdk SDK 사용법

`examples/` 가 "복사 → 값만 바꿔 실행" 하는 단발 스크립트 모음이라면,
`dbsec_sdk/` 는 애플리케이션·봇에 임베드하는 **파이썬 라이브러리(SDK)** 입니다.

실행 예제: [`dbsec_sdk/client_examples/quickstart.py`](../dbsec_sdk/client_examples/quickstart.py)

---

## 1. 설치

```bash
pip install -e .          # repo 루트에서
# 또는: uv pip install -e .
```

의존성: `requests`, `pyyaml`, `python-dotenv`, `websockets` (+ DataFrame 쓰면 `pandas`).

## 2. 설정

`config.yaml` 에 mode 와 앱키를 넣습니다 (`config.yaml.example` 복사).

```yaml
auth:
  prd_app_key:    "실전 앱키"
  prd_app_secret: "실전 시크릿"
  vtl_app_key:    "모의 앱키"
  vtl_app_secret: "모의 시크릿"
environment:
  base_url: "https://openapi.dbsec.co.kr:8443"
  mode: "demo"          # demo → vtl_* 사용 / production → prd_* 사용
```

## 3. 기본 호출 패턴

`DBSecClient` 는 **비동기** 클라이언트입니다 — 모든 API 호출에 `await` 가 필요하고,
`asyncio.run()` 으로 진입합니다.

```python
import asyncio
from dbsec_sdk import DBSecClient

async def main():
    # 클라이언트는 한 번만 생성해서 재사용한다 (토큰 캐싱 — 아래 4번 참고)
    async with DBSecClient("config.yaml") as client:
        # client.apis.<그룹>.<메서드>(...) — 모든 비즈니스 인자는 keyword-only + 필수
        resp = await client.apis.kr_stock_quote.kr_stock_inquire_price(
            InputCondMrktDivCode="J",
            InputIscd1="005930",
        )
        print(resp.is_ok)                 # True (HTTP 2xx)
        print(resp.message)               # "정상 처리 되었습니다."
        print(resp.body["Out"]["Prpr"])   # 현재가
        df = resp.to_dataframe()          # pandas DataFrame (pandas 설치 시)

        # 여러 API 는 asyncio.gather 로 '동시' 호출 (유량제어가 TPS 를 자동 준수)
        balance, deposit = await asyncio.gather(
            client.apis.kr_stock_order.kr_stock_inquire_balance(QryTpCode0="0"),
            client.apis.kr_stock_order.kr_stock_inquire_deposit(),
        )

asyncio.run(main())
```

> 같은 엔드포인트를 여러 번 부르면 그 API 의 TPS 만큼만 동시 진행되고(자동 페이싱),
> 서로 다른 엔드포인트는 각자 리미터라 진짜 병렬로 끝납니다.

### 연속조회(자동 페이징) — `fetch_all=True`

응답이 여러 페이지로 나뉘는 조회(순위·종목조회·시간대별 체결·틱차트 등)는 **단건과 똑같이 호출하되
`fetch_all=True` 만 더하면** **서버가 끝(`cont_yn='N'`)을 알릴 때까지 전부** 받아 하나의 `APIResponse` 로
병합합니다(list 블록 Out1/Out2 누적, 원본 페이지는 `resp.pages`). `cont_yn`/`cont_key` 는 자동 처리됩니다.

```python
# 단건과 같은 호출 + fetch_all=True (max_pages 미지정 시 끝까지)
resp = await client.apis.kr_stock_quote.kr_stock_inquire_condition_rise_fall(
    InputDateClsCode="0", InputRankSortClsCode1="12",   # 당일 / 상승률
    InputMrktClsCode="K", InputBstpIscd="1001",          # 코스피
    fetch_all=True,
)
df = resp.to_dataframe()   # 전 페이지 누적
n_pages = len(resp.pages)  # 받은 페이지 수

# 데이터가 매우 많은 조회(예: 틱차트)는 max_pages 로 상한 (기본 None = 끝까지)
ticks = await client.apis.kr_chart.kr_chart_chart_tick(**tick_args, fetch_all=True, max_pages=10)

# 단건 응답에서도 resp.has_more / resp.cont_key 로 다음 페이지 존재를 확인할 수 있습니다.
```

> 저수준(raw 경로 직접 호출)이 필요하면 `client.post_paged(path, body)` → `list[APIResponse]`.
> 각 페이지 호출은 유량제어가 자동 페이싱합니다(별도 sleep 불필요).
> (구버전 `client.fetch_all(메서드, …)` 도 하위호환으로 동작하지만, 위 `fetch_all=True` 형태를 권장합니다.)

### 그룹 목록 (`client.apis.<그룹>`)

| 그룹 slug | 내용 |
|---|---|
| `auth` / `common` | 인증 토큰 / 관심종목 |
| `kr_stock_order` / `kr_stock_quote` / `kr_stock_realtime` | 국내주식 |
| `kr_futopt_order` / `kr_futopt_quote` / `kr_futopt_realtime` | 국내선물옵션 |
| `kr_chart` | 국내주식·선물 차트 |
| `ov_stock_order` / `ov_stock_quote` / `ov_stock_realtime` | 해외주식 |
| `ov_futopt_order` / `ov_futopt_quote` / `ov_futopt_realtime` | 해외선물옵션 |
| `bond_order` / `bond_quote` / `bond_realtime` | 장내채권 |
| `ws_common` | 웹소켓 공통 |

메서드 이름과 인자는 각 `dbsec_sdk/apis/<그룹>/endpoints.py` 의 시그니처 + docstring 참고.

## 4. 토큰 관리

토큰 발급/갱신/폐기는 명시적 메서드로 제공하고, 요청 경로의 자동 발급은 `auto_token` 으로 제어합니다.

```python
token = await client.get_token()      # 유효 토큰 확보 (캐시에 없으면 발급, 프롬프트 없음)
await client.force_refresh()           # 강제 갱신 (revoke 후 재발급)
await client.revoke()                  # 폐기 (서버 무효화 + 로컬 캐시 삭제)
```

- **`auto_token` (기본 `True`)**: 요청(REST/WebSocket) 시 토큰이 없거나 무효/만료(`IGW00121`/`00123`)면
  SDK 가 자동으로 발급·재발급합니다 — **stdin 프롬프트 없음**(헤드리스/봇·CI 에서도 멈추지 않음).
  토큰거부 응답의 재발급은 요청당 최대 `token_retry_limit`회(기본 5).
- **`auto_token=False`**: 자동 발급하지 않습니다 → 토큰이 없으면 `AuthError`, 무효/만료는 `APIError`.
  토큰을 `get_token()` / `force_refresh()` / `revoke()` 로 직접 관리하세요.
  ```python
  client = DBSecClient("config.yaml", auto_token=False)
  await client.get_token()   # 호출 전에 명시적으로 발급해 두어야 함
  ```
- 토큰은 **파일(`.dbsec_token.json`, 루트, examples 와 공유)** 에만 캐싱됩니다 — 메모리 상태 없이
  매 호출마다 파일에서 읽고 씁니다. 프로세스를 재시작하거나 client 를 여러 번 생성해도 같은
  캐시 파일을 공유해 재사용됩니다.
- **토큰 발급은 1분에 1건 제한**입니다 (`IGW00201`). 파일 캐시 덕분에 짧은 간격으로
  스크립트를 재실행해도 재발급되지 않습니다.
- 토큰 유효기간은 24시간이며, **만료 *시각*까지 그대로 사용합니다(만료 전 미리 갱신하지 않음).**
  24시간 이내 재발급 요청은 서버가 기존 토큰을 반환하므로, 강제 갱신은 `force_refresh()`(revoke 후 발급)를 씁니다.

> 비대화형(자동화/봇)이라도 `auto_token=True`(기본)면 토큰이 없거나 만료돼도 자동으로 발급/재발급되어
> 멈추지 않습니다. 토큰을 직접 통제하려면 `auto_token=False` 로 두고 `get_token()`/`force_refresh()` 로
> 관리하세요. 캐시 파일 `.dbsec_token.json` 은 **액세스 토큰 평문** 이라 `.gitignore` 에 포함되어 있습니다.

## 5. 실시간 WebSocket

```python
async def stream(client):
    ws = client.create_websocket()
    ws.on_message(lambda tr_cd, tr_key, data: print(tr_cd, tr_key, data))
    await ws.connect()
    await ws.add_realtime(tr_cd="S00", tr_key="J 005930", tr_type="1")   # 일반 시세 구독
    await ws.add_realtime(tr_cd="P",   tr_key=client.config.app_key, tr_type="3")  # 계좌(잔고) 등록
    await ws.run()
```

- `tr_type` 은 호출자가 직접 지정합니다 (기본값 `"1"`, `"1"/"2"/"3"` 문자열 또는 `1/2/3` 정수 허용). `"1"`=시세구독, `"2"`=시세해제(`remove_realtime`), `"3"`=계좌등록.
- 계좌 단위 TR (`IS0/IS1/IS2/IF0/O/P`) 은 `tr_type="3"` (계좌등록) 으로 호출하세요 — 해제 메시지가 없어 세션 종료가 곧 해제입니다.
- `*_realtime` 그룹의 `client.apis.*_realtime.*()` 메서드는 REST 가 아닌 WebSocket TR 이므로
  호출 시 `NotImplementedError` 로 위 WebSocket 사용법을 안내합니다.

## 6. ⚠️ 주문 주의

`*_order`, `*_order_modify`, `*_order_cancel` 계열은 **실제 매매가 실행**됩니다.
모든 비즈니스 인자가 필수(기본값 없음)이므로 빈 호출 시 `TypeError` 가 나도록 설계되어
실수로 인한 주문을 방지합니다. 운영(`production`) 모드에서는 특히 주의하세요.

---

## examples vs SDK

| | `examples/` (dbsec_helper) | `dbsec_sdk/` (SDK) |
|---|---|---|
| 호출 | `resp, data = call_rest(url, body={...})` → 출력은 `print_response(resp, data)` | `await client.apis.그룹.메서드(필드=값)` (async) |
| 인자 | dict 자유 입력 | 메서드 시그니처 (keyword-only, 필수) |
| 토큰 캐시 | `.dbsec_token.json` (루트, 공유) | `.dbsec_token.json` (루트, 공유) |
| 적합 | 빠른 단발 테스트·학습 | 애플리케이션/봇 임베드 |
