"""웹소켓 세션 초기화 [DisconnectSession] — standalone REST 예제.

그룹    : 웹소켓(공통)
엔드포인트: POST /api/v1/websocket/disconnectSession
TPS     : 1
가이드  : https://openapi.dbsec.co.kr/apiservice?group_id=0140b583-0f93-4aff-897b-e350b3652b40&api_id=cc424a15-7d38-46d6-ab6e-5d46b2b386fc

접속중인 모든 웹소켓 세션을 초기화 하는 API 입니다.
※ 발급받은 토큰정보와 일치하는 계좌의 세션이 초기화 됩니다.
※ 이름은 "웹소켓 세션 초기화" 이지만 호출 자체는 REST POST 입니다.

토큰은 examples/dbsec_helper.py 가 자동 발급/캐싱합니다.

실행:
    # examples/ 폴더에서 실행하는 경우:
    python ws_common/ws_session_disconnect.py
    # examples/ws_common/ 폴더에서 실행하는 경우:
    python ws_session_disconnect.py

── 응답 파라미터 (Out) ─ OUT_BEGIN ──────────────────────
  [TR DisconnectSession]
    Out  (오브젝트)  Out
      acntNo  (문자)  계좌번호 — 웹소켓 세션 초기화를 완료한 계좌번호
      result  (문자)  result — 처리 메세지

  공통: rsp_cd  응답코드  ·  rsp_msg  응답메시지
── OUT_END ──────────────────────────────────────────────
"""


import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from dbsec_helper import call_rest, print_response

resp, data = call_rest(
    url="/api/v1/websocket/disconnectSession",
    body={},  # 요청 본문 없음 (스펙상 req_body 빈 배열)
    label="웹소켓 세션 초기화",
)
print_response(resp, data)
