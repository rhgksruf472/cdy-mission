# 프로젝트 1 — 동일 워크플로우 설계 (Make vs Zapier 비교용)

Make와 Zapier에 **완전히 동일한 구조**로 구현한다. 서비스 조합은 원문 6번 "권장 최소 구성"의 `Google Sheets + Gmail + Webhook`을 그대로 사용한다.

## 시나리오

"문의 접수 시트에 새 행이 추가되면, 우선순위에 따라 담당자에게 알림을 다르게 보내는 자동화"

## 준비물 (사용자가 미리 만들어야 하는 것)

1. **Google Sheets** — 새 스프레드시트 1개, 시트명 예: `문의접수`
   - 컬럼: `타임스탬프` / `이름` / `이메일` / `문의내용` / `우선순위` (값은 `높음` 또는 `보통`만 사용)
2. **Gmail** — Make/Zapier와 연동할 본인 Gmail 계정 (수신자는 본인 이메일로 테스트해도 됨)
3. **Webhook 수신처** — [webhook.site](https://webhook.site) 접속 시 즉시 발급되는 고유 URL 사용 (회원가입 불필요, 받은 요청이 화면에 실시간으로 표시됨)

## 워크플로우 구조 (Make · Zapier 동일)

```
[Trigger] Google Sheets — 새 행 감지 ("문의접수" 시트)
    │
    ▼
[Router/Filter] "우선순위" 열 값으로 분기
    │
    ├── 분기 A: 우선순위 = "높음"
    │       └─ [Action 1] Gmail — 이메일 발송 ("긴급 문의 접수" 제목, 담당자 앞)
    │
    └── 분기 B: 우선순위 = "보통"
            └─ [Action 2] Webhook — webhook.site URL로 HTTP POST (문의 내용 JSON으로 전송, 로그 적재 용도)
```

- Trigger 1개 (Google Sheets 새 행)
- Action 2개 (Gmail 발송 / Webhook POST) — 분기마다 1개씩
- 조건 분기 1개 (우선순위 값 기준)
- **각 분기를 최소 1회씩 실행 확인해야 하므로, 테스트 시 "높음" 행 1개 + "보통" 행 1개를 각각 시트에 추가해서 두 경로 모두 실행 결과를 캡처한다.**

## 캡처해야 하는 화면 (도구별로 동일 목록)

| 파일명 | 내용 |
|---|---|
| `01-trigger-config.png` | Google Sheets Trigger 설정 화면 (시트/범위 지정) |
| `02-router-config.png` | Router/Filter 조건 설정 화면 (우선순위 분기 조건) |
| `03-action-gmail-config.png` | Gmail Action 설정 화면 (분기 A) |
| `04-action-webhook-config.png` | Webhook Action 설정 화면 (분기 B) |
| `05-execution-branch-a.png` | "높음" 행 실행 후 히스토리/로그 (분기 A 성공 확인) |
| `06-execution-branch-b.png` | "보통" 행 실행 후 히스토리/로그 (분기 B 성공 확인) — webhook.site 수신 화면도 함께 캡처 권장 |

캡처 저장 위치: `comparison/make/`, `comparison/zapier/` (도구별 폴더)

## 보안 주의

캡처에 Gmail 주소 전체, API Key/토큰이 노출되면 마스킹(`***`) 처리 후 저장한다.

## Make 구현 중 발생한 이슈 (구현 과정 요약용 실측 기록)

**문제**: HTTP(Webhook) Action의 Body content를 "JSON string" 모드로 작성하는 과정에서 2차례 `InvalidConfigurationError` 발생 — "The provided JSON body content is not valid JSON."

- **1차 시도**: `"이름" : [칩]` 형태로 필드 칩만 나열, 중괄호(`{}`)·콤마(`,`)·값 따옴표(`"`) 전부 누락 → 실행 실패
- **원인 추정**: Make의 Content 입력창은 리치 텍스트 매핑 UI라 필드 칩을 넣는 것만으로는 유효한 JSON이 되지 않음 — 최종적으로 "칩이 실제 값으로 치환된 순수 텍스트"가 JSON 문법을 100% 지켜야 함
- **수정 1**: 중괄호로 전체를 감싸고, 각 값 앞뒤로 따옴표 추가 → 재실행 시 새 에러: "Expected ',' or '}' after property value in JSON at position 12"
- **원인 재추정**: 속성(property)들 사이에 콤마가 없어 JSON 파서가 다음 속성을 읽지 못함
- **수정 2**: 마지막 속성(우선순위)을 제외한 3개 속성 끝에 콤마 추가 → 정상 실행 확인
- **학습 포인트**: 노코드 도구의 "필드 매핑 UI"는 문법을 대신 지켜주지 않는 경우가 있다 — Raw/JSON string 모드에서는 결과물이 여전히 개발자가 JSON 문법(중괄호·콤마·따옴표)을 직접 맞춰야 하는 텍스트라는 점을 실제 에러로 확인. Data structure 모드를 썼다면 스키마가 문법을 강제해 이 문제를 피할 수 있었을 것(대안으로 기록).

## 보너스 2 (실패 알림 + 재시도/대체 경로) — 이 워크플로우에 추가

Make 구현 기준으로 추가 설계 (Zapier는 참고만, 필수 아님):
- Gmail Action 연결을 일부러 끊거나 잘못된 수신자로 설정해 **의도적으로 실패**시킨다.
- Make의 **Error Handler**(라우트에 우클릭 → Add error handler)를 Gmail Action에 연결.
- 에러 핸들러 Action: Webhook(또는 Discord/Slack)으로 "실패 알림" 전송 + 실패한 데이터를 임시 시트 탭(`실패로그`)에 대체 기록.
- 캡처: `bonus2-error-handler-config.png`, `bonus2-failure-alert-result.png`

## 보너스 2 구현 중 발생한 이슈 (시행착오 기록)

**문제 1 — Gmail 수신자 필드가 명백히 잘못된 값을 거부함**: 의도적으로 실패시키려고 수신자에 `invalid-email-format`(@ 없음)을 입력했더니, Make의 구조화된 "Recipient email address" 입력창이 저장 전부터 실시간으로 "Value is not a valid email address"라며 막았다.
- **원인**: Make의 Gmail 모듈은 수신자 필드에 클라이언트 단(저장 전) 이메일 형식 검증을 걸어둬서, 명백히 형식이 틀린 값은 애초에 저장이 안 됨.
- **수정**: "To" 필드 옆의 **Map 토글**을 켜서 구조화된 입력 UI 대신 원시 텍스트 입력 모드로 전환 → 형식 검증 없이 `invalid-email-format` 저장 성공.
- **학습 포인트**: 노코드 도구는 실수 방지를 위해 필드별로 자체 검증을 거는 경우가 많다 — 일부러 실패를 유도하는 테스트를 할 때는 그 검증 자체가 막히는 지점을 찾아 우회 방법(Map 모드 등)을 알아야 한다.

**문제 2 — Run once 실행 시 "The module contains unsaved changes" 경고가 반복됨**: 각 모듈을 Save 했는데도 실행 시 같은 경고가 계속 떴다.
- **원인 추정 및 해결**: 브라우저를 새로고침(F5)하니 해결됨 — 화면(클라이언트) 상태가 꼬여있던 것으로 추정.

**문제 3 — Run once 해도 트리거 이후 아무 모듈도 실행되지 않음**: Gmail·Router·Discord·Sheets 어디에도 실행 배지가 안 뜸.
- **원인**: 트리거(Google Sheets Watch New Rows) 모듈의 Output을 직접 열어보니 "The module didn't return any new data."라고 명시되어 있었음 — 시트에 새 행을 추가하지 않고 재실행해서 감지할 데이터가 없었던 것.
- **수정**: "문의접수" 시트에 우선순위=높음인 새 행을 추가한 뒤 재실행 → 정상 처리됨.
- **학습 포인트**: Make 캔버스의 "✓1" 배지는 "오퍼레이션 1회 소비"를 뜻할 뿐 "새 데이터 있음"을 보장하지 않는다 — 모듈을 직접 열어 Output 내용(또는 안내 메시지)까지 확인해야 실제 상태를 알 수 있다.

**문제 4 — 실패 알림 채널을 어디로 보낼지: 텍스트 "일반"과 음성 "일반" 채널 혼동 (재발 방지)**: 프로젝트 2에서 겪었던 것과 동일한 함정이 여기서도 반복될 뻔함.
- **해결**: 아예 **전용 "오류" 채널을 새로 생성**해 실패 알림 전용으로 사용 → 동명 채널 혼동 가능성을 원천 차단. 매번 Channel ID를 대조 확인하는 대신, 애초에 헷갈릴 수 없는 이름을 쓰는 것이 더 근본적인 해결책이라는 걸 확인함.

**최종 실행 검증 결과**: Gmail 발송 실패(의도적) → Error Handler 작동 → Discord "오류" 채널에 실패 알림 도착(`bonus2-failure-alert-result.png`) + "실패로그" 시트에 대체 기록 2건(`bonus2-failure-log-result.png`) 모두 확인. Router의 "보통" 분기는 0건으로 정상적으로 필터링됨(`bonus2-execution-overview.png`).
