# 자동화 워크플로우 설계 문서 (Make)

> 산출물 ①. 주제 입력 → 플랫폼별 텍스트 3종 + 대표 이미지 자동 생성 → 노션 플랫폼별 저장.
> Mission 03에서 쓰던 **Make + Google Gemini 커넥션을 재활용**한다(텍스트는 무료 티어, 결제 불필요).
> **도구 결정 근거(2026-07-20 실측으로 수정됨)**: 텍스트는 Gemini `Generate a response`로 무료 자동화 성공(`content/raw-logs/make-run-raw.md`). **이미지는 Gemini `Generate an Image`가 모든 모델 무료 티어 0 = 유료 전용**으로 확인돼(`content/raw-logs/make-image-raw.md`, 429 실측), 결제 없이 자동화를 유지하기 위해 **무료 이미지 생성 API(Pollinations, Flux 기반)를 Make HTTP 모듈로 연동**하는 방식으로 전환했다. → 텍스트(Gemini)+이미지(무료 HTTP API) 모두 워크플로우 안에서 자동 생성. OpenAI(DALL·E)·Gemini 이미지(유료)는 예비안으로 보존.
> ⚠️ **초기 가정 오류 기록**: 당초 "Gemini 2.5 Flash Image 하루 ~500장 무료"로 가정했으나 실측 결과 유료 전용이었다 — 신규 이미지 도구는 반드시 실행으로 무료 여부를 확인해야 한다는 교훈(도구 스펙 확인 원칙).

---

## 1. 전체 파이프라인 (한눈에)

```
[1] 주제 입력 (트리거)
    - Google Forms "주제/키워드" 1문항  ─(응답 제출)─▶ Make 트리거 실행
        ↓
[2] 플랫폼별 텍스트 생성 (생성형 AI)
    - Gemini Create a Completion #1 → 인스타그램 캡션 + 해시태그
    - Gemini Create a Completion #2 → 블로그 본문(500자+, 소제목)
    - Gemini Create a Completion #3 → X 요약(280자 이내)
        ↓
[3] 대표 이미지 생성 (이미지 AI · 무료 HTTP 연동)
    - HTTP Download a file → 무료 이미지 API(Pollinations/Flux) → 주제 기반 대표 이미지 1장
        ↓
[4] 노션 저장 (결과 저장 · 플랫폼별 구분)
    - Notion "콘텐츠 DB"에 항목 생성
      · 플랫폼 속성으로 인스타/블로그/X 구분
      · 대표 이미지 첨부
```

## 2. 모듈별 역할·연결 구조 (단계별 설명)

| # | Make 모듈 | 역할 | 입력(이전 단계에서 받는 값) | 출력(다음 단계로 넘기는 값) |
|---|-----------|------|------------------------------|------------------------------|
| 1 | **Google Forms › Watch Responses** | 트리거. 주제 입력을 감지 | 폼 응답 | `{{topic}}` (주제 텍스트) |
| 2a | **Gemini › Create a Completion** | 인스타 텍스트 생성 | `{{topic}}` + 인스타 프롬프트 | 캡션+해시태그 |
| 2b | **Gemini › Create a Completion** | 블로그 텍스트 생성 | `{{topic}}` + 블로그 프롬프트 | 제목+본문 |
| 2c | **Gemini › Create a Completion** | X 텍스트 생성 | `{{topic}}` + X 프롬프트 | 요약문 |
| 3 | **HTTP › Download a file** (무료 이미지 API) | 대표 이미지 생성 | `{{topic}}` 기반 이미지 프롬프트(URL 인코딩) | 이미지 파일(바이너리/URL) |
| 4 | **Notion › Create a Database Item** (×3 또는 라우터) | 플랫폼별 결과 저장 | 2a/2b/2c 텍스트 + 3 이미지 | 노션 DB 항목 |

**연결 원리**: 각 모듈의 출력 필드(예: 1번의 폼 응답 값)를 다음 모듈 입력에 매핑(mapping)해 데이터가 사슬처럼 흐른다. 텍스트 생성 3개는 서로 독립이라 순차 또는 병렬(라우터) 배치 가능. 노션 저장은 "플랫폼별로 구분"이 요구사항이므로 **플랫폼 속성(Select)을 가진 DB에 항목 3개**로 나눠 저장한다.

## 3. 노션 콘텐츠 DB 스키마 (저장 대상)

| 속성 | 타입 | 예시 값 |
|------|------|---------|
| 제목 | Title | `{{topic}} — 인스타그램` |
| 플랫폼 | Select | 인스타그램 / 블로그 / X |
| 본문 | Text | 생성된 텍스트 |
| 대표 이미지 | Files & media | DALL·E 이미지 |
| 주제 | Text | `{{topic}}` |
| 생성일 | Created time | (자동) |

## 4. 캡처한 스크린샷 (산출물 ① · ② 증빙 · `../content/screenshots/`)

- [x] `01-scenario-structure.png` — Make 시나리오 전체 모듈 연결 구조
- [x] `02-execution-success.png` — 실행 성공(7모듈 초록불) 전체 뷰 + Simple log
- [x] `03~05-text-output-*.png` — 제미나이 텍스트 3종 실제 출력(인스타/블로그/X)
- [x] `06-notion-module-output.png` — 노션 저장 모듈 출력(page created)
- [x] `07-notion-db-result.png` — 노션 DB에 플랫폼별 저장된 결과
- [ ] (미완) 입력 폼 화면 / 이미지→노션 연결 후 대표이미지 저장 결과 — 크레딧 리셋 후

## 5. 빌드 전 확인 (스펙 확인 — 2026-07 기준 확정)

1. **AI 커넥션**: Make에 **Google Gemini 커넥션 이미 있음**(Mission 03 재활용) → 텍스트 `Generate a response`는 무료 티어로 사용. **이미지 `Generate an Image`는 유료 전용으로 확인**돼(§상단·`make-image-raw.md`) 무료 이미지 API(HTTP `Download a file`)로 전환. OpenAI 결제 불필요.
2. **입력 폼**: Google Forms(권장) — 무료·스크린샷 용이. (대안: Make 웹훅 / 노션 DB 트리거)
3. **노션 저장 방식**: 콘텐츠 DB에 항목 3개(플랫폼 Select로 구분) 방식으로 확정.
