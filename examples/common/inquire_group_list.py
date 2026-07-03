"""관심종목 그룹조회 (MCJDD88840) — standalone 예제.

그룹    : 공통
엔드포인트: POST /api/v1/quote/common/group-list
TPS     : 2
가이드  : https://openapi.dbsec.co.kr/apiservice?group_id=b5b58c45-0066-47ac-8854-67c4d7fb3d32&api_id=ec733ee3-b8c2-4194-bf9f-af773a9216a3

등록된 관심종목 그룹을 조회할 수 있는 API 입니다.

토큰은 examples/dbsec_helper.py 가 자동 발급/캐싱합니다.

실행:
    # examples/ 폴더에서 실행하는 경우:
    python common/inquire_group_list.py
    # examples/common/ 폴더에서 실행하는 경우:
    python inquire_group_list.py

── 응답 파라미터 (Out) ─ OUT_BEGIN ──────────────────────
  [TR MCJDD88840]
    Out  (배열)  Out
      itmcnt  (문자)  그룹 내 종목수
      grpno  (문자)  그룹 번호
      grpnm  (문자)  그룹명

  공통: rsp_cd  응답코드  ·  rsp_msg  응답메시지
── OUT_END ──────────────────────────────────────────────
"""


import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from dbsec_helper import call_rest, print_response

resp, data = call_rest(
    url="/api/v1/quote/common/group-list",
    body={
        "In": {
            "usrdiv": "H",  # 사용자구분 (str) - "H" 고정
        },
    },
    label="관심종목 그룹조회",
)
print_response(resp, data)
