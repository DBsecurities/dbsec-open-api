"""GitHub 동기화 — 서버 기동 시 저장소를 원격 기준으로 강제 동기화(reset)한다.

전략: `git fetch` 후 `git reset --hard FETCH_HEAD` — 로컬을 원격과 **정확히 일치**시킨다.
  · 사용자는 저장소를 소비(pull)만 하고 직접 수정/커밋하지 않으므로, 로컬이 어긋나도
    (ff-only pull 이 실패하는 상황 포함) 항상 원격 상태로 깨끗하게 맞춘다.
  · `reset --hard` 는 **추적(tracked) 파일만** 원복한다. `git clean` 을 돌리지 않으므로
    `config.yaml`·`.dbsec_token.json` 같은 **추적되지 않는(untracked/ignored) 파일은 보존**된다.
c
원칙
  · `git fetch` / `git reset --hard` / `git clone` 만 수행한다.
  · add / commit / push 는 **절대 수행하지 않는다** — 사용자는 받아오기만 한다.
  · 네트워크 실패·오프라인이면 경고만 남기고 기존 로컬 사본으로 진행(fail-soft).

stdio MCP 는 stdout 을 JSON-RPC 채널로 쓰므로, 모든 로그는 **stderr** 로 보낸다.

환경변수
  DBSEC_MCP_GIT_DIR    동기화 대상 로컬 경로 (기본: 저장소 루트)
  DBSEC_MCP_GIT_REPO   clone 대상 git URL (디렉토리가 없을 때만 사용)
  DBSEC_MCP_GIT_BRANCH pull/clone 브랜치 (기본: main)
  DBSEC_MCP_GIT_SKIP_SYNC      "1"/"true" 이면 동기화 생략(오프라인 개발용)
"""
from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]


def _log(msg: str) -> None:
    print(f"[dbsec-mcp sync] {msg}", file=sys.stderr, flush=True)


def _run(args: list[str], cwd: Path | None = None) -> tuple[int, str]:
    try:
        p = subprocess.run(
            args, cwd=str(cwd) if cwd else None,
            capture_output=True, text=True, timeout=120,
        )
        return p.returncode, (p.stdout + p.stderr).strip()
    except FileNotFoundError:
        return 127, "git 실행 파일을 찾을 수 없습니다 (PATH 확인)."
    except subprocess.TimeoutExpired:
        return 124, "git 작업 시간 초과(120s)."


def _is_git_repo(path: Path) -> bool:
    if not path.exists():
        return False
    code, _ = _run(["git", "rev-parse", "--is-inside-work-tree"], cwd=path)
    return code == 0


def sync_repo() -> Path:
    """저장소를 동기화하고 데이터 루트 경로를 반환한다. 실패해도 예외 없이 경로 반환."""
    target = Path(os.environ.get("DBSEC_MCP_GIT_DIR", str(REPO_ROOT))).resolve()
    repo = os.environ.get("DBSEC_MCP_GIT_REPO", "").strip()
    branch = os.environ.get("DBSEC_MCP_GIT_BRANCH", "main").strip() or "main"
    skip = os.environ.get("DBSEC_MCP_GIT_SKIP_SYNC", "").lower() in ("1", "true", "yes")

    if skip:
        _log(f"DBSEC_MCP_GIT_SKIP_SYNC 설정됨 — 동기화 생략. 로컬 사용: {target}")
        return target

    # clone (디렉토리가 없고 repo URL 이 주어진 경우에만)
    if not _is_git_repo(target):
        if repo:
            target.parent.mkdir(parents=True, exist_ok=True)
            _log(f"git clone {repo} (branch={branch}) → {target}")
            code, out = _run(["git", "clone", "--branch", branch, repo, str(target)])
            if code != 0:
                _log(f"clone 실패(무시하고 진행): {out}")
        else:
            _log(f"git 저장소 아님 & DBSEC_MCP_GIT_REPO 미설정 — 로컬 사용: {target}")
        return target

    # 미커밋(추적 파일) 변경이 있으면 reset --hard 가 그것을 파괴하므로 동기화를 건너뛴다.
    # (개발 중인 로컬 변경 보호 — untracked 파일은 reset 대상이 아니므로 -uno 로 제외)
    code, dirty = _run(["git", "-C", str(target), "status", "--porcelain", "--untracked-files=no"])
    if code == 0 and dirty.strip():
        _log("로컬에 미커밋(추적) 변경 있음 — 동기화 생략(작업 보호). "
             "원격과 맞추려면 변경을 커밋/되돌린 뒤 재시작하세요.\n" + dirty.strip())
        return target

    # 강제 동기화: fetch 후 원격 기준으로 reset (commit/push 없음, untracked 보존)
    _log(f"git fetch origin {branch} @ {target}")
    code, out = _run(["git", "-C", str(target), "fetch", "origin", branch])
    if code != 0:
        _log(f"fetch 실패(무시하고 기존 로컬 사본 사용): {out}")
        return target

    _log("git reset --hard FETCH_HEAD")
    code, out = _run(["git", "-C", str(target), "reset", "--hard", "FETCH_HEAD"])
    if code == 0:
        _log("동기화 완료(reset): " + (out.splitlines()[-1] if out else "원격과 일치"))
    else:
        _log(f"reset 실패(무시하고 기존 로컬 사본 사용): {out}")
    return target
