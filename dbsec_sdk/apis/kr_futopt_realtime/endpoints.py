"""국내선물옵션시세(실시간) API 모듈.

DB증권 OpenAPI 그룹: 국내선물옵션시세(실시간)
group_slug: kr_futopt_realtime

이 파일은 `_specs/kr_futopt_realtime/*.json` 에서 자동 생성되었습니다.
스펙이 갱신되면 `_workspace/build_modules.py`로 재생성하세요.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from dbsec_sdk.client import DBSecClient

from dbsec_sdk.response import APIResponse


class KrFutoptRealtimeAPI:
    """국내선물옵션시세(실시간) API 모음.

    사용법:
        >>> client = DBSecClient("config.yaml")
        >>> resp = client.apis.kr_futopt_realtime.<method>(...)
    """

    # API 경로 매핑
    PATHS = {
        'kr_futopt_realtime_order_execution': '/pub/IF0',
        'kr_futopt_realtime_index_future_orderbook': '/pub/F01',
        'kr_futopt_realtime_index_future_execution_price': '/pub/F00',
        'kr_futopt_realtime_mini_index_future_orderbook': '/pub/F91',
        'kr_futopt_realtime_mini_index_future_execution_price': '/pub/F90',
        'kr_futopt_realtime_sector_index_future_orderbook': '/pub/F71',
        'kr_futopt_realtime_sector_index_future_execution': '/pub/F70',
        'kr_futopt_realtime_stock_future_orderbook': '/pub/F21',
        'kr_futopt_realtime_stock_future_execution': '/pub/F20',
        'kr_futopt_realtime_commodity_future_orderbook': '/pub/F11',
        'kr_futopt_realtime_commodity_future_execution_price': '/pub/F10',
        'kr_futopt_realtime_index_option_orderbook': '/pub/O01',
        'kr_futopt_realtime_index_option_execution': '/pub/O00',
        'kr_futopt_realtime_stock_option_orderbook': '/pub/O21',
        'kr_futopt_realtime_stock_option_execution_price': '/pub/O20',
        'kr_futopt_realtime_mini_index_option_orderbook': '/pub/O91',
        'kr_futopt_realtime_mini_index_option_execution_price': '/pub/O90',
        'kr_futopt_realtime_k200_weekly_option_orderbook': '/pub/OB1',
        'kr_futopt_realtime_k200_weekly_option_execution': '/pub/OB0',
        'kr_futopt_realtime_kosdaq150_option_orderbook': '/pub/OA1',
        'kr_futopt_realtime_kosdaq150_option_execution': '/pub/OA0',
        'kr_futopt_realtime_future_execution_night': '/pub/F40',
        'kr_futopt_realtime_future_orderbook_night': '/pub/F41',
        'kr_futopt_realtime_option_execution_night': '/pub/O30',
        'kr_futopt_realtime_option_orderbook_night': '/pub/O31',
        'kr_futopt_realtime_mini_option_orderbook_night': '/pub/E11',
        'kr_futopt_realtime_mini_option_execution_price_night': '/pub/E10',
        'kr_futopt_realtime_kosdaq150_option_execution_price_night': '/pub/E20',
        'kr_futopt_realtime_kosdaq150_option_orderbook_night': '/pub/E21',
    }
    # TR 코드 매핑
    TR_CODES = {
        'kr_futopt_realtime_order_execution': 'IF0',
        'kr_futopt_realtime_index_future_orderbook': 'F01',
        'kr_futopt_realtime_index_future_execution_price': 'F00',
        'kr_futopt_realtime_mini_index_future_orderbook': 'F91',
        'kr_futopt_realtime_mini_index_future_execution_price': 'F90',
        'kr_futopt_realtime_sector_index_future_orderbook': 'F71',
        'kr_futopt_realtime_sector_index_future_execution': 'F70',
        'kr_futopt_realtime_stock_future_orderbook': 'F21',
        'kr_futopt_realtime_stock_future_execution': 'F20',
        'kr_futopt_realtime_commodity_future_orderbook': 'F11',
        'kr_futopt_realtime_commodity_future_execution_price': 'F10',
        'kr_futopt_realtime_index_option_orderbook': 'O01',
        'kr_futopt_realtime_index_option_execution': 'O00',
        'kr_futopt_realtime_stock_option_orderbook': 'O21',
        'kr_futopt_realtime_stock_option_execution_price': 'O20',
        'kr_futopt_realtime_mini_index_option_orderbook': 'O91',
        'kr_futopt_realtime_mini_index_option_execution_price': 'O90',
        'kr_futopt_realtime_k200_weekly_option_orderbook': 'OB1',
        'kr_futopt_realtime_k200_weekly_option_execution': 'OB0',
        'kr_futopt_realtime_kosdaq150_option_orderbook': 'OA1',
        'kr_futopt_realtime_kosdaq150_option_execution': 'OA0',
        'kr_futopt_realtime_future_execution_night': 'F40',
        'kr_futopt_realtime_future_orderbook_night': 'F41',
        'kr_futopt_realtime_option_execution_night': 'O30',
        'kr_futopt_realtime_option_orderbook_night': 'O31',
        'kr_futopt_realtime_mini_option_orderbook_night': 'E11',
        'kr_futopt_realtime_mini_option_execution_price_night': 'E10',
        'kr_futopt_realtime_kosdaq150_option_execution_price_night': 'E20',
        'kr_futopt_realtime_kosdaq150_option_orderbook_night': 'E21',
    }

    def __init__(self, client: 'DBSecClient'):
        self._client = client

    def kr_futopt_realtime_order_execution(self, *, body: dict, cont_yn: str = 'N', cont_key: str = '') -> APIResponse:
        """[실시간]선물옵션주문체결 (IF0).

        국내선물옵션 실시간 주문체결 API 입니다. 주문 체결시 내역이 출력됩니다.

        Args:
            body: 요청 JSON body (TR별 InBlock 형식).
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. resp.body 에 응답 데이터 포함.
        TR코드: IF0   TPS: 2
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=548b70a6-24cc-4d9d-a7c7-90eb84a497f4&api_id=99f558bf-e02f-40e7-a388-00ade0ddf5ce
        """
        raise NotImplementedError(
            "이 API 는 실시간 WebSocket TR 입니다 (tr_cd='IF0'). REST 호출이 아닙니다.\n"
            "사용 예:\n"
            "    ws = client.create_websocket()\n"
            "    ws.on_message(callback)\n"
            "    await ws.connect()\n"
            "    await ws.add_realtime(tr_cd='IF0', tr_key=..., tr_type='3')\n"
            "    await ws.run()"
        )

    def kr_futopt_realtime_index_future_orderbook(self, *, body: dict, cont_yn: str = 'N', cont_key: str = '') -> APIResponse:
        """[실시간]지수선물호가 (F01).

        국내 주식선물 실시간 호가 API 입니다.

        Args:
            body: 요청 JSON body (TR별 InBlock 형식).
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. resp.body 에 응답 데이터 포함.
        TR코드: F01   TPS: 2
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=548b70a6-24cc-4d9d-a7c7-90eb84a497f4&api_id=939266ee-126e-40c7-be0e-4c75df5511f2
        """
        raise NotImplementedError(
            "이 API 는 실시간 WebSocket TR 입니다 (tr_cd='F01'). REST 호출이 아닙니다.\n"
            "사용 예:\n"
            "    ws = client.create_websocket()\n"
            "    ws.on_message(callback)\n"
            "    await ws.connect()\n"
            "    await ws.add_realtime(tr_cd='F01', tr_key=..., tr_type='1')\n"
            "    await ws.run()"
        )

    def kr_futopt_realtime_index_future_execution_price(self, *, body: dict, cont_yn: str = 'N', cont_key: str = '') -> APIResponse:
        """[실시간]지수선물체결가 (F00).

        국내 주식선물 실시간 체결가 API 입니다.

        Args:
            body: 요청 JSON body (TR별 InBlock 형식).
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. resp.body 에 응답 데이터 포함.
        TR코드: F00   TPS: 2
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=548b70a6-24cc-4d9d-a7c7-90eb84a497f4&api_id=255c9383-dc11-41c1-a25c-5e2f8599e168
        """
        raise NotImplementedError(
            "이 API 는 실시간 WebSocket TR 입니다 (tr_cd='F00'). REST 호출이 아닙니다.\n"
            "사용 예:\n"
            "    ws = client.create_websocket()\n"
            "    ws.on_message(callback)\n"
            "    await ws.connect()\n"
            "    await ws.add_realtime(tr_cd='F00', tr_key=..., tr_type='1')\n"
            "    await ws.run()"
        )

    def kr_futopt_realtime_mini_index_future_orderbook(self, *, body: dict, cont_yn: str = 'N', cont_key: str = '') -> APIResponse:
        """[실시간]미니지수선물호가 (F91).

        국내 미니지수선물 실시간 호가 API 입니다.

        Args:
            body: 요청 JSON body (TR별 InBlock 형식).
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. resp.body 에 응답 데이터 포함.
        TR코드: F91   TPS: 2
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=548b70a6-24cc-4d9d-a7c7-90eb84a497f4&api_id=777b955c-17b2-4700-94cd-46735463cffe
        """
        raise NotImplementedError(
            "이 API 는 실시간 WebSocket TR 입니다 (tr_cd='F91'). REST 호출이 아닙니다.\n"
            "사용 예:\n"
            "    ws = client.create_websocket()\n"
            "    ws.on_message(callback)\n"
            "    await ws.connect()\n"
            "    await ws.add_realtime(tr_cd='F91', tr_key=..., tr_type='1')\n"
            "    await ws.run()"
        )

    def kr_futopt_realtime_mini_index_future_execution_price(self, *, body: dict, cont_yn: str = 'N', cont_key: str = '') -> APIResponse:
        """[실시간]미니지수선물체결가 (F90).

        국내 미니지수선물 실시간 체결가 API 입니다.

        Args:
            body: 요청 JSON body (TR별 InBlock 형식).
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. resp.body 에 응답 데이터 포함.
        TR코드: F90   TPS: 2
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=548b70a6-24cc-4d9d-a7c7-90eb84a497f4&api_id=68c12e16-2ab8-4c6e-92ba-b889e57ff49e
        """
        raise NotImplementedError(
            "이 API 는 실시간 WebSocket TR 입니다 (tr_cd='F90'). REST 호출이 아닙니다.\n"
            "사용 예:\n"
            "    ws = client.create_websocket()\n"
            "    ws.on_message(callback)\n"
            "    await ws.connect()\n"
            "    await ws.add_realtime(tr_cd='F90', tr_key=..., tr_type='1')\n"
            "    await ws.run()"
        )

    def kr_futopt_realtime_sector_index_future_orderbook(self, *, body: dict, cont_yn: str = 'N', cont_key: str = '') -> APIResponse:
        """[실시간]섹터지수선물호가 (F71).

        섹터지수선물 실시간 호가 API 입니다.

        Args:
            body: 요청 JSON body (TR별 InBlock 형식).
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. resp.body 에 응답 데이터 포함.
        TR코드: F71   TPS: 10
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=548b70a6-24cc-4d9d-a7c7-90eb84a497f4&api_id=85381b54-3258-48eb-b172-22abbbbd768d
        """
        raise NotImplementedError(
            "이 API 는 실시간 WebSocket TR 입니다 (tr_cd='F71'). REST 호출이 아닙니다.\n"
            "사용 예:\n"
            "    ws = client.create_websocket()\n"
            "    ws.on_message(callback)\n"
            "    await ws.connect()\n"
            "    await ws.add_realtime(tr_cd='F71', tr_key=..., tr_type='1')\n"
            "    await ws.run()"
        )

    def kr_futopt_realtime_sector_index_future_execution(self, *, body: dict, cont_yn: str = 'N', cont_key: str = '') -> APIResponse:
        """[실시간]섹터지수선물체결 (F70).

        섹터지수선물 실시간 체결가 API 입니다.

        Args:
            body: 요청 JSON body (TR별 InBlock 형식).
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. resp.body 에 응답 데이터 포함.
        TR코드: F70   TPS: 10
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=548b70a6-24cc-4d9d-a7c7-90eb84a497f4&api_id=e0dea90d-2247-4e92-843c-0d27592a7a93
        """
        raise NotImplementedError(
            "이 API 는 실시간 WebSocket TR 입니다 (tr_cd='F70'). REST 호출이 아닙니다.\n"
            "사용 예:\n"
            "    ws = client.create_websocket()\n"
            "    ws.on_message(callback)\n"
            "    await ws.connect()\n"
            "    await ws.add_realtime(tr_cd='F70', tr_key=..., tr_type='1')\n"
            "    await ws.run()"
        )

    def kr_futopt_realtime_stock_future_orderbook(self, *, body: dict, cont_yn: str = 'N', cont_key: str = '') -> APIResponse:
        """[실시간]주식선물호가 (F21).

        주식선물 실시간 호가 API 입니다.

        Args:
            body: 요청 JSON body (TR별 InBlock 형식).
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. resp.body 에 응답 데이터 포함.
        TR코드: F21   TPS: 10
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=548b70a6-24cc-4d9d-a7c7-90eb84a497f4&api_id=74f2800a-fbd1-4b2d-98c6-bcc86c84e334
        """
        raise NotImplementedError(
            "이 API 는 실시간 WebSocket TR 입니다 (tr_cd='F21'). REST 호출이 아닙니다.\n"
            "사용 예:\n"
            "    ws = client.create_websocket()\n"
            "    ws.on_message(callback)\n"
            "    await ws.connect()\n"
            "    await ws.add_realtime(tr_cd='F21', tr_key=..., tr_type='1')\n"
            "    await ws.run()"
        )

    def kr_futopt_realtime_stock_future_execution(self, *, body: dict, cont_yn: str = 'N', cont_key: str = '') -> APIResponse:
        """[실시간]주식선물체결 (F20).

        주식선물 실시간 체결가 API 입니다.

        Args:
            body: 요청 JSON body (TR별 InBlock 형식).
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. resp.body 에 응답 데이터 포함.
        TR코드: F20   TPS: 10
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=548b70a6-24cc-4d9d-a7c7-90eb84a497f4&api_id=020303ed-7a90-4b48-9260-b4c2a48bfa3d
        """
        raise NotImplementedError(
            "이 API 는 실시간 WebSocket TR 입니다 (tr_cd='F20'). REST 호출이 아닙니다.\n"
            "사용 예:\n"
            "    ws = client.create_websocket()\n"
            "    ws.on_message(callback)\n"
            "    await ws.connect()\n"
            "    await ws.add_realtime(tr_cd='F20', tr_key=..., tr_type='1')\n"
            "    await ws.run()"
        )

    def kr_futopt_realtime_commodity_future_orderbook(self, *, body: dict, cont_yn: str = 'N', cont_key: str = '') -> APIResponse:
        """[실시간]상품선물호가 (F11).

        국내 상품선물 실시간 호가 API 입니다.

        Args:
            body: 요청 JSON body (TR별 InBlock 형식).
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. resp.body 에 응답 데이터 포함.
        TR코드: F11   TPS: 2
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=548b70a6-24cc-4d9d-a7c7-90eb84a497f4&api_id=6523b603-2f9e-4916-907c-b8b921a61613
        """
        raise NotImplementedError(
            "이 API 는 실시간 WebSocket TR 입니다 (tr_cd='F11'). REST 호출이 아닙니다.\n"
            "사용 예:\n"
            "    ws = client.create_websocket()\n"
            "    ws.on_message(callback)\n"
            "    await ws.connect()\n"
            "    await ws.add_realtime(tr_cd='F11', tr_key=..., tr_type='1')\n"
            "    await ws.run()"
        )

    def kr_futopt_realtime_commodity_future_execution_price(self, *, body: dict, cont_yn: str = 'N', cont_key: str = '') -> APIResponse:
        """[실시간]상품선물체결가 (F10).

        국내 상품선물 실시간 호가 API 입니다.

        Args:
            body: 요청 JSON body (TR별 InBlock 형식).
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. resp.body 에 응답 데이터 포함.
        TR코드: F10   TPS: 2
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=548b70a6-24cc-4d9d-a7c7-90eb84a497f4&api_id=39512330-61ba-4fc6-9a99-355391b5ba87
        """
        raise NotImplementedError(
            "이 API 는 실시간 WebSocket TR 입니다 (tr_cd='F10'). REST 호출이 아닙니다.\n"
            "사용 예:\n"
            "    ws = client.create_websocket()\n"
            "    ws.on_message(callback)\n"
            "    await ws.connect()\n"
            "    await ws.add_realtime(tr_cd='F10', tr_key=..., tr_type='1')\n"
            "    await ws.run()"
        )

    def kr_futopt_realtime_index_option_orderbook(self, *, body: dict, cont_yn: str = 'N', cont_key: str = '') -> APIResponse:
        """[실시간]지수옵션호가 (O01).

        지수옵션 실시간 호가 API 입니다.

        Args:
            body: 요청 JSON body (TR별 InBlock 형식).
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. resp.body 에 응답 데이터 포함.
        TR코드: O01   TPS: 10
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=548b70a6-24cc-4d9d-a7c7-90eb84a497f4&api_id=e5c920ce-204f-47d8-b341-6a26fa600777
        """
        raise NotImplementedError(
            "이 API 는 실시간 WebSocket TR 입니다 (tr_cd='O01'). REST 호출이 아닙니다.\n"
            "사용 예:\n"
            "    ws = client.create_websocket()\n"
            "    ws.on_message(callback)\n"
            "    await ws.connect()\n"
            "    await ws.add_realtime(tr_cd='O01', tr_key=..., tr_type='1')\n"
            "    await ws.run()"
        )

    def kr_futopt_realtime_index_option_execution(self, *, body: dict, cont_yn: str = 'N', cont_key: str = '') -> APIResponse:
        """[실시간]지수옵션체결 (O00).

        지수옵션 실시간 체결가 API 입니다.

        Args:
            body: 요청 JSON body (TR별 InBlock 형식).
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. resp.body 에 응답 데이터 포함.
        TR코드: O00   TPS: 10
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=548b70a6-24cc-4d9d-a7c7-90eb84a497f4&api_id=a9da1f6f-2522-4734-9c5b-b4907bb5d159
        """
        raise NotImplementedError(
            "이 API 는 실시간 WebSocket TR 입니다 (tr_cd='O00'). REST 호출이 아닙니다.\n"
            "사용 예:\n"
            "    ws = client.create_websocket()\n"
            "    ws.on_message(callback)\n"
            "    await ws.connect()\n"
            "    await ws.add_realtime(tr_cd='O00', tr_key=..., tr_type='1')\n"
            "    await ws.run()"
        )

    def kr_futopt_realtime_stock_option_orderbook(self, *, body: dict, cont_yn: str = 'N', cont_key: str = '') -> APIResponse:
        """[실시간]주식옵션호가 (O21).

        국내 주식옵션 실시간 호가 API 입니다.

        Args:
            body: 요청 JSON body (TR별 InBlock 형식).
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. resp.body 에 응답 데이터 포함.
        TR코드: O21   TPS: 2
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=548b70a6-24cc-4d9d-a7c7-90eb84a497f4&api_id=070b02e5-f624-4ea1-9a8c-363ae7acf079
        """
        raise NotImplementedError(
            "이 API 는 실시간 WebSocket TR 입니다 (tr_cd='O21'). REST 호출이 아닙니다.\n"
            "사용 예:\n"
            "    ws = client.create_websocket()\n"
            "    ws.on_message(callback)\n"
            "    await ws.connect()\n"
            "    await ws.add_realtime(tr_cd='O21', tr_key=..., tr_type='1')\n"
            "    await ws.run()"
        )

    def kr_futopt_realtime_stock_option_execution_price(self, *, body: dict, cont_yn: str = 'N', cont_key: str = '') -> APIResponse:
        """[실시간]주식옵션체결가 (O20).

        국내 주식옵션 실시간 체결가 API 입니다.

        Args:
            body: 요청 JSON body (TR별 InBlock 형식).
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. resp.body 에 응답 데이터 포함.
        TR코드: O20   TPS: 2
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=548b70a6-24cc-4d9d-a7c7-90eb84a497f4&api_id=261e3194-15db-4391-82de-3e5b1e0bb505
        """
        raise NotImplementedError(
            "이 API 는 실시간 WebSocket TR 입니다 (tr_cd='O20'). REST 호출이 아닙니다.\n"
            "사용 예:\n"
            "    ws = client.create_websocket()\n"
            "    ws.on_message(callback)\n"
            "    await ws.connect()\n"
            "    await ws.add_realtime(tr_cd='O20', tr_key=..., tr_type='1')\n"
            "    await ws.run()"
        )

    def kr_futopt_realtime_mini_index_option_orderbook(self, *, body: dict, cont_yn: str = 'N', cont_key: str = '') -> APIResponse:
        """[실시간]미니지수옵션호가 (O91).

        국내 미니지수옵션 실시간 호가 API 입니다.

        Args:
            body: 요청 JSON body (TR별 InBlock 형식).
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. resp.body 에 응답 데이터 포함.
        TR코드: O91   TPS: 2
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=548b70a6-24cc-4d9d-a7c7-90eb84a497f4&api_id=3f2a3b96-7217-4154-a2b6-848442e1c247
        """
        raise NotImplementedError(
            "이 API 는 실시간 WebSocket TR 입니다 (tr_cd='O91'). REST 호출이 아닙니다.\n"
            "사용 예:\n"
            "    ws = client.create_websocket()\n"
            "    ws.on_message(callback)\n"
            "    await ws.connect()\n"
            "    await ws.add_realtime(tr_cd='O91', tr_key=..., tr_type='1')\n"
            "    await ws.run()"
        )

    def kr_futopt_realtime_mini_index_option_execution_price(self, *, body: dict, cont_yn: str = 'N', cont_key: str = '') -> APIResponse:
        """[실시간]미니지수옵션체결가 (O90).

        국내 미니지수옵션 실시간 체결가 API 입니다.

        Args:
            body: 요청 JSON body (TR별 InBlock 형식).
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. resp.body 에 응답 데이터 포함.
        TR코드: O90   TPS: 2
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=548b70a6-24cc-4d9d-a7c7-90eb84a497f4&api_id=4d0f0e24-4d99-4fb7-babd-afbe20634c40
        """
        raise NotImplementedError(
            "이 API 는 실시간 WebSocket TR 입니다 (tr_cd='O90'). REST 호출이 아닙니다.\n"
            "사용 예:\n"
            "    ws = client.create_websocket()\n"
            "    ws.on_message(callback)\n"
            "    await ws.connect()\n"
            "    await ws.add_realtime(tr_cd='O90', tr_key=..., tr_type='1')\n"
            "    await ws.run()"
        )

    def kr_futopt_realtime_k200_weekly_option_orderbook(self, *, body: dict, cont_yn: str = 'N', cont_key: str = '') -> APIResponse:
        """[실시간]K200지수위클리옵션호가 (OB1).

        K200지수위클리옵션 실시간 호가 API 입니다.

        Args:
            body: 요청 JSON body (TR별 InBlock 형식).
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. resp.body 에 응답 데이터 포함.
        TR코드: OB1   TPS: 2
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=548b70a6-24cc-4d9d-a7c7-90eb84a497f4&api_id=e6e0b8c7-6f2e-407b-8f1f-b4701950682c
        """
        raise NotImplementedError(
            "이 API 는 실시간 WebSocket TR 입니다 (tr_cd='OB1'). REST 호출이 아닙니다.\n"
            "사용 예:\n"
            "    ws = client.create_websocket()\n"
            "    ws.on_message(callback)\n"
            "    await ws.connect()\n"
            "    await ws.add_realtime(tr_cd='OB1', tr_key=..., tr_type='1')\n"
            "    await ws.run()"
        )

    def kr_futopt_realtime_k200_weekly_option_execution(self, *, body: dict, cont_yn: str = 'N', cont_key: str = '') -> APIResponse:
        """[실시간]K200지수위클리옵션체결 (OB0).

        K200지수위클리옵션 실시간 체결가 API 입니다.

        Args:
            body: 요청 JSON body (TR별 InBlock 형식).
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. resp.body 에 응답 데이터 포함.
        TR코드: OB0   TPS: 2
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=548b70a6-24cc-4d9d-a7c7-90eb84a497f4&api_id=54fab0a8-7bd4-4557-9c45-e332587a64e9
        """
        raise NotImplementedError(
            "이 API 는 실시간 WebSocket TR 입니다 (tr_cd='OB0'). REST 호출이 아닙니다.\n"
            "사용 예:\n"
            "    ws = client.create_websocket()\n"
            "    ws.on_message(callback)\n"
            "    await ws.connect()\n"
            "    await ws.add_realtime(tr_cd='OB0', tr_key=..., tr_type='1')\n"
            "    await ws.run()"
        )

    def kr_futopt_realtime_kosdaq150_option_orderbook(self, *, body: dict, cont_yn: str = 'N', cont_key: str = '') -> APIResponse:
        """[실시간]KOSDAQ150옵션호가 (OA1).

        KOSDAQ150옵션 실시간 호가 API 입니다.

        Args:
            body: 요청 JSON body (TR별 InBlock 형식).
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. resp.body 에 응답 데이터 포함.
        TR코드: OA1   TPS: 10
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=548b70a6-24cc-4d9d-a7c7-90eb84a497f4&api_id=ceda2366-3b40-4545-ab21-ceeb65205d73
        """
        raise NotImplementedError(
            "이 API 는 실시간 WebSocket TR 입니다 (tr_cd='OA1'). REST 호출이 아닙니다.\n"
            "사용 예:\n"
            "    ws = client.create_websocket()\n"
            "    ws.on_message(callback)\n"
            "    await ws.connect()\n"
            "    await ws.add_realtime(tr_cd='OA1', tr_key=..., tr_type='1')\n"
            "    await ws.run()"
        )

    def kr_futopt_realtime_kosdaq150_option_execution(self, *, body: dict, cont_yn: str = 'N', cont_key: str = '') -> APIResponse:
        """[실시간]KOSDAQ150옵션체결 (OA0).

        KOSDAQ150옵션 실시간 체결가 API 입니다.

        Args:
            body: 요청 JSON body (TR별 InBlock 형식).
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. resp.body 에 응답 데이터 포함.
        TR코드: OA0   TPS: 10
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=548b70a6-24cc-4d9d-a7c7-90eb84a497f4&api_id=55d2f2cc-a85e-4bd0-8c61-04e25f0555d1
        """
        raise NotImplementedError(
            "이 API 는 실시간 WebSocket TR 입니다 (tr_cd='OA0'). REST 호출이 아닙니다.\n"
            "사용 예:\n"
            "    ws = client.create_websocket()\n"
            "    ws.on_message(callback)\n"
            "    await ws.connect()\n"
            "    await ws.add_realtime(tr_cd='OA0', tr_key=..., tr_type='1')\n"
            "    await ws.run()"
        )

    def kr_futopt_realtime_future_execution_night(self, *, body: dict, cont_yn: str = 'N', cont_key: str = '') -> APIResponse:
        """[실시간]선물체결(야간) (F40).

        야간선물 실시간 체결가 API 입니다.

        Args:
            body: 요청 JSON body (TR별 InBlock 형식).
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. resp.body 에 응답 데이터 포함.
        TR코드: F40   TPS: 2
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=548b70a6-24cc-4d9d-a7c7-90eb84a497f4&api_id=bbf8d6a7-ddb3-43c7-bb42-f22a0ece2fa5
        """
        raise NotImplementedError(
            "이 API 는 실시간 WebSocket TR 입니다 (tr_cd='F40'). REST 호출이 아닙니다.\n"
            "사용 예:\n"
            "    ws = client.create_websocket()\n"
            "    ws.on_message(callback)\n"
            "    await ws.connect()\n"
            "    await ws.add_realtime(tr_cd='F40', tr_key=..., tr_type='1')\n"
            "    await ws.run()"
        )

    def kr_futopt_realtime_future_orderbook_night(self, *, body: dict, cont_yn: str = 'N', cont_key: str = '') -> APIResponse:
        """[실시간]선물호가(야간) (F41).

        야간선물 실시간 호가 API 입니다.

        Args:
            body: 요청 JSON body (TR별 InBlock 형식).
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. resp.body 에 응답 데이터 포함.
        TR코드: F41   TPS: 2
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=548b70a6-24cc-4d9d-a7c7-90eb84a497f4&api_id=b0591195-6228-4154-9998-3af41ec7c6c6
        """
        raise NotImplementedError(
            "이 API 는 실시간 WebSocket TR 입니다 (tr_cd='F41'). REST 호출이 아닙니다.\n"
            "사용 예:\n"
            "    ws = client.create_websocket()\n"
            "    ws.on_message(callback)\n"
            "    await ws.connect()\n"
            "    await ws.add_realtime(tr_cd='F41', tr_key=..., tr_type='1')\n"
            "    await ws.run()"
        )

    def kr_futopt_realtime_option_execution_night(self, *, body: dict, cont_yn: str = 'N', cont_key: str = '') -> APIResponse:
        """[실시간]옵션체결(야간) (O30).

        야간옵션 실시간 체결가 API 입니다.

        Args:
            body: 요청 JSON body (TR별 InBlock 형식).
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. resp.body 에 응답 데이터 포함.
        TR코드: O30   TPS: 2
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=548b70a6-24cc-4d9d-a7c7-90eb84a497f4&api_id=300225dd-bd76-4ba9-81df-5d468b1f06a8
        """
        raise NotImplementedError(
            "이 API 는 실시간 WebSocket TR 입니다 (tr_cd='O30'). REST 호출이 아닙니다.\n"
            "사용 예:\n"
            "    ws = client.create_websocket()\n"
            "    ws.on_message(callback)\n"
            "    await ws.connect()\n"
            "    await ws.add_realtime(tr_cd='O30', tr_key=..., tr_type='1')\n"
            "    await ws.run()"
        )

    def kr_futopt_realtime_option_orderbook_night(self, *, body: dict, cont_yn: str = 'N', cont_key: str = '') -> APIResponse:
        """[실시간]옵션호가(야간) (O31).

        야간옵션 실시간 호가 API 입니다.

        Args:
            body: 요청 JSON body (TR별 InBlock 형식).
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. resp.body 에 응답 데이터 포함.
        TR코드: O31   TPS: 2
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=548b70a6-24cc-4d9d-a7c7-90eb84a497f4&api_id=eba643d9-c391-4cfc-8def-364c548b72e9
        """
        raise NotImplementedError(
            "이 API 는 실시간 WebSocket TR 입니다 (tr_cd='O31'). REST 호출이 아닙니다.\n"
            "사용 예:\n"
            "    ws = client.create_websocket()\n"
            "    ws.on_message(callback)\n"
            "    await ws.connect()\n"
            "    await ws.add_realtime(tr_cd='O31', tr_key=..., tr_type='1')\n"
            "    await ws.run()"
        )

    def kr_futopt_realtime_mini_option_orderbook_night(self, *, body: dict, cont_yn: str = 'N', cont_key: str = '') -> APIResponse:
        """[실시간]미니옵션호가(야간) (E11).

        미니옵션호가(야간) API입니다.

        Args:
            body: 요청 JSON body (TR별 InBlock 형식).
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. resp.body 에 응답 데이터 포함.
        TR코드: E11   TPS: 2
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=548b70a6-24cc-4d9d-a7c7-90eb84a497f4&api_id=1174e749-16cf-4aaa-bdd2-b881d7072b6e
        """
        raise NotImplementedError(
            "이 API 는 실시간 WebSocket TR 입니다 (tr_cd='E11'). REST 호출이 아닙니다.\n"
            "사용 예:\n"
            "    ws = client.create_websocket()\n"
            "    ws.on_message(callback)\n"
            "    await ws.connect()\n"
            "    await ws.add_realtime(tr_cd='E11', tr_key=..., tr_type='1')\n"
            "    await ws.run()"
        )

    def kr_futopt_realtime_mini_option_execution_price_night(self, *, body: dict, cont_yn: str = 'N', cont_key: str = '') -> APIResponse:
        """[실시간]미니옵션체결가(야간) (E10).

        미니옵션체결가(야간) API입니다.

        Args:
            body: 요청 JSON body (TR별 InBlock 형식).
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. resp.body 에 응답 데이터 포함.
        TR코드: E10   TPS: 2
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=548b70a6-24cc-4d9d-a7c7-90eb84a497f4&api_id=b2fa157e-fa7c-4d13-bb61-cd07ee9d8802
        """
        raise NotImplementedError(
            "이 API 는 실시간 WebSocket TR 입니다 (tr_cd='E10'). REST 호출이 아닙니다.\n"
            "사용 예:\n"
            "    ws = client.create_websocket()\n"
            "    ws.on_message(callback)\n"
            "    await ws.connect()\n"
            "    await ws.add_realtime(tr_cd='E10', tr_key=..., tr_type='1')\n"
            "    await ws.run()"
        )

    def kr_futopt_realtime_kosdaq150_option_execution_price_night(self, *, body: dict, cont_yn: str = 'N', cont_key: str = '') -> APIResponse:
        """[실시간]KOSDAQ150옵션체결가(야간) (E20).

        KOSDAQ150옵션체결가(야간) API입니다.

        Args:
            body: 요청 JSON body (TR별 InBlock 형식).
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. resp.body 에 응답 데이터 포함.
        TR코드: E20   TPS: 2
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=548b70a6-24cc-4d9d-a7c7-90eb84a497f4&api_id=4d593338-5bdb-41f1-8b68-dfef0fd3cea6
        """
        raise NotImplementedError(
            "이 API 는 실시간 WebSocket TR 입니다 (tr_cd='E20'). REST 호출이 아닙니다.\n"
            "사용 예:\n"
            "    ws = client.create_websocket()\n"
            "    ws.on_message(callback)\n"
            "    await ws.connect()\n"
            "    await ws.add_realtime(tr_cd='E20', tr_key=..., tr_type='1')\n"
            "    await ws.run()"
        )

    def kr_futopt_realtime_kosdaq150_option_orderbook_night(self, *, body: dict, cont_yn: str = 'N', cont_key: str = '') -> APIResponse:
        """[실시간]KOSDAQ150옵션호가(야간) (E21).

        KOSDAQ150옵션호가(야간) API입니다.

        Args:
            body: 요청 JSON body (TR별 InBlock 형식).
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. resp.body 에 응답 데이터 포함.
        TR코드: E21   TPS: 2
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=548b70a6-24cc-4d9d-a7c7-90eb84a497f4&api_id=94a4a8ab-102e-4fd7-acd8-9032c1eab191
        """
        raise NotImplementedError(
            "이 API 는 실시간 WebSocket TR 입니다 (tr_cd='E21'). REST 호출이 아닙니다.\n"
            "사용 예:\n"
            "    ws = client.create_websocket()\n"
            "    ws.on_message(callback)\n"
            "    await ws.connect()\n"
            "    await ws.add_realtime(tr_cd='E21', tr_key=..., tr_type='1')\n"
            "    await ws.run()"
        )
