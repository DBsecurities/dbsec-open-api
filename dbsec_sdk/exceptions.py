"""DB증권 API 예외 클래스 및 오류코드."""


class DBSecError(Exception):
    """DB증권 API 기본 예외."""


class AuthError(DBSecError):
    """인증 관련 예외 (토큰 발급 실패 등)."""


class APIError(DBSecError):
    """REST API 호출 예외.

    Attributes:
        status_code: HTTP 상태 코드
        rsp_cd: 응답코드 (예: "IGW00121", "00000")
        body: 전체 응답 body
    """

    def __init__(
        self,
        message: str,
        status_code: int | None = None,
        rsp_cd: str = "",
        body: dict | None = None,
    ):
        super().__init__(message)
        self.status_code = status_code
        self.rsp_cd = rsp_cd
        self.body = body


class WebSocketError(DBSecError):
    """WebSocket 연결/통신 예외."""


class RateLimitError(DBSecError):
    """유량제어 초과 예외.

    REST API 또는 WebSocket의 호출 빈도 제한을 초과했을 때 발생합니다.
    예: 세션당 50종목 초과 시
    """


# 오류코드 → 메시지 매핑 테이블(lookup_error)은 제공하지 않는다.
# 서버가 항상 rsp_cd 와 rsp_msg 를 함께 내려주고, 같은 코드가 상황에 따라
# 여러 메시지로 재사용되므로(1:N) 코드만으로의 역조회는 오답을 만들 수 있다.
# 전체 오류코드 목록은 docs/errors_and_rate_limits.md 참조.
