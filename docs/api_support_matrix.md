# API 모의투자 지원 여부

표기:
- ⭕ — 모의투자(`mode: "demo"`) + 실전투자 모두 호출 가능
- ❌ — 실전투자(`mode: "production"`)에서만 호출 가능
  - 특히 **해외선물옵션(`ov_futopt_*`) 그룹 26개는 DB증권 시스템 차원에서 모의투자가 존재하지 않습니다.** demo 모드로 호출 시 `dbsec_helper` / `dbsec_sdk.Config.ws_url_for()` 가 즉시 차단합니다.

---
## 전체 API 매트릭스


바로가기: [OAuth 인증](#oauth-인증) · [공통](#공통) · [국내주식주문](#국내주식주문) · [국내주식시세](#국내주식시세) · [국내주식시세(실시간)](#국내주식시세실시간) · [국내선물옵션주문](#국내선물옵션주문) · [국내선물옵션시세](#국내선물옵션시세) · [국내선물옵션시세(실시간)](#국내선물옵션시세실시간) · [국내주식/선물차트](#국내주식선물차트) · [해외주식주문](#해외주식주문) · [해외주식시세](#해외주식시세) · [해외주식시세(실시간)](#해외주식시세실시간) · [해외선물옵션주문](#해외선물옵션주문) · [해외선물옵션시세](#해외선물옵션시세) · [해외선물옵션시세(실시간)](#해외선물옵션시세실시간) · [장내채권주문](#장내채권주문) · [장내채권시세](#장내채권시세) · [장내채권시세(실시간)](#장내채권시세실시간) · [웹소켓(공통)](#웹소켓공통)

### OAuth 인증

| API 명 | TR 코드 | 메서드 | 모의투자 | TPS |
|---|---|---|:---:|:---:|
| [접근토큰 발급](../examples/auth/token_issue.py) | `token` | [`token_issue`](../dbsec_sdk/apis/auth/endpoints.py#L42) | ⭕ | - |
| [접근토큰 폐기](../examples/auth/token_revoke.py) | `revoke` | [`token_revoke`](../dbsec_sdk/apis/auth/endpoints.py#L86) | ⭕ | - |

### 공통

| API 명 | TR 코드 | 메서드 | 모의투자 | TPS |
|---|---|---|:---:|:---:|
| [관심그룹 종목조회](../examples/common/inquire_issue_groups.py) | `MCJDD88841` | [`inquire_issue_groups`](../dbsec_sdk/apis/common/endpoints.py#L42) | ❌ | 3 |
| [관심종목 그룹조회](../examples/common/inquire_group_list.py) | `MCJDD88840` | [`inquire_group_list`](../dbsec_sdk/apis/common/endpoints.py#L84) | ❌ | 2 |

### 국내주식주문

| API 명 | TR 코드 | 메서드 | 모의투자 | TPS |
|---|---|---|:---:|:---:|
| [주식종합주문](../examples/kr_stock_order/kr_stock_order.py) | `CSPAT00600` | [`kr_stock_order`](../dbsec_sdk/apis/kr_stock_order/endpoints.py#L72) | ⭕ | 10 |
| [주식정정주문](../examples/kr_stock_order/kr_stock_order_modify.py) | `CSPAT00700` | [`kr_stock_order_modify`](../dbsec_sdk/apis/kr_stock_order/endpoints.py#L140) | ⭕ | 3 |
| [주식취소주문](../examples/kr_stock_order/kr_stock_order_cancel.py) | `CSPAT00800` | [`kr_stock_order_cancel`](../dbsec_sdk/apis/kr_stock_order/endpoints.py#L193) | ⭕ | 3 |
| [주식종합주문- NXT거래소](../examples/kr_stock_order/kr_stock_order_nxt.py) | `CSPAT00610` | [`kr_stock_order_nxt`](../dbsec_sdk/apis/kr_stock_order/endpoints.py#L236) | ❌ | 10 |
| [주식정정주문- NXT거래소](../examples/kr_stock_order/kr_stock_order_modify_nxt.py) | `CSPAT00710` | [`kr_stock_order_modify_nxt`](../dbsec_sdk/apis/kr_stock_order/endpoints.py#L302) | ❌ | 3 |
| [주식취소주문- NXT거래소](../examples/kr_stock_order/kr_stock_order_cancel_nxt.py) | `CSPAT00810` | [`kr_stock_order_cancel_nxt`](../dbsec_sdk/apis/kr_stock_order/endpoints.py#L355) | ❌ | 3 |
| [체결/미체결조회](../examples/kr_stock_order/kr_stock_inquire_executions.py) | `CSPAQ04800` | [`kr_stock_inquire_executions`](../dbsec_sdk/apis/kr_stock_order/endpoints.py#L398) | ⭕ | 2 |
| [주식주문가능수량조회](../examples/kr_stock_order/kr_stock_inquire_psbl_quantity.py) | `CSPBQ00100` | [`kr_stock_inquire_psbl_quantity`](../dbsec_sdk/apis/kr_stock_order/endpoints.py#L461) | ⭕ | 2 |
| [주식잔고조회](../examples/kr_stock_order/kr_stock_inquire_balance.py) | `CSPAQ03420` | [`kr_stock_inquire_balance`](../dbsec_sdk/apis/kr_stock_order/endpoints.py#L515) | ⭕ | 2 |
| [당일매매손익 조회](../examples/kr_stock_order/kr_stock_inquire_daily_pnl.py) | `CSPAQ01800` | [`kr_stock_inquire_daily_pnl`](../dbsec_sdk/apis/kr_stock_order/endpoints.py#L564) | ❌ | 2 |
| [계좌예수금조회](../examples/kr_stock_order/kr_stock_inquire_deposit.py) | `CDPCQ00100` | [`kr_stock_inquire_deposit`](../dbsec_sdk/apis/kr_stock_order/endpoints.py#L613) | ⭕ | 1 |
| [일자별매매내역](../examples/kr_stock_order/kr_stock_inquire_daily_trade.py) | `CSPEQ00400` | [`kr_stock_inquire_daily_trade`](../dbsec_sdk/apis/kr_stock_order/endpoints.py#L654) | ⭕ | 1 |
| [임의기간수익률집계](../examples/kr_stock_order/kr_stock_inquire_period_returns.py) | `FOCCQ10800` | [`kr_stock_inquire_period_returns`](../dbsec_sdk/apis/kr_stock_order/endpoints.py#L706) | ❌ | 1 |
| [주식 실현손익조회](../examples/kr_stock_order/kr_stock_inquire_realized_pnl.py) | `CSPAQ07800` | [`kr_stock_inquire_realized_pnl`](../dbsec_sdk/apis/kr_stock_order/endpoints.py#L760) | ❌ | 1 |
| [계좌별신용한도조회](../examples/kr_stock_order/kr_stock_inquire_credit_limit.py) | `CSPAQ00600` | [`kr_stock_inquire_credit_limit`](../dbsec_sdk/apis/kr_stock_order/endpoints.py#L818) | ⭕ | 1 |
| [신용상환가능총수량조회](../examples/kr_stock_order/kr_stock_inquire_credit_repayment.py) | `CSPAQ09400` | [`kr_stock_inquire_credit_repayment`](../dbsec_sdk/apis/kr_stock_order/endpoints.py#L873) | ❌ | 1 |
| [계좌거래내역 조회](../examples/kr_stock_order/kr_stock_inquire_trading_history.py) | `CDPCQ04700` | [`kr_stock_inquire_trading_history`](../dbsec_sdk/apis/kr_stock_order/endpoints.py#L909) | ⭕ | 2 |

### 국내주식시세

| API 명 | TR 코드 | 메서드 | 모의투자 | TPS |
|---|---|---|:---:|:---:|
| [주식종목 조회](../examples/kr_stock_quote/kr_stock_search_stocks.py) | `JCODES` | [`kr_stock_search_stocks`](../dbsec_sdk/apis/kr_stock_quote/endpoints.py#L68) | ⭕ | 3 |
| [ELW 종목 조회](../examples/kr_stock_quote/kr_stock_inquire_elw_stock.py) | `WCODES` | [`kr_stock_inquire_elw_stock`](../dbsec_sdk/apis/kr_stock_quote/endpoints.py#L106) | ⭕ | 3 |
| [국내주식 멀티현재가조회](../examples/kr_stock_quote/kr_stock_inquire_price_multi.py) | `MULTIPRICE` | [`kr_stock_inquire_price_multi`](../dbsec_sdk/apis/kr_stock_quote/endpoints.py#L143) | ⭕ | 2 |
| [현재가조회](../examples/kr_stock_quote/kr_stock_inquire_price.py) | `PRICE` | [`kr_stock_inquire_price`](../dbsec_sdk/apis/kr_stock_quote/endpoints.py#L218) | ⭕ | 5 |
| [호가조회](../examples/kr_stock_quote/kr_stock_inquire_orderbook.py) | `HOGA` | [`kr_stock_inquire_orderbook`](../dbsec_sdk/apis/kr_stock_quote/endpoints.py#L269) | ⭕ | 3 |
| [시간대별체결조회](../examples/kr_stock_quote/kr_stock_inquire_time_execution.py) | `CONCLUSION` | [`kr_stock_inquire_time_execution`](../dbsec_sdk/apis/kr_stock_quote/endpoints.py#L320) | ⭕ | 3 |
| [일별체결조회](../examples/kr_stock_quote/kr_stock_inquire_daily_executions.py) | `DAYTRADE` | [`kr_stock_inquire_daily_executions`](../dbsec_sdk/apis/kr_stock_quote/endpoints.py#L360) | ⭕ | 3 |
| [주식조건상승하락조회](../examples/kr_stock_quote/kr_stock_inquire_condition_rise_fall.py) | `RANKLIST` | [`kr_stock_inquire_condition_rise_fall`](../dbsec_sdk/apis/kr_stock_quote/endpoints.py#L404) | ⭕ | 3 |
| [일별업종별투자자조회](../examples/kr_stock_quote/kr_stock_inquire_daily_industry_investor.py) | `UPTJJDAY` | [`kr_stock_inquire_daily_industry_investor`](../dbsec_sdk/apis/kr_stock_quote/endpoints.py#L453) | ⭕ | 2 |
| [일별종목별투자자조회](../examples/kr_stock_quote/kr_stock_inquire_daily_issue_investor.py) | `DAYSTOCKTJJ` | [`kr_stock_inquire_daily_issue_investor`](../dbsec_sdk/apis/kr_stock_quote/endpoints.py#L510) | ⭕ | 2 |
| [국내 ETF/ETN 구성종목조회](../examples/kr_stock_quote/kr_stock_inquire_etf_etn_stock.py) | `ETFCOMPCODE` | [`kr_stock_inquire_etf_etn_stock`](../dbsec_sdk/apis/kr_stock_quote/endpoints.py#L567) | ⭕ | 2 |
| [섹터분류코드 조회](../examples/kr_stock_quote/kr_stock_inquire_sector_codes.py) | `SECTORCOND` | [`kr_stock_inquire_sector_codes`](../dbsec_sdk/apis/kr_stock_quote/endpoints.py#L612) | ⭕ | 2 |
| [섹터구성종목 조회](../examples/kr_stock_quote/kr_stock_inquire_sector_components.py) | `SECTORCONDLIST` | [`kr_stock_inquire_sector_components`](../dbsec_sdk/apis/kr_stock_quote/endpoints.py#L647) | ⭕ | 2 |
| [업종분류코드 조회](../examples/kr_stock_quote/kr_stock_inquire_industry_codes.py) | `USTOCKCOND` | [`kr_stock_inquire_industry_codes`](../dbsec_sdk/apis/kr_stock_quote/endpoints.py#L696) | ⭕ | 2 |
| [업종구성종목 조회](../examples/kr_stock_quote/kr_stock_inquire_industry_components.py) | `USTOCKCONDLIST` | [`kr_stock_inquire_industry_components`](../dbsec_sdk/apis/kr_stock_quote/endpoints.py#L734) | ⭕ | 2 |

### 국내주식시세(실시간)

| API 명 | TR 코드 | 메서드 | 모의투자 | TPS |
|---|---|---|:---:|:---:|
| [[실시간]주식주문체결 조회](../examples/kr_stock_realtime/kr_stock_realtime_order_execution.py) | `IS1` | [`kr_stock_realtime_order_execution`](../dbsec_sdk/apis/kr_stock_realtime/endpoints.py#L56) | ⭕ | - |
| [[실시간]주식주문접수 조회](../examples/kr_stock_realtime/kr_stock_realtime_order_accept.py) | `IS0` | [`kr_stock_realtime_order_accept`](../dbsec_sdk/apis/kr_stock_realtime/endpoints.py#L81) | ⭕ | - |
| [[실시간]주식호가](../examples/kr_stock_realtime/kr_stock_realtime_orderbook.py) | `S01` | [`kr_stock_realtime_orderbook`](../dbsec_sdk/apis/kr_stock_realtime/endpoints.py#L106) | ⭕ | - |
| [[실시간]주식체결가](../examples/kr_stock_realtime/kr_stock_realtime_execution_price.py) | `S00` | [`kr_stock_realtime_execution_price`](../dbsec_sdk/apis/kr_stock_realtime/endpoints.py#L131) | ⭕ | - |
| [[실시간]ELW호가](../examples/kr_stock_realtime/kr_stock_realtime_elw_orderbook.py) | `W01` | [`kr_stock_realtime_elw_orderbook`](../dbsec_sdk/apis/kr_stock_realtime/endpoints.py#L156) | ⭕ | - |
| [[실시간]ELW체결](../examples/kr_stock_realtime/kr_stock_realtime_elw_execution.py) | `W00` | [`kr_stock_realtime_elw_execution`](../dbsec_sdk/apis/kr_stock_realtime/endpoints.py#L181) | ⭕ | - |
| [[실시간]업종지수체결가](../examples/kr_stock_realtime/kr_stock_realtime_industry_index_execution_price.py) | `U00` | [`kr_stock_realtime_industry_index_execution_price`](../dbsec_sdk/apis/kr_stock_realtime/endpoints.py#L206) | ⭕ | - |
| [[실시간]업종지수등락](../examples/kr_stock_realtime/kr_stock_realtime_industry_index_change.py) | `U03` | [`kr_stock_realtime_industry_index_change`](../dbsec_sdk/apis/kr_stock_realtime/endpoints.py#L231) | ⭕ | - |
| [[실시간]업종별투자자](../examples/kr_stock_realtime/kr_stock_realtime_industry_investor.py) | `U05` | [`kr_stock_realtime_industry_investor`](../dbsec_sdk/apis/kr_stock_realtime/endpoints.py#L256) | ⭕ | - |

### 국내선물옵션주문

| API 명 | TR 코드 | 메서드 | 모의투자 | TPS |
|---|---|---|:---:|:---:|
| [선물옵션 주문](../examples/kr_futopt_order/kr_futopt_order.py) | `CFOAT00100` | [`kr_futopt_order`](../dbsec_sdk/apis/kr_futopt_order/endpoints.py#L66) | ⭕ | 10 |
| [선물옵션 정정주문](../examples/kr_futopt_order/kr_futopt_order_modify.py) | `CFOAT00200` | [`kr_futopt_order_modify`](../dbsec_sdk/apis/kr_futopt_order/endpoints.py#L115) | ⭕ | 10 |
| [선물옵션 취소주문](../examples/kr_futopt_order/kr_futopt_order_cancel.py) | `CFOAT00300` | [`kr_futopt_order_cancel`](../dbsec_sdk/apis/kr_futopt_order/endpoints.py#L162) | ⭕ | 10 |
| [선물옵션 체결조회](../examples/kr_futopt_order/kr_futopt_inquire_executions.py) | `CFOAQ04000` | [`kr_futopt_inquire_executions`](../dbsec_sdk/apis/kr_futopt_order/endpoints.py#L203) | ⭕ | 2 |
| [선물옵션 주문가능수량](../examples/kr_futopt_order/kr_futopt_inquire_psbl_quantity.py) | `CFOAQ42400` | [`kr_futopt_inquire_psbl_quantity`](../dbsec_sdk/apis/kr_futopt_order/endpoints.py#L260) | ⭕ | 2 |
| [선물옵션 잔고 조회](../examples/kr_futopt_order/kr_futopt_inquire_balance.py) | `CFOAQ02500` | [`kr_futopt_inquire_balance`](../dbsec_sdk/apis/kr_futopt_order/endpoints.py#L317) | ⭕ | 2 |
| [선물옵션 잔고_평가현황조회](../examples/kr_futopt_order/kr_futopt_inquire_balance_eval.py) | `CFOAQ50100` | [`kr_futopt_inquire_balance_eval`](../dbsec_sdk/apis/kr_futopt_order/endpoints.py#L359) | ⭕ | 2 |
| [선물옵션 당일실현손익](../examples/kr_futopt_order/kr_futopt_inquire_realized_pnl.py) | `CFOAQ02600` | [`kr_futopt_inquire_realized_pnl`](../dbsec_sdk/apis/kr_futopt_order/endpoints.py#L414) | ⭕ | 1 |
| [선물옵션 가정산예탁금 상세](../examples/kr_futopt_order/kr_futopt_inquire_estimated_deposit.py) | `CFOEQ11100` | [`kr_futopt_inquire_estimated_deposit`](../dbsec_sdk/apis/kr_futopt_order/endpoints.py#L445) | ⭕ | 1 |
| [선물옵션 주문 (야간)](../examples/kr_futopt_order/kr_futopt_order_night.py) | `CFOHT00100` | [`kr_futopt_order_night`](../dbsec_sdk/apis/kr_futopt_order/endpoints.py#L493) | ❌ | 10 |
| [선물옵션 정정주문 (야간)](../examples/kr_futopt_order/kr_futopt_order_modify_night.py) | `CFOHT00200` | [`kr_futopt_order_modify_night`](../dbsec_sdk/apis/kr_futopt_order/endpoints.py#L543) | ❌ | 10 |
| [선물옵션 취소주문 (야간)](../examples/kr_futopt_order/kr_futopt_order_cancel_night.py) | `CFOHT00300` | [`kr_futopt_order_cancel_night`](../dbsec_sdk/apis/kr_futopt_order/endpoints.py#L589) | ❌ | 10 |
| [선물옵션 체결조회 (야간)](../examples/kr_futopt_order/kr_futopt_inquire_executions_night.py) | `CFOHQ04000` | [`kr_futopt_inquire_executions_night`](../dbsec_sdk/apis/kr_futopt_order/endpoints.py#L629) | ❌ | 2 |
| [선물옵션 잔고조회 (야간)](../examples/kr_futopt_order/kr_futopt_inquire_balance_night.py) | `CFOHQ02500` | [`kr_futopt_inquire_balance_night`](../dbsec_sdk/apis/kr_futopt_order/endpoints.py#L686) | ❌ | 2 |

### 국내선물옵션시세

| API 명 | TR 코드 | 메서드 | 모의투자 | TPS |
|---|---|---|:---:|:---:|
| [선물종목 조회](../examples/kr_futopt_quote/kr_futopt_search_futures.py) | `FCODES` | [`kr_futopt_search_futures`](../dbsec_sdk/apis/kr_futopt_quote/endpoints.py#L54) | ⭕ | 3 |
| [옵션종목 조회](../examples/kr_futopt_quote/kr_futopt_search_options.py) | `OCODES` | [`kr_futopt_search_options`](../dbsec_sdk/apis/kr_futopt_quote/endpoints.py#L98) | ⭕ | 10 |
| [국내선옵 멀티현재가 조회](../examples/kr_futopt_quote/kr_futopt_inquire_price_multi.py) | `FOMULTIPRICE` | [`kr_futopt_inquire_price_multi`](../dbsec_sdk/apis/kr_futopt_quote/endpoints.py#L146) | ⭕ | 2 |
| [현재가조회](../examples/kr_futopt_quote/kr_futopt_inquire_price.py) | `FOPRICE` | [`kr_futopt_inquire_price`](../dbsec_sdk/apis/kr_futopt_quote/endpoints.py#L221) | ⭕ | 5 |
| [호가조회](../examples/kr_futopt_quote/kr_futopt_inquire_orderbook.py) | `HOGA` | [`kr_futopt_inquire_orderbook`](../dbsec_sdk/apis/kr_futopt_quote/endpoints.py#L272) | ⭕ | 5 |
| [일별체결조회](../examples/kr_futopt_quote/kr_futopt_inquire_daily_executions.py) | `DAYTRADE` | [`kr_futopt_inquire_daily_executions`](../dbsec_sdk/apis/kr_futopt_quote/endpoints.py#L323) | ⭕ | 2 |
| [시간대별체결조회](../examples/kr_futopt_quote/kr_futopt_inquire_time_execution.py) | `CONCLUSION` | [`kr_futopt_inquire_time_execution`](../dbsec_sdk/apis/kr_futopt_quote/endpoints.py#L367) | ⭕ | 2 |
| [옵션전광판](../examples/kr_futopt_quote/kr_futopt_option_board.py) | `OSTOCK_CONDT` | [`kr_futopt_option_board`](../dbsec_sdk/apis/kr_futopt_quote/endpoints.py#L407) | ⭕ | 1 |

### 국내선물옵션시세(실시간)

| API 명 | TR 코드 | 메서드 | 모의투자 | TPS |
|---|---|---|:---:|:---:|
| [[실시간]선물옵션주문체결](../examples/kr_futopt_realtime/kr_futopt_realtime_order_execution.py) | `IF0` | [`kr_futopt_realtime_order_execution`](../dbsec_sdk/apis/kr_futopt_realtime/endpoints.py#L96) | ⭕ | - |
| [[실시간]지수선물호가](../examples/kr_futopt_realtime/kr_futopt_realtime_index_future_orderbook.py) | `F01` | [`kr_futopt_realtime_index_future_orderbook`](../dbsec_sdk/apis/kr_futopt_realtime/endpoints.py#L121) | ⭕ | - |
| [[실시간]지수선물체결가](../examples/kr_futopt_realtime/kr_futopt_realtime_index_future_execution_price.py) | `F00` | [`kr_futopt_realtime_index_future_execution_price`](../dbsec_sdk/apis/kr_futopt_realtime/endpoints.py#L146) | ⭕ | - |
| [[실시간]미니지수선물호가](../examples/kr_futopt_realtime/kr_futopt_realtime_mini_index_future_orderbook.py) | `F91` | [`kr_futopt_realtime_mini_index_future_orderbook`](../dbsec_sdk/apis/kr_futopt_realtime/endpoints.py#L171) | ⭕ | - |
| [[실시간]미니지수선물체결가](../examples/kr_futopt_realtime/kr_futopt_realtime_mini_index_future_execution_price.py) | `F90` | [`kr_futopt_realtime_mini_index_future_execution_price`](../dbsec_sdk/apis/kr_futopt_realtime/endpoints.py#L196) | ⭕ | - |
| [[실시간]섹터지수선물호가](../examples/kr_futopt_realtime/kr_futopt_realtime_sector_index_future_orderbook.py) | `F71` | [`kr_futopt_realtime_sector_index_future_orderbook`](../dbsec_sdk/apis/kr_futopt_realtime/endpoints.py#L221) | ⭕ | - |
| [[실시간]섹터지수선물체결](../examples/kr_futopt_realtime/kr_futopt_realtime_sector_index_future_execution.py) | `F70` | [`kr_futopt_realtime_sector_index_future_execution`](../dbsec_sdk/apis/kr_futopt_realtime/endpoints.py#L246) | ⭕ | - |
| [[실시간]주식선물호가](../examples/kr_futopt_realtime/kr_futopt_realtime_stock_future_orderbook.py) | `F21` | [`kr_futopt_realtime_stock_future_orderbook`](../dbsec_sdk/apis/kr_futopt_realtime/endpoints.py#L271) | ⭕ | - |
| [[실시간]주식선물체결](../examples/kr_futopt_realtime/kr_futopt_realtime_stock_future_execution.py) | `F20` | [`kr_futopt_realtime_stock_future_execution`](../dbsec_sdk/apis/kr_futopt_realtime/endpoints.py#L296) | ⭕ | - |
| [[실시간]상품선물호가](../examples/kr_futopt_realtime/kr_futopt_realtime_commodity_future_orderbook.py) | `F11` | [`kr_futopt_realtime_commodity_future_orderbook`](../dbsec_sdk/apis/kr_futopt_realtime/endpoints.py#L321) | ⭕ | - |
| [[실시간]상품선물체결가](../examples/kr_futopt_realtime/kr_futopt_realtime_commodity_future_execution_price.py) | `F10` | [`kr_futopt_realtime_commodity_future_execution_price`](../dbsec_sdk/apis/kr_futopt_realtime/endpoints.py#L346) | ⭕ | - |
| [[실시간]지수옵션호가](../examples/kr_futopt_realtime/kr_futopt_realtime_index_option_orderbook.py) | `O01` | [`kr_futopt_realtime_index_option_orderbook`](../dbsec_sdk/apis/kr_futopt_realtime/endpoints.py#L371) | ⭕ | - |
| [[실시간]지수옵션체결](../examples/kr_futopt_realtime/kr_futopt_realtime_index_option_execution.py) | `O00` | [`kr_futopt_realtime_index_option_execution`](../dbsec_sdk/apis/kr_futopt_realtime/endpoints.py#L396) | ⭕ | - |
| [[실시간]주식옵션호가](../examples/kr_futopt_realtime/kr_futopt_realtime_stock_option_orderbook.py) | `O21` | [`kr_futopt_realtime_stock_option_orderbook`](../dbsec_sdk/apis/kr_futopt_realtime/endpoints.py#L421) | ⭕ | - |
| [[실시간]주식옵션체결가](../examples/kr_futopt_realtime/kr_futopt_realtime_stock_option_execution_price.py) | `O20` | [`kr_futopt_realtime_stock_option_execution_price`](../dbsec_sdk/apis/kr_futopt_realtime/endpoints.py#L446) | ⭕ | - |
| [[실시간]미니지수옵션호가](../examples/kr_futopt_realtime/kr_futopt_realtime_mini_index_option_orderbook.py) | `O91` | [`kr_futopt_realtime_mini_index_option_orderbook`](../dbsec_sdk/apis/kr_futopt_realtime/endpoints.py#L471) | ⭕ | - |
| [[실시간]미니지수옵션체결가](../examples/kr_futopt_realtime/kr_futopt_realtime_mini_index_option_execution_price.py) | `O90` | [`kr_futopt_realtime_mini_index_option_execution_price`](../dbsec_sdk/apis/kr_futopt_realtime/endpoints.py#L496) | ⭕ | - |
| [[실시간]K200지수위클리옵션호가](../examples/kr_futopt_realtime/kr_futopt_realtime_k200_weekly_option_orderbook.py) | `OB1` | [`kr_futopt_realtime_k200_weekly_option_orderbook`](../dbsec_sdk/apis/kr_futopt_realtime/endpoints.py#L521) | ⭕ | - |
| [[실시간]K200지수위클리옵션체결](../examples/kr_futopt_realtime/kr_futopt_realtime_k200_weekly_option_execution.py) | `OB0` | [`kr_futopt_realtime_k200_weekly_option_execution`](../dbsec_sdk/apis/kr_futopt_realtime/endpoints.py#L546) | ⭕ | - |
| [[실시간]KOSDAQ150옵션호가](../examples/kr_futopt_realtime/kr_futopt_realtime_kosdaq150_option_orderbook.py) | `OA1` | [`kr_futopt_realtime_kosdaq150_option_orderbook`](../dbsec_sdk/apis/kr_futopt_realtime/endpoints.py#L571) | ⭕ | - |
| [[실시간]KOSDAQ150옵션체결](../examples/kr_futopt_realtime/kr_futopt_realtime_kosdaq150_option_execution.py) | `OA0` | [`kr_futopt_realtime_kosdaq150_option_execution`](../dbsec_sdk/apis/kr_futopt_realtime/endpoints.py#L596) | ⭕ | - |
| [[실시간]선물체결(야간)](../examples/kr_futopt_realtime/kr_futopt_realtime_future_execution_night.py) | `F40` | [`kr_futopt_realtime_future_execution_night`](../dbsec_sdk/apis/kr_futopt_realtime/endpoints.py#L621) | ⭕ | - |
| [[실시간]선물호가(야간)](../examples/kr_futopt_realtime/kr_futopt_realtime_future_orderbook_night.py) | `F41` | [`kr_futopt_realtime_future_orderbook_night`](../dbsec_sdk/apis/kr_futopt_realtime/endpoints.py#L646) | ⭕ | - |
| [[실시간]옵션체결(야간)](../examples/kr_futopt_realtime/kr_futopt_realtime_option_execution_night.py) | `O30` | [`kr_futopt_realtime_option_execution_night`](../dbsec_sdk/apis/kr_futopt_realtime/endpoints.py#L671) | ⭕ | - |
| [[실시간]옵션호가(야간)](../examples/kr_futopt_realtime/kr_futopt_realtime_option_orderbook_night.py) | `O31` | [`kr_futopt_realtime_option_orderbook_night`](../dbsec_sdk/apis/kr_futopt_realtime/endpoints.py#L696) | ⭕ | - |
| [[실시간]미니옵션호가(야간)](../examples/kr_futopt_realtime/kr_futopt_realtime_mini_option_orderbook_night.py) | `E11` | [`kr_futopt_realtime_mini_option_orderbook_night`](../dbsec_sdk/apis/kr_futopt_realtime/endpoints.py#L721) | ⭕ | - |
| [[실시간]미니옵션체결가(야간)](../examples/kr_futopt_realtime/kr_futopt_realtime_mini_option_execution_price_night.py) | `E10` | [`kr_futopt_realtime_mini_option_execution_price_night`](../dbsec_sdk/apis/kr_futopt_realtime/endpoints.py#L746) | ⭕ | - |
| [[실시간]KOSDAQ150옵션체결가(야간)](../examples/kr_futopt_realtime/kr_futopt_realtime_kosdaq150_option_execution_price_night.py) | `E20` | [`kr_futopt_realtime_kosdaq150_option_execution_price_night`](../dbsec_sdk/apis/kr_futopt_realtime/endpoints.py#L771) | ⭕ | - |
| [[실시간]KOSDAQ150옵션호가(야간)](../examples/kr_futopt_realtime/kr_futopt_realtime_kosdaq150_option_orderbook_night.py) | `E21` | [`kr_futopt_realtime_kosdaq150_option_orderbook_night`](../dbsec_sdk/apis/kr_futopt_realtime/endpoints.py#L796) | ⭕ | - |

### 국내주식/선물차트

| API 명 | TR 코드 | 메서드 | 모의투자 | TPS |
|---|---|---|:---:|:---:|
| [틱차트조회](../examples/kr_chart/kr_chart_chart_tick.py) | `CHARTTICK` | [`kr_chart_chart_tick`](../dbsec_sdk/apis/kr_chart/endpoints.py#L48) | ⭕ | 4 |
| [분차트조회](../examples/kr_chart/kr_chart_chart_min.py) | `CHARTMIN` | [`kr_chart_chart_min`](../dbsec_sdk/apis/kr_chart/endpoints.py#L103) | ⭕ | 4 |
| [일차트조회](../examples/kr_chart/kr_chart_chart_day.py) | `CHARTDAY` | [`kr_chart_chart_day`](../dbsec_sdk/apis/kr_chart/endpoints.py#L158) | ⭕ | 4 |
| [주차트조회](../examples/kr_chart/kr_chart_chart_week.py) | `CHARTWEEK` | [`kr_chart_chart_week`](../dbsec_sdk/apis/kr_chart/endpoints.py#L210) | ⭕ | 4 |
| [월차트조회](../examples/kr_chart/kr_chart_chart_month.py) | `CHARTMONTH` | [`kr_chart_chart_month`](../dbsec_sdk/apis/kr_chart/endpoints.py#L265) | ⭕ | 4 |

### 해외주식주문

| API 명 | TR 코드 | 메서드 | 모의투자 | TPS |
|---|---|---|:---:|:---:|
| [해외주식 주문](../examples/ov_stock_order/ov_stock_order.py) | `CAZCT00100` | [`ov_stock_order`](../dbsec_sdk/apis/ov_stock_order/endpoints.py#L56) | ⭕ | 10 |
| [해외주식 체결내역조회](../examples/ov_stock_order/ov_stock_inquire_executions.py) | `CAZCQ00100` | [`ov_stock_inquire_executions`](../dbsec_sdk/apis/ov_stock_order/endpoints.py#L135) | ⭕ | 2 |
| [해외주식 잔고/증거금 조회](../examples/ov_stock_order/ov_stock_inquire_balance_margin.py) | `CAZCQ00400` | [`ov_stock_inquire_balance_margin`](../dbsec_sdk/apis/ov_stock_order/endpoints.py#L211) | ⭕ | 3 |
| [해외주식 매매내역 조회](../examples/ov_stock_order/ov_stock_inquire_trade_history.py) | `CAZCQ00200` | [`ov_stock_inquire_trade_history`](../dbsec_sdk/apis/ov_stock_order/endpoints.py#L270) | ⭕ | 2 |
| [해외주식 거래내역 조회](../examples/ov_stock_order/ov_stock_inquire_trading_history.py) | `CAZCQ01600` | [`ov_stock_inquire_trading_history`](../dbsec_sdk/apis/ov_stock_order/endpoints.py#L343) | ⭕ | 2 |
| [해외주식 주문가능금액조회](../examples/ov_stock_order/ov_stock_inquire_psbl_amount.py) | `CAZCQ01300` | [`ov_stock_inquire_psbl_amount`](../dbsec_sdk/apis/ov_stock_order/endpoints.py#L407) | ⭕ | 2 |
| [해외주식 실현손익 조회](../examples/ov_stock_order/ov_stock_inquire_realized_pnl.py) | `CAZCQ00300` | [`ov_stock_inquire_realized_pnl`](../dbsec_sdk/apis/ov_stock_order/endpoints.py#L459) | ⭕ | 2 |
| [해외주식 예수금상세](../examples/ov_stock_order/ov_stock_inquire_deposit_detail.py) | `CAZCQ01400` | [`ov_stock_inquire_deposit_detail`](../dbsec_sdk/apis/ov_stock_order/endpoints.py#L526) | ⭕ | 2 |
| [해외주식 평균매입단가 조회](../examples/ov_stock_order/ov_stock_inquire_avg_buy_price.py) | `CAZCQ03400` | [`ov_stock_inquire_avg_buy_price`](../dbsec_sdk/apis/ov_stock_order/endpoints.py#L567) | ❌ | 2 |

### 해외주식시세

| API 명 | TR 코드 | 메서드 | 모의투자 | TPS |
|---|---|---|:---:|:---:|
| [해외주식종목 조회](../examples/ov_stock_quote/ov_stock_search_stocks.py) | `FSTKCODES` | [`ov_stock_search_stocks`](../dbsec_sdk/apis/ov_stock_quote/endpoints.py#L60) | ⭕ | 2 |
| [해외주식 멀티현재가조회](../examples/ov_stock_quote/ov_stock_inquire_price_multi.py) | `FSTKMULTIPRICE` | [`ov_stock_inquire_price_multi`](../dbsec_sdk/apis/ov_stock_quote/endpoints.py#L99) | ⭕ | 2 |
| [해외주식현재가조회](../examples/ov_stock_quote/ov_stock_inquire_price.py) | `FSTKPRICE` | [`ov_stock_inquire_price`](../dbsec_sdk/apis/ov_stock_quote/endpoints.py#L174) | ⭕ | 2 |
| [해외주식호가조회](../examples/ov_stock_quote/ov_stock_inquire_orderbook.py) | `FSTKHOGA` | [`ov_stock_inquire_orderbook`](../dbsec_sdk/apis/ov_stock_quote/endpoints.py#L225) | ⭕ | 2 |
| [해외주식시간대별체결조회](../examples/ov_stock_quote/ov_stock_inquire_time_execution.py) | `FSTKCONCLUSION` | [`ov_stock_inquire_time_execution`](../dbsec_sdk/apis/ov_stock_quote/endpoints.py#L276) | ⭕ | 2 |
| [해외주식 틱차트조회](../examples/ov_stock_quote/ov_stock_chart_tick.py) | `FSTKCHARTTICK` | [`ov_stock_chart_tick`](../dbsec_sdk/apis/ov_stock_quote/endpoints.py#L325) | ⭕ | 4 |
| [해외주식 분차트조회](../examples/ov_stock_quote/ov_stock_chart_min.py) | `FSTKCHARTMIN` | [`ov_stock_chart_min`](../dbsec_sdk/apis/ov_stock_quote/endpoints.py#L389) | ⭕ | 4 |
| [해외주식 일차트조회](../examples/ov_stock_quote/ov_stock_chart_day.py) | `FSTKCHARTDAY` | [`ov_stock_chart_day`](../dbsec_sdk/apis/ov_stock_quote/endpoints.py#L453) | ⭕ | 4 |
| [해외주식 주차트조회](../examples/ov_stock_quote/ov_stock_chart_week.py) | `FSTKCHARTWEEK` | [`ov_stock_chart_week`](../dbsec_sdk/apis/ov_stock_quote/endpoints.py#L505) | ⭕ | 4 |
| [해외주식 월차트조회](../examples/ov_stock_quote/ov_stock_chart_month.py) | `FSTKCHARTMONTH` | [`ov_stock_chart_month`](../dbsec_sdk/apis/ov_stock_quote/endpoints.py#L560) | ⭕ | 4 |
| [해외주식 상승하락조회](../examples/ov_stock_quote/ov_stock_inquire_condition_rise_fall.py) | `FSTKRANKLIST` | [`ov_stock_inquire_condition_rise_fall`](../dbsec_sdk/apis/ov_stock_quote/endpoints.py#L612) | ⭕ | 2 |

### 해외주식시세(실시간)

| API 명 | TR 코드 | 메서드 | 모의투자 | TPS |
|---|---|---|:---:|:---:|
| [[실시간]해외주식 주문체결 조회](../examples/ov_stock_realtime/ov_stock_realtime_order_execution.py) | `IS2` | [`ov_stock_realtime_order_execution`](../dbsec_sdk/apis/ov_stock_realtime/endpoints.py#L48) | ⭕ | - |
| [[실시간]해외주식 체결가](../examples/ov_stock_realtime/ov_stock_realtime_execution_price.py) | `V60` | [`ov_stock_realtime_execution_price`](../dbsec_sdk/apis/ov_stock_realtime/endpoints.py#L73) | ⭕ | - |
| [[실시간]해외주식 호가](../examples/ov_stock_realtime/ov_stock_realtime_orderbook.py) | `V61` | [`ov_stock_realtime_orderbook`](../dbsec_sdk/apis/ov_stock_realtime/endpoints.py#L102) | ⭕ | - |
| [[실시간]해외주식 지연체결가](../examples/ov_stock_realtime/ov_stock_realtime_delayed_execution_price.py) | `V10` | [`ov_stock_realtime_delayed_execution_price`](../dbsec_sdk/apis/ov_stock_realtime/endpoints.py#L131) | ⭕ | - |
| [[실시간]해외주식 지연호가](../examples/ov_stock_realtime/ov_stock_realtime_delayed_orderbook.py) | `V11` | [`ov_stock_realtime_delayed_orderbook`](../dbsec_sdk/apis/ov_stock_realtime/endpoints.py#L159) | ⭕ | - |

### 해외선물옵션주문

| API 명 | TR 코드 | 메서드 | 모의투자 | TPS |
|---|---|---|:---:|:---:|
| [해외선옵 주문](../examples/ov_futopt_order/ov_futopt_order.py) | `ph700101o` | [`ov_futopt_order`](../dbsec_sdk/apis/ov_futopt_order/endpoints.py#L62) | ❌ | 10 |
| [해외선옵 정정/취소주문](../examples/ov_futopt_order/ov_futopt_order_cancel.py) | `ph700201o` | [`ov_futopt_order_cancel`](../dbsec_sdk/apis/ov_futopt_order/endpoints.py#L126) | ❌ | 5 |
| [주문가능수량조회](../examples/ov_futopt_order/ov_futopt_inquire_psbl_quantity.py) | `ph710201o` | [`ov_futopt_inquire_psbl_quantity`](../dbsec_sdk/apis/ov_futopt_order/endpoints.py#L183) | ❌ | 2 |
| [상품별증거금조회](../examples/ov_futopt_order/ov_futopt_inquire_margin_by_product.py) | `ph800404o` | [`ov_futopt_inquire_margin_by_product`](../dbsec_sdk/apis/ov_futopt_order/endpoints.py#L232) | ❌ | 2 |
| [주문내역조회](../examples/ov_futopt_order/ov_futopt_inquire_orders.py) | `ph020101o` | [`ov_futopt_inquire_orders`](../dbsec_sdk/apis/ov_futopt_order/endpoints.py#L276) | ❌ | 2 |
| [체결내역 조회](../examples/ov_futopt_order/ov_futopt_inquire_executions.py) | `ph020301o` | [`ov_futopt_inquire_executions`](../dbsec_sdk/apis/ov_futopt_order/endpoints.py#L316) | ❌ | 2 |
| [미체결내역 조회](../examples/ov_futopt_order/ov_futopt_inquire_unfilled.py) | `ph020201o` | [`ov_futopt_inquire_unfilled`](../dbsec_sdk/apis/ov_futopt_order/endpoints.py#L366) | ❌ | 2 |
| [미결제 약정 조회](../examples/ov_futopt_order/ov_futopt_inquire_open_interest.py) | `ph020401o` | [`ov_futopt_inquire_open_interest`](../dbsec_sdk/apis/ov_futopt_order/endpoints.py#L419) | ❌ | 2 |
| [일별 미결제 약정내역](../examples/ov_futopt_order/ov_futopt_inquire_daily_open_interest.py) | `ph131101o` | [`ov_futopt_inquire_daily_open_interest`](../dbsec_sdk/apis/ov_futopt_order/endpoints.py#L472) | ❌ | 2 |
| [예탁잔고현황](../examples/ov_futopt_order/ov_futopt_inquire_deposit_balance.py) | `ph131601o` | [`ov_futopt_inquire_deposit_balance`](../dbsec_sdk/apis/ov_futopt_order/endpoints.py#L518) | ❌ | 2 |
| [예탁자산현황](../examples/ov_futopt_order/ov_futopt_inquire_deposit_assets.py) | `ph131501o` | [`ov_futopt_inquire_deposit_assets`](../dbsec_sdk/apis/ov_futopt_order/endpoints.py#L566) | ❌ | 2 |
| [기간별 거래내역 조회](../examples/ov_futopt_order/ov_futopt_inquire_trading_history.py) | `ph135102o` | [`ov_futopt_inquire_trading_history`](../dbsec_sdk/apis/ov_futopt_order/endpoints.py#L614) | ❌ | 2 |

### 해외선물옵션시세

| API 명 | TR 코드 | 메서드 | 모의투자 | TPS |
|---|---|---|:---:|:---:|
| [호가 & 현재가 조회](../examples/ov_futopt_quote/ov_futopt_inquire_orderbook_price.py) | `pibo7042` | [`ov_futopt_inquire_orderbook_price`](../dbsec_sdk/apis/ov_futopt_quote/endpoints.py#L54) | ❌ | 2 |
| [일자별 시세추이](../examples/ov_futopt_quote/ov_futopt_daily_price_trend.py) | `pibo7044` | [`ov_futopt_daily_price_trend`](../dbsec_sdk/apis/ov_futopt_quote/endpoints.py#L103) | ❌ | 2 |
| [해외선물 틱차트조회](../examples/ov_futopt_quote/ov_futopt_future_chart_tick.py) | `pibg7301` | [`ov_futopt_future_chart_tick`](../dbsec_sdk/apis/ov_futopt_quote/endpoints.py#L152) | ❌ | 10 |
| [해외선물 분차트조회](../examples/ov_futopt_quote/ov_futopt_future_chart_min.py) | `pibg7302` | [`ov_futopt_future_chart_min`](../dbsec_sdk/apis/ov_futopt_quote/endpoints.py#L210) | ❌ | 2 |
| [해외선물 일주월차트조회](../examples/ov_futopt_quote/ov_futopt_future_chart_day_week_month.py) | `pibg7303` | [`ov_futopt_future_chart_day_week_month`](../dbsec_sdk/apis/ov_futopt_quote/endpoints.py#L268) | ❌ | 2 |
| [해외옵션 틱차트조회](../examples/ov_futopt_quote/ov_futopt_option_chart_tick.py) | `pibg7401` | [`ov_futopt_option_chart_tick`](../dbsec_sdk/apis/ov_futopt_quote/endpoints.py#L324) | ❌ | 10 |
| [해외옵션 분차트조회](../examples/ov_futopt_quote/ov_futopt_option_chart_min.py) | `pibg7402` | [`ov_futopt_option_chart_min`](../dbsec_sdk/apis/ov_futopt_quote/endpoints.py#L382) | ❌ | 2 |
| [해외옵션 일주월차트조회](../examples/ov_futopt_quote/ov_futopt_option_chart_day_week_month.py) | `pibg7403` | [`ov_futopt_option_chart_day_week_month`](../dbsec_sdk/apis/ov_futopt_quote/endpoints.py#L440) | ❌ | 2 |

### 해외선물옵션시세(실시간)

| API 명 | TR 코드 | 메서드 | 모의투자 | TPS |
|---|---|---|:---:|:---:|
| [[실시간]주문체결](../examples/ov_futopt_realtime/ov_futopt_realtime_order_execution.py) | `O` | [`ov_futopt_realtime_order_execution`](../dbsec_sdk/apis/ov_futopt_realtime/endpoints.py#L50) | ❌ | - |
| [[실시간]잔고](../examples/ov_futopt_realtime/ov_futopt_realtime_balance.py) | `P` | [`ov_futopt_realtime_balance`](../dbsec_sdk/apis/ov_futopt_realtime/endpoints.py#L75) | ❌ | - |
| [[실시간]해외선물호가](../examples/ov_futopt_realtime/ov_futopt_realtime_future_orderbook.py) | `L01` | [`ov_futopt_realtime_future_orderbook`](../dbsec_sdk/apis/ov_futopt_realtime/endpoints.py#L100) | ❌ | - |
| [[실시간]해외선물시세](../examples/ov_futopt_realtime/ov_futopt_realtime_future_quote.py) | `K01` | [`ov_futopt_realtime_future_quote`](../dbsec_sdk/apis/ov_futopt_realtime/endpoints.py#L128) | ❌ | - |
| [[실시간]해외옵션시세](../examples/ov_futopt_realtime/ov_futopt_realtime_option_quote.py) | `K02` | [`ov_futopt_realtime_option_quote`](../dbsec_sdk/apis/ov_futopt_realtime/endpoints.py#L156) | ❌ | - |
| [[실시간]해외옵션호가](../examples/ov_futopt_realtime/ov_futopt_realtime_option_orderbook.py) | `L02` | [`ov_futopt_realtime_option_orderbook`](../dbsec_sdk/apis/ov_futopt_realtime/endpoints.py#L184) | ❌ | - |

### 장내채권주문

| API 명 | TR 코드 | 메서드 | 모의투자 | TPS |
|---|---|---|:---:|:---:|
| [채권매수주문](../examples/bond_order/bond_order.py) | `CSPAT02000` | [`bond_order_buy`](../dbsec_sdk/apis/bond_order/endpoints.py#L50) | ❌ | 5 |
| [채권정정주문](../examples/bond_order/bond_order_modify.py) | `CSPAT02100` | [`bond_order_modify`](../dbsec_sdk/apis/bond_order/endpoints.py#L115) | ❌ | 5 |
| [채권취소주문](../examples/bond_order/bond_order_cancel.py) | `CSPAT02200` | [`bond_order_cancel`](../dbsec_sdk/apis/bond_order/endpoints.py#L157) | ❌ | 5 |
| [채권주문체결조회](../examples/bond_order/bond_inquire_executions.py) | `CSPAQ05700` | [`bond_inquire_executions`](../dbsec_sdk/apis/bond_order/endpoints.py#L196) | ❌ | 2 |
| [채권잔고조회](../examples/bond_order/bond_inquire_balance.py) | `CSPAQ01200` | [`bond_inquire_balance`](../dbsec_sdk/apis/bond_order/endpoints.py#L253) | ❌ | 2 |
| [채권잔고평가조회](../examples/bond_order/bond_inquire_balance_eval.py) | `CSPAQ07900` | [`bond_inquire_balance_eval`](../dbsec_sdk/apis/bond_order/endpoints.py#L290) | ❌ | 2 |

### 장내채권시세

| API 명 | TR 코드 | 메서드 | 모의투자 | TPS |
|---|---|---|:---:|:---:|
| [장내채권 상세검색](../examples/bond_quote/bond_search_detail.py) | `BO_SEARCH` | [`bond_search_detail`](../dbsec_sdk/apis/bond_quote/endpoints.py#L44) | ❌ | 2 |
| [장내채권 현재가조회](../examples/bond_quote/bond_inquire_price.py) | `BO_SISE` | [`bond_inquire_price`](../dbsec_sdk/apis/bond_quote/endpoints.py#L106) | ❌ | 2 |
| [장내채권 호가 조회](../examples/bond_quote/bond_inquire_orderbook.py) | `BO_HOGA` | [`bond_inquire_orderbook`](../dbsec_sdk/apis/bond_quote/endpoints.py#L148) | ❌ | 2 |

### 장내채권시세(실시간)

| API 명 | TR 코드 | 메서드 | 모의투자 | TPS |
|---|---|---|:---:|:---:|
| [[실시간]일반채권체결](../examples/bond_realtime/bond_realtime_normal_execution.py) | `B00` | [`bond_realtime_normal_execution`](../dbsec_sdk/apis/bond_realtime/endpoints.py#L46) | ❌ | - |
| [[실시간]일반채권호가](../examples/bond_realtime/bond_realtime_normal_orderbook.py) | `B01` | [`bond_realtime_normal_orderbook`](../dbsec_sdk/apis/bond_realtime/endpoints.py#L71) | ❌ | - |
| [[실시간]소액채권체결](../examples/bond_realtime/bond_realtime_small_execution.py) | `B10` | [`bond_realtime_small_execution`](../dbsec_sdk/apis/bond_realtime/endpoints.py#L96) | ❌ | - |
| [[실시간]소액채권호가](../examples/bond_realtime/bond_realtime_small_orderbook.py) | `B11` | [`bond_realtime_small_orderbook`](../dbsec_sdk/apis/bond_realtime/endpoints.py#L121) | ❌ | - |

### 웹소켓(공통)

| API 명 | TR 코드 | 메서드 | 모의투자 | TPS |
|---|---|---|:---:|:---:|
| [웹소켓 세션 초기화](../examples/ws_common/ws_session_disconnect.py) | `DisconnectSession` | [`ws_session_disconnect`](../dbsec_sdk/apis/ws_common/endpoints.py#L40) | ⭕ | 1 |
