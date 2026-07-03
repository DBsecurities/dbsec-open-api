"""DB증권 OpenAPI 그룹 레지스트리.

client.apis.<group_slug> 로 접근 가능한 API 집합.

조회 그룹(시세/주문조회/차트)은 _PagingProxy 로 감싸 모든 메서드에 fetch_all/max_pages
키워드를 더한다 — 단건은 그대로, fetch_all=True 면 연속조회를 끝까지 병합한다.
endpoints 자동생성 코드는 건드리지 않으며, property 반환 타입을 원본 클래스로 선언해
단건 호출의 타입힌트(인자 자동완성)를 보존한다. (실시간/인증/웹소켓 그룹은 페이징
개념이 없어 프록시 대상에서 제외.)
"""
from __future__ import annotations

import functools
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from dbsec_sdk.client import DBSecClient

from dbsec_sdk.apis.auth.endpoints import AuthAPI
from dbsec_sdk.apis.common.endpoints import CommonAPI
from dbsec_sdk.apis.kr_stock_order.endpoints import KrStockOrderAPI
from dbsec_sdk.apis.kr_stock_quote.endpoints import KrStockQuoteAPI
from dbsec_sdk.apis.kr_stock_realtime.endpoints import KrStockRealtimeAPI
from dbsec_sdk.apis.kr_futopt_order.endpoints import KrFutoptOrderAPI
from dbsec_sdk.apis.kr_futopt_quote.endpoints import KrFutoptQuoteAPI
from dbsec_sdk.apis.kr_futopt_realtime.endpoints import KrFutoptRealtimeAPI
from dbsec_sdk.apis.kr_chart.endpoints import KrChartAPI
from dbsec_sdk.apis.ov_stock_order.endpoints import OvStockOrderAPI
from dbsec_sdk.apis.ov_stock_quote.endpoints import OvStockQuoteAPI
from dbsec_sdk.apis.ov_stock_realtime.endpoints import OvStockRealtimeAPI
from dbsec_sdk.apis.ov_futopt_order.endpoints import OvFutoptOrderAPI
from dbsec_sdk.apis.ov_futopt_quote.endpoints import OvFutoptQuoteAPI
from dbsec_sdk.apis.ov_futopt_realtime.endpoints import OvFutoptRealtimeAPI
from dbsec_sdk.apis.bond_order.endpoints import BondOrderAPI
from dbsec_sdk.apis.bond_quote.endpoints import BondQuoteAPI
from dbsec_sdk.apis.bond_realtime.endpoints import BondRealtimeAPI
from dbsec_sdk.apis.ws_common.endpoints import WsCommonAPI


class _PagingProxy:
    """그룹 API 프록시 — 조회 메서드에 fetch_all/max_pages 키워드를 더한다.

    - fetch_all=False (기본): 단건 호출을 원본 메서드로 그대로 위임 (동작·타입힌트 동일).
    - fetch_all=True: 연속조회를 서버가 끝(cont_yn != 'Y')을 알릴 때까지(또는 max_pages 까지)
      받아 하나의 APIResponse 로 병합 (client.fetch_all 위임).

    예:
        # 단건
        resp = await client.apis.kr_stock_quote.kr_stock_inquire_price(
            InputCondMrktDivCode="J", InputIscd1="005930")
        # 전체(연속조회 자동 병합)
        resp = await client.apis.kr_stock_quote.kr_stock_inquire_condition_rise_fall(
            InputDateClsCode="0", InputRankSortClsCode1="12",
            InputMrktClsCode="K", InputBstpIscd="1001",
            fetch_all=True, max_pages=2)

    endpoints 자동생성 코드는 건드리지 않는다.
    """
    __slots__ = ("_api", "_client")

    def __init__(self, api: object, client: "DBSecClient"):
        self._api = api
        self._client = client

    def __getattr__(self, name: str):
        attr = getattr(self._api, name)
        if not callable(attr):
            return attr  # PATHS/TR_CODES 등 비메서드 속성은 그대로 노출
        client = self._client

        @functools.wraps(attr)
        def method(*, fetch_all: bool = False, max_pages: int | None = None,
                   page_delay: float = 0.0, start_cont_key: str = "", **params):
            if fetch_all:
                return client.fetch_all(
                    attr, max_pages=max_pages, page_delay=page_delay,
                    start_cont_key=start_cont_key, **params,
                )
            return attr(**params)

        return method


class APIRegistry:
    """그룹 API 레지스트리. DBSecClient.apis 속성으로 노출."""

    def __init__(self, client: 'DBSecClient'):
        self._client = client

    def _paged(self, key: str, cls):
        """조회 그룹을 _PagingProxy 로 감싸 캐시·반환 (fetch_all/max_pages 지원)."""
        cache = '_grp_' + key
        if not hasattr(self, cache):
            setattr(self, cache, _PagingProxy(cls(self._client), self._client))
        return getattr(self, cache)

    # ── 조회 그룹 (fetch_all/max_pages 지원, _PagingProxy 래핑) ──
    @property
    def common(self) -> CommonAPI:
        """공통."""
        return self._paged('common', CommonAPI)

    @property
    def kr_stock_order(self) -> KrStockOrderAPI:
        """국내주식주문."""
        return self._paged('kr_stock_order', KrStockOrderAPI)

    @property
    def kr_stock_quote(self) -> KrStockQuoteAPI:
        """국내주식시세."""
        return self._paged('kr_stock_quote', KrStockQuoteAPI)

    @property
    def kr_futopt_order(self) -> KrFutoptOrderAPI:
        """국내선물옵션주문."""
        return self._paged('kr_futopt_order', KrFutoptOrderAPI)

    @property
    def kr_futopt_quote(self) -> KrFutoptQuoteAPI:
        """국내선물옵션시세."""
        return self._paged('kr_futopt_quote', KrFutoptQuoteAPI)

    @property
    def kr_chart(self) -> KrChartAPI:
        """국내주식/선물차트."""
        return self._paged('kr_chart', KrChartAPI)

    @property
    def ov_stock_order(self) -> OvStockOrderAPI:
        """해외주식주문."""
        return self._paged('ov_stock_order', OvStockOrderAPI)

    @property
    def ov_stock_quote(self) -> OvStockQuoteAPI:
        """해외주식시세."""
        return self._paged('ov_stock_quote', OvStockQuoteAPI)

    @property
    def ov_futopt_order(self) -> OvFutoptOrderAPI:
        """해외선물옵션주문."""
        return self._paged('ov_futopt_order', OvFutoptOrderAPI)

    @property
    def ov_futopt_quote(self) -> OvFutoptQuoteAPI:
        """해외선물옵션시세."""
        return self._paged('ov_futopt_quote', OvFutoptQuoteAPI)

    @property
    def bond_order(self) -> BondOrderAPI:
        """장내채권주문."""
        return self._paged('bond_order', BondOrderAPI)

    @property
    def bond_quote(self) -> BondQuoteAPI:
        """장내채권시세."""
        return self._paged('bond_quote', BondQuoteAPI)

    # ── 비조회 그룹 (페이징 개념 없음 — 원본 인스턴스 그대로) ──
    @property
    def auth(self) -> AuthAPI:
        """OAuth 인증."""
        if not hasattr(self, '_auth'):
            self._auth = AuthAPI(self._client)
        return self._auth

    @property
    def kr_stock_realtime(self) -> KrStockRealtimeAPI:
        """국내주식시세(실시간)."""
        if not hasattr(self, '_kr_stock_realtime'):
            self._kr_stock_realtime = KrStockRealtimeAPI(self._client)
        return self._kr_stock_realtime

    @property
    def kr_futopt_realtime(self) -> KrFutoptRealtimeAPI:
        """국내선물옵션시세(실시간)."""
        if not hasattr(self, '_kr_futopt_realtime'):
            self._kr_futopt_realtime = KrFutoptRealtimeAPI(self._client)
        return self._kr_futopt_realtime

    @property
    def ov_stock_realtime(self) -> OvStockRealtimeAPI:
        """해외주식시세(실시간)."""
        if not hasattr(self, '_ov_stock_realtime'):
            self._ov_stock_realtime = OvStockRealtimeAPI(self._client)
        return self._ov_stock_realtime

    @property
    def ov_futopt_realtime(self) -> OvFutoptRealtimeAPI:
        """해외선물옵션시세(실시간)."""
        if not hasattr(self, '_ov_futopt_realtime'):
            self._ov_futopt_realtime = OvFutoptRealtimeAPI(self._client)
        return self._ov_futopt_realtime

    @property
    def bond_realtime(self) -> BondRealtimeAPI:
        """장내채권시세(실시간)."""
        if not hasattr(self, '_bond_realtime'):
            self._bond_realtime = BondRealtimeAPI(self._client)
        return self._bond_realtime

    @property
    def ws_common(self) -> WsCommonAPI:
        """웹소켓(공통)."""
        if not hasattr(self, '_ws_common'):
            self._ws_common = WsCommonAPI(self._client)
        return self._ws_common
