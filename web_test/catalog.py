"""DB증권 OpenAPI 전체 카탈로그 생성.

examples 의 call_rest / ws_subscribe 호출을 모킹해 import 하면서 각 예제가 의도하는
요청(url + 전체 body, 또는 WebSocket tr_cd/tr_key/tr_type)을 수집한다. 라이브 호출 없음.
url → (group, method) 는 각 endpoints.py 의 PATHS 로 역매핑한다.

결과 항목:
  {id, group, method, label, http, url, body, kind('rest'|'order'|'ws'),
   is_ov_futopt, example, tr_cd, tr_key, tr_type, group_slug}
"""
from __future__ import annotations
import sys, io, contextlib, pathlib, importlib, ast, re

REPO = pathlib.Path(__file__).resolve().parents[1]
EXAMPLES = REPO / "examples"
for p in (str(REPO), str(EXAMPLES)):
    if p not in sys.path:
        sys.path.insert(0, p)

# 주문(실거래) 메서드/예제 — kind='order' 로 분류해 UI 에서 기본 비활성.
ORDER_STEMS = {
    "kr_stock_order", "kr_stock_order_cancel", "kr_stock_order_cancel_nxt",
    "kr_stock_order_modify", "kr_stock_order_modify_nxt", "kr_stock_order_nxt",
    "bond_order", "bond_order_cancel", "bond_order_modify",
    "kr_futopt_order", "kr_futopt_order_cancel", "kr_futopt_order_cancel_night",
    "kr_futopt_order_modify", "kr_futopt_order_modify_night", "kr_futopt_order_night",
    "ov_futopt_order", "ov_futopt_order_cancel",
    "ov_stock_order",
}
OV_FUTOPT_GROUPS = {"ov_futopt_order", "ov_futopt_quote", "ov_futopt_realtime"}

# OAuth — examples/auth/* 는 call_rest 가 아니라 헬퍼 get_token/revoke_token 을 직접 쓰므로
# 캡처되지 않는다. 토큰 발급/폐기를 카탈로그에 직접 추가한다(form-urlencoded 전용).
_OAUTH = [
    {"id": "auth.token_issue", "group": "auth", "method": "token_issue", "label": "접근토큰 발급",
     "group_label": "인증",
     "http": "POST", "url": "/oauth2/token", "kind": "rest", "oauth": "issue",
     "is_ov_futopt": False, "paged": False, "example": "examples/auth/token_issue.py",
     "body": {"grant_type": "client_credentials", "appkey": "<APP_KEY>",
              "appsecretkey": "<APP_SECRET>", "scope": "oob"}},
    {"id": "auth.token_revoke", "group": "auth", "method": "token_revoke", "label": "접근토큰 폐기",
     "group_label": "인증",
     "http": "POST", "url": "/oauth2/revoke", "kind": "rest", "oauth": "revoke",
     "is_ov_futopt": False, "paged": False, "example": "examples/auth/token_revoke.py",
     "body": {"appkey": "<APP_KEY>", "appsecretkey": "<APP_SECRET>",
              "token_type_hint": "access_token", "token": "<ACCESS_TOKEN>"}},
]

_current = {"calls": []}


def _rest(*a, **kw):
    if a and "url" not in kw:
        kw = dict(kw); kw["url"] = a[0]
        if len(a) > 1 and "body" not in kw:
            kw["body"] = a[1]
    _current["calls"].append(("rest", kw)); return (None, {})


def _paged(*a, **kw):
    if a and "url" not in kw:
        kw = dict(kw); kw["url"] = a[0]
        if len(a) > 1 and "body" not in kw:
            kw["body"] = a[1]
    _current["calls"].append(("rest_paged", kw)); return []


def _ws_sub(*a, **kw):
    names = ["tr_cd", "tr_key", "group_slug", "tr_type", "on_message"]
    for i, x in enumerate(a):
        if i < len(names) and names[i] not in kw:
            kw[names[i]] = x
    return ("WS", kw)


def _run_ws(coro):
    if isinstance(coro, tuple) and coro and coro[0] == "WS":
        _current["calls"].append(("ws", coro[1]))


_ORIG = {}
_MOCK_NAMES = ["call_rest", "call_rest_paged", "ws_subscribe", "run_ws",
               "get_token", "revoke_token", "issue_token", "print_response", "print_summary"]

def _install_mocks():
    import dbsec_helper as H
    for n in _MOCK_NAMES:                       # 원본 보존 (캡처 후 복원하기 위해)
        _ORIG.setdefault(n, getattr(H, n, None))
    H.call_rest = _rest
    H.call_rest_paged = _paged
    H.ws_subscribe = _ws_sub
    H.run_ws = _run_ws
    H.get_token = lambda *a, **k: "MOCK_TOKEN"
    H.revoke_token = lambda *a, **k: (None, {})
    H.issue_token = lambda *a, **k: (None, {})
    H.print_response = lambda *a, **k: None
    H.print_summary = lambda *a, **k: None


def _restore_mocks():
    # 캡처 후 dbsec_helper 원본 함수 복원 — 서버의 예제 경로(ws_subscribe 등)가 정상 동작하도록.
    import dbsec_helper as H
    for n, fn in _ORIG.items():
        if fn is not None:
            setattr(H, n, fn)


def _url_method_map() -> dict:
    m = {}
    for d in sorted((REPO / "dbsec_sdk" / "apis").glob("*/endpoints.py")):
        grp = d.parent.name
        try:
            mod = importlib.import_module(f"dbsec_sdk.apis.{grp}.endpoints")
        except Exception:
            continue
        for name in dir(mod):
            paths = getattr(getattr(mod, name), "PATHS", None)
            if isinstance(paths, dict):
                for method, url in paths.items():
                    m[url] = (grp, method)
    return m


def _doc_title(src: str) -> str | None:
    """예제 모듈 docstring 첫 줄에서 표시용 한글 API 명을 추출한다.

    형식: '[실시간]<한글명> [<TR코드>] — standalone WebSocket 예제.' (WS)
          '<한글명> [<식별자>] — standalone REST 예제.'              (REST)
    → ' — …' 뒤(안내문)와 끝의 '[TR코드]', 앞의 중복 '[실시간]' 태그를 떼어낸 한글명만 반환.
    """
    try:
        doc = ast.get_docstring(ast.parse(src))
    except Exception:
        return None
    if not doc:
        return None
    first = doc.strip().splitlines()[0].strip()
    head = re.split(r"\s+[—–-]\s+", first, maxsplit=1)[0].strip()   # ' — standalone …' 제거
    head = re.sub(r"\s*\[[^\[\]]+\]\s*$", "", head).strip()         # 끝의 [TR코드] 제거
    if head.startswith("[실시간]"):                                  # ws 배지로 충분하므로 중복 태그 제거
        head = head[len("[실시간]"):].strip()
    return head or None


def _doc_group(src: str) -> str | None:
    """예제 docstring 의 '그룹: <한글>' 줄에서 서비스 그룹 한글명을 추출한다."""
    try:
        doc = ast.get_docstring(ast.parse(src))
    except Exception:
        return None
    if not doc:
        return None
    for line in doc.splitlines():
        m = re.match(r"\s*그룹\s*[:：]\s*(.+?)\s*$", line)
        if m:
            return m.group(1).strip()
    return None


# OUT 섹션 필드 줄: "key  (타입)  이름[ — 설명]"
_RE_OUT_FIELD = re.compile(r"^(\s*)(\S+)\s+\(([^)]+)\)\s+(.*)$")
_RE_OUT_TR = re.compile(r"^\s*\[TR\s+([^\]]+)\]")
# Out 타입 한글 → In 패널과 동일한 영문 표기 (숫자는 소수 필드가 있어 num 으로)
_OUT_TYPE_MAP = {"문자": "str", "숫자": "num", "오브젝트": "object", "배열": "array"}


def _dedash(s: str) -> str:
    """UI 로 나가는 문자열의 em/en dash 를 hyphen 으로 정규화."""
    return s.replace(" — ", " - ").replace("—", "-").replace("–", "-") if s else s


def _parse_out_blocks(text: str) -> tuple[list[dict], str]:
    """OUT 섹션 텍스트를 구조화 — In 패널과 동일한 행 렌더링용.

    반환: ([{tr, block, type, desc, fields:[{key,type,name,desc}]}], 공통 각주)
    블록 헤더(Out/Out1… + 오브젝트/배열)가 없는 실시간 TR 은 무명 블록에 담긴다.
    """
    blocks: list[dict] = []
    common, cur_tr, cur = "", "", None

    def new_block(name: str = "", typ: str = "", desc: str = "") -> dict:
        b = {"tr": cur_tr, "block": name, "type": typ, "desc": desc, "fields": []}
        blocks.append(b)
        return b

    for line in (text or "").splitlines():
        if not line.strip():
            continue
        m = _RE_OUT_TR.match(line)
        if m:
            cur_tr, cur = m.group(1).strip(), None
            continue
        if line.strip().startswith("공통:"):
            common = _dedash(line.strip())
            continue
        m = _RE_OUT_FIELD.match(line)
        if not m:
            continue
        key, typ, rest = m.group(2), m.group(3), m.group(4).strip()
        if re.fullmatch(r"Out\d*", key) and typ in ("오브젝트", "배열"):
            desc = rest.split("—", 1)[1].strip() if "—" in rest else ""
            cur = new_block(key, _OUT_TYPE_MAP.get(typ, typ), _dedash(desc))
            continue
        name, desc = rest, ""
        if "—" in rest:
            name, desc = (s.strip() for s in rest.split("—", 1))
        if cur is None:
            cur = new_block()
        cur["fields"].append({"key": key, "type": _OUT_TYPE_MAP.get(typ, typ),
                              "name": _dedash(name), "desc": _dedash(desc)})
    return blocks, common


def build_catalog() -> list[dict]:
    _install_mocks()
    url_map = _url_method_map()
    out = []
    files = sorted(p for p in EXAMPLES.rglob("*.py")
                   if p.name != "dbsec_helper.py" and "__pycache__" not in p.parts)
    for p in files:
        stem, group = p.stem, p.parent.name
        _current["calls"] = []
        src = p.read_text(encoding="utf-8")
        title = _doc_title(src)          # docstring 첫 줄의 한글명 (WS 는 label 인자가 없어 이걸 사용)
        group_ko = _doc_group(src)       # docstring '그룹:' 줄의 서비스 그룹 한글명
        g = {"__name__": "__main__", "__file__": str(p)}
        try:
            # 일부 예제는 모듈 레벨에서 결과 요약을 print 함 — mock 실행 중 출력은 흡수해
            # 서버 기동 로그를 오염시키지 않는다.
            with contextlib.redirect_stdout(io.StringIO()):
                exec(compile(src, str(p), "exec"), g)
        except SystemExit:
            pass
        except Exception:
            pass  # 사후처리 오류는 무시 (캡처는 mock 안에서 이미 완료)
        for kind, kw in _current["calls"]:
            rel = str(p.relative_to(REPO)).replace("\\", "/")
            is_ov = (group in OV_FUTOPT_GROUPS)
            if kind in ("rest", "rest_paged"):
                url = kw.get("url"); grp2, method = url_map.get(url, (group, None))
                ek = "order" if stem in ORDER_STEMS else "rest"
                out.append({
                    "id": f"{grp2}.{method or stem}" + ("#paged" if kind == "rest_paged" else ""),
                    "group": grp2, "method": method or stem,
                    "label": kw.get("label") or title or stem, "http": "POST", "url": url,
                    "group_label": group_ko or "",
                    "body": kw.get("body") or {}, "kind": ek,
                    "paged": kind == "rest_paged",
                    "is_ov_futopt": grp2 in OV_FUTOPT_GROUPS, "example": rel,
                })
            elif kind == "ws":
                out.append({
                    "id": f"{group}.{stem}", "group": group, "method": stem,
                    "label": title or stem, "http": "WS", "url": None, "body": None,
                    "group_label": group_ko or "",
                    "kind": "ws", "is_ov_futopt": is_ov, "example": rel,
                    "tr_cd": kw.get("tr_cd", ""), "tr_key": kw.get("tr_key", ""),
                    "tr_type": str(kw.get("tr_type", "1")),
                    "group_slug": kw.get("group_slug") or group,
                })
    _restore_mocks()    # 캡처 끝 — dbsec_helper 원본 함수 복원 (서버 예제 경로 정상화)
    out = [dict(o) for o in _OAUTH] + out   # OAuth(토큰 발급/폐기) 추가
    # 정렬: 도메인 묶음 순서(국내주식→해외주식→국내선옵→해외선옵→장내채권→공통),
    #        도메인 내에서는 주문→시세→실시간(→차트) / 같은 그룹 안은 kind, method 순
    _GROUP_ORDER = [
        "auth",                                                                # 인증 (최상단)
        "kr_stock_order", "kr_stock_quote", "kr_stock_realtime", "kr_chart",   # 국내주식
        "ov_stock_order", "ov_stock_quote", "ov_stock_realtime",               # 해외주식
        "kr_futopt_order", "kr_futopt_quote", "kr_futopt_realtime",            # 국내선물옵션
        "ov_futopt_order", "ov_futopt_quote", "ov_futopt_realtime",            # 해외선물옵션
        "bond_order", "bond_quote", "bond_realtime",                           # 장내채권
        "common", "ws_common",                                                 # 공통
    ]
    _rank = {g: i for i, g in enumerate(_GROUP_ORDER)}

    def _method_rank(e):
        # 주문 API 는 알파벳순 대신 업무 순서로: 종합/매수 → 매도 → 정정(modify) → 취소(cancel).
        # 기본 시장 먼저, 변형 시장(_nxt·_night)은 같은 순서로 그 뒤에. 그 외 kind 는 알파벳순 유지.
        if e["kind"] != "order":
            return (0, 0, e["method"])
        m = base = e["method"]
        variant = 0
        for suf in ("_nxt", "_night"):
            if base.endswith(suf):
                base, variant = base[:-len(suf)], 1
                break
        action = base.split("_order", 1)[1].lstrip("_") if "_order" in base else ""
        act = {"": 0, "buy": 0, "sell": 1, "modify": 2, "cancel": 3}.get(action, 99)
        return (variant, act, m)

    out.sort(key=lambda e: (_rank.get(e["group"], len(_GROUP_ORDER)), e["kind"], *_method_rank(e)))

    # ── In/Out 명세 보강 — MCP 카탈로그 파서 재사용 ──
    # 요청(In)은 예제 본문의 인라인 주석, 응답(Out)은 docstring OUT 섹션에서 추출된다.
    # (파서를 새로 만들지 않고 mcp_server.catalog 를 그대로 사용 — 명세 표현 단일화)
    try:
        from mcp_server import catalog as _mcp_catalog
        _apis = _mcp_catalog.load(REPO).apis
        _alias = {"bond_order_buy": "bond_order"}   # SDK 슬러그 ↔ example 파일명 예외
        for e in out:
            api = _apis.get(e["method"]) or _apis.get(_alias.get(e["method"], ""))
            if api:
                # In 타입 정규화 — API 스펙상 타입은 string/number 뿐.
                # 예제 주석의 (str)/(int)는 str/num 으로, 타입이 아닌 괄호 내용
                # (예: tr_type 의 "1=시세구독 …")은 뱃지 대신 설명으로 옮긴다.
                in_fields = []
                for f in api.in_params:
                    t = (f.get("type") or "").strip()
                    if t in ("str", "string"):
                        nt = "str"
                    elif t in ("int", "float", "number"):
                        nt = "num"
                    else:
                        nt = ""
                    d = f.get("desc") or ""
                    if not nt and t:                   # 타입이 아닌 주석 → 설명 앞에 병합
                        d = d.lstrip(":-·— ").strip()
                        d = f"{t} - {d}" if d else t
                    in_fields.append({**f, "type": nt,
                                      "name": _dedash(f.get("name") or ""),
                                      "desc": _dedash(d)})
                e["in_fields"] = in_fields            # [{key, example, name, type, desc}]
                e["out_text"] = _dedash(api.out_text)  # OUT_BEGIN~OUT_END 원문 (폴백용)
                e["out_blocks"], e["out_common"] = _parse_out_blocks(api.out_text)
                e["tr_code"] = api.tr_code or e.get("tr_cd") or ""
                e["demo"] = api.demo                  # 모의투자 지원 여부 (matrix, True/False/None)
    except Exception as ex:
        print(f"[catalog] In/Out 명세 보강 생략: {type(ex).__name__}: {ex}", file=sys.stderr)
    return out


if __name__ == "__main__":
    import io, json
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
    cat = build_catalog()
    (pathlib.Path(__file__).parent / "catalog.json").write_text(
        json.dumps(cat, ensure_ascii=False, indent=1), encoding="utf-8")
    from collections import Counter
    print("총:", len(cat), dict(Counter(e["kind"] for e in cat)),
          "| ov_futopt:", sum(e["is_ov_futopt"] for e in cat))
