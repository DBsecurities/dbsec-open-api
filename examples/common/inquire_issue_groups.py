"""관심그룹 종목조회 (MCJDD88841) — standalone 예제.

그룹    : 공통
엔드포인트: POST /api/v1/quote/common/group-stocks
TPS     : 3
가이드  : https://openapi.dbsec.co.kr/apiservice?group_id=b5b58c45-0066-47ac-8854-67c4d7fb3d32&api_id=c8852378-8a17-41f3-8df5-9b61d633c805

관심그룹에 저장된 종목을 조회할 수 있는 API.

해외주식 종목코드(itmcd) 보정:
  - itmmk == "O" (해외주식) 인 항목의 itmcd 는 '구 시장코드(2자리) + 티커' 형태로
    내려오는데, 구 시장코드가 더 이상 사용되지 않으므로 신 코드로 치환해서 표시한다.
        NS → FN  (나스닥)
        YS → FY  (뉴욕)
        AS → FA  (아멕스)
    예) NSMETA → FNMETA,  YSAAPL → FYAAPL,  ASGLD → FAGLD

토큰은 examples/dbsec_helper.py 가 자동 발급/캐싱.

실행:
    # examples/ 폴더에서 실행하는 경우:
    python common/inquire_issue_groups.py
    # examples/common/ 폴더에서 실행하는 경우:
    python inquire_issue_groups.py

── 응답 파라미터 (Out) ─ OUT_BEGIN ──────────────────────
  [TR MCJDD88841]
    Out  (배열)  Out
      itemcnt  (문자)  조회건수
      grpnm  (문자)  그룹명
    Out1  (배열)  Out1
      itmseq  (문자)  종목순서
      itmmk  (문자)  종목종류
      itmcd  (문자)  종목코드 — 해외주식의 경우, 시장코드 + 종목코드 형태로 출력됩니다. (ex. "NSAAPL") 맨 앞의 시장코드 2자리를 제거하시고 사용 바랍니다. 관심종목의 해외주식 시장코드는 시세 조회시에 사용하는 시장코드와 다르며, 변환표는 다음과 같습니다. NS : 나스닥 거래소 -> FN YS : 뉴욕 거래소 -> FY AS : 아멕스 거래소 -> FA

  공통: rsp_cd  응답코드  ·  rsp_msg  응답메시지
── OUT_END ──────────────────────────────────────────────
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from dbsec_helper import call_rest, print_response


# ─────────────────────────────────────────
# 해외주식 시장코드 변환 룰 (구 → 신)
# ─────────────────────────────────────────
_OVERSEAS_MARKET_CODE_MAP = {
    "NS": "FN",   # 나스닥
    "YS": "FY",   # 뉴욕
    "AS": "FA",   # 아멕스
}


def _convert_overseas_itmcd(item: dict) -> dict:
    """itmmk == 'O' (해외주식) 인 경우 itmcd 앞 2자리를 신 코드로 치환."""
    if item.get("itmmk") != "O":
        return item
    code = item.get("itmcd", "") or ""
    if len(code) >= 2 and code[:2] in _OVERSEAS_MARKET_CODE_MAP:
        item["itmcd"] = _OVERSEAS_MARKET_CODE_MAP[code[:2]] + code[2:]
    return item


def _walk_and_convert(obj):
    """응답 본문을 순회하며 해외주식 항목의 itmcd 변환."""
    if isinstance(obj, dict):
        if "itmmk" in obj or "itmcd" in obj:
            _convert_overseas_itmcd(obj)
        for v in obj.values():
            _walk_and_convert(v)
    elif isinstance(obj, list):
        for v in obj:
            _walk_and_convert(v)


# ─────────────────────────────────────────
# API 호출 → 응답 가공 → 출력
# ─────────────────────────────────────────
# verbose=False: 헬퍼의 기본 응답 출력을 끄고, itmcd 변환 후 직접 출력한다.
resp, data = call_rest(
    url="/api/v1/quote/common/group-stocks",
    body={
        "In": {
            "usrdiv": "H",  # 사용자구분 (str) - "H" 고정
            "grpno":  "001",  # 그룹넘버 (str)
        },
    },
    label="관심그룹 종목조회",
    verbose=False,
)

# 응답 본문 내 해외주식 항목 itmcd 변환 (NS→FN, YS→FY, AS→FA)
_walk_and_convert(data)

# 변환된 데이터 기준으로 출력 (다른 예제와 동일한 포맷)
print_response(resp, data, label="관심그룹 종목조회")
