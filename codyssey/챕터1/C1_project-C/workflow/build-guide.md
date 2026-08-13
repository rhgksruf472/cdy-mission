# Make 빌드 가이드 (혼자 수행 · 무료 Gemini 경로)

> 목표: Google Forms에 주제 입력 → Gemini가 플랫폼별 텍스트 3종 + 대표 이미지 생성 → Notion에 플랫폼별 저장.
> 도구: Make + Google Gemini(무료 티어, Mission 03 커넥션 재활용) + Notion + Google Forms. **결제 불필요.**
> 순서대로 따라가면 됩니다. 각 Phase 끝의 📸는 과제 제출용 스크린샷 시점.

---

## Phase 0 — 저장소부터 (Notion DB) ⏱️ 먼저 해야 병목 없음

1. Notion에서 새 페이지 → `/database` 입력 → **Table - Inline** 선택.
2. DB 이름: `Project C 콘텐츠`.
3. 속성(열)을 아래처럼 만든다. **이름·타입을 정확히** (나중에 Make가 이 이름으로 찾음):

| 속성 이름 | 타입 | 비고 |
| --- | --- | --- |
| 제목 | Title | 기본 존재 (이름만 `제목`으로) |
| 플랫폼 | Select | 옵션 3개 추가: `인스타그램`, `블로그`, `X` |
| 본문 | Text | 생성된 글 |
| 대표이미지 | Files & media | 이미지 첨부 |
| 주제 | Text | 입력 주제 |

4. Make가 이 DB에 접근하도록 공유: DB 우상단 `•••` → **Connections** → Make(Notion) 커넥션 연결. (Mission 03에서 이미 연결했다면 워크스페이스 권한 확인만)

📸 `01-notion-db-schema.png` — 빈 DB와 속성 구조

---

## Phase 0b — 입력 폼 (Google Forms)

1. [forms.google.com](https://forms.google.com) → 빈 양식.
2. 질문 1개: `주제 또는 키워드` (단답형).
3. 상단 **응답 → Google Sheets에 연결**(스프레드시트 생성). Make 트리거가 이 시트를 감시.

📸 `02-form-input.png` — 폼 화면

---

## Phase 1 — Make 시나리오 시작 + 트리거

1. Make → **Create a new scenario**.
2. 첫 모듈 `+` → **Google Forms**(또는 **Google Sheets**) → **Watch Responses**(또는 Watch New Rows) → 폼/시트 선택.
   - Google Forms 앱이 안 보이면 **Google Sheets › Watch New Rows**로 Phase 0b에서 연결한 응답 시트를 감시(동일 효과).
3. 우하단 **Run once**로 트리거 테스트: 폼에 아무 주제나 제출 → 모듈에 응답이 들어오는지 확인.
   - 여기서 들어온 주제 텍스트가 앞으로 쓸 **`{{topic}}`** (매핑 소스).

📸 `03-trigger-config.png` — 트리거 설정

---

## Phase 2 — Gemini 텍스트 3종 (핵심)

트리거 뒤에 **Google Gemini AI › Create a Completion** 모듈을 **3개** 순서대로 추가. 각 모듈의 프롬프트에
`prompts/prompt-templates.md`의 최종 프롬프트를 붙여넣고, **주제 자리에 트리거의 응답값을 매핑**(파란 태그로 끼워 넣기).

**모듈 2a — 인스타그램**
```
너는 소셜 미디어 카피라이터다. 아래 주제를 인스타그램 캡션으로 변환해라.
- 2~4문장의 짧고 친근한 캡션, 이모지 2~3개, 첫 문장은 후킹.
- 끝에 해시태그 10개 내외 한 줄. 소제목/목록 금지.
주제: [여기에 트리거의 '주제' 응답값을 매핑]
```

**모듈 2b — 블로그**
```
아래 주제를 블로그 본문으로 작성해라.
- 제목·소제목 제외 본문 문단 합계 500자 이상, 정보 전달 톤, 이모지 없음.
- 구조: 제목 + 소제목 3개 이상 + 각 소제목 아래 2~4문장 + 마지막 1문장 마무리.
주제: [트리거 '주제' 매핑]
```

**모듈 2c — X**
```
아래 주제를 X(트위터) 게시물로 요약해라.
- 공백 포함 280자 이내(반드시 준수), 핵심만 임팩트 있게, 해시태그 2~3개, 이모지 0~1개.
주제: [트리거 '주제' 매핑]
```

> 💡 매핑하는 법: 프롬프트 입력칸에서 `주제:` 뒤를 클릭하면 오른쪽에 트리거가 넘긴 필드 목록(파란 태그)이 뜬다. `주제` 응답 필드를 클릭하면 칩이 꽂힌다. 이게 STAGE 1→2 데이터 흐름.

📸 `04-gemini-text-config.png` — Gemini 텍스트 모듈 프롬프트 설정(3개 중 대표 1개 이상)

---

## Phase 3 — Notion 저장 3개 (텍스트 먼저)

**Notion › Create a Data Source Item** 모듈을 **3개** 추가(인스타/블로그/X 각각).
> ⚠️ 실제 Make UI 확인 결과(2026-07-18): Notion 모듈이 `Create a Data Source Item`(신규)과 `Create a Database Item (Legacy)`로 나뉘어 있음. 오늘 새로 만든 DB는 최신 Notion API 구조이므로 **Legacy가 아닌 `Create a Data Source Item`**을 선택할 것. `Watch Data Source Items`는 트리거용 모듈이라 이 단계에서 쓰지 않는다.
DB는 `Project C 콘텐츠` 선택 후 매핑:

| Notion 속성 | 인스타 모듈 | 블로그 모듈 | X 모듈 |
| --- | --- | --- | --- |
| 제목 | `{{topic}} — 인스타그램` | `{{topic}} — 블로그` | `{{topic}} — X` |
| 플랫폼 | 인스타그램 | 블로그 | X |
| 본문 | 2a 출력 매핑 | 2b 출력 매핑 | 2c 출력 매핑 |
| 주제 | 트리거 주제 | 트리거 주제 | 트리거 주제 |

📸 `05-notion-action-config.png` — 노션 저장 모듈 매핑

---

## Phase 4 — 첫 실행 & 검증 (텍스트 파이프라인 완성)

1. **Run once** → 폼에 실제 주제 제출(예: `2026년 직장인 AI 생산성 도구 트렌드`).
2. 모든 모듈에 초록 체크 확인.
3. **⚠️ Mission 03 교훈**: 초록 체크는 "API 호출 성공"일 뿐이다. **실제 Notion DB를 눈으로 열어** 3개 항목이 플랫폼별로 잘 들어갔는지, 본문이 JSON이 아니라 실제 글인지 확인.

📸 `06-execution-overview.png` — 실행 성공 전체 뷰
📸 `07-notion-result.png` — 노션에 플랫폼별 저장된 결과

---

## Phase 5 — 대표 이미지 추가 (무료 이미지 AI를 HTTP로 연동)

> ⚠️ **도구 스펙 확인 결과(2026-07-20, 실측)**: Make의 Google Gemini `Generate an Image`는 **모든 이미지 모델(2.5/3.1/3 Pro)이 무료 티어 0 = 유료 전용**이라 429 실패(`content/raw-logs/make-image-raw.md`). 텍스트는 무료지만 이미지는 유료. → 결제 없이 **자동화를 유지**하기 위해 무료 이미지 생성 API를 HTTP 모듈로 연동한다.

**모듈: HTTP › Download a file** (이미지를 바이너리로 받아 Notion에 바로 첨부 가능)

1. 텍스트 모듈들 뒤에 **HTTP › Download a file** 추가.
2. **URL** 칸에 아래를 넣는다. `{{topic}}` 자리에 트리거의 주제 응답값을 매핑:
   ```
   https://image.pollinations.ai/prompt/{{encodeURL("clean modern flat illustration hero image about " + topic + ", minimal office desk, laptop with glowing AI assistant interface, automation flow lines, soft blue white subtle purple, professional optimistic, centered, generous negative space, social media thumbnail, no text no letters no logos")}}?width=1024&height=1024&nologo=true&model=flux
   ```
   - `encodeURL(...)`로 프롬프트 전체를 URL 인코딩(공백·한글 안전). 스타일은 고정하고 **주제만 변수**로 끼운다.
   - 검증 실측: 위 엔드포인트가 HTTP 200 + 실제 JPEG(768~1024px) 반환 확인(키 불필요, 무료).
3. 이 모듈의 출력(바이너리 파일 `data`)을 Phase 3의 Notion 모듈 `대표이미지`(Files & media) 속성에 연결.
   - ⚠️ Notion Files 속성에 넣는 방식(파일 업로드 vs 외부 URL)은 Make Notion 모듈 옵션을 **UI에서 확인 후 확정**한다. Pollinations는 URL 자체가 이미지라, Files 속성이 **외부 URL 첨부**를 지원하면 HTTP 모듈 없이 URL만 넣어도 된다(더 간단). 지원 안 하면 HTTP `Download a file` → 바이너리 업로드 경로 사용.
4. **Run once**로 실행 → Notion에 이미지가 실제로 붙는지 눈으로 확인.

> 💡 **대안 무료 이미지 AI**(Pollinations가 불안정할 때): Hugging Face Inference API(무료 토큰 + FLUX/SD 모델) 또는 Cloudflare Workers AI(무료 티어) — 둘 다 Make HTTP 모듈로 호출. 실패한 Gemini 시도와 함께 도구 비교 자료로 보존.

📸 `08-image-http-config.png` (HTTP 모듈 URL 설정) · `09-notion-image-result.png` (노션에 붙은 이미지)

---

## Phase 6 — 보너스 A/B (친근 vs 전문)

- Phase 2 프롬프트의 톤 한 줄만 바꿔 2세트 실행(친근형/전문형) → 결과를 `bonus/ab-test-report.md`에 비교·결론.
  - 친근형: `톤: 친구에게 말하듯 편하게, 반말/구어체 허용, 이모지 적극.`
  - 전문형: `톤: 전문가처럼 신뢰감 있고 정제된 존댓말, 이모지 최소, 근거 중심.`

---

## 막히면
각 Phase에서 화면이 예상과 다르면 **그 화면 상태(모듈 이름/에러 메시지/필드 목록)를 알려주세요.** 스크린샷 넘겨주시면 폴더 정리·다음 클릭까지 바로 안내합니다. (Mission 03처럼 매핑에서 배열 `[]` leaf 노드 문제, 같은 이름 리소스 오선택 등이 흔한 함정)
