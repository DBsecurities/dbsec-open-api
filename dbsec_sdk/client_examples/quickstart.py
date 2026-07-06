"""dbsec_sdk SDK 사용법 — 읽기 전용 조회 예제 (비동기).

  import asyncio
  from dbsec_sdk import DBSecClient

  async def main():
      client = DBSecClient("config.yaml")
      resp = await client.apis.<그룹>.<메서드>(...)   # 모든 호출은 await, 인자는 keyword-only + 필수
      print(resp.to_dataframe())                       # 응답을 DataFrame 으로
  asyncio.run(main())

토큰: get_token()/force_refresh()/revoke() 로 명시적 관리. auto_token=True(기본)면 요청 시
없거나 만료/무효인 토큰을 자동 발급·재발급(프롬프트 없음), False 면 직접 발급해야 함.
이 예제는 토큰 수명주기를 처음부터 끝까지 보여준다: 발급(get_token) → 조회 1~7 → 폐기(revoke).
주문(order/modify/cancel) 계열은 실제 매매가 실행되므로 이 예제는 조회만 사용.

필요 패키지: pandas (pip install pandas)
실행: python dbsec_sdk/client_examples/quickstart.py
"""
import asyncio, sys, io, pathlib
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

import pandas as pd
pd.set_option("display.unicode.east_asian_width", True)  # 한글 컬럼 정렬

from dbsec_sdk import DBSecClient

_CONFIG = pathlib.Path(__file__).resolve().parents[2] / "config.yaml"


def show(title, resp):
    print(f"\n=== {title}  (status={resp.status_code} rsp_cd= {resp.rsp_cd} | rsp_msg= {resp.rsp_msg}) ===")
    print(resp.to_dataframe())


async def main():
    client = DBSecClient(
        str(_CONFIG),
        # ── 유량제어 / 토큰 옵션
        rate_limit=True,          # 유량제어 적용여부: 호출 전 앱TPS+API별 TPS 간격을 맞춰 IGW00201(호출초과)을 예방. False면 미적용.
        rate_limit_safety=0.9,    # 안전계수(0<s≤1): 실제율 = 앱 TPS × s. 0.9=90%(10% 여유, 권장. 당사 기준 0.9 적용시 18TPS까지 호출가능)
        auto_token=False,          # 토큰 자동 발급/재발급: True면 요청 시 토큰이 없거나 만료/무효(IGW00121/123)면 자동 발급·재발급(프롬프트 없음).
                                  # False면 자동 발급 안 함 → 토큰 없으면 AuthError, 만료/무효는 APIError. get_token()/force_refresh()/revoke()로 직접 관리.
        rate_limit_backoff=True,  # 지수백오프 재시도: 유량제어 초과 메세지 (IGW00201) 받으면 1·2·4·8초 후 재시도(순간버스트 사후 회복).
                                  # False면 IGW00201을 즉시 APIError로 표면화.
    )
    print(f"mode = {client.config.mode}")

    # ── 토큰 수명주기 (명시적 관리) ───────────────────────────────
    # 발급/확보: 캐시에 유효 토큰 있으면 재사용, 없으면 발급. (auto_token=True면 아래 조회에서도 자동 발급되지만 명시적으로)
    token = await client.get_token()
    print(f"토큰 확보 완료 (…{token[-6:]})")
    #
    # 강제 갱신 — 현재 토큰을 폐기(revoke)하고 새로 발급. 보통은 불필요(만료 시 auto_token이 처리):
    #   await client.force_refresh()
    #
    # 명시적 폐기(revoke)는 아래 1~7 조회를 모두 마친 뒤 스크립트 끝에서 데모합니다.

    # 1) 주식현재가 — 삼성전자
    show("주식현재가조회",
         await client.apis.kr_stock_quote.kr_stock_inquire_price(
             InputCondMrktDivCode="J", 
             InputIscd1="005930"))
    # 2) 주식잔고조회
    show("주식잔고조회",
         await client.apis.kr_stock_order.kr_stock_inquire_balance(QryTpCode0="0"))

    # 3) 계좌예수금조회
    show("계좌예수금조회",
         await client.apis.kr_stock_order.kr_stock_inquire_deposit())

    # 4) 분차트조회 — 삼성전자 10분봉
    show("분차트조회",
         await client.apis.kr_chart.kr_chart_chart_min(
             InputCondMrktDivCode="J",
             InputIscd1="005930",
             InputDate1="20260526",
             InputDivXtick="600",
             dataCnt="5",
             InputOrgAdjPrc="1"))

    # 5) 멀티현재가조회 — 5종목
    show("멀티현재가조회",
         await client.apis.kr_stock_quote.kr_stock_inquire_price_multi(
             dataCnt=5,
             InputCondMrktDivCode1="J",
             InputIscd1="005930",
             InputCondMrktDivCode2="J",
             InputIscd2="000660",
             InputCondMrktDivCode3="J",
             InputIscd3="035720",
             InputCondMrktDivCode4="J",
             InputIscd4="005380",
             InputCondMrktDivCode5="U",
             InputIscd5="1001"))

    # 6) 주식조건상승하락조회 — 전일 상승률 상위
    show("주식조건상승하락조회",
         await client.apis.kr_stock_quote.kr_stock_inquire_condition_rise_fall(
             InputDateClsCode="1",
             InputRankSortClsCode1="12",
             InputMrktClsCode="A",
             InputBstpIscd=""))

    # 7) 해외주식 상승하락조회 — 미국 상승률 상위(거래량 100만주↑)
    show("해외주식 상승하락조회",
         await client.apis.ov_stock_quote.ov_stock_inquire_condition_rise_fall(
             InputRealDelayClsCode="1",
             InputDataCode="US",
             InputDateClsCode="0",
             InputRankSortClsCode1="249",
             InputVolClsCode="9",
             InputTrPbmn1="",
             InputDprice1="",
             InputDprice2=""))

    # ── 토큰 폐기 (revoke) ────────────────────────────────────────
    # 모든 조회(1~7)를 마쳤으니 토큰을 명시적으로 폐기 — 서버에서 무효화하고
    # 로컬 캐시(.dbsec_token.json)도 삭제한다. 다음 실행은 get_token()에서 다시 발급.
    # (DB증권은 24시간 내 재발급 시 동일 토큰을 반환하므로, 새 토큰이 필요할 땐 이렇게 폐기 후 발급한다.)
    #await client.revoke()
    #print("\n토큰 폐기 완료 (revoke) — 로컬 캐시(.dbsec_token.json) 삭제됨")

if __name__ == "__main__":
    asyncio.run(main())
