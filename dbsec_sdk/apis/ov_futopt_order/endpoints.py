"""해외선물옵션주문 API 모듈.

DB증권 OpenAPI 그룹: 해외선물옵션주문
group_slug: ov_futopt_order

이 파일은 `_specs/ov_futopt_order/*.json` 에서 자동 생성되었습니다.
스펙이 갱신되면 `_workspace/build_modules.py`로 재생성하세요.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from dbsec_sdk.client import DBSecClient

from dbsec_sdk.response import APIResponse


class OvFutoptOrderAPI:
    """해외선물옵션주문 API 모음.

    사용법:
        >>> client = DBSecClient("config.yaml")
        >>> resp = client.apis.ov_futopt_order.<method>(...)
    """

    # API 경로 매핑
    PATHS = {
        'ov_futopt_order': '/api/v1/trading/overseas-futureoption/order',
        'ov_futopt_order_cancel': '/api/v1/trading/overseas-futureoption/order-revision',
        'ov_futopt_inquire_psbl_quantity': '/api/v1/trading/overseas-futureoption/inquiry/able-orderqty',
        'ov_futopt_inquire_margin_by_product': '/api/v1/trading/overseas-futureoption/inquiry/product-margin',
        'ov_futopt_inquire_orders': '/api/v1/trading/overseas-futureoption/inquiry/order-history',
        'ov_futopt_inquire_executions': '/api/v1/trading/overseas-futureoption/inquiry/transaction-history',
        'ov_futopt_inquire_unfilled': '/api/v1/trading/overseas-futureoption/inquiry/untransaction-history',
        'ov_futopt_inquire_open_interest': '/api/v1/trading/overseas-futureoption/inquiry/open-interest',
        'ov_futopt_inquire_daily_open_interest': '/api/v1/trading/overseas-futureoption/inquiry/daily-open-interest',
        'ov_futopt_inquire_deposit_balance': '/api/v1/trading/overseas-futureoption/inquiry/balance',
        'ov_futopt_inquire_deposit_assets': '/api/v1/trading/overseas-futureoption/inquiry/deposit',
        'ov_futopt_inquire_trading_history': '/api/v1/trading/overseas-futureoption/inquiry/term-trade-history',
    }
    # TR 코드 매핑
    TR_CODES = {
        'ov_futopt_order': 'ph700101o',
        'ov_futopt_order_cancel': 'ph700201o',
        'ov_futopt_inquire_psbl_quantity': 'ph710201o',
        'ov_futopt_inquire_margin_by_product': 'ph800404o',
        'ov_futopt_inquire_orders': 'ph020101o',
        'ov_futopt_inquire_executions': 'ph020301o',
        'ov_futopt_inquire_unfilled': 'ph020201o',
        'ov_futopt_inquire_open_interest': 'ph020401o',
        'ov_futopt_inquire_daily_open_interest': 'ph131101o',
        'ov_futopt_inquire_deposit_balance': 'ph131601o',
        'ov_futopt_inquire_deposit_assets': 'ph131501o',
        'ov_futopt_inquire_trading_history': 'ph135102o',
    }

    def __init__(self, client: 'DBSecClient'):
        self._client = client

    def ov_futopt_order(
        self,
        *,
        Code: str,
        Mdms: str,
        Jtyp: str,
        Jmgb: str,
        Jqty: str,
        Jprc: str,
        Sprc: str,
        Date: str,
        Hsbg: str,
        cont_yn: str = 'N',
        cont_key: str = '',
    ) -> APIResponse:
        """해외선옵 주문 (ph700101o).

        해외선물옵션 주문 API입니다. ※ 수수료 및 제세금 안내는 아래 링크 참고 부탁드립니다. https://www.dbsec.co.kr/custcenter/jobservice/cu_FeeTrading_viw10.do ※ 매수/매도 진입으로 양방향 거래가
        가능하여 API를 이용한 반복주문시, 예기치 못한 손실이 발생 할 수 있습니다. 옵션 상품을 포함한 특정 종목의 경우 유동성이
        부족으로 인해 불리한 체결 가격으로 손실이 발생할 수 있으니 프로그램 작성에 반드시 주의 바랍니다. ※ 추가증거금 미납 또는
        예탁자산평가액이 위탁증거금의 20%를 하회할 경우 반대매매를 통해 강제청산이 실행될 수 있으니 유의 바랍니다. ※ 당사는
        실물인수도 절차상의 어려움, 운반비용 등의 사유로 실물인수도 및 현금결제 업무를 취급하지 않으므로 만기도래일 (FND와 LTD 중
        먼저 도래하는 날) 이전 영업일까지 청산거래를 하셔야 합니다. ※ 해외선물옵션 증거금 및 위험관리(반대매매)와 관련된 상세 내용은
        다음 주소에서 확인 부탁드립니다. https://www.dbsec.co.kr/research/osft/re_Osft_viw06.do
        ※ 해외선물옵션 가이드는 다음 주소에서 확인 가능하십니다. http://link.dbsec.co.kr/gts/ebook/index.html#page=1

        엔드포인트: POST /api/v1/trading/overseas-futureoption/order
        유량제어: 10 TPS
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=344c4c78-ead3-448a-aeb8-0f6bce60efbc&api_id=4ee438c9-16dd-4648-935e-e91ccbe599bd

        Args:
            Code: 종목코드 — 선물옵션 종목코드 입력
            Mdms: 매수/매도 구분 — 1:매수 2:매도
            Jtyp: 주문유형 구분 — 1:시장가 2:지정가 3:STOP 4:STOP LIMIT
            Jmgb: 주문구분 — 0: DAY(당일) 1: GTC 6: GTD
            Jqty: 주문수량
            Jprc: 주문가격 — 시장가 주문시 "0" 입력
            Sprc: STOP-LIMIT 가격
            Date: 유효일자 — YYYYMMDD ex.20240101
            Hsbg: 행사예약 — Y/N
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. 주요 응답 필드:
              - Jmno: 주문번호

        """
        body = {
            'In': {
                'Code': Code,
                'Mdms': Mdms,
                'Jtyp': Jtyp,
                'Jmgb': Jmgb,
                'Jqty': Jqty,
                'Jprc': Jprc,
                'Sprc': Sprc,
                'Date': Date,
                'Hsbg': Hsbg,
            },
        }
        headers = {'cont_yn': cont_yn, 'cont_key': cont_key}
        return self._client.post(self.PATHS['ov_futopt_order'], body, extra_headers=headers)

    def ov_futopt_order_cancel(
        self,
        *,
        Jcgb: str,
        Ojno: str,
        Code: str,
        Mdms: str,
        Jtyp: str,
        Jqty: str,
        Jprc: str,
        Sprc: str,
        Hsbg: str,
        cont_yn: str = 'N',
        cont_key: str = '',
    ) -> APIResponse:
        """해외선옵 정정/취소주문 (ph700201o).

        해외선물옵션 정정/취소 API입니다. ※ 이미 체결완료된 주문은 정정 및 취소주문이 불가능합니다.

        엔드포인트: POST /api/v1/trading/overseas-futureoption/order-revision
        유량제어: 5 TPS
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=344c4c78-ead3-448a-aeb8-0f6bce60efbc&api_id=4bf364e6-1a5d-4a74-887f-be98de14bc60

        Args:
            Jcgb: 정정/취소 구분 — 2:정정 3:취소
            Ojno: 원주문번호 — 정정/취소를 진행할 주문 번호
            Code: 종목코드 — 원 주문에서 사용한 종목코드
            Mdms: 매수/매도 구분 — 취소주문시 "" (공백) 설정 1:매수 2:매도
            Jtyp: 주문유형 구분 — 취소주문시 "" (공백) 설정 1:시장가 2:지정가 3:STOP 4:STOP LIMIT
            Jqty: 주문수량 — 취소주문시 "" (공백) 설정
            Jprc: 주문가격 — 취소주문시 "" (공백) 설정
            Sprc: STOP-LIMIT 가격 — 취소주문시 "" (공백) 설정
            Hsbg: 행사예약 — 옵션 주문시 사용 Y: 행사예약 O N: 행사예약 X
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. 주요 응답 필드:
              - Jmno: 주문번호

        """
        body = {
            'In': {
                'Jcgb': Jcgb,
                'Ojno': Ojno,
                'Code': Code,
                'Mdms': Mdms,
                'Jtyp': Jtyp,
                'Jqty': Jqty,
                'Jprc': Jprc,
                'Sprc': Sprc,
                'Hsbg': Hsbg,
            },
        }
        headers = {'cont_yn': cont_yn, 'cont_key': cont_key}
        return self._client.post(self.PATHS['ov_futopt_order_cancel'], body, extra_headers=headers)

    def ov_futopt_inquire_psbl_quantity(
        self,
        *,
        Code: str,
        Mdms: str,
        Jprc: str,
        Jtyp: str,
        Sprc: str,
        Hsbg: str,
        cont_yn: str = 'N',
        cont_key: str = '',
    ) -> APIResponse:
        """주문가능수량조회 (ph710201o).

        해외선물옵션 주문가능수량 조회 API 입니다.

        엔드포인트: POST /api/v1/trading/overseas-futureoption/inquiry/able-orderqty
        유량제어: 2 TPS
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=344c4c78-ead3-448a-aeb8-0f6bce60efbc&api_id=f29b1de6-cdba-42c0-91be-af8638f5abda

        Args:
            Code: 종목코드
            Mdms: 매도매수구분 — 1:매수 2:매도
            Jprc: 주문가격 — "1:시장가" 선택시 "" (공백) 입력
            Jtyp: 주문유형구분 — 1:시장가 2:지정가 3:STOP 4:STOP LIMIT
            Sprc: STOP-LIMIT 가격
            Hsbg: 행사예약 — Y/N
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. 주요 응답 필드:
              - Jqty: 주문가능수량
              - Cqty: 청산가능수량

        """
        body = {
            'In': {
                'Code': Code,
                'Mdms': Mdms,
                'Jprc': Jprc,
                'Jtyp': Jtyp,
                'Sprc': Sprc,
                'Hsbg': Hsbg,
            },
        }
        headers = {'cont_yn': cont_yn, 'cont_key': cont_key}
        return self._client.post(self.PATHS['ov_futopt_inquire_psbl_quantity'], body, extra_headers=headers)

    def ov_futopt_inquire_margin_by_product(
        self,
        *,
        Code: str,
        cont_yn: str = 'N',
        cont_key: str = '',
    ) -> APIResponse:
        """상품별증거금조회 (ph800404o).

        해외선물옵션 상품별 증거금 조회 API 입니다.

        엔드포인트: POST /api/v1/trading/overseas-futureoption/inquiry/product-margin
        유량제어: 2 TPS
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=344c4c78-ead3-448a-aeb8-0f6bce60efbc&api_id=f0e3ef2e-f895-444e-a51c-3fb825316428

        Args:
            Code: 상품코드
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. 주요 응답 필드:
              - Ikey: 조회구분
              - Sdir: 정렬방식
              - Aflg: 추가위치
              - Ckey: 다음조회가능여부
              - Nrow: 조회건수
              - Kval: 다음키값
              - Code: 상품코드
              - Cdnm: 상품명
              - Mrg1: 위탁증거금구분
              - Mrgn: 위탁증거금
              - Mrg2: 유지증거금구분
              - Urgn: 유지증거금

        """
        body = {
            'In': {
                'Code': Code,
            },
        }
        headers = {'cont_yn': cont_yn, 'cont_key': cont_key}
        return self._client.post(self.PATHS['ov_futopt_inquire_margin_by_product'], body, extra_headers=headers)

    def ov_futopt_inquire_orders(
        self,
        *,
        cont_yn: str = 'N',
        cont_key: str = '',
    ) -> APIResponse:
        """주문내역조회 (ph020101o).

        해외선물옵션 주문내역 조회 API 입니다. ※ 주문내역이 전부 표시되지 않는경우 연속키 조회를 통해 확인하실 수 있습니다.

        엔드포인트: POST /api/v1/trading/overseas-futureoption/inquiry/order-history
        유량제어: 2 TPS
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=344c4c78-ead3-448a-aeb8-0f6bce60efbc&api_id=e12c05bb-9ee8-4cce-966a-4b29ac67f742

        Returns:
            APIResponse. 주요 응답 필드:
              - Ikey: 조회구분
              - Sdir: 정렬방식
              - Aflg: 추가위치
              - Ckey: 다음조회가능여부
              - Nrow: 조회건수
              - Kval: 다음키값
              - Jmno: 주문번호
              - Ojno: 원주문번호
              - Stat: 처리상태 — 상태값: 주문대기 주문 정정대기 정정 취소대기 취소 거부
              - Mtst: 전략유형 — 확인필요
              - Code: 종목코드
              - Mdms: 매도/매수구분 — 1:매수 2:매도
              - Jqty: 주문수량
              - Cqty: 체결수량
              - Mqty: 미체결량
              - (이하 생략 — 가이드 참조)

        """
        body = {
            'In': {},
        }
        headers = {'cont_yn': cont_yn, 'cont_key': cont_key}
        return self._client.post(self.PATHS['ov_futopt_inquire_orders'], body, extra_headers=headers)

    def ov_futopt_inquire_executions(
        self,
        *,
        Sdir: str,
        Code: str,
        cont_yn: str = 'N',
        cont_key: str = '',
    ) -> APIResponse:
        """체결내역 조회 (ph020301o).

        해외선물옵션 체결내역 조회 API 입니다. ※ 내역이 전부 표시되지 않는경우 연속키 조회를 통해 확인하실 수 있습니다.

        엔드포인트: POST /api/v1/trading/overseas-futureoption/inquiry/transaction-history
        유량제어: 2 TPS
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=344c4c78-ead3-448a-aeb8-0f6bce60efbc&api_id=5e24f62a-802a-4f80-a86a-102a066bde58

        Args:
            Sdir: 정렬방식 — 1: 오름차순 정렬 2: 내림차순 정렬
            Code: 종목코드 — "": 기본값(공백) 전체 체결내역 조회 "종목코드": 입력한 종목코드의 체결내역 조회
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. 주요 응답 필드:
              - Ikey: 조회구분
              - Sdir: 정렬방식
              - Aflg: 추가위치
              - Ckey: 다음조회가능여부
              - Nrow: 조회건수
              - Kval: 다음키값
              - Jmno: 주문번호
              - Code: 종목코드
              - Mdms: 매도/매수구분
              - Cprc: 체결가
              - Cqty: 체결수량
              - Mqty: 미체결량
              - Ctim: 체결시간

        """
        body = {
            'In1': {
                'Sdir': Sdir,
            },
            'In': {
                'Code': Code,
            },
        }
        headers = {'cont_yn': cont_yn, 'cont_key': cont_key}
        return self._client.post(self.PATHS['ov_futopt_inquire_executions'], body, extra_headers=headers)

    def ov_futopt_inquire_unfilled(
        self,
        *,
        Sdir: str,
        Hsbg: str,
        cont_yn: str = 'N',
        cont_key: str = '',
    ) -> APIResponse:
        """미체결내역 조회 (ph020201o).

        해외선물옵션 미체결내역 조회 API 입니다. ※ 내역이 전부 표시되지 않는경우 연속키 조회를 통해 확인하실 수 있습니다.

        엔드포인트: POST /api/v1/trading/overseas-futureoption/inquiry/untransaction-history
        유량제어: 2 TPS
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=344c4c78-ead3-448a-aeb8-0f6bce60efbc&api_id=ceddad6d-b0f4-4ada-be11-b77a011df389

        Args:
            Sdir: 정렬방식 — 1: 오름차순 정렬 2: 내림차순 정렬
            Hsbg: 행사예약 구분 — "": 기본값 공백 Y: 옵션 주문 행사예약구분 Y인 경우 만 조회 N: 옵션 주문 행사예약구분 N인 경우 만 조회
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. 주요 응답 필드:
              - Ikey: 조회구분
              - Sdir: 정렬방식
              - Aflg: 추가위치
              - Ckey: 다음조회가능여부
              - Nrow: 조회건수
              - Kval: 다음키값
              - Jmno: 주문번호
              - Stat: 처리상태
              - Mtst: 전략유형
              - Type: 주문유형
              - Code: 종목코드
              - Mdms: 매도/매수구분
              - Jqty: 주문수량
              - Jprc: 주문가격
              - Cqty: 체결수량
              - (이하 생략 — 가이드 참조)

        """
        body = {
            'In1': {
                'Sdir': Sdir,
            },
            'In': {
                'Hsbg': Hsbg,
            },
        }
        headers = {'cont_yn': cont_yn, 'cont_key': cont_key}
        return self._client.post(self.PATHS['ov_futopt_inquire_unfilled'], body, extra_headers=headers)

    def ov_futopt_inquire_open_interest(
        self,
        *,
        Sdir: str,
        Hsbg: str,
        cont_yn: str = 'N',
        cont_key: str = '',
    ) -> APIResponse:
        """미결제 약정 조회 (ph020401o).

        해외선물옵션 미결제 약정 조회 API 입니다. ※ 내역이 전부 표시되지 않는경우 연속키 조회를 통해 확인하실 수 있습니다.

        엔드포인트: POST /api/v1/trading/overseas-futureoption/inquiry/open-interest
        유량제어: 2 TPS
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=344c4c78-ead3-448a-aeb8-0f6bce60efbc&api_id=5025f940-6dea-44d0-aa3a-80872f14cce7

        Args:
            Sdir: 정렬방식 — 1: 오름차순 정렬 2: 내림차순 정렬
            Hsbg: 행사예약구분 — "": 기본값 공백 Y: 옵션 주문 행사예약구분 Y인 경우 만 조회 N: 옵션 주문 행사예약구분 N인 경우 만 조회
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. 주요 응답 필드:
              - Ikey: 조회구분
              - Sdir: 정렬방식
              - Aflg: 추가위치
              - Ckey: 다음조회가능여부
              - Nrow: 조회건수
              - Kval: 다음키값
              - Code: 종목코드
              - Curr: 통화코드
              - Mdms: 매도/매수구분
              - Pqty: 미결제수량
              - Rqty: 전일미결제수량
              - Avgc: 평균가
              - Lprc: 현재가
              - Pamt: 평가손익
              - Cqty: 청산가능수량
              - (이하 생략 — 가이드 참조)

        """
        body = {
            'In1': {
                'Sdir': Sdir,
            },
            'In': {
                'Hsbg': Hsbg,
            },
        }
        headers = {'cont_yn': cont_yn, 'cont_key': cont_key}
        return self._client.post(self.PATHS['ov_futopt_inquire_open_interest'], body, extra_headers=headers)

    def ov_futopt_inquire_daily_open_interest(
        self,
        *,
        Date: str,
        cont_yn: str = 'N',
        cont_key: str = '',
    ) -> APIResponse:
        """일별 미결제 약정내역 (ph131101o).

        해외선물옵션 일별 미결제약정내역 조회 API 입니다.

        엔드포인트: POST /api/v1/trading/overseas-futureoption/inquiry/daily-open-interest
        유량제어: 2 TPS
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=344c4c78-ead3-448a-aeb8-0f6bce60efbc&api_id=6e5baafd-3cc6-43b2-a009-3f4b2c31f331

        Args:
            Date: 조회일자 — 조회하려는 날짜 입력 YYYYMMDD ex.20240101
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. 주요 응답 필드:
              - Ikey: 키액션
              - Sdir: 정렬방향
              - Aflg: 추가위치
              - Ckey: 연속키
              - Nrow: 열 개수
              - Kval: 다음 키값
              - Code: 종목코드
              - Msmd: 매매구분
              - Qtyx: 수량
              - Avgp: 평균단가
              - Pric: 현재가(정산가)
              - Pson: 평가손익
              - Hson: 평가손익증감
              - Curr: 거래통화

        """
        body = {
            'In': {
                'Date': Date,
            },
        }
        headers = {'cont_yn': cont_yn, 'cont_key': cont_key}
        return self._client.post(self.PATHS['ov_futopt_inquire_daily_open_interest'], body, extra_headers=headers)

    def ov_futopt_inquire_deposit_balance(
        self,
        *,
        Date: str,
        cont_yn: str = 'N',
        cont_key: str = '',
    ) -> APIResponse:
        """예탁잔고현황 (ph131601o).

        계좌의 예탁 잔고현황 조회 API 입니다.

        엔드포인트: POST /api/v1/trading/overseas-futureoption/inquiry/balance
        유량제어: 2 TPS
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=344c4c78-ead3-448a-aeb8-0f6bce60efbc&api_id=104976f7-aba0-4209-9ec8-0cbe836f73a5

        Args:
            Date: 조회일자 — YYYYMMDD 형식의 날짜 입력 (EX. 20240101) "99999999": 입력시 당일 날짜로 조회
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. 주요 응답 필드:
              - Ikey: 조회구분
              - Sdir: 정렬방식
              - Aflg: 추가위치
              - Ckey: 다음조회가능여부
              - Nrow: 조회건수
              - Kval: 다음키값
              - Curr: 통화코드
              - Pamt: 전일예탁금잔액
              - Tamt: 당일예탁금잔액
              - Camt: 입출금액
              - Clpl: 선물청산손익
              - Feea: 수수료
              - Inpl: 선물평가손익
              - Bamt: 옵션매매대금
              - Opta: 옵션시장가치
              - (이하 생략 — 가이드 참조)

        """
        body = {
            'In': {
                'Date': Date,
            },
        }
        headers = {'cont_yn': cont_yn, 'cont_key': cont_key}
        return self._client.post(self.PATHS['ov_futopt_inquire_deposit_balance'], body, extra_headers=headers)

    def ov_futopt_inquire_deposit_assets(
        self,
        *,
        Date: str,
        cont_yn: str = 'N',
        cont_key: str = '',
    ) -> APIResponse:
        """예탁자산현황 (ph131501o).

        계좌의 예탁 자산현황 조회 API 입니다.

        엔드포인트: POST /api/v1/trading/overseas-futureoption/inquiry/deposit
        유량제어: 2 TPS
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=344c4c78-ead3-448a-aeb8-0f6bce60efbc&api_id=875bd9a7-4d03-499b-a721-6cf9adcda634

        Args:
            Date: 조회일자 — YYYYMMDD 형식의 날짜 입력 (EX. 20240101) "99999999": 입력시 당일 날짜로 조회
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. 주요 응답 필드:
              - Date: 조회일자
              - Pamt: 전일예탁금잔액
              - Tamt: 당일예탁금잔액
              - Camt: 입출금액
              - Clpl: 선물청산손익
              - Feea: 수수료
              - Inpl: 선물평가손익
              - Bamt: 옵션매매대금
              - Opta: 옵션시장가치
              - Appa: 예탁자산평가액
              - Outa: 인출가능금액
              - Orda: 주문가능금액
              - Uncl: 미수금
              - Daly: 연체료
              - Omrg: 위탁증거금
              - (이하 생략 — 가이드 참조)

        """
        body = {
            'In': {
                'Date': Date,
            },
        }
        headers = {'cont_yn': cont_yn, 'cont_key': cont_key}
        return self._client.post(self.PATHS['ov_futopt_inquire_deposit_assets'], body, extra_headers=headers)

    def ov_futopt_inquire_trading_history(
        self,
        *,
        Frdt: str,
        Todt: str,
        Curr: str,
        cont_yn: str = 'N',
        cont_key: str = '',
    ) -> APIResponse:
        """기간별 거래내역 조회 (ph135102o).

        기간별 거래내역 조회 API 입니다.

        엔드포인트: POST /api/v1/trading/overseas-futureoption/inquiry/term-trade-history
        유량제어: 2 TPS
        가이드: https://openapi.dbsec.co.kr/apiservice?group_id=344c4c78-ead3-448a-aeb8-0f6bce60efbc&api_id=964af1f0-b701-453d-8327-c74c3831bebc

        Args:
            Frdt: 조회일자 from — YYYYMMDD ex.20240101
            Todt: 조회일자 to — YYYYMMDD ex.20240115
            Curr: 통화코드 — "": 전체 "USD": 달러 "JPY": 엔 "HKD": 홍콩달러 "EUR":유로
            cont_yn: 연속거래 여부 ('Y'/'N').
            cont_key: 연속키 값.

        Returns:
            APIResponse. 주요 응답 필드:
              - Msqt: 매수수량 합계
              - Mdqt: 매도수량 합계
              - Cqty: 수량 합계
              - Susu: 수수료 합계
              - Ikey: 조회구분
              - Sdir: 정렬방식
              - Aflg: 추가위치
              - Ckey: 다음조회가능여부
              - Nrow: 조회건수
              - Kval: 다음키값
              - Date: 거래일자
              - Jmno: 주문번호
              - Ojno: 원주문번호
              - Code: 종목코드
              - Mdms: 매매구분
              - (이하 생략 — 가이드 참조)

        """
        body = {
            'In': {
                'Frdt': Frdt,
                'Todt': Todt,
                'Curr': Curr,
            },
        }
        headers = {'cont_yn': cont_yn, 'cont_key': cont_key}
        return self._client.post(self.PATHS['ov_futopt_inquire_trading_history'], body, extra_headers=headers)
