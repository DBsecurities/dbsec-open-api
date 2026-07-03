"""[실시간]해외주식 지연호가 [V11] — standalone WebSocket 예제.

그룹: 해외주식시세(실시간)
프로토콜: WebSocket (실시간)
가이드: https://openapi.dbsec.co.kr/apiservice?group_id=68dccbef-704a-4ebc-86ac-e44056c5687b&api_id=daf5e5be-d465-413d-85d9-0bdebfbca727

해외주식(미국) 지연 호가 API 입니다. ※ 15분 지연된 실시간 시세를 받아보실 수 있습니다. ※ 해외주식(미국) 무료실시간시세 신청을 하지 않을 경우 실시간 시세를 수신 하실 수 없습니다. (V10,V11 지연시세는 별도 신청없이 사용 가능하십니다.) ※ 실시간무료시세(0분) 신청방법 HTS : [7325] 해외주식 실시간 시세 신청 MTS : 해외주식 > 서비스신청 > 실시간시세신청

토큰은 examples/dbsec_helper.py 가 자동 확보합니다.
필요한 외부 패키지: requests, pyyaml, websockets

실행:
    # examples/ 폴더에서 실행하는 경우:
    python ov_stock_realtime/ov_stock_realtime_delayed_orderbook.py
    # examples/ov_stock_realtime/ 폴더에서 실행하는 경우:
    python ov_stock_realtime_delayed_orderbook.py

── 응답 파라미터 (Out) ─ OUT_BEGIN ──────────────────────
  [TR V11]
    RealYn  (문자)  실시간여부(0:지연, 1:실시간)
    locdate  (문자)  현지일자
    symbol  (문자)  종목코드
    loctime  (문자)  현지시간
    kordate  (문자)  한국일자
    kortime  (문자)  한국시간
    totbidsize  (문자)  매수호가 총잔량
    totasksize  (문자)  매도호가 총잔량
    totbidcount  (문자)  매도호가 총건수
    totaskcount  (문자)  매수호가 총건수
    Bid1  (문자)  매수1호가
    Bid1clr  (문자)  색참조(+상승, -하락)
    Ask1  (문자)  매도1호가
    Ask1clr  (문자)  색참조(+상승, -하락)
    Bidsize1  (문자)  매수1호가잔량
    Asksize1  (문자)  매도1호가잔량
    Bidcount1  (문자)  매수1호가건수
    Askcount1  (문자)  매도1호가건수
    Bid2  (문자)  매수2호가
    Bid2clr  (문자)  색참조(+상승, -하락)
    Ask2  (문자)  매도2호가
    Ask2clr  (문자)  색참조(+상승, -하락)
    Bidsize2  (문자)  매수2호가잔량
    Asksize2  (문자)  매도2호가잔량
    Bidcount2  (문자)  매수2호가건수
    Askcount2  (문자)  매도2호가건수
    Bid3  (문자)  매수3호가
    Bid3clr  (문자)  색참조(+상승, -하락)
    Ask3  (문자)  매도3호가
    Ask3clr  (문자)  색참조(+상승, -하락)
    Bidsize3  (문자)  매수3호가잔량
    Asksize3  (문자)  매도3호가잔량
    Bidcount3  (문자)  매수3호가건수
    Askcount3  (문자)  매도3호가건수
    Bid4  (문자)  매수4호가
    Bid4clr  (문자)  색참조(+상승, -하락)
    Ask4  (문자)  매도4호가
    Ask4clr  (문자)  색참조(+상승, -하락)
    Bidsize4  (문자)  매수4호가잔량
    Asksize4  (문자)  매도4호가잔량
    Bidcount4  (문자)  매수4호가건수
    Askcount4  (문자)  매도4호가건수
    Bid5  (문자)  매수5호가
    Bid5clr  (문자)  색참조(+상승, -하락)
    Ask5  (문자)  매도5호가
    Ask5clr  (문자)  색참조(+상승, -하락)
    Bidsize5  (문자)  매수5호가잔량
    Asksize5  (문자)  매도5호가잔량
    Bidcount5  (문자)  매수5호가건수
    Askcount5  (문자)  매도5호가건수
    Bid6  (문자)  매수6호가
    Bid6clr  (문자)  색참조(+상승, -하락)
    Ask6  (문자)  매도6호가
    Ask6clr  (문자)  색참조(+상승, -하락)
    Bidsize6  (문자)  매수6호가잔량
    Asksize6  (문자)  매도6호가잔량
    Bidcount6  (문자)  매수6호가건수
    Askcount6  (문자)  매도6호가건수
    Bid7  (문자)  매수7호가
    Bid7clr  (문자)  색참조(+상승, -하락)
    Ask7  (문자)  매도7호가
    Ask7clr  (문자)  색참조(+상승, -하락)
    Bidsize7  (문자)  매수7호가잔량
    Asksize7  (문자)  매도7호가잔량
    Bidcount7  (문자)  매수7호가건수
    Askcount7  (문자)  매도7호가건수
    Bid8  (문자)  매수8호가
    Bid8clr  (문자)  색참조(+상승, -하락)
    Ask8  (문자)  매도8호가
    Ask8clr  (문자)  색참조(+상승, -하락)
    Bidsize8  (문자)  매수8호가잔량
    Asksize8  (문자)  매도8호가잔량
    Bidcount8  (문자)  매수8호가건수
    Askcount8  (문자)  매도8호가건수
    Bid9  (문자)  매수9호가
    Bid9clr  (문자)  색참조(+상승, -하락)
    Ask9  (문자)  매도9호가
    Ask9clr  (문자)  색참조(+상승, -하락)
    Bidsize9  (문자)  매수9호가잔량
    Asksize9  (문자)  매도9호가잔량
    Bidcount9  (문자)  매수9호가건수
    Askcount9  (문자)  매도9호가건수
    Bid10  (문자)  매수10호가
    Bid10clr  (문자)  색참조(+상승, -하락)
    Ask10  (문자)  매도10호가
    Ask10clr  (문자)  색참조(+상승, -하락)
    Bidsize10  (문자)  매수10호가잔량
    Asksize10  (문자)  매도10호가잔량
    Bidcount10  (문자)  매수10호가건수
    Askcount10  (문자)  매도10호가건수
    TotbidsizeIcdc  (문자)  매수호가 총잔량 증감
    TotbidsizeIcdcclr  (문자)  색참조(+상승, -하락)
    TotasksizeIcdc  (문자)  매도호가 총잔량 증감
    TotasksizeIcdcclr  (문자)  색참조(+상승, -하락)
    BidsizeIcdc1  (문자)  매수 1호가잔량 증감
    BidsizeIcdc1clr  (문자)  색참조(+상승, -하락)
    AsksizeIcdc1  (문자)  매도 1호가잔량 증감
    AsksizeIcdc1clr  (문자)  색참조(+상승, -하락)
    BidsizeIcdc2  (문자)  매수 2호가잔량 증감
    BidsizeIcdc2clr  (문자)  색참조(+상승, -하락)
    AsksizeIcdc2  (문자)  매도 2호가잔량 증감
    AsksizeIcdc2clr  (문자)  색참조(+상승, -하락)
    BidsizeIcdc3  (문자)  매수 3호가잔량 증감
    BidsizeIcdc3clr  (문자)  색참조(+상승, -하락)
    AsksizeIcdc3  (문자)  매도 3호가잔량 증감
    AsksizeIcdc3clr  (문자)  색참조(+상승, -하락)
    BidsizeIcdc4  (문자)  매수 4호가잔량 증감
    BidsizeIcdc4clr  (문자)  색참조(+상승, -하락)
    AsksizeIcdc4  (문자)  매도 4호가잔량 증감
    AsksizeIcdc4clr  (문자)  색참조(+상승, -하락)
    BidsizeIcdc5  (문자)  매수 5호가잔량 증감
    BidsizeIcdc5clr  (문자)  색참조(+상승, -하락)
    AsksizeIcdc5  (문자)  매도 5호가잔량 증감
    AsksizeIcdc5clr  (문자)  색참조(+상승, -하락)
    BidsizeIcdc6  (문자)  매수 6호가잔량 증감
    BidsizeIcdc6clr  (문자)  색참조(+상승, -하락)
    AsksizeIcdc6  (문자)  매도 6호가잔량 증감
    AsksizeIcdc6clr  (문자)  색참조(+상승, -하락)
    BidsizeIcdc7  (문자)  매수 7호가잔량 증감
    BidsizeIcdc7clr  (문자)  색참조(+상승, -하락)
    AsksizeIcdc7  (문자)  매도 7호가잔량 증감
    AsksizeIcdc7clr  (문자)  색참조(+상승, -하락)
    BidsizeIcdc8  (문자)  매수 8호가잔량 증감
    BidsizeIcdc8clr  (문자)  색참조(+상승, -하락)
    AsksizeIcdc8  (문자)  매도 8호가잔량 증감
    AsksizeIcdc8clr  (문자)  색참조(+상승, -하락)
    BidsizeIcdc9  (문자)  매수 9호가잔량 증감
    BidsizeIcdc9clr  (문자)  색참조(+상승, -하락)
    AsksizeIcdc9  (문자)  매도 9호가잔량 증감
    AsksizeIcdc9clr  (문자)  색참조(+상승, -하락)
    BidsizeIcdc10  (문자)  매수10호가잔량 증감
    BidsizeIcdc10clr  (문자)  색참조(+상승, -하락)
    AsksizeIcdc10  (문자)  매도10호가잔량 증감
    AsksizeIcdc10clr  (문자)  색참조(+상승, -하락)
    Bid1krw  (문자)  매수1호가 원화
    Bid1krwclr  (문자)  색참조(+상승, -하락)
    Ask1krw  (문자)  매도1호가 원화
    Ask1krwclr  (문자)  색참조(+상승, -하락)
    Bid2krw  (문자)  매수2호가 원화
    Bid2krwclr  (문자)  색참조(+상승, -하락)
    Ask2krw  (문자)  매도2호가 원화
    Ask2krwclr  (문자)  색참조(+상승, -하락)
    Bid3krw  (문자)  매수3호가 원화
    Bid3krwclr  (문자)  색참조(+상승, -하락)
    Ask3krw  (문자)  매도3호가 원화
    Ask3krwclr  (문자)  색참조(+상승, -하락)
    Bid4krw  (문자)  매수4호가 원화
    Bid4krwclr  (문자)  색참조(+상승, -하락)
    Ask4krw  (문자)  매도4호가 원화
    Ask4krwclr  (문자)  색참조(+상승, -하락)
    Bid5krw  (문자)  매수5호가 원화
    Bid5krwclr  (문자)  색참조(+상승, -하락)
    Ask5krw  (문자)  매도5호가 원화
    Ask5krwclr  (문자)  색참조(+상승, -하락)
    Bid6krw  (문자)  매수6호가 원화
    Bid6krwclr  (문자)  색참조(+상승, -하락)
    Ask6krw  (문자)  매도6호가 원화
    Ask6krwclr  (문자)  색참조(+상승, -하락)
    Bid7krw  (문자)  매수7호가 원화
    Bid7krwclr  (문자)  색참조(+상승, -하락)
    Ask7krw  (문자)  매도7호가 원화
    Ask7krwclr  (문자)  색참조(+상승, -하락)
    Bid8krw  (문자)  매수8호가 원화
    Bid8krwclr  (문자)  색참조(+상승, -하락)
    Ask8krw  (문자)  매도8호가 원화
    Ask8krwclr  (문자)  색참조(+상승, -하락)
    Bid9krw  (문자)  매수9호가 원화
    Bid9krwclr  (문자)  색참조(+상승, -하락)
    Ask9krw  (문자)  매도9호가 원화
    Ask9krwclr  (문자)  색참조(+상승, -하락)
    Bid10krw  (문자)  매수10호가 원화
    Bid10krwclr  (문자)  색참조(+상승, -하락)
    Ask10krw  (문자)  매도10호가 원화
    Ask10krwclr  (문자)  색참조(+상승, -하락)

  공통: rsp_cd  응답코드  ·  rsp_msg  응답메시지
── OUT_END ──────────────────────────────────────────────
"""


import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from dbsec_helper import ws_subscribe, run_ws

run_ws(ws_subscribe(
    tr_type="1",  # 등록 종류 (1=시세구독 2=해제 3=계좌등록): 시세구독
    tr_cd="V11",  # 거래코드 (str) - TR코드입력: V11
    tr_key="",  # 종목코드 (str) - 뉴욕거래소 주식/ETF: "DY" + "종목코드" 나스닥거래소 주식/ETF: "DN" + "종목코드" 아멕스거래소 주식/ETF: "DA" + "종목코드"
    group_slug="ov_stock_realtime",
))
