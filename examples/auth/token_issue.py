"""접근토큰 발급 (token) — standalone 예제.

엔드포인트: POST /oauth2/token
가이드  : https://openapi.dbsec.co.kr/apiservice?group_id=cc55b867-e049-421b-a798-be016370ff44&api_id=9e3097ab-7d39-4433-8002-00649604f0de

본인을 인증하는 확인 절차로, 접근 토큰을 부여받아 오픈 API 활용이 가능합니다. ※ API호출 유량은 1분에 1건 입니다. ※ 접근토큰 유효기간 개인/법인 : 신청일시로부터 24시간 ※ 유효기간 만료 전 토큰을 발급을 하는경우, 동일한 토큰이 발급됩니다. (만료기간도 동일) 유효기간 만료 전 새 토큰이 필요한 경우 접근토큰 폐기 후 발급 부탁드립니다.
※ 토큰 만료 전 재발급 시 기존 토큰과 동일한 토큰이 발급되며, 만료기간도 동일합니다. 새로운 만료기간이 필요하신 경우에는, 기존 토큰을 폐기(revoke)하신 후에 다시 발급(issue)해 주시기 바랍니다.

기능:
  · 토큰을 발급받아 루트 .dbsec_token.json 에 캐시 저장
  · 다른 API 예제는 이 캐시를 자동으로 재사용 (만료 시 [1] 자동 발급 / [2] 취소 선택)
  · 폐기는 token_revoke.py 실행

실행:
    # examples/ 폴더에서 실행하는 경우:
    python auth/token_issue.py
    # examples/auth/ 폴더에서 실행하는 경우:
    python token_issue.py

── 응답 파라미터 (Out) ─ OUT_BEGIN ──────────────────────
  [TR token]
    token  (문자)  접근토큰 — G/W 에서 발급하는 접근토큰
    expire_in  (문자)  접근토큰 유효기간 — 유효기간(초)
    scope  (문자)  scope — "oob"
    token_type  (문자)  토큰 유형 — Bearer

  공통: rsp_cd  응답코드  ·  rsp_msg  응답메시지
── OUT_END ──────────────────────────────────────────────
"""

import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

# dbsec_helper import 시점에 stdout/stderr 이 UTF-8 로 재설정됨 (cp949 우회)
from dbsec_helper import issue_token, load_config, print_response, _TOKEN_CACHE

# 어떤 환경으로 호출하는지 먼저 표시
_cfg = load_config()
_env_label = "운영(production)" if _cfg["mode"] == "production" else "모의투자(demo)"

resp, data = issue_token(_cfg)
print_response(resp, data, label=f"접근토큰 발급 [{_env_label}]")

if resp.ok and data.get("access_token"):
    print()
    print(f"✓ 토큰 캐시 저장: {_TOKEN_CACHE}")
    print(f"  환경       : {_env_label}")
