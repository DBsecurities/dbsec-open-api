# HOWTOUSE — DB증권 Open API 샘플코드 사용 가이드 (초보자용)

이 문서는 프로그래밍이 처음이거나 DB증권 Open API 를 처음 써보는 분도
**순서대로 따라 하면** 시세 조회·예제 실행·LLM 코드 어시스턴트(MCP) 연결까지
할 수 있도록 만든 가이드입니다.

---

## 0. 이 저장소는 무엇인가요?

DB증권 Open API(주식·선물옵션·채권 시세/주문/실시간)를 파이썬으로 호출하는
**샘플코드 모음**입니다. 크게 세 부분으로 되어 있습니다.

| 폴더 | 내용 |
|---|---|
| `examples/` | API 별 **단독 실행 가능한** 파이썬 예제 (그룹별 폴더, 총 170개). **명세의 원본** — 각 파일 docstring 에 요청(In)·응답(Out) 파라미터가 정리되어 있습니다. |
| `mcp_server/` | LLM 이 API 명세·샘플코드를 조회하는 **MCP 서버** (examples 를 읽어 제공) |
| `docs/api_support_matrix.md` | 그룹·TR코드·모의투자 지원·TPS 일람표 |

`examples/` 의 각 파일은 다른 파일에 의존하지 않고 **혼자서 실행**됩니다
(`examples/dbsec_helper.py` 공통 헬퍼만 사용).

---

## 1. 준비물

1. **Python 3.10 이상** — 터미널에서 확인:
   ```bash
   python --version
   ```
2. **DB증권 Open API 앱키(App Key/Secret)**
   - [openapi.dbsec.co.kr](https://openapi.dbsec.co.kr) 에서 로그인 → API 서비스 신청 →
     **실전투자용**(`prd_*`) 과 **모의투자용**(`vtl_*`) 앱키를 발급받습니다.
   - 처음에는 **모의투자(demo)** 로 시작하길 권장합니다(실제 매매 위험 없음).
3. (선택) **git** — MCP 서버의 자동 동기화 기능을 쓰려면 필요합니다.

---

## 2. 설치

저장소를 내려받은 폴더(루트)에서:

```bash
pip install -r requirements.txt
```

> 가상환경(venv) 사용을 권장합니다.
> ```bash
> python -m venv .venv
> # macOS/Linux
> source .venv/bin/activate
> # Windows PowerShell
> .\.venv\Scripts\Activate.ps1
> pip install -r requirements.txt
> ```

---

## 3. 설정 파일 만들기 (`config.yaml`)

예시 파일을 복사해서 내 앱키를 채워 넣습니다.

```bash
# macOS/Linux
cp config.yaml.example config.yaml
# Windows PowerShell
Copy-Item config.yaml.example config.yaml
```

`config.yaml` 을 열어 아래를 수정합니다.

```yaml
auth:
  # 실전투자 앱키
  prd_app_key:    "발급받은 실전 앱키"
  prd_app_secret: "발급받은 실전 시크릿"
  # 모의투자 앱키
  vtl_app_key:    "발급받은 모의 앱키"
  vtl_app_secret: "발급받은 모의 시크릿"

environment:
  # 처음에는 모의투자로!
  mode: "demo"        # demo = 모의투자, production = 실전투자
```

- `mode: "demo"` 이면 `vtl_*` 앱키를, `production` 이면 `prd_*` 앱키를 사용합니다.
- `config.yaml` 에는 비밀키가 들어가므로 **외부에 공유하지 마세요**(이미 `.gitignore` 에 포함).

---

## 4. 접근토큰 발급

API 호출에는 접근토큰이 필요합니다. 아래 한 번만 실행하면 토큰을 받아
루트 `.dbsec_token.json` 에 캐시합니다(24시간 유효, 이후 예제들이 자동 재사용).

```bash
python examples/auth/token_issue.py
```

성공하면 `✓ 토큰 캐시 저장: ...` 메시지가 나옵니다.
토큰을 폐기하려면 `python examples/auth/token_revoke.py`.

---

## 5. 첫 예제 실행 — 삼성전자 현재가 조회

```bash
python examples/kr_stock_quote/kr_stock_inquire_price.py
```

응답 JSON 과 함께 `rsp_cd=00000 정상 처리 되었습니다.` 가 보이면 성공입니다.

> 토큰 캐시가 없으면 예제가 자동 발급 여부를 물어봅니다. `1` 을 누르면 발급 후 계속 진행합니다.

---

## 6. 다른 예제 둘러보기

예제는 **그룹별 폴더**로 정리되어 있고, 각 폴더에 `README.md` 와 API 목록이 있습니다.

| 그룹 폴더 | 내용 |
|---|---|
| `examples/kr_stock_quote/` | 국내주식 시세(현재가·호가·체결 등) |
| `examples/kr_stock_order/` | 국내주식 주문/조회 |
| `examples/kr_futopt_quote/` `kr_futopt_order/` | 국내 선물옵션 |
| `examples/ov_stock_quote/` `ov_stock_order/` | 해외주식 |
| `examples/kr_chart/` | 차트(틱·분·일·주·월) |
| `examples/*_realtime/` | 실시간(WebSocket) 시세 |
| `examples/bond_*` | 장내채권 |

각 예제 파일 **맨 위 docstring** 에는 이런 정보가 들어 있습니다.

- 엔드포인트 / TPS / 가이드 링크
- 요청(In) 파라미터 — 호출부 주석으로 설명
- **응답(Out) 파라미터** — `── 응답 파라미터 (Out) ──` 섹션에 필드명·한글명·타입·길이 정리

실행 방법:
```bash
python examples/<그룹>/<파일이름>.py
```

> ⚠️ **주문/정정/취소 예제는 실제 매매가 실행될 수 있습니다.**
> 반드시 `config.yaml` 의 `mode: "demo"`(모의투자)에서 먼저 테스트하세요.
> 해외선물옵션(`ov_futopt_*`)은 모의투자를 지원하지 않아 실전 전용입니다.

---

## 7. LLM 코드 어시스턴트(MCP) 연결하기

`mcp_server/` 는 Claude Desktop · Claude Code · Cursor 같은 **AI 코딩 도구**가
"어떤 API 가 있고, 파라미터·샘플코드가 무엇인지" 직접 물어볼 수 있게 해줍니다.

### 7-1. 설치

```bash
pip install -r mcp_server/requirements.txt
```

### 7-2. 단독 실행 테스트

```bash
# 저장소 루트에서 (로컬 테스트)
python mcp_server/run_server.py
# 또는 위치에 상관없이 절대경로로 (Claude Desktop 과 동일한 방식)
python /절대경로/dbsec-open-api/mcp_server/run_server.py
```

실행 시 GitHub 저장소를 **원격 기준으로 동기화(fetch + reset)** 한 뒤 서버가 뜹니다.
(오프라인이면 동기화를 건너뛰려고 `DBSEC_MCP_GIT_SKIP_SYNC=1` 을 앞에 붙이세요.)

> **중요 — 동기화 방식 (fetch + reset)**
> 서버는 저장소를 **받아오기만** 합니다(커밋·푸시 안 함 → 로컬 변경이 GitHub 로 올라가지 않음).
> 동기화 시 로컬을 원격과 **정확히 일치**시키므로, 추적되는 파일을 직접 고쳐 두면 다음 실행에서
> 원격 내용으로 **덮어쓰여집니다.** 단, `config.yaml`·`.dbsec_token.json` 처럼 Git 이 추적하지 않는
> 파일은 **그대로 보존**되니 안심하세요.

### 7-3. AI 도구에 등록

Claude Desktop / Claude Code 설정에 추가(자기 경로·주소로 수정).
`args` 에 **`run_server.py` 의 절대경로**를 적습니다 — `cwd` 는 필요 없습니다.

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

> Windows 경로는 `"C:/.../run_server.py"`(슬래시) 또는 `"C:\\...\\run_server.py"`(역슬래시 2개)로 적습니다.
> 이전처럼 `"args": ["-m","mcp_server"]` + `"cwd"` 방식은 Claude Desktop 이 `cwd` 를 인식하지 못하면
> 실패할 수 있어, 절대경로 `run_server.py` 방식을 권장합니다.

등록 후 AI 에게 이렇게 물어볼 수 있습니다.

- "DB증권 API 그룹 목록 보여줘" → `list_api_groups`
- "현재가 조회 API 찾아줘" → `search_apis`
- "kr_stock_inquire_price 의 요청/응답 파라미터 알려줘" → `get_api_spec`
- "그 API 샘플코드 줘" → `get_sample_code`

자세한 도구 설명·환경변수는 [`mcp_server/README.md`](mcp_server/README.md) 참고.

---

## 8. 자주 묻는 질문 (FAQ)

**Q. `config.yaml 을 찾을 수 없습니다` 오류가 나요.**
3번 단계대로 `config.yaml.example` 을 `config.yaml` 로 복사했는지 확인하세요.

**Q. 토큰 관련 오류 / 401 이 나요.**
앱키가 `mode` 에 맞는지 확인하세요. `demo` 면 `vtl_*`, `production` 이면 `prd_*` 가 채워져 있어야 합니다.
`python examples/auth/token_revoke.py` 후 다시 `token_issue.py` 로 재발급해 보세요.

**Q. 한글이 깨져 보여요(Windows).**
예제 헬퍼가 출력 인코딩을 UTF-8 로 맞추지만, 콘솔 자체가 cp949 면 일부 글자가 `?` 로 보일 수 있습니다.
데이터 자체는 정상입니다. PowerShell 에서 `chcp 65001` 로 UTF-8 콘솔을 쓰면 깔끔합니다.

**Q. `cont_yn=Y / 연속 데이터 있음` 안내가 나와요.**
응답이 여러 페이지로 나뉜 경우입니다. 예제를 `call_rest` 대신 `call_rest_paged` 로 바꾸면
전체를 자동으로 받아옵니다(차트·시계열 예제 참고).

**Q. 실시간(WebSocket) 예제는 어떻게 멈추나요?**
`Ctrl + C` 로 종료합니다. 일반 시세는 구독 해제 메시지를 보낸 뒤 종료합니다.

---

준비가 끝났습니다. `examples/` 를 둘러보며 원하는 시세·주문 API 를 찾아 실행해 보세요.
API 명세·샘플코드는 각 예제 파일의 docstring, 또는 MCP 서버에서 언제든 확인할 수 있습니다.
