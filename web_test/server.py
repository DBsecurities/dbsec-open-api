"""DB증권 OpenAPI 웹 테스터 — 로컬 프록시 서버 (stdlib only).

브라우저는 CORS 로 DB API 를 직접 못 부르므로, 이 서버가 토큰을 주입해 대신 호출한다.
- GET  /            → index.html
- GET  /catalog     → 전체 API 목록 + 자격증명(키 마스킹)·base_url
- POST /token       → {kind:"prd"|"demo"|"ov_futopt"} 토큰 발급(폼 인코딩)
- POST /call        → {id, body?, allow_order?, key_kind?} REST 실행 → {status, json, curl, used_key}
- POST /ws          → {id} WebSocket 프로브: 연결·구독·~3초 수신·정상 종료 → {messages, graceful}

실행:  python web_test/server.py   (기본 http://127.0.0.1:8765)
토큰/키는 config.yaml 에서 읽는다(서버에만 존재, 페이지로 평문 전송 안 함).
"""
from __future__ import annotations
import io, os, sys, json, time, threading, asyncio, pathlib, subprocess
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse, parse_qs

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parent
for p in (str(REPO), str(REPO / "examples")):
    if p not in sys.path:
        sys.path.insert(0, p)


def _git_sync() -> None:
    """기동 시 저장소를 git pull --ff-only 로 동기화 (fail-soft).

    GitHub 에 추가된 API 가 재시작만으로 목록에 반영되도록 한다.
    ff-only 라 로컬 커밋/작업본은 절대 건드리지 않는다(분기·오프라인이면 그냥 건너뜀).
    DBSEC_WEBTEST_SKIP_SYNC=1 로 생략 가능.
    """
    if os.environ.get("DBSEC_WEBTEST_SKIP_SYNC", "").lower() in ("1", "true", "yes"):
        return
    try:
        p = subprocess.run(["git", "-C", str(REPO), "pull", "--ff-only"],
                           capture_output=True, text=True,
                           encoding="utf-8", errors="replace", timeout=30)
        last = ((p.stdout or "") + (p.stderr or "")).strip().splitlines()
        print(f"[web-tester] git 동기화: {last[-1] if last else 'ok'}", file=sys.stderr, flush=True)
    except Exception as ex:
        print(f"[web-tester] git 동기화 생략: {type(ex).__name__}: {ex}", file=sys.stderr, flush=True)


_git_sync()

import yaml, requests
from catalog import build_catalog

# keep-alive 연결 재사용 — 매 호출 TCP+TLS 핸드셰이크(~230ms) 제거.
# requests.Session 은 urllib3 커넥션 풀 기반이라 ThreadingHTTPServer 의 동시 요청에도 안전.
_HTTP = requests.Session()

CFG = yaml.safe_load((REPO / "config.yaml").read_text(encoding="utf-8"))
AUTH, ENV = CFG.get("auth", {}), CFG.get("environment", {})
BASE = ENV.get("base_url", "https://openapi.dbsec.co.kr:8443")
KEYS = {
    "prd":       (str(AUTH.get("prd_app_key", "")).strip(),       str(AUTH.get("prd_app_secret", "")).strip()),
    "demo":      (str(AUTH.get("vtl_app_key", "")).strip(),       str(AUTH.get("vtl_app_secret", "")).strip()),
    "ov_futopt": (str(AUTH.get("ov_futopt_prd_app_key", "")).strip(), str(AUTH.get("ov_futopt_prd_app_secret", "")).strip()),
}
KIND_NAME = {"prd": "일반", "demo": "모의투자", "ov_futopt": "해외선옵"}
# 모의투자 WebSocket 전용 포트 (REST 는 운영/모의 URL 동일 - 토큰이 환경을 결정)
WS_DEMO = ENV.get("ws_demo", "wss://openapi.dbsec.co.kr:17070/websocket")


def req_kind(e: dict, payload: dict) -> str:
    """사용할 토큰 슬롯 결정. ov_futopt 그룹은 고정(모의 미지원), 그 외는 페이지의 실행 환경 선택."""
    if e["is_ov_futopt"]:
        return "ov_futopt"
    return "demo" if payload.get("key_kind") == "demo" else "prd"
CATALOG = build_catalog()
BY_ID = {e["id"]: e for e in CATALOG}
_TOKENS: dict[str, str] = {}     # kind -> access_token (서버 메모리 캐시)
_LOCK = threading.Lock()


def mask(s: str) -> str:
    s = s or ""
    return (s[:5] + "…" + s[-3:]) if len(s) >= 10 else (s or "(미설정)")


def issue_token(kind: str) -> str:
    key, sec = KEYS.get(kind, ("", ""))
    if not key:
        raise RuntimeError(f"{kind} 앱키가 config.yaml 에 없습니다.")
    r = _HTTP.post(f"{BASE}/oauth2/token",
                   headers={"content-type": "application/x-www-form-urlencoded"},
                   data={"grant_type": "client_credentials", "appkey": key,
                         "appsecretkey": sec, "scope": "oob"}, timeout=15)
    if r.status_code != 200 or not r.json().get("access_token"):
        raise RuntimeError(f"토큰 발급 실패 {r.status_code}: {r.text[:160]}")
    tok = r.json()["access_token"]
    with _LOCK:
        _TOKENS[kind] = tok
    return tok


def ensure_token(kind: str) -> str:
    with _LOCK:
        t = _TOKENS.get(kind)
    return t or issue_token(kind)


def build_curl(url: str, body: dict, token_kind: str) -> str:
    return ("curl --request POST \\\n"
            f"     --url '{BASE}{url}' \\\n"
            "     --header 'content-type: application/json; charset=utf-8' \\\n"
            f"     --header 'authorization: Bearer <{token_kind.upper()}_TOKEN>' \\\n"
            f"     --data '{json.dumps(body, ensure_ascii=False)}'")


def _oauth_curl(url: str, data: str) -> str:
    return ("curl --request POST \\\n"
            f"     --url '{BASE}{url}' \\\n"
            "     --header 'content-type: application/x-www-form-urlencoded' \\\n"
            f"     --data '{data}'")


def do_oauth(e: dict, payload: dict) -> dict:
    """OAuth 토큰 발급/폐기 — /oauth2/* 는 form-urlencoded·무인증(발급) 이므로 전용 경로."""
    kind = payload.get("key_kind", "prd")
    key, sec = KEYS.get(kind, ("", ""))
    if not key:
        return {"error": f"{KIND_NAME.get(kind, kind)} 앱키가 config.yaml 에 없습니다."}
    op = e.get("oauth")
    if op == "issue":
        data = {"grant_type": "client_credentials", "appkey": key, "appsecretkey": sec, "scope": "oob"}
        curl = _oauth_curl(e["url"], "grant_type=client_credentials&appkey=<APP_KEY>&appsecretkey=<APP_SECRET>&scope=oob")
    else:  # revoke
        token = (payload.get("token") or "").strip()
        if not token:
            return {"error": f"폐기할 {KIND_NAME.get(kind, kind)} ACCESS TOKEN 을 입력하세요.", "need_token": kind}
        data = {"appkey": key, "appsecretkey": sec, "token_type_hint": "access_token", "token": token}
        curl = _oauth_curl(e["url"], "appkey=<APP_KEY>&appsecretkey=<APP_SECRET>&token_type_hint=access_token&token=<ACCESS_TOKEN>")
    r = _HTTP.post(f"{BASE}{e['url']}", headers={"content-type": "application/x-www-form-urlencoded"}, data=data, timeout=15)
    try: j = r.json()
    except Exception: j = {"raw": r.text[:1000]}
    rsp_cd = (j.get("rsp_cd") or j.get("code") or "") if isinstance(j, dict) else ""
    rsp_msg = (j.get("rsp_msg") or j.get("message") or j.get("msg") or "") if isinstance(j, dict) else ""
    out = {"status": r.status_code, "rsp_cd": str(rsp_cd), "rsp_msg": str(rsp_msg),
           "json": j, "used_key": kind, "mode": "oauth", "curl": curl}
    if op == "issue" and r.status_code == 200 and isinstance(j, dict) and j.get("access_token"):
        out["issued_token"] = j["access_token"]      # 클라가 입력칸 자동 채움
    if op == "revoke" and r.status_code == 200:
        out["revoked"] = True                          # 클라가 입력칸 비움
    return out


def do_call(payload: dict) -> dict:
    e = BY_ID.get(payload.get("id"))
    if not e:
        return {"error": "알 수 없는 id"}
    if e.get("oauth"):
        return do_oauth(e, payload)
    if e["kind"] == "order" and not payload.get("allow_order"):
        return {"error": "주문(실거래) API 는 기본 비활성입니다. 체크 후 실행하세요.",
                "blocked": True}
    if e["kind"] == "ws":
        return {"error": "WebSocket API 는 /ws 로 실행하세요.", "ws": True}
    kind = req_kind(e, payload)
    # 인증: 페이지에서 입력한 access token 을 그대로 Bearer 로 사용 (key/secret 아님).
    # REST 는 운영/모의 URL 이 동일하므로 모의투자는 demo 토큰 사용만으로 충분하다.
    token = (payload.get("token") or "").strip()
    if not token:
        return {"error": f"{KIND_NAME[kind]} ACCESS TOKEN 을 입력하거나 [발급] 하세요.", "need_token": kind}
    body = payload.get("body") if payload.get("body") is not None else e["body"]
    mode = payload.get("mode", "example")
    if mode == "sdk":
        # SDK 경로: client.apis.<group>.<method>(**평탄화된 In* 필드)
        # 상주 루프 + 캐시된 클라이언트 사용 (매 호출 클라이언트 생성 오버헤드 제거)
        return _sdk_run(_sdk_rest(e, body, token, kind))
    if e.get("paged"):
        # 페이징 예제: call_rest_paged 와 동일한 연속조회 루프 (SDK 경로의 max_pages=3 과 동일 상한)
        return _rest_paged_example(e, body, token, kind)
    # Example 경로(기본): 예제 call_rest 와 동일하게 전체 body 를 raw POST.
    url = f"{BASE}{e['url']}"
    headers = {"content-type": "application/json; charset=utf-8",
               "authorization": f"Bearer {token}", "cont_yn": "N", "cont_key": ""}
    r = _HTTP.post(url, headers=headers, json=body, timeout=30)
    try:
        data = r.json()
    except Exception:
        data = {"raw": r.text[:2000]}
    rsp_cd = (data.get("rsp_cd") or data.get("code") or "") if isinstance(data, dict) else ""
    rsp_msg = (data.get("rsp_msg") or data.get("message") or data.get("msg") or "") if isinstance(data, dict) else ""
    return {"status": r.status_code, "rsp_cd": str(rsp_cd), "rsp_msg": str(rsp_msg),
            "json": data, "used_key": kind, "mode": "example",
            "curl": build_curl(e["url"], body, kind)}


def _rest_paged_example(e: dict, body, token: str, kind: str,
                        max_pages: int = 3, page_sleep: float = 0.5) -> dict:
    """연속조회(페이징) Example 경로 - dbsec_helper.call_rest_paged 와 동일한 프로토콜.

    응답 헤더 cont_yn=='Y' 인 동안 cont_key 를 패스스루하며 반복 호출한다.
    페이지 간 page_sleep 대기(TPS 안전선), 무진행 가드(cont_key 미변경 시 중단),
    max_pages 상한(SDK 경로의 fetch_all·max_pages=3 과 동일)을 적용한다.
    """
    url = f"{BASE}{e['url']}"
    base_headers = {"content-type": "application/json; charset=utf-8",
                    "authorization": f"Bearer {token}"}
    pages, note, more = [], "", False
    cur_yn, cur_key = "N", ""
    r, data = None, None
    for page_no in range(1, max_pages + 1):
        r = _HTTP.post(url, headers={**base_headers, "cont_yn": cur_yn, "cont_key": cur_key},
                       json=body, timeout=30)
        try:
            data = r.json()
        except Exception:
            data = {"raw": r.text[:2000]}
        pages.append(data)
        if r.status_code != 200:
            break
        next_yn = r.headers.get("cont_yn", "N")
        next_key = r.headers.get("cont_key", "")
        if next_yn != "Y":
            break
        if not next_key or next_key == cur_key:     # 무진행 가드 (무한루프 방지)
            note = "서버가 cont_yn='Y' 이나 cont_key 무진행 - 중단"
            break
        if page_no >= max_pages:
            more = True                              # 상한 도달, 데이터 더 남음
            cur_key = next_key
            break
        cur_yn, cur_key = "Y", next_key
        time.sleep(page_sleep)
    rsp_cd = (data.get("rsp_cd") or data.get("code") or "") if isinstance(data, dict) else ""
    rsp_msg = (data.get("rsp_msg") or data.get("message") or data.get("msg") or "") if isinstance(data, dict) else ""
    return {"status": r.status_code if r is not None else None,
            "rsp_cd": str(rsp_cd), "rsp_msg": str(rsp_msg),
            "json": pages if len(pages) > 1 else (pages[0] if pages else None),
            "used_key": kind, "mode": "example",
            "paged": {"pages": len(pages), "more": more, "max_pages": max_pages,
                      "next_cont_key": cur_key if more else "", "note": note},
            "curl": build_curl(e["url"], body, kind)}


def flatten_body(body) -> dict:
    """{In:{...}, In1:{...}} → 평평한 kwargs (SDK 메서드는 In* 필드를 flat 인자로 받음)."""
    if not isinstance(body, dict):
        return {}
    blocks = [v for v in body.values() if isinstance(v, dict)]
    if blocks:
        kw = {}
        for b in blocks:
            kw.update(b)
        return kw
    return dict(body)


# ── SDK 경로 최적화: 상주 이벤트 루프 + 토큰별 DBSecClient 캐시 ──
# 호출마다 asyncio.run + 클라이언트 생성(~1s)을 없애고, aiohttp 세션의
# keep-alive 도 재사용한다. 클라이언트 생성/사용은 항상 이 루프 위에서 수행
# (aiohttp 세션이 이벤트 루프에 묶이므로).
_SDK_LOOP: asyncio.AbstractEventLoop | None = None
_SDK_CLIENTS: dict[str, object] = {}          # token -> DBSecClient (루프 스레드에서만 접근)
_SDK_LOOP_LOCK = threading.Lock()


def _sdk_loop() -> asyncio.AbstractEventLoop:
    global _SDK_LOOP
    with _SDK_LOOP_LOCK:
        if _SDK_LOOP is None:
            loop = asyncio.new_event_loop()
            threading.Thread(target=loop.run_forever, daemon=True, name="sdk-loop").start()
            _SDK_LOOP = loop
    return _SDK_LOOP


def _sdk_run(coro, timeout: float = 90):
    """핸들러 스레드에서 SDK 코루틴을 상주 루프에 제출하고 결과를 기다린다."""
    return asyncio.run_coroutine_threadsafe(coro, _sdk_loop()).result(timeout)


async def _sdk_client(token: str):
    """토큰별 DBSecClient 반환(없으면 생성·캐시). 상주 루프 위에서만 호출된다."""
    client = _SDK_CLIENTS.get(token)
    if client is None:
        from dbsec_sdk import DBSecClient
        client = DBSecClient(str(REPO / "config.yaml"))
        tm = client.token_manager
        tm._token_for_request = lambda: token
        tm.get_token = lambda: token
        tm.force_refresh = lambda *a, **k: token
        if len(_SDK_CLIENTS) >= 8:               # 토큰 재발급 누적 대비 상한
            _, old = _SDK_CLIENTS.popitem()
            try:
                await old.close()
            except Exception:
                pass
        _SDK_CLIENTS[token] = client
    return client


async def _sdk_rest(e: dict, body, token: str, kind: str) -> dict:
    from dbsec_sdk.exceptions import APIError
    kwargs = flatten_body(body)
    if e.get("paged"):
        kwargs["fetch_all"] = True
        kwargs["max_pages"] = 3
    client = await _sdk_client(token)
    fn = getattr(getattr(client.apis, e["group"]), e["method"])
    try:
        resp = await fn(**kwargs)
        out = {"status": resp.status_code, "rsp_cd": str(resp.rsp_cd or ""),
               "rsp_msg": str(resp.rsp_msg or ""), "json": resp.body, "used_key": kind, "mode": "sdk"}
        if e.get("paged"):
            # fetch_all 병합 응답: resp.pages=페이지별 원본 목록, has_more/cont_key=마지막 페이지 헤더
            more = bool(resp.has_more)
            out["paged"] = {"pages": len(resp.pages) if resp.pages else 1, "more": more,
                            "max_pages": kwargs.get("max_pages", 3),
                            "next_cont_key": resp.cont_key if more else "",
                            "note": "페이지 본문 병합됨 (list 블록 이어붙임)"}
        return out
    except APIError as ex:
        # SDK 는 업무에러(non-ok rsp_cd)를 예외로 표면화한다 — 그대로 보여준다.
        return {"status": getattr(ex, "status_code", None), "rsp_cd": str(getattr(ex, "rsp_cd", "") or ""),
                "rsp_msg": str(ex), "json": None, "used_key": kind, "mode": "sdk", "sdk_raises": "APIError"}
    except Exception as ex:
        return {"error": f"{type(ex).__name__}: {ex}", "used_key": kind, "mode": "sdk"}


def _ws_url_override(e: dict, kind: str, client) -> str | None:
    """SDK WS URL 결정: ov_futopt 는 전용 포트, demo 는 17070, 그 외 None(=config 기본)."""
    if e["is_ov_futopt"]:
        return client.config.ws_url_for(e.get("group_slug"))
    return WS_DEMO if kind == "demo" else None


def _patch_helper_ws_url(H, kind: str) -> None:
    """예제 경로: 모의 선택 시 helper 의 ws_url_for 를 demo URL 로 패치 (prd 면 원복)."""
    if not hasattr(H, "_orig_ws_url_for"):
        H._orig_ws_url_for = H.ws_url_for
    H.ws_url_for = (lambda *a, **k: WS_DEMO) if kind == "demo" else H._orig_ws_url_for


async def _ws_probe_sdk(e: dict, token: str, kind: str) -> dict:
    """SDK 경로: client.create_websocket() → DBSecWebSocket. 강제 드롭 후 graceful 확인."""
    from dbsec_sdk import DBSecClient
    client = DBSecClient(str(REPO / "config.yaml"))
    tm = client.token_manager
    tm._token_for_request = lambda: token; tm.get_token = lambda: token; tm.force_refresh = lambda: token
    ws = client.create_websocket(ws_url=_ws_url_override(e, kind, client))
    msgs, errs = [], []
    ws.on_message(lambda cd, k, d: msgs.append({"tr_cd": cd, "tr_key": k, "data": d}))
    graceful = False
    try:
        await ws.connect()
        await ws.add_realtime(e.get("tr_cd", ""), e.get("tr_key", ""), tr_type=e.get("tr_type", "1"))
        task = asyncio.create_task(ws.run())
        await asyncio.sleep(3.0)
        ws._running = False
        try: await ws._ws.close()       # 강제 종료(드롭)
        except Exception: pass
        try: await asyncio.wait_for(task, timeout=8)
        except Exception as ex: errs.append(f"task: {type(ex).__name__}")
        graceful = True
    except Exception as ex:
        errs.append(f"{type(ex).__name__}: {ex}")
    finally:
        try: await ws.close()
        except Exception: pass
    return {"connected": graceful, "graceful": graceful, "count": len(msgs),
            "messages": msgs[:8], "errors": errs, "url": ws._url, "used_key": kind, "mode": "sdk",
            "tr_cd": e.get("tr_cd"), "tr_key": e.get("tr_key"), "tr_type": e.get("tr_type")}


async def _ws_probe_example(e: dict, token: str, kind: str) -> dict:
    """Example 경로: 헬퍼 ws_subscribe + run_ws. 취소(Ctrl+C 등가)로 강제 종료."""
    import dbsec_helper as H
    H.get_token = lambda *a, **k: token          # 예제 경로 토큰 주입
    _patch_helper_ws_url(H, kind)
    msgs, errs = [], []
    def on_msg(m):
        try: msgs.append(json.loads(m))
        except Exception: msgs.append({"raw": str(m)[:200]})
    graceful = False
    try:
        url = H.ws_url_for(e.get("group_slug"))
        task = asyncio.create_task(H.ws_subscribe(
            tr_cd=e.get("tr_cd", ""), tr_key=e.get("tr_key", ""),
            group_slug=e.get("group_slug"), tr_type=e.get("tr_type", "1"), on_message=on_msg))
        await asyncio.sleep(3.0)
        task.cancel()                            # Ctrl+C 등가 (강제 종료)
        try: await asyncio.wait_for(task, timeout=13)
        except asyncio.CancelledError: errs.append("CancelledError 누출")
        except Exception as ex: errs.append(f"task: {type(ex).__name__}")
        graceful = not errs
    except Exception as ex:
        errs.append(f"{type(ex).__name__}: {ex}")
        url = None
    return {"connected": True, "graceful": graceful, "count": len(msgs),
            "messages": msgs[:8], "errors": errs, "url": url, "used_key": kind, "mode": "example",
            "tr_cd": e.get("tr_cd"), "tr_key": e.get("tr_key"), "tr_type": e.get("tr_type")}


def do_ws(payload: dict) -> dict:
    e = BY_ID.get(payload.get("id"))
    if not e or e["kind"] != "ws":
        return {"error": "WebSocket id 가 아닙니다."}
    kind = req_kind(e, payload)
    token = (payload.get("token") or "").strip()
    if not token:
        return {"error": f"{KIND_NAME[kind]} ACCESS TOKEN 을 입력하거나 [발급] 하세요.", "need_token": kind, "graceful": False}
    mode = payload.get("mode", "example")
    try:
        if mode == "sdk":
            return asyncio.run(_ws_probe_sdk(e, token, kind))
        return asyncio.run(_ws_probe_example(e, token, kind))
    except Exception as ex:
        return {"error": f"{type(ex).__name__}: {ex}", "graceful": False, "mode": mode}


def credentials() -> dict:
    # 키는 페이지로 보내지 않는다. [발급] 가능 여부(config 키 존재)만 알려준다.
    return {"base_url": BASE, "has": {k: bool(key) for k, (key, _s) in KEYS.items()}}


# ──────────────────────────────────────────────
# WebSocket 실시간 스트리밍 (SSE) — 수신할 때마다 브라우저로 push
# ──────────────────────────────────────────────
MAX_STREAM_SECONDS = 300   # 안전 상한 (클라가 ⏹ 중지하면 즉시 종료)


def _sse(write, event, data):
    write(f"event: {event}\ndata: {json.dumps(data, ensure_ascii=False)}\n\n")


async def _ws_stream(e: dict, token: str, mode: str, write, tr_key=None, kind: str = "prd") -> None:
    """WebSocket 구독 후 수신 메시지를 SSE 로 실시간 push. Example/SDK 양쪽 지원.

    tr_key: 페이지에서 입력한 구독 키(종목코드 등). None 이면 카탈로그 기본값을 사용한다.
    kind:   토큰 슬롯(prd/demo/ov_futopt). demo 면 모의투자 WS 포트(17070)로 접속한다.
    """
    key = e.get("tr_key", "") if tr_key is None else tr_key
    count = [0]; stop = asyncio.Event(); ws = None; task = None

    def emit(cd, k, d):
        count[0] += 1
        try:
            _sse(write, "msg", {"n": count[0], "tr_cd": cd, "tr_key": k, "data": d})
        except Exception:
            stop.set()      # 클라 연결 끊김 → 중단

    try:
        if mode == "example":
            import dbsec_helper as H
            H.get_token = lambda *a, **k: token
            _patch_helper_ws_url(H, kind)
            url = H.ws_url_for(e.get("group_slug"))

            def on_raw(m):
                try: d = json.loads(m)
                except Exception: d = {"raw": str(m)[:400]}
                cd = (d.get("header") or {}).get("tr_cd", "") if isinstance(d, dict) else ""
                emit(cd or e.get("tr_cd", ""), key, d)

            task = asyncio.create_task(H.ws_subscribe(
                tr_cd=e.get("tr_cd", ""), tr_key=key,
                group_slug=e.get("group_slug"), tr_type=e.get("tr_type", "1"), on_message=on_raw))
        else:
            from dbsec_sdk import DBSecClient
            client = DBSecClient(str(REPO / "config.yaml"))
            tm = client.token_manager
            tm._token_for_request = lambda: token; tm.get_token = lambda: token; tm.force_refresh = lambda: token
            ws = client.create_websocket(ws_url=_ws_url_override(e, kind, client))
            ws.on_message(emit)
            await ws.connect()
            await ws.add_realtime(e.get("tr_cd", ""), key, tr_type=e.get("tr_type", "1"))
            url = ws._url
            task = asyncio.create_task(ws.run())

        _sse(write, "opened", {"url": url, "mode": mode, "used_key": kind,
                               "tr_cd": e.get("tr_cd"), "tr_key": key, "tr_type": e.get("tr_type")})

        loop = asyncio.get_event_loop(); start = loop.time()
        while not stop.is_set() and task and not task.done():
            await asyncio.sleep(1.5)
            if loop.time() - start > MAX_STREAM_SECONDS:
                break
            try: write(": ping\n\n")     # 하트비트 — 클라 종료 감지 + keep-alive
            except Exception: break
    except Exception as ex:
        try: _sse(write, "err", {"error": f"{type(ex).__name__}: {ex}"})
        except Exception: pass
    finally:
        if ws is not None:
            ws._running = False
            try: await ws._ws.close()
            except Exception: pass
        if task is not None:
            task.cancel()
            try: await asyncio.wait_for(task, timeout=10)
            except Exception: pass
        if ws is not None:
            try: await ws.close()
            except Exception: pass
        try: _sse(write, "ended", {"count": count[0], "graceful": True})
        except Exception: pass


class Handler(BaseHTTPRequestHandler):
    def _send(self, code, body, ctype="application/json; charset=utf-8"):
        data = body if isinstance(body, (bytes, bytearray)) else json.dumps(body, ensure_ascii=False).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(data)))
        # 로컬 단일 사용자 도구 — 미리보기/다른 출처에서도 호출 가능하도록 CORS 허용.
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(data)

    def do_OPTIONS(self):     # CORS preflight
        self.send_response(204)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "content-type")
        self.send_header("Content-Length", "0")
        self.end_headers()

    def log_message(self, *a):  # 콘솔 소음 줄이기
        pass

    def do_GET(self):
        if self.path == "/" or self.path.startswith("/index"):
            html = (HERE / "index.html").read_bytes()
            return self._send(200, html, "text/html; charset=utf-8")
        # 정적 자산(favicon·로고 등) — HERE 디렉토리의 최상위 파일만 서빙(경로탐색 차단)
        name = urlparse(self.path).path.lstrip("/")
        if name and "/" not in name:
            ctypes = {"ico": "image/x-icon", "png": "image/png", "svg": "image/svg+xml",
                      "jpg": "image/jpeg", "jpeg": "image/jpeg", "gif": "image/gif"}
            ext = name.rsplit(".", 1)[-1].lower() if "." in name else ""
            f = HERE / name
            if ext in ctypes and f.is_file() and f.parent == HERE:
                return self._send(200, f.read_bytes(), ctypes[ext])
        if self.path == "/catalog":
            return self._send(200, {"catalog": CATALOG, "credentials": credentials()})
        if self.path.startswith("/ws_stream"):
            return self._ws_stream_route()
        return self._send(404, {"error": "not found"})

    def _ws_stream_route(self):
        q = parse_qs(urlparse(self.path).query, keep_blank_values=True)
        e = BY_ID.get(q.get("id", [""])[0])
        token = (q.get("token", [""])[0] or "").strip()
        mode = q.get("mode", ["example"])[0] or "example"
        tr_key = q.get("tr_key", [None])[0]   # 없으면 카탈로그 기본값, 있으면(빈값 포함) 입력값 사용
        key_kind = q.get("key_kind", [""])[0]
        self.send_response(200)
        self.send_header("Content-Type", "text/event-stream; charset=utf-8")
        self.send_header("Cache-Control", "no-cache")
        self.send_header("Connection", "keep-alive")
        self.send_header("X-Accel-Buffering", "no")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()

        def write(s):
            self.wfile.write(s.encode("utf-8")); self.wfile.flush()

        if not e or e["kind"] != "ws":
            return _sse(write, "err", {"error": "WebSocket id 가 아닙니다."})
        if not token:
            return _sse(write, "err", {"error": "ACCESS TOKEN 이 필요합니다."})
        try:
            asyncio.run(_ws_stream(e, token, mode, write, tr_key, req_kind(e, {"key_kind": key_kind})))
        except Exception as ex:
            try: _sse(write, "err", {"error": f"{type(ex).__name__}: {ex}"})
            except Exception: pass

    def do_POST(self):
        n = int(self.headers.get("Content-Length", 0) or 0)
        try:
            payload = json.loads(self.rfile.read(n) or b"{}")
        except Exception:
            payload = {}
        try:
            if self.path == "/token":
                # config.yaml 키로 발급해 페이지 입력칸을 채우는 보조 기능. 로컬 도구라 전체 토큰 반환.
                kind = payload.get("kind", "prd")
                tok = issue_token(kind)
                return self._send(200, {"ok": True, "kind": kind, "token": tok})
            if self.path == "/call":
                return self._send(200, do_call(payload))
            if self.path == "/ws":
                return self._send(200, do_ws(payload))
        except Exception as ex:
            return self._send(200, {"error": f"{type(ex).__name__}: {ex}"})
        return self._send(404, {"error": "not found"})


def main():
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", line_buffering=True)
    host, port = "127.0.0.1", 8765
    srv = ThreadingHTTPServer((host, port), Handler)
    url = f"http://{host}:{port}"
    print("─" * 52)
    print("DB증권 API 웹 테스터 기동 완료")
    print(f"  카탈로그 {len(CATALOG)}개 (rest/order/ws) · base_url={BASE}")
    print("  Ctrl+C 로 종료")
    print()
    # 대부분의 터미널(Windows Terminal·VS Code 등)에서 Ctrl+클릭으로 바로 열림
    print(f"  ▶ 브라우저로 열기:  {url}")
    print("─" * 52)
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        print("\n종료")
        srv.shutdown()


if __name__ == "__main__":
    main()
