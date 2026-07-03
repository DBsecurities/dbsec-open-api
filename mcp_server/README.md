# DB증권 Open API 코드 어시스턴트 MCP 서버

LLM(Claude Desktop · Claude Code · Cursor 등)이 DB증권 Open API 의 **그룹·엔드포인트 목록**,
**요청(In)·응답(Out) 파라미터 명세**, **실행 가능한 파이썬 샘플코드**를 직접 조회할 수 있게 해주는
MCP(Model Context Protocol, stdio) 서버입니다.

명세의 **원본은 `examples/`(샘플코드)** 입니다 — 요청(In)은 코드 내 인라인 주석에서,
응답(Out)은 docstring 의 `응답 파라미터 (Out)` 섹션에서 파싱하며, 모의투자·TPS·TR코드는
`docs/api_support_matrix.md` 로 보강합니다. 예제를 수정하면 MCP 가 그대로 반영합니다
(별도 명세 캐시에 의존하지 않음). 서버를 실행하면 **GitHub 저장소를 원격 기준으로 강제
동기화(reset)** 한 뒤 기동합니다.

> **동기화 전략 — `git fetch` 후 `git reset --hard`**
> 로컬을 원격과 **정확히 일치**시킵니다(로컬 커밋·수정이 있어도 원격 상태로 덮어씀).
> `add` · `commit` · `push` 는 **절대 하지 않습니다** — 사용자는 받아오기만 합니다.
> `reset --hard` 는 **추적 파일만** 원복하며 `git clean` 을 돌리지 않으므로,
> `config.yaml`·`.dbsec_token.json` 같은 **추적되지 않는 파일은 그대로 보존**됩니다.

---

## 제공 도구 (MCP tools)

| 도구 | 설명 |
|---|---|
| `list_api_groups()` | 전체 그룹(도메인) 목록 + 그룹별 API 개수 + 모의투자 지원 수 |
| `search_apis(query, group?)` | 키워드·TR코드·slug·경로로 API 검색 (한글 가능) |
| `get_api_spec(identifier)` | 엔드포인트·메서드·TPS·모의투자·**In/Out 파라미터**·요청/응답 예시 전체 |
| `get_sample_code(identifier)` | 해당 API 의 실행 가능한 파이썬 샘플코드 원문 |
| `get_setup_guide()` | 설치·`config.yaml`·토큰 발급·실행법 시작 가이드 |

리소스: `dbsec://catalog` — 전체 API 인덱스(JSON).

`identifier` 는 **메서드 slug**(예: `kr_stock_inquire_price`) 또는 **TR코드**(예: `PRICE`).
TR코드가 여러 그룹에 중복되면(예: `HOGA`) 후보 목록을 돌려주므로 slug 로 다시 지정하면 됩니다.

---

## 설치

```bash
# 저장소 루트에서
pip install -r mcp_server/requirements.txt
```

Python 3.10+ 와 `git` 이 필요합니다.

## 실행

진입점은 **`run_server.py` 하나**입니다. cwd(작업 디렉토리)에 의존하지 않으므로
어느 위치에서 실행해도 동작합니다(자기 파일 위치로 저장소 루트를 계산).

```bash
# 저장소 루트에서
python mcp_server/run_server.py

# 또는 절대경로로 (Claude Desktop 등록과 동일한 방식)
python /절대경로/dbsec-open-api/mcp_server/run_server.py
```

오프라인/개발 중 동기화를 건너뛰려면:

```bash
DBSEC_MCP_GIT_SKIP_SYNC=1 python mcp_server/run_server.py          # macOS/Linux
$env:DBSEC_MCP_GIT_SKIP_SYNC="1"; python mcp_server/run_server.py  # Windows PowerShell
```

### 환경변수

| 변수                        | 기본값 | 용도 |
|---------------------------|---|---|
| `DBSEC_MCP_GIT_REPO`      | (없음) | 로컬에 저장소가 없을 때 `git clone` 할 GitHub URL |
| `DBSEC_MCP_GIT_BRANCH`    | `main` | fetch/clone 브랜치 |
| `DBSEC_MCP_GIT_DIR`       | 저장소 루트 | 동기화 대상 로컬 경로 |
| `DBSEC_MCP_GIT_SKIP_SYNC` | (없음) | `1` 이면 동기화 생략 (오프라인) |

> 이미 `git clone` 으로 받아 둔 저장소 안에서 실행하면 `DBSEC_MCP_GIT_REPO` 없이도
> 현재 저장소의 `origin` 을 `git fetch` 한 뒤 `git reset --hard` 로 원격과 일치시킵니다.

---

## 클라이언트 연결

### Claude Desktop / Claude Code (`mcpServers`)

설정 파일(예: `claude_desktop_config.json` 또는 `~/.claude.json`)에 추가:

`args` 에 **`run_server.py` 의 절대경로**를 넣습니다(`cwd` 불필요).

```json
{
  "mcpServers": {
    "dbsec-code-assistant": {
      "command": "python",
      "args": ["C:/절대경로/dbsec-open-api/mcp_server/run_server.py"]
    }
  }
}
```

- `args` 의 경로는 이 저장소를 `clone` 한 위치의 **`mcp_server/run_server.py` 절대경로**.
  `cwd` 에 의존하지 않으므로 `cwd` 항목은 넣지 않아도 됩니다.
- Windows 경로는 `"C:/.../run_server.py"`(슬래시) 또는 `"C:\\...\\run_server.py"`(역슬래시 2개)
  형식으로 적습니다.
- `"command": "python"` 은 PATH 의 파이썬을 사용합니다. 가상환경을 쓰면 그 환경의
  `python.exe` 절대경로를 지정하세요.

### Cursor (`.cursor/mcp.json`)

```json
{
  "mcpServers": {
    "dbsec-code-assistant": {
      "command": "python",
      "args": ["/절대경로/dbsec-open-api/mcp_server/run_server.py"]
    }
  }
}
```

---

## 동작 검증 (MCP Inspector)

```bash
npx @modelcontextprotocol/inspector python /절대경로/dbsec-open-api/mcp_server/run_server.py
```

브라우저에서 `list_api_groups` → `search_apis(현재가)` → `get_api_spec(kr_stock_inquire_price)`
→ `get_sample_code(kr_stock_inquire_price)` 순서로 호출해 보세요.

---

## 구조

```
mcp_server/
├── run_server.py # 유일한 진입점: sync(fetch+reset) → 카탈로그 적재 → mcp.run(stdio)  (cwd 무관)
├── sync.py       # GitHub 강제 동기화 fetch+reset (commit/push 없음)
├── catalog.py    # examples/*.py(docstring·In주석) + api_support_matrix.md 파싱 인덱스
├── server.py     # FastMCP 인스턴스 + 5개 tool + 1개 resource
├── requirements.txt
└── pyproject.toml
```

명세의 원본은 `examples/` 이므로, API 가 추가·변경되면 **해당 예제 파일을 직접 수정**하면 됩니다.
요청(In)은 코드 내 인라인 주석, 응답(Out)은 docstring 의 `OUT_BEGIN ~ OUT_END` 섹션에 작성합니다.
