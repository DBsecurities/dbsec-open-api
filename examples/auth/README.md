# OAuth 인증 — 예제

group_slug: `auth`

각 파일은 **standalone** 입니다. `examples/dbsec_helper.py` 의 공통 헬퍼만 사용합니다.
(토큰 발급·캐싱·응답코드 분류 등 boilerplate 는 헬퍼가 담당)

## 실행 전 준비

```bash
pip install requests pyyaml
cp config.yaml.example config.yaml      # 그리고 prd_app_key/vtl_app_key 입력
python examples/auth/token_issue.py     # 토큰을 .dbsec_token.json 에 캐시
```

## API 목록

| # | API 명 | TR 코드 | 파일 |
|---:|---|---|---|
| 1 | 접근토큰 발급 | `token` | [`token_issue.py`](token_issue.py) |
| 2 | 접근토큰 폐기 | `revoke` | [`token_revoke.py`](token_revoke.py) |

## 실행

```bash
python examples/auth/<method>.py
```

## 토큰 캐시 (루트 `.dbsec_token.json`)

`token_issue.py` 실행 또는 다른 예제 실행 중 자동 발급이 일어나면, 발급된 접근토큰이 저장소 루트의 `.dbsec_token.json` 에 캐시됩니다. 이 캐시는 examples 와 SDK 가 함께 공유하며, 같은 모드(`demo`/`production`)에서 유효기간이 남아있다면 이후 모든 예제가 이 캐시를 재사용합니다.

캐시 파일 구조 (발급 직후 예시):

```json
{
  "access_token":    "eyJhbGciOi...",
  "issued_at":       1716700800,
  "issued_at_kst":   "2026-05-26 19:00:00 KST",
  "expires_at":      1716787200,
  "expires_at_kst":  "2026-05-27 19:00:00 KST",
  "expires_in":      86400,
  "expires_in_hours": 24,
  "mode":            "demo"
}
```

### 만료 시각은 "참고용" 입니다 — 표기값보다 일찍 만료될 수 있습니다

`expires_at` / `expires_at_kst` 는 **DB증권 서버가 토큰 발급 응답 시점에 내려준 `expires_in`(초)을 클라이언트 수신 시각에 더한 값**입니다. 다음과 같은 이유로 실제 서버 측 만료 시점은 캐시에 적힌 시각보다 **수 초~수십 초 빠를 수 있습니다**:

- **네트워크 왕복 지연** — 서버가 만료 카운트를 시작한 시점과 클라이언트가 응답을 받은 시점 사이의 RTT(왕복시간) 만큼 격차가 발생합니다.
- **서버 시간과 로컬 시간의 차이(clock skew)** — NTP 동기화 오차가 있는 환경에서 두 시계가 어긋날 수 있습니다.
- **서버 측 내부 처리 시간** — 발급 → 응답 인코딩 → 네트워크 전송 사이에도 시간이 흐릅니다.

이 격차를 감안해 `dbsec_helper.load_cached_token()` 은 **만료 1분 전부터 캐시 토큰을 무효로 간주**하고 재발급을 시도하도록 되어 있습니다(`dbsec_helper.py` 의 `load_cached_token`). 따라서 정상적인 예제 실행 흐름에서는 이 격차를 신경 쓰지 않아도 됩니다. 다만 만료 직전 1분 구간에서는 DB증권 정책상(아래 '토큰 정책' 참조) 재발급을 요청해도 **동일 토큰이 그대로 반환**될 수 있으므로, 확실히 새 토큰이 필요하면 `token_revoke.py` 로 폐기한 뒤 발급해야 합니다.

다만 직접 `.dbsec_token.json` 의 `expires_at` 값을 읽어 자체 스케줄러·만료 관리 로직을 구현하신다면, **표기 시각 그대로 신뢰하지 마시고 최소 30초~1분 정도의 안전 마진을 빼고 사용하시기 바랍니다.** 마진 없이 표기 시각 직전까지 사용하면, 마지막 호출에서 `IGW00123`("기간이 만료된 token입니다.") 응답을 받을 가능성이 있습니다.

### 토큰 정책 (DB증권)

- 한 번 발급된 토큰은 **24시간** 유효합니다.
- 유효기간 내 재발급을 요청하면 **새 토큰이 아닌 기존 토큰**이 그대로 반환됩니다 (정책).
- 새 토큰이 필요하면 `token_revoke.py` 로 폐기 후 다시 `token_issue.py` 를 실행하세요. `revoke_token()` 은 폐기 후 `.dbsec_token.json` 캐시도 함께 삭제합니다.
