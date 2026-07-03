"""해외선물옵션시세(실시간) API 모듈.

DB증권 OpenAPI 그룹: 해외선물옵션시세(실시간)
group_slug: ov_futopt_realtime

이 파일은 `_specs/ov_futopt_realtime/*.json` 에서 자동 생성되었습니다.
스펙이 갱신되면 `_workspace/build_modules.py`로 재생성하세요.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from dbsec_sdk.client import DBSecClient

from dbsec_sdk.response import APIResponse


class OvFutoptRealtimeAPI:
    """해외선물옵션시세(실시간) API 모음.

    사용법:
        >>> client = DBSecClient("config.yaml")
        >>> resp = client.apis.ov_futopt_realtime.<method>(...)
    """

    # API 경로 매핑
    PATHS = {
        'ov_futopt_realtime_order_execution': '/pub/O',
        'ov_futopt_realtime_balance': '/pub/P',
        'ov_futopt_realtime_future_orderbook': '/pub/L01',
        'ov_futopt_realtime_future_quote': '/pub/K01',
        'ov_futopt_realtime_option_quote': '/pub/K02',
        'ov_futopt_realtime_option_orderbook': '/pub/L02',
    }
    # TR 코드 매핑
    TR_CODES = {
        'ov_futopt_realtime_order_execution': 'O',
        'ov_futopt_realtime_balance': 'P',
        'ov_futopt_realtime_future_orderbook': 'L01',
        'ov_futopt_realtime_future_quote': 'K01',
        'ov_futopt_realtime_option_quote': 'K02',
        'ov_futopt_realtime_option_orderbook': 'L02',
    }

    def __init__(self, client: 'DBSecClient'):
        self._client = client

    def ov_futopt_realtime_order_execution(self, *, body: dict, cont_yn: str = 'N', cont_key: str = '') -> APIResponse:
        """[실시간]주문체결 (O).

        해외선물옵션 실시간 주문체결 API 입니다. 주문 체결시 내역이 출력됩니다.

        Args:
            body: 요청 JSON body (TR별 InBlock 형식).
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. resp.body 에 응답 데이터 포함.
        TR코드: O   TPS: 2
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=f1819725-95e6-4445-ad7f-aa1908b20b03&api_id=227bff3a-ef1f-41b5-aee7-13c034f1e1f8
        """
        raise NotImplementedError(
            "이 API 는 실시간 WebSocket TR 입니다 (tr_cd='O'). REST 호출이 아닙니다.\n"
            "사용 예:\n"
            "    ws = client.create_websocket()\n"
            "    ws.on_message(callback)\n"
            "    await ws.connect()\n"
            "    await ws.add_realtime(tr_cd='O', tr_key=..., tr_type='3')\n"
            "    await ws.run()"
        )

    def ov_futopt_realtime_balance(self, *, body: dict, cont_yn: str = 'N', cont_key: str = '') -> APIResponse:
        """[실시간]잔고 (P).

        해외선물옵션 실시간 잔고 API 입니다. 주문 체결시 내역이 출력됩니다.

        Args:
            body: 요청 JSON body (TR별 InBlock 형식).
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. resp.body 에 응답 데이터 포함.
        TR코드: P   TPS: 2
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=f1819725-95e6-4445-ad7f-aa1908b20b03&api_id=8c1c0e6a-a0cd-4eb8-a170-40832b8317c4
        """
        raise NotImplementedError(
            "이 API 는 실시간 WebSocket TR 입니다 (tr_cd='P'). REST 호출이 아닙니다.\n"
            "사용 예:\n"
            "    ws = client.create_websocket()\n"
            "    ws.on_message(callback)\n"
            "    await ws.connect()\n"
            "    await ws.add_realtime(tr_cd='P', tr_key=..., tr_type='3')\n"
            "    await ws.run()"
        )

    def ov_futopt_realtime_future_orderbook(self, *, body: dict, cont_yn: str = 'N', cont_key: str = '') -> APIResponse:
        """[실시간]해외선물호가 (L01).

        해외선물 실시간 호가 API 입니다. ※ 해외선물옵션 API시세 신청이 되어있지 않은 경우 실시간 시세를 수신 하실 수 없습니다.
        ※ API시세(유료) 신청방법 GTS(Happy+ Global) : [1761] API시세 신청 ※ 해외선물옵션 가이드는 다음
        주소에서 확인 가능하십니다. http://link.dbsec.co.kr/gts/ebook/index.html#page=1 ※ GTS
        다운로드는 다음 링크 확인 부탁드리겠습니다. https://www.dbsec.co.kr/research/osft/re_Osft_viw14.do

        Args:
            body: 요청 JSON body (TR별 InBlock 형식).
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. resp.body 에 응답 데이터 포함.
        TR코드: L01   TPS: 2
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=f1819725-95e6-4445-ad7f-aa1908b20b03&api_id=393c083a-f119-4f7a-a16a-5e6c6cd8901b
        """
        raise NotImplementedError(
            "이 API 는 실시간 WebSocket TR 입니다 (tr_cd='L01'). REST 호출이 아닙니다.\n"
            "사용 예:\n"
            "    ws = client.create_websocket()\n"
            "    ws.on_message(callback)\n"
            "    await ws.connect()\n"
            "    await ws.add_realtime(tr_cd='L01', tr_key=..., tr_type='1')\n"
            "    await ws.run()"
        )

    def ov_futopt_realtime_future_quote(self, *, body: dict, cont_yn: str = 'N', cont_key: str = '') -> APIResponse:
        """[실시간]해외선물시세 (K01).

        해외선물 실시간 시세(체결가) API 입니다. ※ 해외선물옵션 API시세 신청이 되어있지 않은 경우 실시간 시세를 수신 하실 수
        없습니다. ※ API시세(유료) 신청방법 GTS(Happy+ Global) : [1761] API시세 신청 ※ 해외선물옵션
        가이드는 다음 주소에서 확인 가능하십니다. http://link.dbsec.co.kr/gts/ebook/index.html#page=1 ※ GTS 다운로드는 다음 링크 확인 부탁드리겠습니다.
        https://www.dbsec.co.kr/research/osft/re_Osft_viw14.do

        Args:
            body: 요청 JSON body (TR별 InBlock 형식).
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. resp.body 에 응답 데이터 포함.
        TR코드: K01   TPS: 2
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=f1819725-95e6-4445-ad7f-aa1908b20b03&api_id=80f69aed-a8a9-4c96-bbfc-070b1946b41a
        """
        raise NotImplementedError(
            "이 API 는 실시간 WebSocket TR 입니다 (tr_cd='K01'). REST 호출이 아닙니다.\n"
            "사용 예:\n"
            "    ws = client.create_websocket()\n"
            "    ws.on_message(callback)\n"
            "    await ws.connect()\n"
            "    await ws.add_realtime(tr_cd='K01', tr_key=..., tr_type='1')\n"
            "    await ws.run()"
        )

    def ov_futopt_realtime_option_quote(self, *, body: dict, cont_yn: str = 'N', cont_key: str = '') -> APIResponse:
        """[실시간]해외옵션시세 (K02).

        해외옵션 실시간 시세(체결가) API 입니다. ※ 해외선물옵션 API시세 신청이 되어있지 않은 경우 실시간 시세를 수신 하실 수
        없습니다. ※ API시세(유료) 신청방법 GTS(Happy+ Global) : [1761] API시세 신청 ※ 해외선물옵션
        가이드는 다음 주소에서 확인 가능하십니다. http://link.dbsec.co.kr/gts/ebook/index.html#page=1 ※ GTS 다운로드는 다음 링크 확인 부탁드리겠습니다.
        https://www.dbsec.co.kr/research/osft/re_Osft_viw14.do

        Args:
            body: 요청 JSON body (TR별 InBlock 형식).
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. resp.body 에 응답 데이터 포함.
        TR코드: K02   TPS: 2
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=f1819725-95e6-4445-ad7f-aa1908b20b03&api_id=97d9cab2-1b76-40e3-82e7-cc9db12a2120
        """
        raise NotImplementedError(
            "이 API 는 실시간 WebSocket TR 입니다 (tr_cd='K02'). REST 호출이 아닙니다.\n"
            "사용 예:\n"
            "    ws = client.create_websocket()\n"
            "    ws.on_message(callback)\n"
            "    await ws.connect()\n"
            "    await ws.add_realtime(tr_cd='K02', tr_key=..., tr_type='1')\n"
            "    await ws.run()"
        )

    def ov_futopt_realtime_option_orderbook(self, *, body: dict, cont_yn: str = 'N', cont_key: str = '') -> APIResponse:
        """[실시간]해외옵션호가 (L02).

        해외옵션 실시간 호가 API 입니다. ※ 해외선물옵션 API시세 신청이 되어있지 않은 경우 실시간 시세를 수신 하실 수 없습니다.
        ※ API시세(유료) 신청방법 GTS(Happy+ Global) : [1761] API시세 신청 ※ 해외선물옵션 가이드는 다음
        주소에서 확인 가능하십니다. http://link.dbsec.co.kr/gts/ebook/index.html#page=1 ※ GTS
        다운로드는 다음 링크 확인 부탁드리겠습니다. https://www.dbsec.co.kr/research/osft/re_Osft_viw14.do

        Args:
            body: 요청 JSON body (TR별 InBlock 형식).
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. resp.body 에 응답 데이터 포함.
        TR코드: L02   TPS: 2
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=f1819725-95e6-4445-ad7f-aa1908b20b03&api_id=6573bf4f-c8ec-4bfd-9285-859c271a0d7a
        """
        raise NotImplementedError(
            "이 API 는 실시간 WebSocket TR 입니다 (tr_cd='L02'). REST 호출이 아닙니다.\n"
            "사용 예:\n"
            "    ws = client.create_websocket()\n"
            "    ws.on_message(callback)\n"
            "    await ws.connect()\n"
            "    await ws.add_realtime(tr_cd='L02', tr_key=..., tr_type='1')\n"
            "    await ws.run()"
        )
