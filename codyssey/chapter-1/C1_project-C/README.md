# Codyssey Project C — AI 기반 소셜 미디어 콘텐츠 자동 생성

> 🟡 **[예습] 개인 예습 단계** — 팀 랜덤 배정 전, 혼자 예습으로 파이프라인을 구축·검증한 기록입니다. 팀 실전 배정 후 이 문서를 `[실전]`으로 승격해 팀 결과로 채웁니다. 아래 결과물은 별도 표기가 없는 한 **개인 예습 실측**(Claude Opus 4.8 / Make + Google Gemini 무료 티어)입니다.
>
> 과제 원문: [`codyssey.md`](codyssey.md)

## 미션 요약

하나의 주제를 입력하면 **여러 소셜 미디어 플랫폼(인스타그램·블로그·X)에 맞는 텍스트와 대표 이미지를 자동 생성**하는 워크플로우를 구축하는 팀 과제입니다. 생성형 AI로 플랫폼별 텍스트를, 이미지 생성 AI로 대표 이미지를 만든 뒤 결과를 노션에 플랫폼별로 저장하는 전체 파이프라인을 설계·실행합니다.

- **자동화 도구**: Make(make.com) — Google Forms 트리거 → Google Gemini(텍스트) → 무료 이미지 AI(HTTP 연동) → Notion 저장
- **도구 선택 근거**: 텍스트는 Gemini `Generate a response`로 무료 자동화. **이미지는 Gemini `Generate an Image`가 유료 전용(무료 티어 0)으로 실측 확인**돼([`make-image-raw.md`](content/raw-logs/make-image-raw.md)), 결제 없이 자동화를 유지하도록 **무료 이미지 생성 API(Pollinations/Flux)를 Make HTTP 모듈로 연동**하는 방식으로 전환. (Gemini 이미지·OpenAI DALL·E는 유료라 예비안으로 보존)

---

## 저장소 구조

```
codyssey/chapter-1/C1_project-C/
├── codyssey.md                     과제 원문
├── team-role-plan.md               팀 역할 분배 & 킥오프 플랜 (파이프라인 단계별 분배안)
├── track-briefings.md              4개 트랙 전체 예습 브리핑 (어느 역할이 걸려도 대비)
├── workflow/
│   ├── workflow-spec.md            산출물① 자동화 워크플로우 설계 문서
│   ├── build-guide.md              Make 단계별 빌드 가이드 (Phase 0~6)
│   └── workflow-explainer.html     워크플로우 구조 시각 설명 페이지
├── prompts/
│   └── prompt-templates.md         산출물③ 플랫폼별 프롬프트 + 수정이력(초안→v1→v2)
├── content/
│   ├── final/
│   │   ├── content-final.md        산출물② 플랫폼별 텍스트 최종본(2026 AI 주제)
│   │   └── cover-ironman-v1.jpg    산출물② 대표 이미지(무료 이미지 AI 생성)
│   ├── screenshots/                Make 실행·노션 저장 증빙 캡처 7장
│   │   ├── 01-scenario-structure.png    워크플로우 전체 구조
│   │   ├── 02-execution-success.png     성공 실행(7모듈 초록)
│   │   ├── 03~05-text-output-*.png       제미나이 3종 실제 출력
│   │   ├── 06-notion-module-output.png  노션 저장 모듈 출력
│   │   └── 07-notion-db-result.png      노션 DB 플랫폼별 저장 결과
│   └── raw-logs/                   근거 raw 로그 (실측)
│       ├── v1-test-raw.md          프롬프트 v1 실측
│       ├── v2-test-raw.md          프롬프트 v2 실측 (v1 위반 교정)
│       ├── make-run-raw.md         Make 자동화 성공 실행 실측(아이언맨, 스크린샷 근거)
│       └── make-image-raw.md       이미지 도구 스펙 실측(Gemini 유료→무료 API 전환)
└── bonus/
    ├── ab-test-raw.md              보너스 A/B 톤 테스트 실측 raw 로그
    └── ab-test-report.md           보너스 A/B 효과 결론 리포트
```

---

## 산출물 ① 자동화 워크플로우

📄 설계: [`workflow/workflow-spec.md`](workflow/workflow-spec.md) · 빌드 가이드: [`workflow/build-guide.md`](workflow/build-guide.md) · 시각 설명: [`workflow/workflow-explainer.html`](workflow/workflow-explainer.html)

```
[1] 주제 입력 (Google Forms 트리거)
        ↓
[2] 플랫폼별 텍스트 생성 (Gemini × 3)
    - 인스타그램 캡션 + 해시태그
    - 블로그 본문(500자+, 소제목)
    - X 요약(280자 이내)
        ↓
[3] 대표 이미지 생성 (무료 이미지 AI · Make HTTP 연동)
        ↓
[4] 노션 저장 (플랫폼 Select로 구분)
```

**실행 검증**: 주제 `아이언맨은 누구인가`로 Make 워크플로우를 실행해 **7개 모듈 전부 성공**(19초, Gemini `gemini-3.5-flash`, 2026-07-19) → 텍스트 3종이 플랫폼별 포맷 규칙(글자수·해시태그·280자)을 지키며 자동 생성되고 노션에 플랫폼별로 저장됨을 실측 확인.

| 증빙 | 스크린샷 |
|------|----------|
| 워크플로우 전체 구조 | [`01-scenario-structure.png`](content/screenshots/01-scenario-structure.png) |
| 성공 실행(7모듈 초록 체크) | [`02-execution-success.png`](content/screenshots/02-execution-success.png) |
| 근거 로그(출력 전문·측정) | [`content/raw-logs/make-run-raw.md`](content/raw-logs/make-run-raw.md) |

---

## 산출물 ② 플랫폼별 콘텐츠 결과물

### (A) Make 자동 생성 결과 — 주제 `아이언맨은 누구인가` (실행 실측)
워크플로우가 실제로 생성한 플랫폼별 텍스트. 실제 출력 전문은 [`make-run-raw.md`](content/raw-logs/make-run-raw.md), 화면 증빙은 아래.

| 플랫폼 | 포맷 규칙 | 실측 결과 | 출력 캡처 |
|--------|-----------|-----------|-----------|
| 인스타그램 | 짧은 캡션 + 해시태그 10개 | 캡션 158자 · 해시태그 10개 · 친근+이모지 | [03](content/screenshots/03-text-output-instagram.png) |
| 블로그 | 본문 500자+ · 소제목 3개+ | 본문 593자(공백제외) · 소제목 3개 | [04](content/screenshots/04-text-output-blog.png) |
| X | 280자 이내 | 105자 · 해시태그 3개 | [05](content/screenshots/05-text-output-x.png) |

- **대표 이미지**: [`content/final/cover-ironman-v1.jpg`](content/final/cover-ironman-v1.jpg) — 무료 이미지 AI(Pollinations/Flux)로 생성, SNS 썸네일 품질, 글자 없음.
- **노션 저장(플랫폼별 구분)**: [`07-notion-db-result.png`](content/screenshots/07-notion-db-result.png) — DB `Project C 콘텐츠`에 인스타/블로그/X 3항목이 플랫폼(Select) 속성으로 구분 저장됨. (대표이미지 컬럼 연결은 크레딧 리셋 후 완성 예정)

### (B) 프롬프트 설계 최종본 — 주제 `2026년 직장인 AI 생산성 도구 트렌드`
📄 [`content/final/content-final.md`](content/final/content-final.md) — 프롬프트 v1→v2 수정 과정을 거친 텍스트 최종본(인스타 126자·블로그 563자·X 136자).

플랫폼별 특성(분량·구조·톤앤매너)을 프롬프트로 구분해 반영한 근거는 산출물 ③에 정리했습니다.

---

## 산출물 ③ 프롬프트 템플릿 문서

📄 [`prompts/prompt-templates.md`](prompts/prompt-templates.md)

플랫폼별 프롬프트 설계 3원칙(**분량·구조·톤을 숫자와 구조로 못 박기**)과 **수정 과정(초안→수정→최종)**을 실측 근거와 함께 기록했습니다.

- **블로그 v1 위반 → v2 교정**: v1 본문이 439자로 500자 미달(실측) → "제목·소제목을 제외한 본문 합계 500자 이상"으로 프롬프트를 명확화 → v2에서 563자로 통과.
- 근거 로그: [`content/raw-logs/v1-test-raw.md`](content/raw-logs/v1-test-raw.md) · [`content/raw-logs/v2-test-raw.md`](content/raw-logs/v2-test-raw.md)
- **학습 포인트**: LLM은 글자 수 하한을 자주 놓친다 → "무엇을 세는지"를 프롬프트에 명시해야 한다.

---

## 보너스 ① A/B 톤 테스트

📄 실측 로그: [`bonus/ab-test-raw.md`](bonus/ab-test-raw.md) · 결론 리포트: [`bonus/ab-test-report.md`](bonus/ab-test-report.md)

같은 주제를 **톤 한 줄만** 바꿔 친근형(A) vs 전문형(B) 두 버전으로 3개 플랫폼 모두 생성·실측했습니다.

- **핵심 결론**: 인스타=친근형, 블로그=전문형이 유리. X는 주제 목적(바이럴 vs 전문)이 톤을 결정.
- **예상 밖 발견**: 톤은 문체뿐 아니라 **글자 수·해시태그·이모지 정책까지 연쇄로 흔든다** — 친근형(구어체)은 같은 프롬프트에서 본문 분량이 덜 나와 분량 하한을 먼저 위반. A/B는 톤만 바꾸는 것으로 끝나지 않고 채널별 포맷 규칙을 함께 재점검해야 한다.

---

## 과제 목표 (동료 평가 대비 — 스스로 설명 가능)

1. 하나의 주제에서 플랫폼별 특성에 맞는 콘텐츠를 자동 생성하는 워크플로우 (Forms→Gemini×3→이미지→Notion)
2. 생성형 AI + 이미지 생성 AI를 연동해 텍스트+이미지 콘텐츠를 자동화하는 방법 (Make로 Gemini 텍스트 3모듈 + 무료 이미지 AI HTTP 모듈을 한 시나리오에 연결)
3. 포맷(글자수·해시태그·톤)을 고려한 프롬프트 설계 원리 (모호한 지시를 숫자·구조·금지규칙으로 못 박기)

---

## 진행 상태

**✅ 예습에서 완료(실측)**
- [x] 워크플로우 구조 + 텍스트 3종 자동 생성 + 노션 플랫폼별 저장 — 실행 성공(아이언맨), 스크린샷 7장 확보
- [x] 대표 이미지 생성 — 무료 이미지 AI로 SNS 품질 1장 확보([`cover-ironman-v1.jpg`](content/final/cover-ironman-v1.jpg))
- [x] 프롬프트 템플릿 + 수정이력(v1→v2), 보너스 A/B 톤 테스트

**⏸️ 크레딧 리셋 후 / 팀 실전에서 완성**
- [ ] **이미지→노션 연결** — HTTP 이미지 모듈을 노션 저장 앞단에 배치해 대표이미지 컬럼까지 자동 채우기 (현재 텍스트만 저장, 이미지 asset은 별도 확보됨)
- [ ] **텍스트+이미지+노션 풀 실행 1회** — Make 무료 크레딧 소진으로 대기 중(과금 아님, 월 리셋). 재시 텍스트 모델을 2.5/2.0 Flash로 낮춰 503 회피 권장
- [ ] **협업 도구(노션) 페이지** — 프로젝트 개요 + 팀 구성원 역할 + 개인별 작업 요약 (팀 배정 후)

> 제약 메모: 이미지는 Gemini `Generate an Image`가 유료 전용이라 무료 이미지 AI(HTTP)로 전환, Make는 무료 플랜 월 1,000 operations 한도 소진으로 풀 실행 일시 대기 — 상세는 [`make-image-raw.md`](content/raw-logs/make-image-raw.md).
