"""해외주식시세(실시간) API 모듈.

DB증권 OpenAPI 그룹: 해외주식시세(실시간)
group_slug: ov_stock_realtime

이 파일은 `_specs/ov_stock_realtime/*.json` 에서 자동 생성되었습니다.
스펙이 갱신되면 `_workspace/build_modules.py`로 재생성하세요.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from dbsec_sdk.client import DBSecClient

from dbsec_sdk.response import APIResponse


class OvStockRealtimeAPI:
    """해외주식시세(실시간) API 모음.

    사용법:
        >>> client = DBSecClient("config.yaml")
        >>> resp = client.apis.ov_stock_realtime.<method>(...)
    """

    # API 경로 매핑
    PATHS = {
        'ov_stock_realtime_order_execution': '/pub/IS2',
        'ov_stock_realtime_execution_price': '/pub/V60',
        'ov_stock_realtime_orderbook': '/pub/V61',
        'ov_stock_realtime_delayed_execution_price': '/pub/V10',
        'ov_stock_realtime_delayed_orderbook': '/pub/V11',
    }
    # TR 코드 매핑
    TR_CODES = {
        'ov_stock_realtime_order_execution': 'IS2',
        'ov_stock_realtime_execution_price': 'V60',
        'ov_stock_realtime_orderbook': 'V61',
        'ov_stock_realtime_delayed_execution_price': 'V10',
        'ov_stock_realtime_delayed_orderbook': 'V11',
    }

    def __init__(self, client: 'DBSecClient'):
        self._client = client

    def ov_stock_realtime_order_execution(self, *, body: dict, cont_yn: str = 'N', cont_key: str = '') -> APIResponse:
        """[실시간]해외주식 주문체결 조회 (IS2).

        해외주식 실시간 주문체결 API 입니다. 주문 체결시 내역이 출력됩니다.

        Args:
            body: 요청 JSON body (TR별 InBlock 형식).
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. resp.body 에 응답 데이터 포함.
        TR코드: IS2   TPS: 2
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=68dccbef-704a-4ebc-86ac-e44056c5687b&api_id=85fc552d-4bcd-45e5-8fd3-62eaf01b7e5c
        """
        raise NotImplementedError(
            "이 API 는 실시간 WebSocket TR 입니다 (tr_cd='IS2'). REST 호출이 아닙니다.\n"
            "사용 예:\n"
            "    ws = client.create_websocket()\n"
            "    ws.on_message(callback)\n"
            "    await ws.connect()\n"
            "    await ws.add_realtime(tr_cd='IS2', tr_key=..., tr_type='3')\n"
            "    await ws.run()"
        )

    def ov_stock_realtime_execution_price(self, *, body: dict, cont_yn: str = 'N', cont_key: str = '') -> APIResponse:
        """[실시간]해외주식 체결가 (V60).

        해외주식(미국) 실시간 체결가 API 입니다. ※ 해외주식(미국) 무료실시간시세 신청을 하지 않을 경우 실시간 시세를 수신 하실
        수 없습니다. (V10,V11 지연시세는 별도 신청없이 사용 가능하십니다.) ※ 실시간무료시세(0분) 신청방법 HTS :
        [7325] 해외주식 실시간 시세 신청 MTS : 해외주식 > 서비스신청 > 실시간시세신청 ※ 무료 실시간 시세는 전체 시세에
        비해 50% 수준의 체결 데이터를 제공합니다. ※ 무료 실시간 시세 자동결제 신청 시 당월 거래가 없거나 말일에 보유한 미국주식
        잔고가 없을 시 자동 해지됩니다.

        Args:
            body: 요청 JSON body (TR별 InBlock 형식).
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. resp.body 에 응답 데이터 포함.
        TR코드: V60   TPS: 2
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=68dccbef-704a-4ebc-86ac-e44056c5687b&api_id=bb2ec432-194d-49dc-819b-763244cc6efa
        """
        raise NotImplementedError(
            "이 API 는 실시간 WebSocket TR 입니다 (tr_cd='V60'). REST 호출이 아닙니다.\n"
            "사용 예:\n"
            "    ws = client.create_websocket()\n"
            "    ws.on_message(callback)\n"
            "    await ws.connect()\n"
            "    await ws.add_realtime(tr_cd='V60', tr_key=..., tr_type='1')\n"
            "    await ws.run()"
        )

    def ov_stock_realtime_orderbook(self, *, body: dict, cont_yn: str = 'N', cont_key: str = '') -> APIResponse:
        """[실시간]해외주식 호가 (V61).

        해외주식(미국) 실시간 호가 API 입니다. ※ 해외주식(미국) 무료실시간시세 신청을 하지 않을 경우 실시간 시세를 수신 하실 수
        없습니다. (V10,V11 지연시세는 별도 신청없이 사용 가능하십니다.) ※ 실시간무료시세(0분) 신청방법 HTS : [7325]
        해외주식 실시간 시세 신청 MTS : 해외주식 > 서비스신청 > 실시간시세신청 ※ 무료 실시간 시세는 전체 시세에 비해 50%
        수준의 체결 데이터를 제공합니다. ※ 무료 실시간 시세 자동결제 신청 시 당월 거래가 없거나 말일에 보유한 미국주식 잔고가 없을
        시 자동 해지됩니다. ※ 상세 안내는 다음 링크 확인 부탁드리겠습니다. https://www.dbsec.co.kr/research/osst/re_OsstDealInfo_viw30.do

        Args:
            body: 요청 JSON body (TR별 InBlock 형식).
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. resp.body 에 응답 데이터 포함.
        TR코드: V61   TPS: 2
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=68dccbef-704a-4ebc-86ac-e44056c5687b&api_id=13cee8fb-b055-4a2e-8fa0-ce7d0aa2b37a
        """
        raise NotImplementedError(
            "이 API 는 실시간 WebSocket TR 입니다 (tr_cd='V61'). REST 호출이 아닙니다.\n"
            "사용 예:\n"
            "    ws = client.create_websocket()\n"
            "    ws.on_message(callback)\n"
            "    await ws.connect()\n"
            "    await ws.add_realtime(tr_cd='V61', tr_key=..., tr_type='1')\n"
            "    await ws.run()"
        )

    def ov_stock_realtime_delayed_execution_price(self, *, body: dict, cont_yn: str = 'N', cont_key: str = '') -> APIResponse:
        """[실시간]해외주식 지연체결가 (V10).

        해외주식(미국) 지연 체결가 API 입니다. ※ 15분 지연된 실시간 시세를 받아보실 수 있습니다. ※ 해외주식(미국)
        무료실시간시세 신청을 하지 않을 경우 실시간 시세를 수신 하실 수 없습니다. (V10,V11 지연시세는 별도 신청없이 사용
        가능하십니다.) ※ 실시간무료시세(0분) 신청방법 HTS : [7325] 해외주식 실시간 시세 신청 MTS : 해외주식 >
        서비스신청 > 실시간시세신청

        Args:
            body: 요청 JSON body (TR별 InBlock 형식).
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. resp.body 에 응답 데이터 포함.
        TR코드: V10   TPS: 2
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=68dccbef-704a-4ebc-86ac-e44056c5687b&api_id=504007f6-1d8c-49b9-a533-43c7c1d27726
        """
        raise NotImplementedError(
            "이 API 는 실시간 WebSocket TR 입니다 (tr_cd='V10'). REST 호출이 아닙니다.\n"
            "사용 예:\n"
            "    ws = client.create_websocket()\n"
            "    ws.on_message(callback)\n"
            "    await ws.connect()\n"
            "    await ws.add_realtime(tr_cd='V10', tr_key=..., tr_type='1')\n"
            "    await ws.run()"
        )

    def ov_stock_realtime_delayed_orderbook(self, *, body: dict, cont_yn: str = 'N', cont_key: str = '') -> APIResponse:
        """[실시간]해외주식 지연호가 (V11).

        해외주식(미국) 지연 호가 API 입니다. ※ 15분 지연된 실시간 시세를 받아보실 수 있습니다. ※ 해외주식(미국)
        무료실시간시세 신청을 하지 않을 경우 실시간 시세를 수신 하실 수 없습니다. (V10,V11 지연시세는 별도 신청없이 사용
        가능하십니다.) ※ 실시간무료시세(0분) 신청방법 HTS : [7325] 해외주식 실시간 시세 신청 MTS : 해외주식 >
        서비스신청 > 실시간시세신청

        Args:
            body: 요청 JSON body (TR별 InBlock 형식).
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. resp.body 에 응답 데이터 포함.
        TR코드: V11   TPS: 2
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=68dccbef-704a-4ebc-86ac-e44056c5687b&api_id=daf5e5be-d465-413d-85d9-0bdebfbca727
        """
        raise NotImplementedError(
            "이 API 는 실시간 WebSocket TR 입니다 (tr_cd='V11'). REST 호출이 아닙니다.\n"
            "사용 예:\n"
            "    ws = client.create_websocket()\n"
            "    ws.on_message(callback)\n"
            "    await ws.connect()\n"
            "    await ws.add_realtime(tr_cd='V11', tr_key=..., tr_type='1')\n"
            "    await ws.run()"
        )
