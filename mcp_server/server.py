"""FastMCP 서버 정의 — DB증권 Open API 코드 어시스턴트 툴.

명세의 원본은 `examples/<group>/<slug>.py` 다 (catalog 가 파싱).
  · 요청(In) 파라미터 → 본문 코드의 인라인 주석에서 추출
  · 응답(Out) 파라미터 → docstring 의 OUT_BEGIN~OUT_END 섹션
  · 모의투자/TPS/TR코드 → api_support_matrix.md 보강

툴
  list_api_groups()              그룹(도메인) 목록 + API 개수 + 모의투자 지원 수
  search_apis(query, group?)     키워드/TR코드/그룹으로 API 검색
  get_api_spec(identifier)       엔드포인트·In·Out 파라미터 요약
  get_sample_code(identifier)    실행 가능한 파이썬 샘플코드 원문
  get_setup_guide()              config.yaml·토큰 발급·실행법 시작 가이드
프롬프트 (Claude Desktop 등에서 사용자가 메뉴로 직접 선택하는 워크플로 템플릿)
  dbsec_easy_code(request)                   자연어 요청만으로 호출 코드 생성
  dbsec_detailed_code(api_identifier, task)  API(slug/TR코드) 지정 정밀 코드 생성
리소스
  dbsec://catalog                전체 API 인덱스(JSON)

identifier 는 메서드 slug(예: kr_stock_inquire_price) 또는 TR코드(예: PRICE).
"""
from __future__ import annotations

import json
import os
from pathlib import Path

from mcp.server.fastmcp import FastMCP

from . import catalog as _catalog
from .catalog import Api

# run_server.py 가 동기화 후 DBSEC_DATA_ROOT 를 설정한다. 없으면 저장소 루트.
_ROOT = Path(os.environ.get("DBSEC_DATA_ROOT", str(Path(__file__).resolve().parents[1])))
CAT = _catalog.load(_ROOT)

mcp = FastMCP("dbsec-code-assistant")


# ── 렌더링 헬퍼 ───────────────────────────────────────────
def _demo_label(api: Api) -> str:
    if api.demo is None:
        return "정보 없음"
    return "지원(모의+실전)" if api.demo else "실전 전용(모의 미지원)"


def _api_oneline(api: Api) -> str:
    tr = api.tr_code or "-"
    return (f"{api.slug}  [{api.group_name}]  {api.api_name}  "
            f"(TR:{tr}, {api.protocol}, {api.method or '-'}, TPS:{api.tps or '-'})")


def _render_in(api: Api) -> list[str]:
    if not api.in_params:
        return ["  (요청 파라미터 없음 또는 본문 참조)"]
    lines = []
    for p in api.in_params:
        meta = p["type"] or ""
        ex = f"예:{p['example']}" if p.get("example") not in ("", None) else ""
        head = f"  {p['key']}  ({meta})" if meta else f"  {p['key']}"
        tail = f"  {p['name']}".rstrip()
        if ex:
            tail += f"  [{ex}]"
        line = f"{head}{tail}".rstrip()
        if p.get("desc"):
            line += f" — {p['desc']}"
        lines.append(line)
    return lines


def _multi_variant(api: Api) -> Api | None:
    """단건 API 에 대응하는 멀티 조회 API(<slug>_multi)가 카탈로그에 있으면 반환한다.

    예: kr_stock_inquire_price → kr_stock_inquire_price_multi (국내/해외주식·국내선물옵션 멀티현재가).
    카탈로그 존재 여부로 판별하므로 멀티 API 가 추가되어도 자동 반영된다.
    """
    return CAT.apis.get(api.slug + "_multi")


def _multi_hint(api: Api) -> str | None:
    """단건 API 조회 시 멀티 우선 사용을 안내하는 한 줄 (없으면 None)."""
    m = _multi_variant(api)
    if m is None:
        return None
    return (f"※ 현재가 등 시세 조회는 멀티 조회 API '{m.slug}' (TR:{m.tr_code or '-'}) 를 "
            f"기본으로 사용하세요 — 1회 최대 50종목, 1종목만 조회할 때도 dataCnt=1 로 호출 가능합니다.")


def _resolve_or_msg(identifier: str):
    apis = CAT.resolve(identifier)
    if not apis:
        return None, (f"'{identifier}' 에 해당하는 API 를 찾지 못했습니다. "
                      f"search_apis 로 먼저 검색하거나 정확한 slug/TR코드를 사용하세요.")
    if len(apis) > 1:
        opts = "\n".join("  - " + _api_oneline(a) for a in apis)
        return None, (f"'{identifier}' 가 여러 API 에 매칭됩니다. 아래 중 slug 로 다시 지정하세요:\n{opts}")
    return apis[0], None


# ── 툴 ───────────────────────────────────────────────────
@mcp.tool()
def list_api_groups() -> str:
    """DB증권 Open API 그룹(도메인) 목록을 반환한다.

    각 그룹의 slug, 한글명, API 개수, 모의투자 지원 API 수를 보여준다.
    특정 그룹의 API 를 보려면 search_apis(query="", group="<slug>") 를 사용.
    """
    groups = CAT.groups()
    total = sum(g["count"] for g in groups)
    lines = [f"DB증권 Open API — {len(groups)}개 그룹 / 총 {total}개 API", ""]
    lines.append(f"{'group_slug':<22}{'한글명':<24}{'API수':>5}  {'모의투자':>6}")
    lines.append("-" * 64)
    for g in groups:
        lines.append(f"{g['group_slug']:<22}{g['group_name']:<24}{g['count']:>5}  {g['demo_supported']:>6}")
    return "\n".join(lines)


@mcp.tool()
def search_apis(query: str = "", group: str = "") -> str:
    """API 를 키워드/TR코드/그룹으로 검색한다.

    Args:
        query: 검색어 (API명·TR코드·slug·경로 부분일치, 한글 가능). 빈 문자열이면 전체.
        group: group_slug 로 범위 제한 (예: kr_stock_quote). 비우면 전체 그룹.
    """
    res = CAT.search(query, group or None)
    if not res:
        return f"검색 결과 없음 (query={query!r}, group={group!r}). list_api_groups 로 그룹을 확인하세요."
    head = f"검색 결과 {len(res)}건 (query={query!r}" + (f", group={group!r}" if group else "") + ")"
    lines = [head, ""]
    lines += [_api_oneline(a) for a in res[:200]]
    if len(res) > 200:
        lines.append(f"... 외 {len(res) - 200}건 (query 를 좁혀주세요)")
    # 단건 시세 API 가 결과에 있으면 멀티 조회 우선 사용을 안내 (한 줄로 압축)
    multis = []
    for a in res[:200]:
        m = _multi_variant(a)
        if m and m.slug not in multis:
            multis.append(m.slug)
    if multis:
        lines.append("")
        lines.append("※ 현재가 등 시세 조회는 멀티 조회 API 를 기본으로 사용하세요 "
                     f"(1회 최대 50종목, 1종목도 dataCnt=1 가능): {', '.join(multis)}")
    return "\n".join(lines)


@mcp.tool()
def get_api_spec(identifier: str) -> str:
    """API 한 건의 명세를 반환한다 — 엔드포인트·요청(In)·응답(Out) 파라미터.

    명세는 해당 예제 파일(examples/<group>/<slug>.py)에서 파싱한 것이다.
    전체 실행 코드는 get_sample_code 로 조회.

    Args:
        identifier: 메서드 slug(예: kr_stock_inquire_price) 또는 TR코드(예: PRICE).
    """
    api, msg = _resolve_or_msg(identifier)
    if msg:
        return msg

    if api.protocol == "REST":
        # 전체 요청 URL = base_url(포트 :8443 포함) + path. 반드시 포트까지 노출한다.
        endpoint = f"{api.method} {CAT.full_url(api)}".strip()
    else:
        endpoint = "WebSocket (실시간)"
    out = [
        f"[{api.group_name}] {api.api_name}",
        f"slug      : {api.slug}",
        f"group     : {api.group_slug}",
        f"TR코드    : {api.tr_code or '-'}",
        f"프로토콜  : {api.protocol}",
        f"엔드포인트: {endpoint}",
        f"TPS       : {api.tps or '-'}   모의투자: {_demo_label(api)}",
    ]
    if api.protocol == "REST":
        out.append(f"※ 요청 URL 은 위 전체 주소(도메인·포트 {CAT.base_url} 포함)를 그대로 사용하세요.")
    hint = _multi_hint(api)
    if hint:
        out.append(hint)
    out += [
        "",
        "■ 요청(In) 파라미터",
    ]
    out += _render_in(api)
    out.append("")
    out.append("■ 응답(Out) 파라미터")
    out.append(api.out_text or "  (응답 명세 없음 — rsp_cd/rsp_msg 만 반환)")
    out.append("")
    out.append(f"■ 샘플코드: examples/{api.group_slug}/{api.slug}.py "
               f"→ get_sample_code({api.slug!r}) 로 원문 조회")
    return "\n".join(out)


@mcp.tool()
def get_sample_code(identifier: str) -> str:
    """API 의 실행 가능한 파이썬 샘플코드 원문을 반환한다.

    Args:
        identifier: 메서드 slug(예: kr_stock_inquire_price) 또는 TR코드(예: PRICE).
    """
    api, msg = _resolve_or_msg(identifier)
    if msg:
        return msg
    code = CAT.sample_code(api)
    if code is None:
        return f"샘플코드 파일이 없습니다: examples/{api.group_slug}/{api.slug}.py"
    rel = f"examples/{api.group_slug}/{api.slug}.py"
    # examples/ 밖에서 실행할 때를 위한 안내를 헤더 주석으로만 덧붙인다(코드 본문은 원문 그대로).
    hint = _multi_hint(api)
    hint_block = f"#\n# {hint}\n#   → get_sample_code({_multi_variant(api).slug!r}) 로 멀티 샘플 조회\n" if hint else ""
    header = (
        f"# 파일: {rel}\n"
        f"# (standalone — examples/dbsec_helper.py 헬퍼만 사용)\n"
        f"{hint_block}"
        f"#\n"
        f"# ※ 이 스크립트는 examples/<group>/ 안에서 실행하도록 설계됨(아래 sys.path 가 상대경로).\n"
        f"#   examples/ 밖(내 프로젝트 폴더 등)에서 실행하려면 sys.path 줄을 절대경로로 바꾸세요:\n"
        f'#       sys.path.insert(0, r"{CAT.examples_dir}")\n'
        f"#   config.yaml 이 저장소 루트가 아니면 환경변수로 위치 지정: set DBSEC_CONFIG=<경로>\\config.yaml\n"
    )
    return f"{header}\n{code}"


@mcp.tool()
def get_setup_guide() -> str:
    """처음 사용자를 위한 설정/실행 가이드(설치·config.yaml·토큰 발급·실행)를 반환한다."""
    return (
        "DB증권 Open API 샘플코드 — 시작 가이드\n"
        "\n"
        "1) 의존성 설치\n"
        "   pip install -r requirements.txt\n"
        "\n"
        "2) 설정 파일 작성\n"
        "   cp config.yaml.example config.yaml\n"
        "   → auth.vtl_app_key / vtl_app_secret (모의투자) 또는\n"
        "     auth.prd_app_key / prd_app_secret (실전) 입력\n"
        "   → environment.mode 를 'demo'(모의) 또는 'production'(실전) 으로 설정\n"
        "   (앱키는 openapi.dbsec.co.kr 에서 API 서비스 신청 후 발급)\n"
        "\n"
        "3) 접근토큰 발급 (24시간 유효, 루트 .dbsec_token.json 에 캐시)\n"
        "   python examples/auth/token_issue.py\n"
        "\n"
        "4) 예제 실행 (모두 standalone)\n"
        "   python examples/kr_stock_quote/kr_stock_inquire_price.py\n"
        "\n"
        "주의\n"
        "  · 주문/정정/취소 API 는 실제 매매가 실행됩니다 — 반드시 모의투자(mode='demo')로 먼저 테스트.\n"
        "  · 해외선물옵션(ov_futopt_*) 그룹은 모의투자를 지원하지 않습니다(실전 전용).\n"
        "  · API 별 In/Out 파라미터는 get_api_spec, 샘플코드는 get_sample_code 로 조회하세요.\n"
    )


# ── 프롬프트 ─────────────────────────────────────────────
# 툴은 모델이 판단해 호출하지만, 프롬프트는 사용자가 클라이언트(Claude Desktop 등)
# 메뉴에서 직접 선택하는 워크플로 템플릿이다 — 검색→명세→샘플→수정 절차를 보장한다.

@mcp.prompt(name="dbsec_easy_code")
def dbsec_easy_code(request: str) -> str:
    """자연어 요청만으로 DB증권 Open API 호출 코드를 생성한다.

    Args:
        request: 만들고 싶은 것 (예: "삼성전자 현재가 조회", "테슬라 호가 보여줘")
    """
    return f"""사용자 요청: {request}

너는 DB증권 Open API 코드 어시스턴트다. dbsec-code-assistant MCP 도구를 사용해
아래 절차를 **반드시 순서대로** 수행하라. 명세를 추측하거나 기억으로 코드를 지어내지 말 것.

1. 탐색 — search_apis(query=...) 로 요청에 맞는 API 를 찾는다 (한글 키워드 가능).
   · 후보가 여러 개면 가장 적합한 1개를 고르고, 판단이 어려우면 후보 목록을 보여주고 사용자에게 확인.
   · 그룹 감이 안 오면 list_api_groups() 로 도메인부터 파악.
2. 명세 확인 — get_api_spec(slug) 로 전체 요청 URL·요청(In)/응답(Out) 파라미터·TPS·모의투자 지원을 확인한다.
3. 샘플 확보 — get_sample_code(slug) 로 examples/ 원문을 가져온다.
4. 코드 작성 — 샘플 구조(dbsec_helper.call_rest / ws_subscribe)를 유지한 채 요청 값만 바꿔
   완성 코드를 제시한다. In 파라미터의 의미·허용값 주석은 보존한다.
   · 앱/봇 임베드 목적이면 비동기 SDK 패턴(await client.apis.<그룹>.<메서드>(...), dbsec_sdk)도 함께 제시.
5. 안내 — 다음을 반드시 함께 알려라:
   · 주문(order/modify/cancel) 계열이면 ⚠ 실제 매매가 실행됨 — 모의투자(mode='demo') 선행 테스트 필수.
   · 해당 API 의 TPS(유량제어)와 모의투자 지원 여부 (2단계에서 확인한 값).
   · 처음 사용자라면 get_setup_guide() 의 설정/토큰 발급 절차.
"""


@mcp.prompt(name="dbsec_detailed_code")
def dbsec_detailed_code(api_identifier: str, task: str) -> str:
    """대상 API(slug 또는 TR코드)를 지정해 정밀한 호출 코드를 생성한다.

    Args:
        api_identifier: 메서드 slug(예: kr_stock_inquire_price) 또는 TR코드(예: PRICE)
        task: 수행할 작업 (예: "삼성전자(005930) 현재가를 조회해 등락률만 출력")
    """
    return f"""대상 API: {api_identifier}
작업: {task}

너는 DB증권 Open API 코드 어시스턴트다. dbsec-code-assistant MCP 도구로 아래 절차를 수행하라.

1. get_api_spec({api_identifier!r}) 로 명세를 확인한다 — 전체 요청 URL, 요청(In) 파라미터의
   타입·허용값, 응답(Out) 필드, TPS, 모의투자 지원.
   · TR코드가 여러 API 에 매칭되면 반환된 후보 중 작업에 맞는 slug 로 다시 조회.
2. get_sample_code(slug) 로 examples/ 원문을 가져온다.
3. 샘플 구조를 유지한 채 작업에 맞게 수정한 **실행 가능한 완성 코드**를 제시한다.
   · In 파라미터는 명세의 허용값만 사용하고, 응답 가공은 Out 필드명을 그대로 사용.
   · 작업이 응답 후처리를 요구하면(필터링·출력 형식 등) call_rest(verbose=False) 후 직접 처리.
4. 주문 계열이면 ⚠ 실제 매매 실행 경고 + 모의투자 선행 테스트를 안내하고,
   TPS·모의투자 지원 여부를 함께 알려라.
"""


@mcp.resource("dbsec://catalog")
def catalog_resource() -> str:
    """전체 API 인덱스(JSON) — group/slug/tr_code/method/path/tps/demo 요약."""
    data = {
        "base_url": CAT.base_url,   # REST 요청 도메인(포트 :8443 포함)
        "groups": CAT.groups(),
        "apis": [
            {
                "slug": a.slug, "group_slug": a.group_slug, "group_name": a.group_name,
                "api_name": a.api_name, "tr_code": a.tr_code, "protocol": a.protocol,
                "method": a.method, "path": a.path,
                "url": CAT.full_url(a),   # 전체 요청 URL (base_url + path)
                "tps": a.tps, "demo": a.demo,
            }
            for a in sorted(CAT.apis.values(), key=lambda x: (x.group_slug, x.slug))
        ],
    }
    return json.dumps(data, ensure_ascii=False, indent=2)
