"""[실시간]해외선물호가 [L01] — standalone WebSocket 예제.

그룹: 해외선물옵션시세(실시간)
프로토콜: WebSocket (실시간)
가이드: https://openapi.dbsec.co.kr/apiservice?group_id=f1819725-95e6-4445-ad7f-aa1908b20b03&api_id=393c083a-f119-4f7a-a16a-5e6c6cd8901b

해외선물 실시간 호가 API 입니다. ※ 해외선물옵션 API시세 신청이 되어있지 않은 경우 실시간 시세를 수신 하실 수 없습니다. ※ API시세(유료) 신청방법 GTS(Happy+ Global) : [1761] API시세 신청 ※ 해외선물옵션 가이드는 다음 주소에서 확인 가능하십니다. http://link.dbsec.co.kr/gts/ebook/index.html#page=1 ※ GTS 다운로드는 다음 링크 확인 부탁드리겠습니다. https://www.dbsec.co.kr/research/osft/re_...

토큰은 examples/dbsec_helper.py 가 자동 확보합니다.
필요한 외부 패키지: requests, pyyaml, websockets

실행:
    # examples/ 폴더에서 실행하는 경우:
    python ov_futopt_realtime/ov_futopt_realtime_future_orderbook.py
    # examples/ov_futopt_realtime/ 폴더에서 실행하는 경우:
    python ov_futopt_realtime_future_orderbook.py

── 응답 파라미터 (Out) ─ OUT_BEGIN ──────────────────────
  [TR L01]
    Out  (오브젝트)  Out
      SvTp  (문자)  선옵구분 — F:Future O:Option
      PrTp  (문자)  상품코드
      Code  (문자)  종목코드
      Pind  (문자)  price indicator
      htim  (문자)  현재시각
    Out1  (배열)  Out1
      AskP  (문자)  매수호가가격
      AskQ  (문자)  매수호가수량
      AskN  (문자)  매수호가건수
    Out2  (배열)  Out2
      BidP  (문자)  매도호가가격
      BidQ  (문자)  매도호가수량
      BidN  (문자)  매도호가건수
    Out3  (오브젝트)  Out3
      AskQ  (문자)  누적매수호가수량
      BidQ  (문자)  누적매도호가수량
      AskN  (문자)  누적매수호가건수
      BidN  (문자)  누적매도호가건수

  공통: rsp_cd  응답코드  ·  rsp_msg  응답메시지
── OUT_END ──────────────────────────────────────────────
"""


import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from dbsec_helper import ws_subscribe, run_ws

run_ws(ws_subscribe(
    tr_type="1",  # 등록 종류 (1=시세구독 2=해제 3=계좌등록): 시세구독
    tr_cd="",  # 거래코드 (str) - 입력X
    tr_key="MESU26",  # 종목코드 (str) - 해외선물옵션 종목코드 입력
    group_slug="ov_futopt_realtime",
))
