<h1 align="center">DB증권 Open API 샘플코드 (Python)</h1>

<p align="center">
  <img src="https://img.shields.io/badge/python-3.10+-blue.svg" alt="Python 3.10+">
  <img src="https://img.shields.io/badge/license-MIT-green.svg" alt="License: MIT">
  <img src="https://img.shields.io/badge/DB%EC%A6%9D%EA%B6%8C-Open%20API-orange.svg" alt="DB증권 Open API">
</p>

<p align="center">
  DB증권 Open API <strong>전체 그룹 · 엔드포인트</strong>를 한 클라이언트로 호출하는 파이썬 라이브러리 + 예제 모음.<br>
  국내주식 · 해외주식 · 국내선물옵션 · 해외선물옵션 · 장내채권 · 실시간 WebSocket 지원.
</p>

<p align="center">
  <a href="https://openapi.dbsec.co.kr" target="_blank" rel="noopener noreferrer">
    <img src="https://img.shields.io/badge/DB증권_Open_API_포털_바로가기-00A862?style=flat-square&logoColor=white" alt="DB증권 Open API 포털">
  </a>
</p>

---

## 제작 의도 및 대상 사용자

### 샘플코드 제작 의도

본 저장소는 DB증권 Open API를 위한 파이썬 샘플코드 저장소로, **생성형 AI 기반 바이브 코딩**(ChatGPT · Claude · Gemini)과 **전통적인 Python 개발 환경** 양쪽 모두에서 직관적으로 학습하고 실전에 적용할 수 있도록 설계되었습니다.

- **`dbsec_sdk/`** 인증·HTTP 클라이언트·WebSocket 클라이언트
- **`examples/`** — 그룹별 디렉토리 안에 API당 1파일(`<method>.py`) — 모두 standalone 으로 단독 실행 가능
- **`mcp_server/`** — LLM 코딩 도구(Claude Code·Cursor 등)가 API 그룹·명세·샘플코드를 조회하는 코드 어시스턴트 MCP 서버
- **MCP·LLM 친화 네이밍** — 메서드 이름만 봐도 시장 도메인이 식별되도록 `kr_stock_*`, `ov_stock_*`, `kr_futopt_*`, `ov_futopt_*`, `bond_*` 접두어 일관 적용

### 대상 사용자

- DB증권 Open API를 처음 접하시는 Python 개발자
- 본인의 투자 아이디어를 코드로 옮겨 백테스트하거나 자동화해보고 싶으신 개인 투자자
- 타 증권사 Open API 경험자 또는 멀티 브로커 구성을 검토 중이신 개발자
- LLM 코드 에이전트(MCP 도구 포함)로 종목 탐색·시세 분석·자동매매를 구축하려는 사용자

---

**[OpenAPI 샘플코드 이용시 유의사항]**

- 본 샘플코드는 DB증권 Open API 연동방법을 제공하는 예시입니다. 고객님의 개발 시작 부담을 덜어드리고자 참고용으로 제공하고 있습니다.
- 샘플코드는 지속적으로 개선·업데이트될 수 있으며, 별도의 공지 없이 변경될 수 있습니다.
- 샘플코드는 참고용 예시로 제공되므로, 실제 서비스에 적용하기 전에 반드시 충분한 검토와 테스트를 거쳐주시기 바랍니다.
- 샘플코드를 활용해 개발·운영하신 프로그램의 오작동, 매매 손실, 데이터 오류 등으로 발생하는 직·간접적인 손해에 대해 당사는 책임지지 않습니다.
- 실제 매매 주문이 실행될 수 있으므로, 반드시 **모의투자 환경**에서 먼저 테스트하세요.
- 접근토큰 유효기간은 **24시간**이며, 유효기간 내 발급 시 **동일 토큰**이 발급됩니다. 유효기간 내 토큰 재발급을 원하시면 기존토큰 폐기 후 발급 바랍니다. 
- TR코드별 InBlock/OutBlock 세부사항은 [DB증권 API 가이드](https://openapi.dbsec.co.kr/apiservice) 참조.
- 해외주식 실시간 시세 수신 시 MTS/HTS를 통해 **실시간 시세 신청(무료)** 이 필요합니다.
- 해외선물옵션 실시간 시세 수신 시 GMTS/GTS를 통해 **실시간 시세 신청(유료)** 이 필요합니다.

---

## 목차

- [핵심 기능](#핵심-기능)
- [사전 준비](#사전-준비)
- [빠른 시작 (5분)](#빠른-시작-5분)
- [examples 폴더 사용법](#examples-폴더-사용법)
- [코드 어시스턴트 MCP 서버](#코드-어시스턴트-mcp-서버)
- [폴더 구조](#폴더-구조)
- [설치](#설치)
- [설정](#설정)
- [사용법](#사용법)
  - [인증 (토큰 자동)](#1-인증-토큰-자동)
  - [통합 API 호출 패턴 — `client.apis`](#2-통합-api-호출-패턴--clientapis)
  - [국내주식 — 주문/조회](#3-국내주식--주문조회)
  - [그 외 상품 — 해외주식 · 선물옵션 · 채권 · 차트 · WebSocket](#4-그-외-상품--해외주식--선물옵션--채권--차트--websocket)
  - [DataFrame 변환](#5-dataframe-변환)
- [전체 그룹 & API](#전체-그룹--api)
- [메서드 네이밍 규칙 (도메인 접두어)](#메서드-네이밍-규칙-도메인-접두어)
- [운영 vs 모의투자](#운영-vs-모의투자)
- [오류코드 & 유량제어](#오류코드--유량제어)
- [부록 — API 모의투자 지원 현황](#부록--api-모의투자-지원-현황)

---

## 핵심 기능

| 기능 | 내용 |
|------|------|
| **API 커버리지** | DB증권 Open API **전체 엔드포인트 커버** |
| **비동기 클라이언트** | `DBSecClient` 는 **async** — `await client.apis.그룹.메서드(...)`. `asyncio.gather` 로 동시 호출 |
| **단일 진입점** | 클라이언트 한 줄 생성으로 인증·토큰 캐싱·연속조회 자동 처리 |
| **도메인 접두 메서드** | `kr_stock_order`, `ov_stock_inquire_balance_margin` 같이 메서드명만으로 시장 식별 (MCP 친화) |
| **유량제어 자동** | 앱 20TPS + 엔드포인트별 TPS **2-tier** 자동 페이싱 → 서버 `IGW00201`(호출건수 초과) 사전 차단 |
| **토큰 자동 발급/재발급** | `auto_token=True`(기본): 요청 시 토큰이 없거나 무효/만료(`IGW00121`/`00123`)면 자동 발급·재발급(stdin 프롬프트 없음 → 헤드리스 안전). `False`면 `get_token()`/`force_refresh()`/`revoke()` 로 직접 관리(↓토큰 정책) |
| **유연한 응답** | `APIResponse` dict 래퍼 기본, `resp.to_dataframe(key="Out1")` 로 DataFrame 변환 선택 |
| **WebSocket 자동화** | 연결·재연결(exponential backoff)·구독 복원·종료 라이프사이클 내장 |
| **개별 실행 가능 예제** | `examples/<group>/<method>.py` — 복사 → 값만 바꿔 실행 |
| **LLM · AI 에이전트 친화** | [`llms.txt`](llms.txt)(저장소 구조·명세·예제 안내) + 코드 어시스턴트 MCP 서버 — LLM·AI 에이전트가 API를 쉽게 탐색 |

---

## 사전 준비

1. **DB증권 계좌 개설** — [비대면 계좌개설](https://www.dbsec.co.kr/custcenter/account/cu_NonfaceBranch_viw.do)
2. **Open API 사용 신청** — DB증권 홈페이지 -> OpenAPI 서비스 신청 메뉴(https://www.dbsec.co.kr/online/accservice/on_OpenApi_wrk00.do) 에서 신청
3. **APP_KEY / APP_SECRET 발급** — 신청 완료 후 발급
4. 모의투자 OpenAPI 앱 신청 전 **모의투자 신청** 필수 — DB증권 홈페이지 -> 모의투자 -> 상시모의투자 신청 메뉴(https://www.dbsec.co.kr/custcenter/vts/vts_Index_viw02.do) 에서 신청 
5. **Python 3.10 이상** 설치

---

## 빠른 시작 (5분)

> 프로그래밍이 처음이거나 단계별 안내가 필요하면 **[HOWTOUSE.md](HOWTOUSE.md)** (초보자용 가이드)를 참고하세요.

```bash
git clone https://github.com/DBsecurities/dbsec-open-api.git
cd dbsec-open-api
pip install -e .                            # dbsec_sdk + 의존성(requests·pyyaml·websockets·pandas) 일괄 설치 — standalone 예제도 이걸로 동작
cp config.yaml.example config.yaml          # APP_KEY/SECRET 입력 + mode: demo  (macOS/Linux/Git Bash)
# Windows CMD:        copy config.yaml.example config.yaml
# Windows PowerShell: Copy-Item config.yaml.example config.yaml
python dbsec_sdk/client_examples/quickstart.py   # SDK 데모 (읽기 전용 조회)
# 또는 단발 standalone 예제(examples/dbsec_helper.py 사용): python examples/kr_stock_quote/kr_stock_inquire_price.py
```

`DBSecClient` 는 **비동기** 클라이언트입니다 (모든 호출에 `await`, 진입은 `asyncio.run`).

```python
import asyncio
from dbsec_sdk import DBSecClient

async def main():
    # 클라이언트 생성 — 유량제어·토큰 옵션 (모두 기본값이라 생략 가능: DBSecClient("config.yaml") 만으로도 동작)
    async with DBSecClient(
        "config.yaml",
        rate_limit=True,          # 유량제어: 호출 전 앱TPS+API별 TPS 간격을 맞춰 IGW00201(호출초과) 예방. False면 미적용.
        rate_limit_safety=0.9,    # 안전계수(0<s≤1): 실제율 = 앱 TPS × s. 0.9=90%(10% 여유, 권장. 0.9 적용 시 최대 18TPS)
        auto_token=True,          # 토큰 자동 발급/재발급: True면 요청 시 토큰이 없거나 만료/무효(IGW00121/123)면 자동 처리.
                                  # False면 자동 발급 안 함 → 토큰 없으면 AuthError, 만료/무효는 APIError (직접 관리).
        rate_limit_backoff=True,  # 지수백오프: IGW00201 받으면 1·2·4·8초 후 재시도. False면 즉시 APIError.
    ) as client:
        # 국내주식 현재가조회 — 삼성전자 (읽기 전용)
        resp = await client.apis.kr_stock_quote.kr_stock_inquire_price(
            InputCondMrktDivCode="J",   # J: KRX 주식
            InputIscd1="005930")        # 삼성전자
        # 응답 성공(rsp_cd == "00000")을 확인한 뒤 값을 사용한다.
        if resp.rsp_cd == "00000":
            out = resp.body["Out"]
            print(f"삼성전자 현재가: {int(out['Prpr']):,}원\n")
            # 응답 전체 필드 출력 (DataFrame 으로 보려면 resp.to_dataframe())
            for field, value in out.items():
                print(f"  {field}: {value}")
        else:
            print(f"[{resp.rsp_cd}] 조회 실패: {resp.rsp_msg}")

asyncio.run(main())
```

---

## examples 폴더 사용법

`examples/` 는 **SDK 없이 단독 실행되는 스크립트 모음**입니다. API 1개당 파일 1개(`<method>.py`)이며,
`examples/dbsec_helper.py`(표준 라이브러리 + `requests`·`pyyaml`)만으로 동작합니다 — `dbsec_sdk` 와는 **독립적**입니다.
"복사 → 값만 바꿔 실행"으로 API를 빠르게 익히기에 적합합니다.

### 실행

```bash
cp config.yaml.example config.yaml      # 앱키 입력 + mode: demo (최초 1회, macOS/Linux/Git Bash)
# Windows CMD:        copy config.yaml.example config.yaml
# Windows PowerShell: Copy-Item config.yaml.example config.yaml

# 저장소 루트에서:
python examples/kr_stock_quote/kr_stock_inquire_price.py
# 또는 examples/ 안에서:
cd examples && python kr_stock_quote/kr_stock_inquire_price.py
```

- 토큰은 루트 `.dbsec_token.json` 캐시를 우선 사용하며(SDK 와 공유), 유효한 캐시가 없으면 첫 실행 시
  발급 여부를 묻습니다 — `[1]` 지금 발급하고 계속 / `[2]` 취소(기본). 비대화형(파이프/CI) 환경이면
  발급 프롬프트 없이 안전하게 취소됩니다.
- 각 그룹 폴더의 `README.md` 에 그 그룹의 메서드 목록·호출 패턴이 정리되어 있습니다.

### REST 조회/주문 예제 패턴

```python
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))  # dbsec_helper 경로 추가
from dbsec_helper import call_rest, print_response

resp, data = call_rest(                      # call_rest 는 요청만 하고 (resp, data) 반환
    url="/api/v1/quote/kr-stock/inquiry/price",
    body={"In": {"InputCondMrktDivCode": "J", "InputIscd1": "005930"}},
    label="현재가조회",
)
print_response(resp, data)                   # 응답 전체 출력 (원하면)
print("현재가:", data["Out"]["Prpr"])        # 또는 값 추출해서 사용
# 연속조회가 필요하면 pages = call_rest_paged(...) 사용
```

### 실시간(WebSocket) 예제 패턴

```python
from dbsec_helper import ws_subscribe, run_ws

run_ws(ws_subscribe(
    tr_cd="S00",                    # 체결가 TR
    tr_key="",                      # 종목코드 (계좌 단위 TR 은 app_key)
    group_slug="kr_stock_realtime",
    tr_type="1",                    # 등록 종류 (직접 지정): 1=시세구독 2=해제 3=계좌등록
))   # Ctrl+C 로 종료 (시세구독 tr_type="1" 은 구독 해제 후 종료)
```

> `tr_type` 은 호출자가 직접 지정합니다(자동판별 안 함). 일반 시세 TR 은 `tr_type="1"`,
> 계좌 단위 TR(`IS0/IS1/IS2/IF0/O/P` — 주문접수/체결/잔고)은 `tr_type="3"` 으로 호출하세요.

> **examples vs SDK** — `examples/` 는 `call_rest("/api/...", body={...})`(dict 자유 입력·동기)로 빠른 학습·단발 테스트용,
> `dbsec_sdk/` 는 `await client.apis.그룹.메서드(필드=값)`(타입 시그니처·비동기·유량제어·토큰 자동발급(auto_token))로 앱/봇 임베드용입니다.
> 자세한 SDK 사용법은 [docs/sdk_usage.md](docs/sdk_usage.md) 참조.

---

## 코드 어시스턴트 MCP 서버

`mcp_server/` 는 LLM 코딩 도구(Claude Desktop · Claude Code · Cursor 등)가 DB증권 Open API 의
**그룹·엔드포인트 목록**, **요청(In)·응답(Out) 파라미터 명세**, **실행 가능한 샘플코드**를
직접 조회할 수 있게 해주는 MCP(stdio) 서버입니다. 명세의 **원본은 `examples/`(샘플코드)** 이며
(요청 파라미터 = 코드 내 주석, 응답 파라미터 = docstring 의 `응답 파라미터 (Out)` 섹션),
모의투자 지원·TPS·TR코드는 `docs/api_support_matrix.md` 로 보강합니다. 즉, **예제를 고치면
MCP 가 그대로 반영**합니다(별도 명세 캐시에 의존하지 않음).

| 도구 | 설명 |
|---|---|
| `list_api_groups()` | 그룹 목록 + 그룹별 API 개수 + 모의투자 지원 수 |
| `search_apis(query, group?)` | 키워드·TR코드·slug·경로로 API 검색(한글 가능) |
| `get_api_spec(identifier)` | 엔드포인트·TPS·**In/Out 파라미터**·요청/응답 예시 전체 |
| `get_sample_code(identifier)` | 해당 API 의 파이썬 샘플코드 원문 |
| `get_setup_guide()` | 설치·설정·토큰 발급·실행 시작 가이드 |

```bash
pip install -r mcp_server/requirements.txt
python mcp_server/run_server.py                              # 저장소 루트에서 (로컬)
python /절대경로/dbsec-open-api/mcp_server/run_server.py   # cwd 무관 (Claude Desktop 동일)
```

- 서버는 기동 시 저장소를 **`git fetch` + `git reset --hard`** 로 원격과 일치시킵니다
  — **commit/push 는 하지 않습니다.** (`config.yaml`·`.dbsec_token.json` 등 untracked 파일은 보존)
- Claude Desktop 등 `cwd` 를 보장하지 않는 환경에서는 `args` 에 **`run_server.py` 절대경로**를
  지정하세요(`cwd` 불필요).
- 환경변수 `DBSEC_MCP_GIT_REPO`(clone 대상 URL) · `DBSEC_MCP_GIT_BRANCH` · `DBSEC_MCP_GIT_DIR` ·
  `DBSEC_MCP_GIT_SKIP_SYNC`(오프라인) 로 동작을 제어합니다.
- 클라이언트 등록 방법(`mcpServers` JSON)·검증법은 **[mcp_server/README.md](mcp_server/README.md)** 참고.

> 각 예제 docstring 의 `응답 파라미터 (Out)` 섹션은 포털 명세를 바탕으로 작성되어 있습니다.
> API 가 바뀌면 해당 **예제 파일의 docstring 을 직접 수정**하면 MCP 서버에 그대로 반영됩니다.

---

## 폴더 구조

```
dbsec-open-api/
├── pyproject.toml                          # 패키지 설정 (pip + uv)
├── requirements.txt                        # 의존성
├── config.yaml.example                     # 설정 템플릿
│
├── dbsec_sdk/                              # 클라이언트 라이브러리
│   ├── client.py                           #   DBSecClient (비동기 단일 진입점) + 내부 동기 코어
│   ├── config.py                           #   설정 (YAML + env)
│   ├── auth.py                             #   OAuth2 토큰 수명주기(get_token/force_refresh/revoke) + auto_token 자동발급
│   ├── rate_limiter.py                     #   유량제어 (앱 20TPS + 엔드포인트별 TPS, 2-tier)
│   ├── exceptions.py                       #   APIError + 오류코드 레퍼런스
│   ├── response.py                         #   APIResponse + to_dataframe()
│   │
│   ├── apis/                               #   ★ 그룹별 API 메서드
│   │   ├── registry.py                     #     APIRegistry — client.apis 진입점
│   │   ├── auth/                           #     OAuth 인증
│   │   ├── common/                         #     관심종목
│   │   ├── kr_stock_order/                 #     국내주식주문
│   │   ├── kr_stock_quote/                 #     국내주식시세
│   │   ├── kr_stock_realtime/              #     국내주식 실시간
│   │   ├── kr_futopt_order/                #     국내선물옵션주문
│   │   ├── kr_futopt_quote/                #     국내선물옵션시세
│   │   ├── kr_futopt_realtime/             #     국내선물옵션 실시간
│   │   ├── kr_chart/                       #     국내주식/선물 차트
│   │   ├── ov_stock_order/                 #     해외주식주문
│   │   ├── ov_stock_quote/                 #     해외주식시세
│   │   ├── ov_stock_realtime/              #     해외주식 실시간
│   │   ├── ov_futopt_order/                #     해외선물옵션주문
│   │   ├── ov_futopt_quote/                #     해외선물옵션시세
│   │   ├── ov_futopt_realtime/             #     해외선물옵션 실시간
│   │   ├── bond_order/                     #     장내채권주문
│   │   ├── bond_quote/                     #     장내채권시세
│   │   ├── bond_realtime/                  #     장내채권 실시간
│   │   └── ws_common/                      #     웹소켓 공통
│   │
│   ├── websocket/                          #   실시간 WebSocket (stream.py)
│   └── client_examples/                    #   SDK(client.apis.*) 사용 예제
│       ├── quickstart.py                   #     읽기전용 조회 데모 (async)
│       ├── kr-stock-trading-basic.ipynb    #     국내주식 트레이딩 기본 (노트북)
│       └── ov-stock-trading-basic.ipynb    #     해외주식 트레이딩 기본 (노트북)
│
├── examples/                               # 그룹별 standalone 예제 (call_rest 방식)
│   ├── dbsec_helper.py                     #   공통 헬퍼 (config 로드·토큰·REST/WS 호출)
│   └── <group_slug>/
│       ├── README.md                       #   그룹 내 메서드 목록 + 호출 패턴
│       └── <method>.py                     #   API당 1파일 — 독립 실행 (docstring 에 In/Out 명세)
│
├── mcp_server/                             # 코드 어시스턴트 MCP 서버 (stdio)
│   ├── run_server.py                       #   진입점(cwd 무관): sync→인덱싱→서버 기동
│   ├── sync.py                             #   GitHub 강제 동기화 fetch+reset (commit/push 없음)
│   ├── catalog.py                          #   examples + api_support_matrix.md 파싱 인덱스
│   └── server.py                           #   FastMCP tools (list/search/spec/sample/guide)
│
├── HOWTOUSE.md                             # 초보자용 단계별 사용 가이드
└── docs/                                   # 가이드 문서
    ├── sdk_usage.md                        #   dbsec_sdk SDK 사용법 (client.apis.*)
    ├── api_support_matrix.md               #   API 인벤토리 + 모의투자 ⭕/❌ + 엔드포인트별 TPS
    └── errors_and_rate_limits.md           #   오류코드·유량제어 전수
```

---

## 설치

### pip

```bash
pip install -e .
```

### uv (권장)

```bash
uv pip install -e .
```

### 의존성

| 패키지 | 용도 | 필수 |
|--------|------|:----:|
| `requests` | REST API 호출 | ✓ |
| `websockets` | 실시간 WebSocket 통신 | ✓ |
| `python-dotenv` | 환경변수 관리 | ✓ |
| `pyyaml` | YAML 설정 파일 로드 | ✓ |
| `pandas` | `resp.to_dataframe()` · 예제(quickstart·노트북) | ✓ |

---

## 설정

### 1. 설정 파일 생성

```bash
cp config.yaml.example config.yaml          # macOS / Linux / Git Bash
# Windows CMD:        copy config.yaml.example config.yaml
# Windows PowerShell: Copy-Item config.yaml.example config.yaml
```

### 2. `config.yaml` 수정

```yaml
auth:
  # 실전투자
  prd_app_key:    "앱키"
  prd_app_secret: "앱키 시크릿"

  # 모의투자
  vtl_app_key:    "모의투자 앱키"
  vtl_app_secret: "모의투자 앱키 시크릿"

environment:
  base_url: "https://openapi.dbsec.co.kr:8443"
  # WebSocket — 일반 (대부분 그룹)
  ws_production: "wss://openapi.dbsec.co.kr:7070/websocket"
  ws_demo:       "wss://openapi.dbsec.co.kr:17070/websocket"
  # WebSocket — 해외선물옵션(ov_futopt) 전용 포트 — 운영 전용 (모의투자 미지원)
  ws_production_ov_futopt: "wss://openapi.dbsec.co.kr:7071/websocket"
  mode: "demo"   # "production" → prd_* / "demo" → vtl_*
```

> ⚠️ **해외선물옵션(`ov_futopt_*`)은 모의투자를 지원하지 않습니다.** 운영(`mode: "production"`) 환경에서만 호출 가능하며, `dbsec_helper` 와 `dbsec_sdk.Config.ws_url_for()` 가 demo 모드 호출을 명시적으로 차단합니다.

---

## 사용법

### 1. 인증 (토큰 자동)

`DBSecClient` 는 **비동기** 클라이언트입니다 — 모든 호출에 `await`, 진입은 `asyncio.run()`.

```python
import asyncio
from dbsec_sdk import DBSecClient

async def main():
    async with DBSecClient("config.yaml") as client:
        # auto_token=True(기본): 첫 API 호출 시 토큰 자동 발급(없거나 만료/무효면 자동 재발급)
        ...

asyncio.run(main())
```

> **토큰 정책**: 24시간 유효. 24시간 이내 재발급 요청은 기존 토큰 반환. 새 토큰이 필요하면 `await client.force_refresh()`(revoke→재발급). 토큰은 만료 *시각*까지 사용하며 만료 전 미리 갱신하지 않습니다.
> **`auto_token` (기본 True)**: 요청 시 토큰이 없거나 무효/만료(IGW00121/00123)면 SDK 가 자동으로 발급·재발급합니다(stdin 프롬프트 없음 → 헤드리스/봇·CI 에서도 안전). 토큰거부 응답의 재발급은 요청당 최대 `token_retry_limit`회(기본 5).
> **`auto_token=False`**: 자동 발급하지 않습니다 → 토큰이 없으면 `AuthError`, 무효/만료는 `APIError`. `await client.get_token()` / `force_refresh()` / `revoke()` 로 토큰을 직접 관리하세요.

토큰을 명시적으로 다루려면:

```python
token = await client.get_token()                 # 현재 토큰 확보 (캐시에 없으면 발급)
await client.force_refresh()                      # 강제 갱신 (폐기 후 재발급)
await client.revoke()                             # 폐기 (서버 무효화 + 로컬 캐시 삭제)
```

### 2. 통합 API 호출 패턴 — `client.apis`

모든 API는 `await client.apis.<그룹>.<메서드>(...)` 형태로 호출합니다.
(아래 스니펫들은 위 `main()` 같은 **async 함수 안**에서 실행한다고 가정합니다.)

```python
resp = await client.apis.<group_slug>.<method_name>(
    필드1=값,
    필드2=값,
    ...
    cont_yn="N",                  # 연속거래 여부 (기본 N; 전체 자동수신은 fetch_all)
    cont_key="",                  # 연속키 (자동 페이징 시 직접 넘길 필요 없음)
)
```

- `<group_slug>` : `kr_stock_order`, `ov_stock_quote`, `kr_futopt_realtime`, `bond_order` 등
- `<method_name>` : 도메인 접두어 + 동작/대상. 예) `kr_stock_order`, `ov_stock_inquire_balance_margin`
- 반환값 : `APIResponse` (`.body`, `.rsp_cd`, `.message`, `.to_dataframe()`, `.has_more`, `.cont_key`)

#### 연속조회(자동 페이징) — `fetch_all=True`

응답이 여러 페이지로 나뉘는 조회(순위·종목조회·시간대별 체결·틱차트 등)는
**단건과 똑같이 호출하되 `fetch_all=True`** 만 더하면 **서버가 끝(`cont_yn='N'`)을 알릴 때까지
전부** 받아 **하나의 `APIResponse` 로 병합**합니다(단건에서도 `resp.has_more`/`resp.cont_key` 로 확인 가능).

```python
# 단건과 같은 호출 + fetch_all=True (list 블록 Out1/Out2 가 페이지 간 누적됨)
resp = await client.apis.kr_stock_quote.kr_stock_inquire_condition_rise_fall(
    InputDateClsCode="0",
    InputRankSortClsCode1="12",  # 당일 / 상승률
    InputMrktClsCode="K",
    InputBstpIscd="1001",  # 코스피
    fetch_all=True)
df = resp.to_dataframe()          # 전 페이지 누적 결과
n_pages = len(resp.pages)         # 받은 페이지 수 (원본 페이지는 resp.pages 로 접근)

# 데이터가 매우 많은 조회(예: 틱차트)는 max_pages 로 상한을 둘 수 있음 (기본 None = 끝까지)
ticks = await client.apis.kr_chart.kr_chart_chart_tick(
    **tick_args,
    fetch_all=True,
    max_pages=10)

# 저수준(raw 경로 직접 호출): post_paged / get_paged → list[APIResponse]
pages = await client.post_paged("/api/v1/quote/kr-chart/tick", {"In": {...}})
```

- 연속키 인자(`cont_yn`/`cont_key`)는 자동 처리되므로 신경 쓰지 않아도 됩니다.
- 각 페이지 호출은 **유량제어가 자동 페이싱**합니다(별도 sleep 불필요).
- 구버전 `client.fetch_all(메서드, …)` 도 하위호환으로 동작하지만, 위 `fetch_all=True` 형태를 권장합니다.

### 3. 국내주식 — 주문/조회

#### 3-1. 종합주문 (CSPAT00600)

```python
# 시장가 매수
resp = await client.apis.kr_stock_order.kr_stock_order(
    IsuNo="A005930",            # A + 6자리 (삼성전자)
    OrdQty=1,
    OrdPrc=0,                   # 시장가 시 0
    BnsTpCode="2",              # 1: 매도, 2: 매수
    OrdprcPtnCode="03",         # 00:지정가, 03:시장가, 05:조건부지정, 06:최유리, 07:최우선
    MgntrnCode="000",           # 000:보통(일반주문), 신용상환 101/103/105/107/180
    LoanDt="00000000",          # 일반:00000000, 신용매도:결제일자(YYYYMMDD)
    OrdCndiTpCode="0",          # 0:없음, 1:IOC, 2:FOK
    TrchNo=1,                   # 1:KRX 고정
)
print(resp.body["Out"]["OrdNo"])
```

#### 3-2. 정정/취소

```python
# 정정주문 (CSPAT00700)
await client.apis.kr_stock_order.kr_stock_order_modify(
    OrgOrdNo=14404,
    IsuNo="A005930",
    OrdQty=5,
    OrdprcPtnCode="00",
    OrdCndiTpCode="0",
    OrdPrc=80000)

# 취소주문 (CSPAT00800)
await client.apis.kr_stock_order.kr_stock_order_cancel(
    OrgOrdNo=14414,
    IsuNo="A005930",
    OrdQty=10)
```

#### 3-3. 잔고 / 체결 / 예수금

```python
# 여러 조회는 asyncio.gather 로 동시에 (유량제어가 TPS 자동 준수)
balance, deposit = await asyncio.gather(
    client.apis.kr_stock_order.kr_stock_inquire_balance(QryTpCode0="0"),
    client.apis.kr_stock_order.kr_stock_inquire_deposit(),
)
executions  = await client.apis.kr_stock_order.kr_stock_inquire_executions(
    SorTpYn="2",
    ExecYn="0",
    TrdMktCode="0",
    BnsTpCode="0",
    IsuTpCode="0",
    QryTp="0")
psbl_qty    = await client.apis.kr_stock_order.kr_stock_inquire_psbl_quantity(
    BnsTpCode="2",
    IsuNo="A005930",
    OrdPrc=77000)
```

#### 3-4. 시세

```python
price       = await client.apis.kr_stock_quote.kr_stock_inquire_price(
    InputCondMrktDivCode="J",
    InputIscd1="005930")
orderbook   = await client.apis.kr_stock_quote.kr_stock_inquire_orderbook(
    InputCondMrktDivCode="J",
    InputIscd1="005930")
ranks       = await client.apis.kr_stock_quote.kr_stock_inquire_condition_rise_fall(...)
```

### 4. 그 외 상품 — 해외주식 · 선물옵션 · 채권 · 차트 · WebSocket

위 국내주식과 동일한 `client.apis.<그룹>.<메서드>(...)` 패턴입니다. 각 그룹의 전체 메서드·필수 필드·실행 예제는 그룹별 README에서 확인하세요.

| 상품군 | 주요 메서드 예시 | 그룹별 가이드 |
|-------|----------------|--------------|
| 해외주식 주문/조회 | `ov_stock_order`, `ov_stock_inquire_balance_margin` | [examples/ov_stock_order](examples/ov_stock_order/README.md) · [quote](examples/ov_stock_quote/README.md) · [realtime](examples/ov_stock_realtime/README.md) |
| 국내선물옵션 | `kr_futopt_order`, `kr_futopt_order_night`, `kr_futopt_inquire_balance` | [order](examples/kr_futopt_order/README.md) · [quote](examples/kr_futopt_quote/README.md) · [realtime](examples/kr_futopt_realtime/README.md) |
| 해외선물옵션 ⚠️ (운영 전용) | `ov_futopt_order`, `ov_futopt_inquire_open_interest` | [order](examples/ov_futopt_order/README.md) · [quote](examples/ov_futopt_quote/README.md) · [realtime](examples/ov_futopt_realtime/README.md) |
| 장내채권 | `bond_order`, `bond_inquire_balance`, `bond_inquire_price` | [order](examples/bond_order/README.md) · [quote](examples/bond_quote/README.md) · [realtime](examples/bond_realtime/README.md) |
| 차트 (국내주식·선물 공용) | `kr_chart_tick`, `kr_chart_day` | [kr_chart](examples/kr_chart/README.md) |
| WebSocket 실시간 | `client.create_websocket()` → `add_realtime(tr_cd, tr_key, tr_type)` (1=시세구독·3=계좌등록) | [kr_stock_realtime](examples/kr_stock_realtime/README.md) · [ws_common](examples/ws_common/README.md) |

### 5. DataFrame 변환

```python
resp = await client.apis.kr_stock_order.kr_stock_inquire_balance(QryTpCode0="0")

print(resp.body["Out"]["TotEvalAmt"])         # dict 그대로 (pandas 불필요)
df = resp.to_dataframe()                      # 자동 탐색 (list[dict] 우선)
df = resp.to_dataframe(key="Out1")            # 특정 블록 지정
```

---

## 전체 그룹 & API

| 그룹 | slug | 비고 |
|------|------|------|
| OAuth 인증 | `auth` | 토큰 발급/폐기 |
| 공통 | `common` | 관심종목 |
| **국내주식주문** | `kr_stock_order` | NXT 포함, 잔고·체결·예수금·신용 |
| 국내주식시세 | `kr_stock_quote` | 종목/현재가/호가/체결/투자자/섹터 |
| 국내주식 실시간 | `kr_stock_realtime` | 주문체결/호가/ELW/업종지수 |
| **국내선물옵션주문** | `kr_futopt_order` | 주간/야간 분리 |
| 국내선물옵션시세 | `kr_futopt_quote` | 종목/현재가/호가/체결/전광판 |
| 국내선물옵션 실시간 | `kr_futopt_realtime` | 지수/주식/상품 선물·옵션, 미니, 위클리, KOSDAQ150, 야간 |
| 국내주식/선물 차트 | `kr_chart` | 틱/분/일/주/월 |
| **해외주식주문** | `ov_stock_order` | 미국주식, 잔고/증거금/평균매입단가 |
| 해외주식시세 | `ov_stock_quote` | 현재가/호가/체결 + 차트 5종 |
| 해외주식 실시간 | `ov_stock_realtime` | 체결가/호가 + 지연버전 |
| **해외선물옵션주문** | `ov_futopt_order` | 주문/체결/미결제/예탁 |
| 해외선물옵션시세 | `ov_futopt_quote` | 호가&현재가 + 차트(선물/옵션 분리) |
| 해외선물옵션 실시간 | `ov_futopt_realtime` | 주문체결/잔고/시세/호가 |
| 장내채권주문 | `bond_order` | 매수/매도/정정/취소/잔고 |
| 장내채권시세 | `bond_quote` | 상세검색/현재가/호가 |
| 장내채권 실시간 | `bond_realtime` | 일반/소액 채권 체결·호가 |
| 웹소켓 공통 | `ws_common` | 세션 초기화 |

> 자세한 메서드 이름은 `docs/api_support_matrix.md` 또는 각 그룹의 `examples/<slug>/README.md` 참조.

---

## 메서드 네이밍 규칙 (도메인 접두어)

MCP 툴로 노출하거나 LLM 에이전트에서 사용할 때 **메서드 이름만으로 시장 도메인이 식별**되도록 접두어를 일관 적용했습니다.

| 도메인 | 접두어 | 예시 |
|--------|--------|------|
| 국내주식 | `kr_stock_` | `kr_stock_order`, `kr_stock_inquire_balance`, `kr_stock_realtime_execution_price` |
| 해외주식 | `ov_stock_` | `ov_stock_order`, `ov_stock_inquire_balance_margin`, `ov_stock_realtime_orderbook` |
| 국내선물옵션 | `kr_futopt_` | `kr_futopt_order`, `kr_futopt_inquire_balance`, `kr_futopt_realtime_index_future_orderbook` |
| 해외선물옵션 | `ov_futopt_` | `ov_futopt_order`, `ov_futopt_inquire_open_interest`, `ov_futopt_realtime_future_quote` |
| 장내채권 | `bond_` | `bond_order`, `bond_inquire_balance`, `bond_realtime_normal_execution` |
| 차트 (국내주식·선물 공용) | `kr_chart_` | `kr_chart_tick`, `kr_chart_day`, `kr_chart_month` |
| 인증 / 공통 / 웹소켓 | (없음) | `token_issue`, `inquire_group_list`, `ws_session_disconnect` |

**동사/주제 패턴**

| 동사 | 의미 |
|------|------|
| `order`, `order_modify`, `order_cancel`, `order_buy`, `order_sell` | 주문 |
| `inquire_*` | 조회 (잔고/체결/예수금/실현손익 등) |
| `realtime_*` | WebSocket 실시간 |
| `chart_*` | 시계열 차트 |
| `search_*` | 종목·코드 마스터 검색 |
| `token_*`, `ws_*` | 인증/세션 제어 |

→ 모든 메서드 **전역 유일** 보장 (그룹 내 + 그룹 간 중복 0건)

---

## 운영 vs 모의투자

| 항목 | 운영 | 모의투자 |
|------|------|----------|
| **REST API URL** | `https://openapi.dbsec.co.kr:8443` | **동일** (앱 속성으로 내부 분기) |
| **WebSocket URL (일반)** | `wss://openapi.dbsec.co.kr:7070/websocket` | `wss://openapi.dbsec.co.kr:17070/websocket` |
| **WebSocket URL (해외선옵)** | `wss://openapi.dbsec.co.kr:7071/websocket` | — (미지원) |
| **APP_KEY / APP_SECRET** | 운영용 발급 | 모의투자용 발급 |

> REST API는 운영/모의투자 URL이 동일합니다. 발급받은 앱 키의 속성으로 서버가 분기합니다. **WebSocket 포트만 다릅니다** (운영: 7070, 모의: 17070).
>
> ⚠️ **해외선물옵션(`ov_futopt_*`)은 모의투자가 시스템 차원에서 없습니다** — 운영(7071) 전용. demo 모드로 호출 시 라이브러리가 즉시 차단합니다.

`config.yaml`에서 `mode`를 변경하면 WebSocket URL이 자동 전환됩니다:

```yaml
environment:
  mode: "demo"          # 모의투자 (17070)
  # mode: "production"  # 운영 (7070)
```

> ⚠️ **모든 API가 모의투자에서 동작하지는 않습니다.** [부록 — API 모의투자 지원 현황](#부록--api-모의투자-지원-현황) 참조.

---

## 오류코드 & 유량제어

핵심만 요약합니다. 전체 오류코드표·유량제어 세부 정책·사용 예시는 **[docs/errors_and_rate_limits.md](docs/errors_and_rate_limits.md)** 참조.

**자주 만나는 오류**

| 코드 | 설명 |
|------|------|
| IGW00121 / IGW00123 | 토큰 무효/만료 — `auto_token=True`면 자동 재발급, `False`면 APIError 로 표면화 |
| IGW00201 | 호출 거래건수 초과 — 호출 빈도 조절 |
| 2611 | 장시작 전 또는 장마감 |
| 2714 / 2752 | 매매가능수량·증거금 부족 |

**유량제어 (SDK 가 자동 페이싱)**

SDK 가 호출 직전에 **2-tier 유량제어**(앱 20TPS + 엔드포인트별 TPS)를 자동 적용해
서버 `IGW00201`(호출 거래건수 초과)을 사전 차단합니다. 끄려면 `DBSecClient(..., rate_limit=False)`.
엔드포인트별 TPS 의 단일 소스는 [docs/api_support_matrix.md](docs/api_support_matrix.md) 의 `TPS` 컬럼입니다.

| 구분 | 제한 | 비고 |
|------|------|------|
| REST 앱(계좌)별 | 20 TPS | 엔드포인트별(주문 10·잔고 2 등)은 매트릭스 `TPS` 컬럼 |
| 토큰 발급/폐기 | 1 TPM | 파일 캐시(24h 재사용)로 사실상 회피 |
| WebSocket 세션 / 종목 | 2세션 / 세션당 50종목 | 50종목 초과 시 `RateLimitError` |

```python
from dbsec_sdk.exceptions import lookup_error
print(lookup_error("IGW00123"))   # "기간이 만료된 token입니다."
```

---

## 부록 — API 모의투자 지원 현황

DB증권 Open API 가이드 페이지 Description 영역에 **`※ 모의투자 계좌로 사용가능한 API입니다.`** 문구가 있으면 모의투자에서도 사용 가능합니다. 그 외는 실전투자 환경에서만 호출됩니다.

- **⭕ 모의투자 + 실전투자 모두 지원** — 시세 · 실시간 · 차트 그룹은 전부 사용 가능
- **❌ 실전투자 전용** — 대부분의 주문 및 일부 조회 API (특히 해외선물옵션은 시스템 차원 모의투자 미지원)

**각 API별 ⭕/❌ 표시가 담긴 전체 매트릭스는** → **[docs/api_support_matrix.md](docs/api_support_matrix.md)**

