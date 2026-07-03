"""국내주식시세(실시간) API 모듈.

DB증권 OpenAPI 그룹: 국내주식시세(실시간)
group_slug: kr_stock_realtime

이 파일은 `_specs/kr_stock_realtime/*.json` 에서 자동 생성되었습니다.
스펙이 갱신되면 `_workspace/build_modules.py`로 재생성하세요.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from dbsec_sdk.client import DBSecClient

from dbsec_sdk.response import APIResponse


class KrStockRealtimeAPI:
    """국내주식시세(실시간) API 모음.

    사용법:
        >>> client = DBSecClient("config.yaml")
        >>> resp = client.apis.kr_stock_realtime.<method>(...)
    """

    # API 경로 매핑
    PATHS = {
        'kr_stock_realtime_order_execution': '/pub/IS1',
        'kr_stock_realtime_order_accept': '/pub/IS0',
        'kr_stock_realtime_orderbook': '/pub/S01',
        'kr_stock_realtime_execution_price': '/pub/S00',
        'kr_stock_realtime_elw_orderbook': '/pub/W01',
        'kr_stock_realtime_elw_execution': '/pub/W00',
        'kr_stock_realtime_industry_index_execution_price': '/pub/U00',
        'kr_stock_realtime_industry_index_change': '/pub/U03',
        'kr_stock_realtime_industry_investor': '/pub/U05',
    }
    # TR 코드 매핑
    TR_CODES = {
        'kr_stock_realtime_order_execution': 'IS1',
        'kr_stock_realtime_order_accept': 'IS0',
        'kr_stock_realtime_orderbook': 'S01',
        'kr_stock_realtime_execution_price': 'S00',
        'kr_stock_realtime_elw_orderbook': 'W01',
        'kr_stock_realtime_elw_execution': 'W00',
        'kr_stock_realtime_industry_index_execution_price': 'U00',
        'kr_stock_realtime_industry_index_change': 'U03',
        'kr_stock_realtime_industry_investor': 'U05',
    }

    def __init__(self, client: 'DBSecClient'):
        self._client = client

    def kr_stock_realtime_order_execution(self, *, body: dict, cont_yn: str = 'N', cont_key: str = '') -> APIResponse:
        """[실시간]주식주문체결 조회 (IS1).

        국내주식 실시간 주문체결 API 입니다. 주문 체결시 내역이 출력됩니다.

        Args:
            body: 요청 JSON body (TR별 InBlock 형식).
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. resp.body 에 응답 데이터 포함.
        TR코드: IS1   TPS: 2
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=94b5fddc-b819-451b-9619-13ee42468798&api_id=a3a93ec3-2ccc-4fa5-8096-b45616b785e4
        """
        raise NotImplementedError(
            "이 API 는 실시간 WebSocket TR 입니다 (tr_cd='IS1'). REST 호출이 아닙니다.\n"
            "사용 예:\n"
            "    ws = client.create_websocket()\n"
            "    ws.on_message(callback)\n"
            "    await ws.connect()\n"
            "    await ws.add_realtime(tr_cd='IS1', tr_key=..., tr_type='3')\n"
            "    await ws.run()"
        )

    def kr_stock_realtime_order_accept(self, *, body: dict, cont_yn: str = 'N', cont_key: str = '') -> APIResponse:
        """[실시간]주식주문접수 조회 (IS0).

        국내주식 실시간 주문접수 API 입니다. 주문 접수시 내역이 출력됩니다.

        Args:
            body: 요청 JSON body (TR별 InBlock 형식).
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. resp.body 에 응답 데이터 포함.
        TR코드: IS0   TPS: 2
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=94b5fddc-b819-451b-9619-13ee42468798&api_id=24ae5513-5186-4e7e-a4eb-66bfe10a0d8a
        """
        raise NotImplementedError(
            "이 API 는 실시간 WebSocket TR 입니다 (tr_cd='IS0'). REST 호출이 아닙니다.\n"
            "사용 예:\n"
            "    ws = client.create_websocket()\n"
            "    ws.on_message(callback)\n"
            "    await ws.connect()\n"
            "    await ws.add_realtime(tr_cd='IS0', tr_key=..., tr_type='3')\n"
            "    await ws.run()"
        )

    def kr_stock_realtime_orderbook(self, *, body: dict, cont_yn: str = 'N', cont_key: str = '') -> APIResponse:
        """[실시간]주식호가 (S01).

        국내주식 실시간 호가 API 입니다.

        Args:
            body: 요청 JSON body (TR별 InBlock 형식).
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. resp.body 에 응답 데이터 포함.
        TR코드: S01   TPS: 2
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=94b5fddc-b819-451b-9619-13ee42468798&api_id=973365c6-91fd-4ca8-ac66-fa1a65017c0e
        """
        raise NotImplementedError(
            "이 API 는 실시간 WebSocket TR 입니다 (tr_cd='S01'). REST 호출이 아닙니다.\n"
            "사용 예:\n"
            "    ws = client.create_websocket()\n"
            "    ws.on_message(callback)\n"
            "    await ws.connect()\n"
            "    await ws.add_realtime(tr_cd='S01', tr_key=..., tr_type='1')\n"
            "    await ws.run()"
        )

    def kr_stock_realtime_execution_price(self, *, body: dict, cont_yn: str = 'N', cont_key: str = '') -> APIResponse:
        """[실시간]주식체결가 (S00).

        국내주식 실시간 체결가 API 입니다.

        Args:
            body: 요청 JSON body (TR별 InBlock 형식).
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. resp.body 에 응답 데이터 포함.
        TR코드: S00   TPS: 2
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=94b5fddc-b819-451b-9619-13ee42468798&api_id=7c257cdc-5807-46ca-8d86-666a2bfd6798
        """
        raise NotImplementedError(
            "이 API 는 실시간 WebSocket TR 입니다 (tr_cd='S00'). REST 호출이 아닙니다.\n"
            "사용 예:\n"
            "    ws = client.create_websocket()\n"
            "    ws.on_message(callback)\n"
            "    await ws.connect()\n"
            "    await ws.add_realtime(tr_cd='S00', tr_key=..., tr_type='1')\n"
            "    await ws.run()"
        )

    def kr_stock_realtime_elw_orderbook(self, *, body: dict, cont_yn: str = 'N', cont_key: str = '') -> APIResponse:
        """[실시간]ELW호가 (W01).

        ELW 실시간 호가 API 입니다.

        Args:
            body: 요청 JSON body (TR별 InBlock 형식).
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. resp.body 에 응답 데이터 포함.
        TR코드: W01   TPS: 10
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=94b5fddc-b819-451b-9619-13ee42468798&api_id=f6d79404-3c1e-4f7f-b176-49b542477bf4
        """
        raise NotImplementedError(
            "이 API 는 실시간 WebSocket TR 입니다 (tr_cd='W01'). REST 호출이 아닙니다.\n"
            "사용 예:\n"
            "    ws = client.create_websocket()\n"
            "    ws.on_message(callback)\n"
            "    await ws.connect()\n"
            "    await ws.add_realtime(tr_cd='W01', tr_key=..., tr_type='1')\n"
            "    await ws.run()"
        )

    def kr_stock_realtime_elw_execution(self, *, body: dict, cont_yn: str = 'N', cont_key: str = '') -> APIResponse:
        """[실시간]ELW체결 (W00).

        ELW 실시간 체결가 API 입니다.

        Args:
            body: 요청 JSON body (TR별 InBlock 형식).
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. resp.body 에 응답 데이터 포함.
        TR코드: W00   TPS: 10
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=94b5fddc-b819-451b-9619-13ee42468798&api_id=cd318c5d-5bd3-4998-99a5-c74002e9caba
        """
        raise NotImplementedError(
            "이 API 는 실시간 WebSocket TR 입니다 (tr_cd='W00'). REST 호출이 아닙니다.\n"
            "사용 예:\n"
            "    ws = client.create_websocket()\n"
            "    ws.on_message(callback)\n"
            "    await ws.connect()\n"
            "    await ws.add_realtime(tr_cd='W00', tr_key=..., tr_type='1')\n"
            "    await ws.run()"
        )

    def kr_stock_realtime_industry_index_execution_price(self, *, body: dict, cont_yn: str = 'N', cont_key: str = '') -> APIResponse:
        """[실시간]업종지수체결가 (U00).

        업종지수 체결가 조회 API 입니다.

        Args:
            body: 요청 JSON body (TR별 InBlock 형식).
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. resp.body 에 응답 데이터 포함.
        TR코드: U00   TPS: 2
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=94b5fddc-b819-451b-9619-13ee42468798&api_id=831d29dc-d607-474a-b85a-5dd4fe1ab74d
        """
        raise NotImplementedError(
            "이 API 는 실시간 WebSocket TR 입니다 (tr_cd='U00'). REST 호출이 아닙니다.\n"
            "사용 예:\n"
            "    ws = client.create_websocket()\n"
            "    ws.on_message(callback)\n"
            "    await ws.connect()\n"
            "    await ws.add_realtime(tr_cd='U00', tr_key=..., tr_type='1')\n"
            "    await ws.run()"
        )

    def kr_stock_realtime_industry_index_change(self, *, body: dict, cont_yn: str = 'N', cont_key: str = '') -> APIResponse:
        """[실시간]업종지수등락 (U03).

        업종지수 등락 조회 API 입니다.

        Args:
            body: 요청 JSON body (TR별 InBlock 형식).
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. resp.body 에 응답 데이터 포함.
        TR코드: U03   TPS: 2
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=94b5fddc-b819-451b-9619-13ee42468798&api_id=017147ee-baef-41de-8826-d0208a780be7
        """
        raise NotImplementedError(
            "이 API 는 실시간 WebSocket TR 입니다 (tr_cd='U03'). REST 호출이 아닙니다.\n"
            "사용 예:\n"
            "    ws = client.create_websocket()\n"
            "    ws.on_message(callback)\n"
            "    await ws.connect()\n"
            "    await ws.add_realtime(tr_cd='U03', tr_key=..., tr_type='1')\n"
            "    await ws.run()"
        )

    def kr_stock_realtime_industry_investor(self, *, body: dict, cont_yn: str = 'N', cont_key: str = '') -> APIResponse:
        """[실시간]업종별투자자 (U05).

        업종별 투자자 조회 API 입니다.

        Args:
            body: 요청 JSON body (TR별 InBlock 형식).
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. resp.body 에 응답 데이터 포함.
        TR코드: U05   TPS: 2
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=94b5fddc-b819-451b-9619-13ee42468798&api_id=73819a0e-7df0-4f15-b9f5-e8e3c945caf8
        """
        raise NotImplementedError(
            "이 API 는 실시간 WebSocket TR 입니다 (tr_cd='U05'). REST 호출이 아닙니다.\n"
            "사용 예:\n"
            "    ws = client.create_websocket()\n"
            "    ws.on_message(callback)\n"
            "    await ws.connect()\n"
            "    await ws.add_realtime(tr_cd='U05', tr_key=..., tr_type='1')\n"
            "    await ws.run()"
        )
