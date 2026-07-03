#!/usr/bin/env python3
"""MCP 서버 실행 진입점 — GitHub 동기화(fetch + reset) 후 stdio 서버 기동.

cwd 에 의존하지 않는다: 자기 파일 위치(__file__)로 저장소 루트를 계산해 sys.path 에
추가하므로 어느 위치에서 실행하든 동작한다 (Claude Desktop 등록에 적합).

    python /절대경로/dbsec-open-api/mcp_server/run_server.py

기동 순서
  1) sync.sync_repo()  — git fetch + reset --hard (commit/push 없음, untracked 보존)
  2) DBSEC_DATA_ROOT 설정 후 server 로드 → 카탈로그 적재(인덱싱)
  3) mcp.run(stdio)

주의: stdio 는 stdout 을 JSON-RPC 채널로 쓰므로 모든 로그는 stderr 로만 출력한다.
"""
import os
import sys
from pathlib import Path

# mcp_server/ 의 부모 = 저장소 루트. cwd 와 무관하게 __file__ 로 결정.
_REPO_ROOT = Path(__file__).resolve().parents[1]
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))


def main() -> None:
    from mcp_server import sync

    data_root = sync.sync_repo()
    os.environ["DBSEC_DATA_ROOT"] = str(data_root)

    # 동기화로 확정된 경로를 server 가 읽도록 import 는 이 시점에.
    try:
        from mcp_server import server
    except Exception as e:  # 카탈로그 적재 실패 등
        print(f"[dbsec-mcp] 카탈로그 로드 실패: {e}", file=sys.stderr, flush=True)
        raise

    print("[dbsec-mcp] stdio 서버 시작 — 툴: list_api_groups, search_apis, "
          "get_api_spec, get_sample_code, get_setup_guide / "
          "프롬프트: dbsec_easy_code, dbsec_detailed_code", file=sys.stderr, flush=True)
    server.mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
