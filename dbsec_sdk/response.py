"""API 응답 래퍼 모듈.

REST API 응답을 일관된 인터페이스로 감쌉니다.

사용법:
    resp = client.apis.kr_stock_quote.kr_stock_inquire_price(IsuNo="A005930")
    if resp.is_ok:
        print(resp.body)       # 응답 JSON body
        print(resp.message)    # 응답 메시지
        df = resp.to_dataframe()  # pandas DataFrame 변환
"""

from __future__ import annotations

from typing import Any


class APIResponse:
    """REST API 응답 래퍼.

    DB증권 API 응답을 일관된 형태로 제공합니다.

    Attributes:
        status_code: HTTP 상태 코드 (200, 400, 403, 500 등)
        body: 응답 JSON body (dict)
        headers: 응답 HTTP 헤더
        cont_yn: 연속조회 여부 ("Y"이면 다음 페이지 데이터 존재) — 응답 헤더 cont_yn
        cont_key: 연속조회 키 (다음 조회 시 요청 헤더 cont_key 로 전달) — 응답 헤더 cont_key
        tr_cont / tr_cont_key: cont_yn / cont_key 의 하위호환 별칭(deprecated)
        pages: fetch_all() 로 병합된 경우 원본 페이지별 응답 목록 (단건이면 None)
        message: 응답 메시지 (rsp_msg 또는 msg 필드)
        rsp_cd: 응답 코드 (성공 '00000') — body 의 rsp_cd
        rsp_msg: 응답 메시지 — body 의 rsp_msg/msg (message 와 동일 값)
    """

    def __init__(self, status_code: int, body: dict, headers: dict | None = None):
        self.status_code = status_code
        self.body = body
        self.headers = headers or {}

        # 연속조회 정보 (대량 데이터 조회 시 페이징에 사용).
        # DB증권 서버는 응답에 cont_yn(다음 페이지 존재 'Y'/'N')·cont_key(다음 키) 헤더를 내려준다
        # (요청 헤더와 동일 이름). tr_cont/tr_cont_key 는 타사(KIS) 관례이며 DB증권은 쓰지 않는다.
        # 헤더는 대소문자 무관하게 조회한다(서버/프록시의 케이스 변형 + dict(resp.headers) 변환 대비).
        self.cont_yn: str = self._header("cont_yn")
        self.cont_key: str = self._header("cont_key")
        # 하위호환 별칭(deprecated): 과거 tr_cont/tr_cont_key 명칭. 이제 cont_yn/cont_key 와 같은 값.
        self.tr_cont: str = self.cont_yn
        self.tr_cont_key: str = self.cont_key

        # fetch_all() 이 병합 시 채우는 페이지별 원본 응답 목록 (단건 호출이면 None)
        self.pages: list["APIResponse"] | None = None

        # 응답 메시지 (성공/실패 메시지)
        self.message: str = body.get("rsp_msg", body.get("msg", ""))

    def _header(self, name: str) -> str:
        """응답 헤더를 대소문자 무관하게 조회 (없으면 빈 문자열)."""
        target = name.lower()
        for k, v in self.headers.items():
            if str(k).lower() == target:
                return v
        return ""

    @property
    def has_more(self) -> bool:
        """연속(다음 페이지) 데이터가 더 있으면 True (응답 헤더 cont_yn == 'Y').

        DBSecClient.fetch_all() 가 이 값으로 자동 페이징 종료를 판단한다.
        """
        return str(self.cont_yn).upper() == "Y"

    @property
    def is_ok(self) -> bool:
        """요청 성공 여부. HTTP 2xx이면 True."""
        return 200 <= self.status_code < 300

    @property
    def rsp_cd(self) -> str:
        """응답 코드 (성공은 '00000'). body 의 rsp_cd (없으면 빈 문자열).

        is_ok 는 HTTP 2xx 만 보므로, 업무 성공은 rsp_cd == '00000' 으로 확인한다
        (서버가 HTTP 200 과 함께 업무오류코드 M100/IGW… 를 내려주는 경우가 있음).
        """
        return self.body.get("rsp_cd", "")

    @property
    def rsp_msg(self) -> str:
        """응답 메시지 — body 의 rsp_msg(없으면 msg). message 와 동일 값."""
        return self.body.get("rsp_msg", self.body.get("msg", ""))

    def get(self, key: str, default: Any = None) -> Any:
        """body에서 키로 값 조회.

        Args:
            key: 조회할 키
            default: 키가 없을 때 기본값
        """
        return self.body.get(key, default)

    def to_dataframe(self, key: str | None = None):
        """응답 body 를 pandas DataFrame 으로 변환.

        DB증권 API 응답은 보통 다음 3가지 형태:
          1. 단건: body = {"Out": {...}, "rsp_cd": "...", ...}
          2. 리스트: body = {"Out": {...}, "Out1": [{...}, ...]}
          3. 다중 리스트: body = {"Out1": [...], "Out2": [...]}

        Args:
            key: 변환 대상 블록 이름 (예: "Out1"). 미지정 시 자동 탐색 —
                 body 에서 첫 번째 list[dict] 를 찾고, 없으면 단건 dict 를
                 1-row DataFrame 으로 변환.

        Returns:
            pd.DataFrame (빈 응답이면 empty DataFrame).

        Raises:
            ImportError: pandas 미설치 시.
            KeyError:    명시한 key 가 body 에 없을 때.

        사용 예:
            df = resp.to_dataframe()           # 자동 탐색
            df = resp.to_dataframe("Out1")     # 특정 블록 지정
            df = resp.to_dataframe("Out")      # 단건도 DataFrame 으로
        """
        import pandas as pd

        # 1) key 명시된 경우
        if key is not None:
            if key not in self.body:
                raise KeyError(f"응답 body 에 {key!r} 블록이 없습니다. 가능한 키: {list(self.body.keys())}")
            value = self.body[key]
            if isinstance(value, list):
                return pd.DataFrame(value)
            if isinstance(value, dict):
                return pd.DataFrame([value])
            return pd.DataFrame([{key: value}])

        # 2) 자동 탐색: list[dict] 우선
        for value in self.body.values():
            if isinstance(value, list) and value and isinstance(value[0], dict):
                return pd.DataFrame(value)

        # 3) 단건 dict 블록(Out/In 등) — 가장 큰 dict 를 row 로
        best = None
        for k, v in self.body.items():
            if isinstance(v, dict) and len(v) > (len(best) if best else 0):
                best = v
        if best is not None:
            return pd.DataFrame([best])

        return pd.DataFrame()

    @staticmethod
    def merge(pages: list["APIResponse"]) -> "APIResponse":
        """여러 연속조회 페이지 응답을 하나로 병합.

        list 블록(Out1/Out2 또는 배열 Out 등)은 페이지 순서대로 이어붙이고,
        스칼라/요약 블록(rsp_cd, 요약 dict 등)은 첫 페이지 값을 유지한다.
        DBSecClient.fetch_all() 이 사용한다.

        반환 객체:
          - body: 병합된 본문 (to_dataframe() 시 전 페이지 누적 행)
          - headers/status_code: 마지막 페이지 값 (→ has_more 는 False)
          - pages: 원본 페이지별 APIResponse 목록 (개별 접근용)

        빈 목록이면 빈 200 응답을 반환한다.
        """
        pages = [p for p in pages if p is not None]
        if not pages:
            return APIResponse(200, {}, {})

        merged_body: dict = {}
        for p in pages:
            if not isinstance(p.body, dict):
                continue
            for k, v in p.body.items():
                if isinstance(v, list):
                    bucket = merged_body.get(k)
                    if isinstance(bucket, list):
                        bucket.extend(v)
                    else:
                        merged_body[k] = list(v)
                elif k not in merged_body:
                    merged_body[k] = v

        last = pages[-1]
        out = APIResponse(last.status_code, merged_body, last.headers)
        out.pages = list(pages)
        return out

    def __repr__(self) -> str:
        return (f"APIResponse(status={self.status_code}, "
                f"rsp_cd={self.rsp_cd!r}, message={self.message!r})")

    def __bool__(self) -> bool:
        """if resp: 문법으로 성공 여부 확인 가능."""
        return self.is_ok
