# API 모의투자 지원 여부

표기:
- ⭕ — 모의투자(`mode: "demo"`) + 실전투자 모두 호출 가능
- ❌ — 실전투자(`mode: "production"`)에서만 호출 가능
  - 특히 **해외선물옵션(`ov_futopt_*`) 그룹 26개는 DB증권 시스템 차원에서 모의투자가 존재하지 않습니다.** demo 모드로 호출 시 `dbsec_helper` / `dbsec_sdk.Config.ws_url_for()` 가 즉시 차단합니다.

---
## 전체 API 매트릭스

| 구분 | API 명 | TR 코드 | 메서드 | 모의투자 | TPS |
|---|---|---|---|:---:|:---:|
| OAuth 인증 | 접근토큰 발급 | `token` | `token_issue` | ⭕ | - |
| OAuth 인증 | 접근토큰 폐기 | `revoke` | `token_revoke` | ⭕ | - |
| 공통 | 관심그룹 종목조회 | `MCJDD88841` | `inquire_issue_groups` | ❌ | 3 |
| 공통 | 관심종목 그룹조회 | `MCJDD88840` | `inquire_group_list` | ❌ | 2 |
| 국내주식주문 | 주식종합주문 | `CSPAT00600` | `kr_stock_order` | ⭕ | 10 |
| 국내주식주문 | 주식정정주문 | `CSPAT00700` | `kr_stock_order_modify` | ⭕ | 3 |
| 국내주식주문 | 주식취소주문 | `CSPAT00800` | `kr_stock_order_cancel` | ⭕ | 3 |
| 국내주식주문 | 주식종합주문- NXT거래소 | `CSPAT00610` | `kr_stock_order_nxt` | ❌ | 10 |
| 국내주식주문 | 주식정정주문- NXT거래소 | `CSPAT00710` | `kr_stock_order_modify_nxt` | ❌ | 3 |
| 국내주식주문 | 주식취소주문- NXT거래소 | `CSPAT00810` | `kr_stock_order_cancel_nxt` | ❌ | 3 |
| 국내주식주문 | 체결/미체결조회 | `CSPAQ04800` | `kr_stock_inquire_executions` | ⭕ | 2 |
| 국내주식주문 | 주식주문가능수량조회 | `CSPBQ00100` | `kr_stock_inquire_psbl_quantity` | ⭕ | 2 |
| 국내주식주문 | 주식잔고조회 | `CSPAQ03420` | `kr_stock_inquire_balance` | ⭕ | 2 |
| 국내주식주문 | 당일매매손익 조회 | `CSPAQ01800` | `kr_stock_inquire_daily_pnl` | ❌ | 2 |
| 국내주식주문 | 계좌예수금조회 | `CDPCQ00100` | `kr_stock_inquire_deposit` | ⭕ | 1 |
| 국내주식주문 | 일자별매매내역 | `CSPEQ00400` | `kr_stock_inquire_daily_trade` | ⭕ | 1 |
| 국내주식주문 | 임의기간수익률집계 | `FOCCQ10800` | `kr_stock_inquire_period_returns` | ❌ | 1 |
| 국내주식주문 | 주식 실현손익조회 | `CSPAQ07800` | `kr_stock_inquire_realized_pnl` | ❌ | 1 |
| 국내주식주문 | 계좌별신용한도조회 | `CSPAQ00600` | `kr_stock_inquire_credit_limit` | ⭕ | 1 |
| 국내주식주문 | 신용상환가능총수량조회 | `CSPAQ09400` | `kr_stock_inquire_credit_repayment` | ❌ | 1 |
| 국내주식주문 | 계좌거래내역 조회 | `CDPCQ04700` | `kr_stock_inquire_trading_history` | ⭕ | 2 |
| 국내주식시세 | 주식종목 조회 | `JCODES` | `kr_stock_search_stocks` | ⭕ | 3 |
| 국내주식시세 | ELW 종목 조회 | `WCODES` | `kr_stock_inquire_elw_stock` | ⭕ | 3 |
| 국내주식시세 | 국내주식 멀티현재가조회 | `MULTIPRICE` | `kr_stock_inquire_price_multi` | ⭕ | 2 |
| 국내주식시세 | 현재가조회 | `PRICE` | `kr_stock_inquire_price` | ⭕ | 5 |
| 국내주식시세 | 호가조회 | `HOGA` | `kr_stock_inquire_orderbook` | ⭕ | 3 |
| 국내주식시세 | 시간대별체결조회 | `CONCLUSION` | `kr_stock_inquire_time_execution` | ⭕ | 3 |
| 국내주식시세 | 일별체결조회 | `DAYTRADE` | `kr_stock_inquire_daily_executions` | ⭕ | 3 |
| 국내주식시세 | 주식조건상승하락조회 | `RANKLIST` | `kr_stock_inquire_condition_rise_fall` | ⭕ | 3 |
| 국내주식시세 | 일별업종별투자자조회 | `UPTJJDAY` | `kr_stock_inquire_daily_industry_investor` | ⭕ | 2 |
| 국내주식시세 | 일별종목별투자자조회 | `DAYSTOCKTJJ` | `kr_stock_inquire_daily_issue_investor` | ⭕ | 2 |
| 국내주식시세 | 국내 ETF/ETN 구성종목조회 | `ETFCOMPCODE` | `kr_stock_inquire_etf_etn_stock` | ⭕ | 2 |
| 국내주식시세 | 섹터분류코드 조회 | `SECTORCOND` | `kr_stock_inquire_sector_codes` | ⭕ | 2 |
| 국내주식시세 | 섹터구성종목 조회 | `SECTORCONDLIST` | `kr_stock_inquire_sector_components` | ⭕ | 2 |
| 국내주식시세 | 업종분류코드 조회 | `USTOCKCOND` | `kr_stock_inquire_industry_codes` | ⭕ | 2 |
| 국내주식시세 | 업종구성종목 조회 | `USTOCKCONDLIST` | `kr_stock_inquire_industry_components` | ⭕ | 2 |
| 국내주식시세(실시간) | [실시간]주식주문체결 조회 | `IS1` | `kr_stock_realtime_order_execution` | ⭕ | - |
| 국내주식시세(실시간) | [실시간]주식주문접수 조회 | `IS0` | `kr_stock_realtime_order_accept` | ⭕ | - |
| 국내주식시세(실시간) | [실시간]주식호가 | `S01` | `kr_stock_realtime_orderbook` | ⭕ | - |
| 국내주식시세(실시간) | [실시간]주식체결가 | `S00` | `kr_stock_realtime_execution_price` | ⭕ | - |
| 국내주식시세(실시간) | [실시간]ELW호가 | `W01` | `kr_stock_realtime_elw_orderbook` | ⭕ | - |
| 국내주식시세(실시간) | [실시간]ELW체결 | `W00` | `kr_stock_realtime_elw_execution` | ⭕ | - |
| 국내주식시세(실시간) | [실시간]업종지수체결가 | `U00` | `kr_stock_realtime_industry_index_execution_price` | ⭕ | - |
| 국내주식시세(실시간) | [실시간]업종지수등락 | `U03` | `kr_stock_realtime_industry_index_change` | ⭕ | - |
| 국내주식시세(실시간) | [실시간]업종별투자자 | `U05` | `kr_stock_realtime_industry_investor` | ⭕ | - |
| 국내선물옵션주문 | 선물옵션 주문 | `CFOAT00100` | `kr_futopt_order` | ⭕ | 10 |
| 국내선물옵션주문 | 선물옵션 정정주문 | `CFOAT00200` | `kr_futopt_order_modify` | ⭕ | 10 |
| 국내선물옵션주문 | 선물옵션 취소주문 | `CFOAT00300` | `kr_futopt_order_cancel` | ⭕ | 10 |
| 국내선물옵션주문 | 선물옵션 체결조회 | `CFOAQ04000` | `kr_futopt_inquire_executions` | ⭕ | 2 |
| 국내선물옵션주문 | 선물옵션 주문가능수량 | `CFOAQ42400` | `kr_futopt_inquire_psbl_quantity` | ⭕ | 2 |
| 국내선물옵션주문 | 선물옵션 잔고 조회 | `CFOAQ02500` | `kr_futopt_inquire_balance` | ⭕ | 2 |
| 국내선물옵션주문 | 선물옵션 잔고_평가현황조회 | `CFOAQ50100` | `kr_futopt_inquire_balance_eval` | ⭕ | 2 |
| 국내선물옵션주문 | 선물옵션 당일실현손익 | `CFOAQ02600` | `kr_futopt_inquire_realized_pnl` | ⭕ | 1 |
| 국내선물옵션주문 | 선물옵션 가정산예탁금 상세 | `CFOEQ11100` | `kr_futopt_inquire_estimated_deposit` | ⭕ | 1 |
| 국내선물옵션주문 | 선물옵션 주문 (야간) | `CFOHT00100` | `kr_futopt_order_night` | ❌ | 10 |
| 국내선물옵션주문 | 선물옵션 정정주문 (야간) | `CFOHT00200` | `kr_futopt_order_modify_night` | ❌ | 10 |
| 국내선물옵션주문 | 선물옵션 취소주문 (야간) | `CFOHT00300` | `kr_futopt_order_cancel_night` | ❌ | 10 |
| 국내선물옵션주문 | 선물옵션 체결조회 (야간) | `CFOHQ04000` | `kr_futopt_inquire_executions_night` | ❌ | 2 |
| 국내선물옵션주문 | 선물옵션 잔고조회 (야간) | `CFOHQ02500` | `kr_futopt_inquire_balance_night` | ❌ | 2 |
| 국내선물옵션시세 | 선물종목 조회 | `FCODES` | `kr_futopt_search_futures` | ⭕ | 3 |
| 국내선물옵션시세 | 옵션종목 조회 | `OCODES` | `kr_futopt_search_options` | ⭕ | 10 |
| 국내선물옵션시세 | 국내선옵 멀티현재가 조회 | `FOMULTIPRICE` | `kr_futopt_inquire_price_multi` | ⭕ | 2 |
| 국내선물옵션시세 | 현재가조회 | `FOPRICE` | `kr_futopt_inquire_price` | ⭕ | 5 |
| 국내선물옵션시세 | 호가조회 | `HOGA` | `kr_futopt_inquire_orderbook` | ⭕ | 5 |
| 국내선물옵션시세 | 일별체결조회 | `DAYTRADE` | `kr_futopt_inquire_daily_executions` | ⭕ | 2 |
| 국내선물옵션시세 | 시간대별체결조회 | `CONCLUSION` | `kr_futopt_inquire_time_execution` | ⭕ | 2 |
| 국내선물옵션시세 | 옵션전광판 | `OSTOCK_CONDT` | `kr_futopt_option_board` | ⭕ | 2 |
| 국내선물옵션시세(실시간) | [실시간]선물옵션주문체결 | `IF0` | `kr_futopt_realtime_order_execution` | ⭕ | - |
| 국내선물옵션시세(실시간) | [실시간]지수선물호가 | `F01` | `kr_futopt_realtime_index_future_orderbook` | ⭕ | - |
| 국내선물옵션시세(실시간) | [실시간]지수선물체결가 | `F00` | `kr_futopt_realtime_index_future_execution_price` | ⭕ | - |
| 국내선물옵션시세(실시간) | [실시간]미니지수선물호가 | `F91` | `kr_futopt_realtime_mini_index_future_orderbook` | ⭕ | - |
| 국내선물옵션시세(실시간) | [실시간]미니지수선물체결가 | `F90` | `kr_futopt_realtime_mini_index_future_execution_price` | ⭕ | - |
| 국내선물옵션시세(실시간) | [실시간]섹터지수선물호가 | `F71` | `kr_futopt_realtime_sector_index_future_orderbook` | ⭕ | - |
| 국내선물옵션시세(실시간) | [실시간]섹터지수선물체결 | `F70` | `kr_futopt_realtime_sector_index_future_execution` | ⭕ | - |
| 국내선물옵션시세(실시간) | [실시간]주식선물호가 | `F21` | `kr_futopt_realtime_stock_future_orderbook` | ⭕ | - |
| 국내선물옵션시세(실시간) | [실시간]주식선물체결 | `F20` | `kr_futopt_realtime_stock_future_execution` | ⭕ | - |
| 국내선물옵션시세(실시간) | [실시간]상품선물호가 | `F11` | `kr_futopt_realtime_commodity_future_orderbook` | ⭕ | - |
| 국내선물옵션시세(실시간) | [실시간]상품선물체결가 | `F10` | `kr_futopt_realtime_commodity_future_execution_price` | ⭕ | - |
| 국내선물옵션시세(실시간) | [실시간]지수옵션호가 | `O01` | `kr_futopt_realtime_index_option_orderbook` | ⭕ | - |
| 국내선물옵션시세(실시간) | [실시간]지수옵션체결 | `O00` | `kr_futopt_realtime_index_option_execution` | ⭕ | - |
| 국내선물옵션시세(실시간) | [실시간]주식옵션호가 | `O21` | `kr_futopt_realtime_stock_option_orderbook` | ⭕ | - |
| 국내선물옵션시세(실시간) | [실시간]주식옵션체결가 | `O20` | `kr_futopt_realtime_stock_option_execution_price` | ⭕ | - |
| 국내선물옵션시세(실시간) | [실시간]미니지수옵션호가 | `O91` | `kr_futopt_realtime_mini_index_option_orderbook` | ⭕ | - |
| 국내선물옵션시세(실시간) | [실시간]미니지수옵션체결가 | `O90` | `kr_futopt_realtime_mini_index_option_execution_price` | ⭕ | - |
| 국내선물옵션시세(실시간) | [실시간]K200지수위클리옵션호가 | `OB1` | `kr_futopt_realtime_k200_weekly_option_orderbook` | ⭕ | - |
| 국내선물옵션시세(실시간) | [실시간]K200지수위클리옵션체결 | `OB0` | `kr_futopt_realtime_k200_weekly_option_execution` | ⭕ | - |
| 국내선물옵션시세(실시간) | [실시간]KOSDAQ150옵션호가 | `OA1` | `kr_futopt_realtime_kosdaq150_option_orderbook` | ⭕ | - |
| 국내선물옵션시세(실시간) | [실시간]KOSDAQ150옵션체결 | `OA0` | `kr_futopt_realtime_kosdaq150_option_execution` | ⭕ | - |
| 국내선물옵션시세(실시간) | [실시간]선물체결(야간) | `F40` | `kr_futopt_realtime_future_execution_night` | ⭕ | - |
| 국내선물옵션시세(실시간) | [실시간]선물호가(야간) | `F41` | `kr_futopt_realtime_future_orderbook_night` | ⭕ | - |
| 국내선물옵션시세(실시간) | [실시간]옵션체결(야간) | `O30` | `kr_futopt_realtime_option_execution_night` | ⭕ | - |
| 국내선물옵션시세(실시간) | [실시간]옵션호가(야간) | `O31` | `kr_futopt_realtime_option_orderbook_night` | ⭕ | - |
| 국내선물옵션시세(실시간) | [실시간]미니옵션호가(야간) | `E11` | `kr_futopt_realtime_mini_option_orderbook_night` | ⭕ | - |
| 국내선물옵션시세(실시간) | [실시간]미니옵션체결가(야간) | `E10` | `kr_futopt_realtime_mini_option_execution_price_night` | ⭕ | - |
| 국내선물옵션시세(실시간) | [실시간]KOSDAQ150옵션체결가(야간) | `E20` | `kr_futopt_realtime_kosdaq150_option_execution_price_night` | ⭕ | - |
| 국내선물옵션시세(실시간) | [실시간]KOSDAQ150옵션호가(야간) | `E21` | `kr_futopt_realtime_kosdaq150_option_orderbook_night` | ⭕ | - |
| 국내주식/선물차트 | 틱차트조회 | `CHARTTICK` | `kr_chart_chart_tick` | ⭕ | 4 |
| 국내주식/선물차트 | 분차트조회 | `CHARTMIN` | `kr_chart_chart_min` | ⭕ | 4 |
| 국내주식/선물차트 | 일차트조회 | `CHARTDAY` | `kr_chart_chart_day` | ⭕ | 4 |
| 국내주식/선물차트 | 주차트조회 | `CHARTWEEK` | `kr_chart_chart_week` | ⭕ | 4 |
| 국내주식/선물차트 | 월차트조회 | `CHARTMONTH` | `kr_chart_chart_month` | ⭕ | 4 |
| 해외주식주문 | 해외주식 주문 | `CAZCT00100` | `ov_stock_order` | ⭕ | 10 |
| 해외주식주문 | 해외주식 체결내역조회 | `CAZCQ00100` | `ov_stock_inquire_executions` | ⭕ | 2 |
| 해외주식주문 | 해외주식 잔고/증거금 조회 | `CAZCQ00400` | `ov_stock_inquire_balance_margin` | ⭕ | 3 |
| 해외주식주문 | 해외주식 매매내역 조회 | `CAZCQ00200` | `ov_stock_inquire_trade_history` | ⭕ | 2 |
| 해외주식주문 | 해외주식 거래내역 조회 | `CAZCQ01600` | `ov_stock_inquire_trading_history` | ⭕ | 2 |
| 해외주식주문 | 해외주식 주문가능금액조회 | `CAZCQ01300` | `ov_stock_inquire_psbl_amount` | ⭕ | 2 |
| 해외주식주문 | 해외주식 실현손익 조회 | `CAZCQ00300` | `ov_stock_inquire_realized_pnl` | ⭕ | 2 |
| 해외주식주문 | 해외주식 예수금상세 | `CAZCQ01400` | `ov_stock_inquire_deposit_detail` | ⭕ | 2 |
| 해외주식주문 | 해외주식 평균매입단가 조회 | `CAZCQ03400` | `ov_stock_inquire_avg_buy_price` | ❌ | 2 |
| 해외주식시세 | 해외주식종목 조회 | `FSTKCODES` | `ov_stock_search_stocks` | ⭕ | 2 |
| 해외주식시세 | 해외주식 멀티현재가조회 | `FSTKMULTIPRICE` | `ov_stock_inquire_price_multi` | ⭕ | 1 |
| 해외주식시세 | 해외주식현재가조회 | `FSTKPRICE` | `ov_stock_inquire_price` | ⭕ | 2 |
| 해외주식시세 | 해외주식호가조회 | `FSTKHOGA` | `ov_stock_inquire_orderbook` | ⭕ | 2 |
| 해외주식시세 | 해외주식시간대별체결조회 | `FSTKCONCLUSION` | `ov_stock_inquire_time_execution` | ⭕ | 2 |
| 해외주식시세 | 해외주식 틱차트조회 | `FSTKCHARTTICK` | `ov_stock_chart_tick` | ⭕ | 4 |
| 해외주식시세 | 해외주식 분차트조회 | `FSTKCHARTMIN` | `ov_stock_chart_min` | ⭕ | 4 |
| 해외주식시세 | 해외주식 일차트조회 | `FSTKCHARTDAY` | `ov_stock_chart_day` | ⭕ | 4 |
| 해외주식시세 | 해외주식 주차트조회 | `FSTKCHARTWEEK` | `ov_stock_chart_week` | ⭕ | 4 |
| 해외주식시세 | 해외주식 월차트조회 | `FSTKCHARTMONTH` | `ov_stock_chart_month` | ⭕ | 4 |
| 해외주식시세 | 해외주식 상승하락조회 | `FSTKRANKLIST` | `ov_stock_inquire_condition_rise_fall` | ⭕ | 2 |
| 해외주식시세(실시간) | [실시간]해외주식 주문체결 조회 | `IS2` | `ov_stock_realtime_order_execution` | ⭕ | - |
| 해외주식시세(실시간) | [실시간]해외주식 체결가 | `V60` | `ov_stock_realtime_execution_price` | ⭕ | - |
| 해외주식시세(실시간) | [실시간]해외주식 호가 | `V61` | `ov_stock_realtime_orderbook` | ⭕ | - |
| 해외주식시세(실시간) | [실시간]해외주식 지연체결가 | `V10` | `ov_stock_realtime_delayed_execution_price` | ⭕ | - |
| 해외주식시세(실시간) | [실시간]해외주식 지연호가 | `V11` | `ov_stock_realtime_delayed_orderbook` | ⭕ | - |
| 해외선물옵션주문 | 해외선옵 주문 | `ph700101o` | `ov_futopt_order` | ❌ | 10 |
| 해외선물옵션주문 | 해외선옵 정정/취소주문 | `ph700201o` | `ov_futopt_order_cancel` | ❌ | 5 |
| 해외선물옵션주문 | 주문가능수량조회 | `ph710201o` | `ov_futopt_inquire_psbl_quantity` | ❌ | 2 |
| 해외선물옵션주문 | 상품별증거금조회 | `ph800404o` | `ov_futopt_inquire_margin_by_product` | ❌ | 2 |
| 해외선물옵션주문 | 주문내역조회 | `ph020101o` | `ov_futopt_inquire_orders` | ❌ | 2 |
| 해외선물옵션주문 | 체결내역 조회 | `ph020301o` | `ov_futopt_inquire_executions` | ❌ | 2 |
| 해외선물옵션주문 | 미체결내역 조회 | `ph020201o` | `ov_futopt_inquire_unfilled` | ❌ | 2 |
| 해외선물옵션주문 | 미결제 약정 조회 | `ph020401o` | `ov_futopt_inquire_open_interest` | ❌ | 2 |
| 해외선물옵션주문 | 일별 미결제 약정내역 | `ph131101o` | `ov_futopt_inquire_daily_open_interest` | ❌ | 2 |
| 해외선물옵션주문 | 예탁잔고현황 | `ph131601o` | `ov_futopt_inquire_deposit_balance` | ❌ | 2 |
| 해외선물옵션주문 | 예탁자산현황 | `ph131501o` | `ov_futopt_inquire_deposit_assets` | ❌ | 2 |
| 해외선물옵션주문 | 기간별 거래내역 조회 | `ph135102o` | `ov_futopt_inquire_trading_history` | ❌ | 2 |
| 해외선물옵션시세 | 호가 & 현재가 조회 | `pibo7042` | `ov_futopt_inquire_orderbook_price` | ❌ | 2 |
| 해외선물옵션시세 | 일자별 시세추이 | `pibo7044` | `ov_futopt_daily_price_trend` | ❌ | 2 |
| 해외선물옵션시세 | 해외선물 틱차트조회 | `pibg7301` | `ov_futopt_future_chart_tick` | ❌ | 10 |
| 해외선물옵션시세 | 해외선물 분차트조회 | `pibg7302` | `ov_futopt_future_chart_min` | ❌ | 2 |
| 해외선물옵션시세 | 해외선물 일주월차트조회 | `pibg7303` | `ov_futopt_future_chart_day_week_month` | ❌ | 2 |
| 해외선물옵션시세 | 해외옵션 틱차트조회 | `pibg7401` | `ov_futopt_option_chart_tick` | ❌ | 10 |
| 해외선물옵션시세 | 해외옵션 분차트조회 | `pibg7402` | `ov_futopt_option_chart_min` | ❌ | 2 |
| 해외선물옵션시세 | 해외옵션 일주월차트조회 | `pibg7403` | `ov_futopt_option_chart_day_week_month` | ❌ | 2 |
| 해외선물옵션시세(실시간) | [실시간]주문체결 | `O` | `ov_futopt_realtime_order_execution` | ❌ | - |
| 해외선물옵션시세(실시간) | [실시간]잔고 | `P` | `ov_futopt_realtime_balance` | ❌ | - |
| 해외선물옵션시세(실시간) | [실시간]해외선물호가 | `L01` | `ov_futopt_realtime_future_orderbook` | ❌ | - |
| 해외선물옵션시세(실시간) | [실시간]해외선물시세 | `K01` | `ov_futopt_realtime_future_quote` | ❌ | - |
| 해외선물옵션시세(실시간) | [실시간]해외옵션시세 | `K02` | `ov_futopt_realtime_option_quote` | ❌ | - |
| 해외선물옵션시세(실시간) | [실시간]해외옵션호가 | `L02` | `ov_futopt_realtime_option_orderbook` | ❌ | - |
| 장내채권주문 | 채권매수주문 | `CSPAT02000` | `bond_order_buy` | ❌ | 5 |
| 장내채권주문 | 채권정정주문 | `CSPAT02100` | `bond_order_modify` | ❌ | 5 |
| 장내채권주문 | 채권취소주문 | `CSPAT02200` | `bond_order_cancel` | ❌ | 5 |
| 장내채권주문 | 채권주문체결조회 | `CSPAQ05700` | `bond_inquire_executions` | ❌ | 2 |
| 장내채권주문 | 채권잔고조회 | `CSPAQ01200` | `bond_inquire_balance` | ❌ | 2 |
| 장내채권주문 | 채권잔고평가조회 | `CSPAQ07900` | `bond_inquire_balance_eval` | ❌ | 2 |
| 장내채권시세 | 장내채권 상세검색 | `BO_SEARCH` | `bond_search_detail` | ❌ | 2 |
| 장내채권시세 | 장내채권 현재가조회 | `BO_SISE` | `bond_inquire_price` | ❌ | 2 |
| 장내채권시세 | 장내채권 호가 조회 | `BO_HOGA` | `bond_inquire_orderbook` | ❌ | 2 |
| 장내채권시세(실시간) | [실시간]일반채권체결 | `B00` | `bond_realtime_normal_execution` | ❌ | - |
| 장내채권시세(실시간) | [실시간]일반채권호가 | `B01` | `bond_realtime_normal_orderbook` | ❌ | - |
| 장내채권시세(실시간) | [실시간]소액채권체결 | `B10` | `bond_realtime_small_execution` | ❌ | - |
| 장내채권시세(실시간) | [실시간]소액채권호가 | `B11` | `bond_realtime_small_orderbook` | ❌ | - |
| 웹소켓(공통) | 웹소켓 세션 초기화 | `DisconnectSession` | `ws_session_disconnect` | ⭕ | 1 |
