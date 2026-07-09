# Codyssey Mission 03 — 노코드 자동화 워크플로우

> 과제 원문: [`codyssey.md`](codyssey.md)

## 미션 요약

Trigger(시작 이벤트)와 Action(처리 동작)을 시각적으로 연결해 반복 업무를 자동화하는 노코드 도구의 원리를 익히고, 두 가지 프로젝트로 직접 구현합니다.

- **프로젝트 1**: 동일한 워크플로우를 Make와 Zapier 두 도구로 각각 구현하고 비교 분석
- **프로젝트 2**: 자유 주제로 실제 반복 업무(Codyssey 학습 기록 자동화) 설계·구현
- **보너스 1**: 생성형 AI(Gemini)를 Action으로 연동해 텍스트 자동 생성
- **보너스 2**: 실행 실패 시 알림 + 대체 경로(Error Handler) 구현

두 프로젝트 모두 "설계만"이 아니라 실제로 실행해 Trigger·조건 분기(Router/Filter)의 각 경로가 최소 1회 이상 성공적으로 작동하는 것까지 실측으로 확인했습니다. 구현 과정에서 발견한 버그와 원인 추적 과정도 그대로 기록으로 남겼습니다.

---

## 저장소 구조

```
codyssey/mission-03/
├── codyssey.md                        과제 원문
├── comparison/                        프로젝트 1 — 도구 비교 구현
│   ├── workflow-spec.md               워크플로우 설계 + 구현 중 이슈·시행착오 기록
│   ├── comparison-report.md           Make vs Zapier 비교 분석 보고서
│   ├── make/                          Make 구현 캡처 (설정 6장 + 보너스2 관련 6장)
│   └── zapier/                        Zapier 구현 캡처 (설정·실행 7장)
└── freetopic/                         프로젝트 2 — 자유 주제 자동화
    ├── workflow-design.md             워크플로우 설계 + 버그 발견·해결 기록
    └── make/                          Make 구현 캡처 (설정·실행 20장+, 버그 수정 전/후 보존)
```

캡처 파일명은 번호 순으로 진행 단계를 나타내며, `-fixed`/`-final` 접미사가 붙은 파일이 최종 확인된 결과물입니다. 버그 수정 전 캡처는 지우지 않고 그대로 두어 원인 추적 과정의 실측 증거로 보존했습니다.

---

## 프로젝트 1 — 자동화 도구 비교 구현 (Make vs Zapier)

📄 설계: [`comparison/workflow-spec.md`](comparison/workflow-spec.md) · 비교 보고서: [`comparison/comparison-report.md`](comparison/comparison-report.md)

**워크플로우**: "문의 접수 시트에 새 행이 추가되면, 우선순위(높음/보통)에 따라 담당자에게 다른 방식으로 알림을 보낸다"

```
[Trigger] Google Sheets 새 행 감지
    │
    ▼
[Router/Filter] 우선순위 분기
    ├── 높음 → [Action] Gmail 발송
    └── 보통 → [Action] Webhook(webhook.site) POST
```

| | Make | Zapier |
|---|---|---|
| 구현 캡처 | [`comparison/make/`](comparison/make/) 6장 | [`comparison/zapier/`](comparison/zapier/) 7장 |
| 실행 결과 | 높음/보통 두 분기 모두 실행 성공 확인 | 높음/보통 두 분기 모두 실행 성공 확인 |
| 특이사항 | HTTP Body(JSON string) 작성 중 문법 오류 2차 디버깅 | Json Payload Type 덕분에 문법 오류 없이 한 번에 성공 |

비교 항목 6개(UI/UX, 설정 난이도, Webhook 작성 난이도, 테스트 방식, 실행 로그 확인, 필드 매핑)와 장단점·적합 상황은 [`comparison-report.md`](comparison/comparison-report.md)에 정리했습니다.

### 구현 중 발생한 문제 — Make의 Webhook Body JSON 문법 오류

`workflow-spec.md`에 상세 기록. 요약: HTTP 모듈의 Body를 "JSON string" 모드로 직접 타이핑하는 과정에서 중괄호·콤마·따옴표를 빠뜨려 2차례 `InvalidConfigurationError` 발생 → 문법을 하나씩 맞춰가며 해결. **학습 포인트**: 노코드 도구의 필드 매핑 UI가 항상 문법을 대신 지켜주지는 않는다.

---

## 프로젝트 2 — 자유 주제: Codyssey 학습 기록 자동화

📄 설계: [`freetopic/workflow-design.md`](freetopic/workflow-design.md)

**반복 업무**: Codyssey 미션을 마칠 때마다 학습 내용을 정리해 스터디 채널에 공유하고 진행률을 기록하는 작업을 자동화

**도구 선정**: Make — Router를 시각적으로 다루기 쉽고, 무료 플랜 범위 내에서 운영 가능, Notion·Sheets·Discord 커넥터를 모두 기본 지원

```
[Trigger] Notion "미션 학습 로그" DB — 새 항목 추가
    │
    ▼
[Action] Google Gemini AI — 학습노트 한 줄 요약  ← 보너스 1
    │
    ▼
[Router] 보너스포함 체크박스 값으로 분기
    ├── 체크됨  → Discord "🎉 보너스까지 완료!" 알림 + Sheets 진행률 기록
    └── 미체크 → Discord "✅ 미션 완료" 알림 + Sheets 진행률 기록
```

**실행 결과**: 두 분기 모두 실제 실행 확인 — [`freetopic/make/15-execution-overview-final.png`](freetopic/make/15-execution-overview-final.png)(전체 캔버스), [`13-execution-discord-final.png`](freetopic/make/13-execution-discord-final.png)(Discord 두 메시지 도착), [`14-sheets-result-final.png`](freetopic/make/14-sheets-result-final.png)(Sheets 기록)

### 구현 중 발견한 버그 2건 (평가 대비 우수 사례)

상세 원인 추적 과정은 `workflow-design.md` 7·8번 섹션에 기록.

1. **Notion 배열/객체 필드가 원본 JSON으로 그대로 노출**: Notion API는 제목·텍스트 속성을 서식 정보를 포함한 배열로, 날짜 속성을 시작/종료를 포함한 객체로 반환한다. 최상위 필드 칩을 그대로 매핑하면 값 대신 JSON 구조 전체가 삽입된다 → `Plain Text`/`Start` 하위 필드로 재매핑해 해결.
2. **Discord 특정 분기 메시지가 로그상 성공인데 채널에 안 보임**: 서버에 동일한 이름("일반")의 텍스트 채널과 음성 채널이 동시에 존재해, 한쪽 분기가 음성 채널을 잘못 가리키고 있었다. Message ID를 직접 대조해 원인을 확인하고 올바른 채널로 재선택해 해결.

**학습 포인트**: Make의 초록 체크(성공 표시)는 "API 호출이 에러 없이 완료됐다"는 뜻일 뿐, 의도한 결과가 나왔다는 보장은 아니다 — 실제 결과물(채널 화면, 시트 값)을 눈으로 직접 확인해야 한다.

---

## 보너스 2 — 실패 알림 및 대체 경로 (Error Handler)

프로젝트 1의 Make 워크플로우에 구현했습니다.

```
[Gmail Action] 의도적으로 실패 유도 (수신자 필드에 잘못된 값 입력)
    │
    ▼ (Error Handler)
[Action] Discord 전용 "오류" 채널 알림 + Sheets "실패로그" 탭 대체 기록
```

**실행 결과**: [`comparison/make/bonus2-execution-overview.png`](comparison/make/bonus2-execution-overview.png)(Router 보통 분기 0건으로 정상 필터링 확인) · [`bonus2-failure-alert-result.png`](comparison/make/bonus2-failure-alert-result.png)(Discord 알림 도착) · [`bonus2-failure-log-result.png`](comparison/make/bonus2-failure-log-result.png)(실패로그 시트 기록)

### 구현 중 발생한 문제들

상세는 [`comparison/workflow-spec.md`](comparison/workflow-spec.md)에 기록.

- Gmail 수신자 필드가 형식이 명백히 틀린 값을 저장 전부터 거부 → **Map 토글**로 원시 텍스트 입력 모드로 전환해 우회
- 실행 시 트리거가 "새 데이터 없음"을 반환해 다운스트림이 전혀 실행되지 않음 → 시트에 새 테스트 행을 추가해야 트리거가 감지한다는 점 확인
- 실패 알림 채널도 텍스트/음성 동명 채널 혼동 가능성이 있어, 아예 **전용 "오류" 채널을 신설**해 재발 자체를 차단

---

## 재현성 기록

| 항목 | 도구/모델 | 날짜 |
|---|---|---|
| 프로젝트 1 — Make | make.com (Google Sheets + Gmail + HTTP) | 2026-07-08 |
| 프로젝트 1 — Zapier | zapier.com (Google Sheets + Gmail + Webhooks by Zapier) | 2026-07-08 |
| 프로젝트 2 — Make | make.com (Notion + Google Gemini AI + Discord + Google Sheets) | 2026-07-09 |
| AI 연동(보너스 1) | Google Gemini AI 모듈 · Gemini 3 Flash Preview (무료) | 2026-07-09 |
| 보너스 2 — Error Handler | make.com (프로젝트 1 시나리오에 추가) | 2026-07-09 |

## 보안 준수

캡처에 노출된 실제 Gmail 계정 이메일은 발견 즉시 마스킹 처리했습니다. API Key(Gemini)·Discord 웹훅 URL 등 민감정보는 캡처에 노출되지 않도록 구성했습니다.
