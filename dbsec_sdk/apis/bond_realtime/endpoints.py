"""장내채권시세(실시간) API 모듈.

DB증권 OpenAPI 그룹: 장내채권시세(실시간)
group_slug: bond_realtime

이 파일은 `_specs/bond_realtime/*.json` 에서 자동 생성되었습니다.
스펙이 갱신되면 `_workspace/build_modules.py`로 재생성하세요.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from dbsec_sdk.client import DBSecClient

from dbsec_sdk.response import APIResponse


class BondRealtimeAPI:
    """장내채권시세(실시간) API 모음.

    사용법:
        >>> client = DBSecClient("config.yaml")
        >>> resp = client.apis.bond_realtime.<method>(...)
    """

    # API 경로 매핑
    PATHS = {
        'bond_realtime_normal_execution': '/pub/B00',
        'bond_realtime_normal_orderbook': '/pub/B01',
        'bond_realtime_small_execution': '/pub/B10',
        'bond_realtime_small_orderbook': '/pub/B11',
    }
    # TR 코드 매핑
    TR_CODES = {
        'bond_realtime_normal_execution': 'B00',
        'bond_realtime_normal_orderbook': 'B01',
        'bond_realtime_small_execution': 'B10',
        'bond_realtime_small_orderbook': 'B11',
    }

    def __init__(self, client: 'DBSecClient'):
        self._client = client

    def bond_realtime_normal_execution(self, *, body: dict, cont_yn: str = 'N', cont_key: str = '') -> APIResponse:
        """[실시간]일반채권체결 (B00).

        일반채권 실시간 체결가 API 입니다.

        Args:
            body: 요청 JSON body (TR별 InBlock 형식).
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. resp.body 에 응답 데이터 포함.
        TR코드: B00   TPS: 2
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=9d49d2cf-5ec2-49f4-b032-e5ea0bdb50d6&api_id=06f92550-04ce-4574-8278-90389ea1fa84
        """
        raise NotImplementedError(
            "이 API 는 실시간 WebSocket TR 입니다 (tr_cd='B00'). REST 호출이 아닙니다.\n"
            "사용 예:\n"
            "    ws = client.create_websocket()\n"
            "    ws.on_message(callback)\n"
            "    await ws.connect()\n"
            "    await ws.add_realtime(tr_cd='B00', tr_key=..., tr_type='1')\n"
            "    await ws.run()"
        )

    def bond_realtime_normal_orderbook(self, *, body: dict, cont_yn: str = 'N', cont_key: str = '') -> APIResponse:
        """[실시간]일반채권호가 (B01).

        일반채권 실시간 호가 API 입니다.

        Args:
            body: 요청 JSON body (TR별 InBlock 형식).
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. resp.body 에 응답 데이터 포함.
        TR코드: B01   TPS: 2
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=9d49d2cf-5ec2-49f4-b032-e5ea0bdb50d6&api_id=ec62334a-6150-4a29-89b0-193a2d8e35f4
        """
        raise NotImplementedError(
            "이 API 는 실시간 WebSocket TR 입니다 (tr_cd='B01'). REST 호출이 아닙니다.\n"
            "사용 예:\n"
            "    ws = client.create_websocket()\n"
            "    ws.on_message(callback)\n"
            "    await ws.connect()\n"
            "    await ws.add_realtime(tr_cd='B01', tr_key=..., tr_type='1')\n"
            "    await ws.run()"
        )

    def bond_realtime_small_execution(self, *, body: dict, cont_yn: str = 'N', cont_key: str = '') -> APIResponse:
        """[실시간]소액채권체결 (B10).

        소액채권 실시간 체결가 API 입니다.

        Args:
            body: 요청 JSON body (TR별 InBlock 형식).
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. resp.body 에 응답 데이터 포함.
        TR코드: B10   TPS: 2
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=9d49d2cf-5ec2-49f4-b032-e5ea0bdb50d6&api_id=2f0f7b1a-b0f6-44f9-971a-ab53e1716f29
        """
        raise NotImplementedError(
            "이 API 는 실시간 WebSocket TR 입니다 (tr_cd='B10'). REST 호출이 아닙니다.\n"
            "사용 예:\n"
            "    ws = client.create_websocket()\n"
            "    ws.on_message(callback)\n"
            "    await ws.connect()\n"
            "    await ws.add_realtime(tr_cd='B10', tr_key=..., tr_type='1')\n"
            "    await ws.run()"
        )

    def bond_realtime_small_orderbook(self, *, body: dict, cont_yn: str = 'N', cont_key: str = '') -> APIResponse:
        """[실시간]소액채권호가 (B11).

        소액채권 실시간 호가 API 입니다.

        Args:
            body: 요청 JSON body (TR별 InBlock 형식).
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. resp.body 에 응답 데이터 포함.
        TR코드: B11   TPS: 2
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=9d49d2cf-5ec2-49f4-b032-e5ea0bdb50d6&api_id=e5fd7bfc-2204-4203-b683-a32879056f20
        """
        raise NotImplementedError(
            "이 API 는 실시간 WebSocket TR 입니다 (tr_cd='B11'). REST 호출이 아닙니다.\n"
            "사용 예:\n"
            "    ws = client.create_websocket()\n"
            "    ws.on_message(callback)\n"
            "    await ws.connect()\n"
            "    await ws.add_realtime(tr_cd='B11', tr_key=..., tr_type='1')\n"
            "    await ws.run()"
        )
