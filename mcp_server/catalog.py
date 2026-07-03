"""카탈로그 — `examples/`(샘플코드=원본) + `api_support_matrix.md`(모의투자/TPS) 조인.

명세의 **단일 원본은 examples/<group>/<slug>.py** 다.
각 예제의 모듈 docstring 에는 엔드포인트·TPS·가이드 링크와 응답(Out) 파라미터 섹션
(`OUT_BEGIN`~`OUT_END`)이 있고, 본문 코드에는 요청(In) 파라미터가 인라인 주석으로 들어있다.
이 파일들을 파싱해 메모리 인덱스를 만든다 (별도 명세 캐시에 의존하지 않음).

api_support_matrix.md 는 모의투자 지원 여부·TPS·TR코드를 보강하는 보조 소스다.
모든 텍스트 파일은 UTF-8 로 읽는다.
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path

# group_slug → 한글 그룹명 (고정 매핑)
GROUP_NAMES = {
    "auth": "OAuth 인증",
    "common": "공통",
    "kr_stock_order": "국내주식주문",
    "kr_stock_quote": "국내주식시세",
    "kr_stock_realtime": "국내주식시세(실시간)",
    "kr_futopt_order": "국내선물옵션주문",
    "kr_futopt_quote": "국내선물옵션시세",
    "kr_futopt_realtime": "국내선물옵션시세(실시간)",
    "kr_chart": "국내주식/선물차트",
    "ov_stock_order": "해외주식주문",
    "ov_stock_quote": "해외주식시세",
    "ov_stock_realtime": "해외주식시세(실시간)",
    "ov_futopt_order": "해외선물옵션주문",
    "ov_futopt_quote": "해외선물옵션시세",
    "ov_futopt_realtime": "해외선물옵션시세(실시간)",
    "bond_order": "장내채권주문",
    "bond_quote": "장내채권시세",
    "bond_realtime": "장내채권시세(실시간)",
    "ws_common": "웹소켓(공통)",
}

# ── docstring/코드 파싱 정규식 ────────────────────────────
_RE_API_ID = re.compile(r"api_id=([0-9a-fA-F-]+)")
_RE_ENDPOINT = re.compile(r"엔드포인트\s*:\s*([A-Z]+)\s+(\S+)")
_RE_TPS = re.compile(r"TPS\s*:\s*(\d+)")
_RE_TITLE = re.compile(r"^\s*(.+?)\s*[\(\[]([A-Za-z0-9_]+)[\)\]]\s*[—-]")  # 이름 (TRCODE) — / 이름 [TRCODE] —
# 본문 In 주석:  "key": value,  # 이름 (타입) - 설명   /   key=value,  # 이름 (타입) - 설명
_RE_IN_KV = re.compile(r'^\s*"(\w+)"\s*:\s*(.+?),\s*#\s*(.+?)\s*$')
_RE_IN_KW = re.compile(r'^\s*(\w+)\s*=\s*(.+?),\s*#\s*(.+?)\s*$')
_RE_IN_COMMENT = re.compile(r"^(.*?)\s*\(([^)]*)\)\s*-?\s*(.*)$")

OUT_BEGIN = "OUT_BEGIN"
OUT_END = "OUT_END"


@dataclass
class Api:
    slug: str
    group_slug: str
    file: Path
    api_name: str = ""
    tr_code: str = ""
    method: str = ""
    path: str = ""
    protocol: str = "REST"
    tps: str | None = None
    api_id: str = ""
    in_params: list[dict] = field(default_factory=list)   # {key, example, name, type, desc}
    out_text: str = ""                                     # docstring 의 Out 섹션 원문(마커 제외)
    demo: bool | None = None                               # matrix 보강

    @property
    def group_name(self) -> str:
        return GROUP_NAMES.get(self.group_slug, self.group_slug)

    @property
    def tr_codes(self) -> list[str]:
        return [self.tr_code] if self.tr_code else []


def _split_docstring(text: str) -> tuple[str, str]:
    """첫 모듈 docstring 과 그 이후 본문을 분리. docstring 없으면 ('', text)."""
    o = text.find('"""')
    if o == -1:
        return "", text
    c = text.find('"""', o + 3)
    if c == -1:
        return "", text
    return text[o + 3:c], text[c + 3:]


def _parse_in_comment(comment: str) -> tuple[str, str, str]:
    """'이름 (타입) - 설명' → (name, type, desc). 형식 안 맞으면 (comment, '', '')."""
    m = _RE_IN_COMMENT.match(comment)
    if m:
        return m.group(1).strip(), m.group(2).strip(), m.group(3).strip()
    return comment.strip(), "", ""


def _parse_example(path: Path) -> Api:
    text = path.read_text(encoding="utf-8")
    doc, body = _split_docstring(text)
    api = Api(slug=path.stem, group_slug=path.parent.name, file=path)

    # ── docstring 헤더 ──
    mt = _RE_TITLE.search(doc)
    if mt:
        api.api_name = mt.group(1).strip()
        api.tr_code = mt.group(2).strip()
    else:
        first = next((ln.strip() for ln in doc.splitlines() if ln.strip()), "")
        api.api_name = re.split(r"\s*[—-]\s*standalone", first)[0].strip() or path.stem
    me = _RE_ENDPOINT.search(doc)
    if me:
        api.method, api.path = me.group(1), me.group(2)
    mtps = _RE_TPS.search(doc)
    if mtps:
        api.tps = mtps.group(1)
    mid = _RE_API_ID.search(doc)
    if mid:
        api.api_id = mid.group(1)
    api.protocol = "WEBSOCKET" if "ws_subscribe" in body else "REST"

    # ── Out 섹션 (docstring 내 OUT_BEGIN ~ OUT_END) ──
    b = doc.find(OUT_BEGIN)
    if b != -1:
        e = doc.find(OUT_END, b)
        if e != -1:
            inner = doc[b + len(OUT_BEGIN):e]
            # 마커 잔여 대시(─) 줄·빈 줄 제거
            api.out_text = "\n".join(
                ln.rstrip() for ln in inner.splitlines()
                if ln.strip() and set(ln.strip()) != {"─"}
            ).strip()

    # ── In 파라미터 (본문 코드 인라인 주석) ──
    for raw in body.splitlines():
        m = _RE_IN_KV.match(raw) or _RE_IN_KW.match(raw)
        if not m:
            continue
        key, val, comment = m.group(1), m.group(2).strip(), m.group(3)
        if key in ("url", "label", "group_slug", "on_message", "method"):
            continue
        name, typ, desc = _parse_in_comment(comment)
        api.in_params.append({
            "key": key, "example": val.strip('"'),
            "name": name, "type": typ, "desc": desc,
        })
    return api


# config.yaml(.example) 의 environment.base_url — REST 호출 도메인(포트 포함).
# 누락 시 사용할 표준 기본값(반드시 포트 :8443 포함).
DEFAULT_BASE_URL = "https://openapi.dbsec.co.kr:8443"
_RE_BASE_URL = re.compile(r'^\s*base_url\s*:\s*["\']?([^"\'\s#]+)')


@dataclass
class Catalog:
    root: Path
    base_url: str = DEFAULT_BASE_URL                              # REST 도메인(포트 포함)
    apis: dict[str, Api] = field(default_factory=dict)             # slug → Api
    _by_trcode: dict[str, list[str]] = field(default_factory=dict)  # TRCODE(upper) → [slug]

    @property
    def examples_dir(self) -> Path:
        return self.root / "examples"

    def full_url(self, api: "Api") -> str:
        """REST API 의 전체 요청 URL (base_url + path, 포트 포함). 그 외 빈 문자열."""
        if api.protocol == "REST" and api.path:
            return f"{self.base_url}{api.path}"
        return ""

    def groups(self) -> list[dict]:
        out: dict[str, dict] = {}
        for api in self.apis.values():
            g = out.setdefault(api.group_slug, {
                "group_slug": api.group_slug, "group_name": api.group_name,
                "count": 0, "demo_supported": 0,
            })
            g["count"] += 1
            if api.demo:
                g["demo_supported"] += 1
        return sorted(out.values(), key=lambda x: x["group_slug"])

    def resolve(self, identifier: str) -> list[Api]:
        if identifier in self.apis:
            return [self.apis[identifier]]
        return [self.apis[s] for s in self._by_trcode.get(identifier.upper(), [])]

    def search(self, query: str, group: str | None = None) -> list[Api]:
        q = (query or "").strip().lower()
        res = []
        for api in self.apis.values():
            if group and api.group_slug != group:
                continue
            hay = " ".join([api.slug, api.group_slug, api.group_name, api.api_name,
                            api.path, api.tr_code]).lower()
            if not q or q in hay:
                res.append(api)
        return sorted(res, key=lambda a: (a.group_slug, a.slug))

    def sample_code(self, api: Api) -> str | None:
        return api.file.read_text(encoding="utf-8") if api.file.exists() else None


# ── api_support_matrix.md 보강 ───────────────────────────
_RE_MATRIX_ROW = re.compile(r"^\|(.+)\|\s*$")


def _parse_matrix(path: Path) -> dict[str, dict]:
    """{method_slug: {name, tr_code, demo, tps}}. 컬럼: 구분|API명|TR코드|메서드|모의투자|TPS"""
    if not path.exists():
        return {}
    out = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        m = _RE_MATRIX_ROW.match(line.strip())
        if not m:
            continue
        cols = [c.strip().strip("`") for c in m.group(1).split("|")]
        if len(cols) < 6 or cols[0] in ("구분", "") or set(cols[0]) <= {"-", ":"}:
            continue
        _, name, tr_code, slug, demo, tps = cols[:6]
        if slug:
            out[slug] = {"name": name, "tr_code": tr_code,
                         "demo": "⭕" in demo, "tps": tps if tps and tps != "-" else None}
    return out


def _read_base_url(root: Path) -> str:
    """config.yaml(있으면) 또는 config.yaml.example 에서 environment.base_url 을 읽는다.

    포트(:8443)가 포함된 전체 값을 그대로 반환. 어느 파일에도 없으면 DEFAULT_BASE_URL.
    """
    for name in ("config.yaml", "config.yaml.example"):
        p = root / name
        if not p.exists():
            continue
        for line in p.read_text(encoding="utf-8").splitlines():
            m = _RE_BASE_URL.match(line)
            if m:
                return m.group(1).strip().rstrip("/")
    return DEFAULT_BASE_URL


def load(root: str | Path) -> Catalog:
    root = Path(root).resolve()
    cat = Catalog(root=root)
    cat.base_url = _read_base_url(root)
    if not cat.examples_dir.exists():
        raise FileNotFoundError(f"examples 디렉토리 없음: {cat.examples_dir}")
    matrix = _parse_matrix(root / "docs" / "api_support_matrix.md")

    for path in sorted(cat.examples_dir.rglob("*.py")):
        if path.name == "dbsec_helper.py":
            continue
        api = _parse_example(path)
        mrow = matrix.get(api.slug, {})
        if mrow:
            api.demo = mrow.get("demo")
            if not api.tr_code:
                api.tr_code = mrow.get("tr_code", "") or ""
            if not api.tps:
                api.tps = mrow.get("tps")
            if mrow.get("name"):
                api.api_name = mrow["name"]
        cat.apis[api.slug] = api
        if api.tr_code:
            cat._by_trcode.setdefault(api.tr_code.upper(), []).append(api.slug)
    return cat
