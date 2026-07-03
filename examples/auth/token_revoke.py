"""접근토큰 폐기 (revoke) — standalone 예제.

엔드포인트: POST /oauth2/revoke
가이드  : https://openapi.dbsec.co.kr/apiservice?group_id=cc55b867-e049-421b-a798-be016370ff44&api_id=3395b34c-f48c-436f-a5fa-dbae6b224af8

발급받은 접근토큰을 더 이상 활용하지 않을 때 사용합니다.

기능:
  · 루트 .dbsec_token.json 에 캐시된 토큰을 폐기
  · 캐시 파일도 함께 삭제
  · 캐시가 비어있으면 안내 메시지 후 종료

실행:
    # examples/ 폴더에서 실행하는 경우:
    python auth/token_revoke.py
    # examples/auth/ 폴더에서 실행하는 경우:
    python token_revoke.py

── 응답 파라미터 (Out) ─ OUT_BEGIN ──────────────────────
  [TR revoke]
    code  (문자)  응답코드
    msg  (문자)  응답메세지

  공통: rsp_cd  응답코드  ·  rsp_msg  응답메시지
── OUT_END ──────────────────────────────────────────────
"""

import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from dbsec_helper import revoke_token, print_response

resp, data = revoke_token()
if resp is None:
    print(data["info"])
else:
    print_response(resp, data, label="접근토큰 폐기")
    print()
    print("✓ 토큰 캐시 파일 삭제됨")
