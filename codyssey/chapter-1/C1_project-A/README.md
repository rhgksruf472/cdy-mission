# Codyssey Project A — AI 기반 UI/UX 디자인 시안 제작

> 🟡 **[예습] 개인 예습 단계** — 팀 랜덤 배정 전, 혼자 예습으로 파이프라인(기획→이미지 생성→후가공→프로토타입)을 구축·검증하는 기록입니다. 팀 실전 배정 후 이 문서를 `[실전]`으로 승격해 팀 결과로 채웁니다.
>
> 과제 원문: [`codyssey.md`](codyssey.md)

## 미션 요약

**중고 책 교환 플랫폼**을 컨셉으로, 이미지 생성 AI로 메인/목록/상세 3개 화면의 UI 디자인 시안을 만들고, 후가공으로 완성도를 높인 뒤 Figma로 클릭 가능한 프로토타입을 구성하는 팀 과제입니다.

- **이미지 생성 도구**: Adobe Firefly(모델 Gemini 3 w/ Nano Banana Pro, 화면1·2) + Google Gemini 웹(모델 Nano Banana 2, 화면3 — Firefly 무료 크레딧 소진으로 교체)
- **프로토타입 도구**: Figma

---

## 저장소 구조

```
codyssey/chapter-1/C1_project-A/
├── codyssey.md                     과제 원문
├── team-role-plan.md               팀 역할 분배 & 킥오프 플랜
├── track-briefings.md              4개 트랙 전체 예습 브리핑
├── figma-prototype-guide.md        산출물③ Figma 실행 가이드 + Hotspot 흐름 설계(우리 3화면 전용)
├── prompts/
│   └── prompt-templates.md         산출물② 화면별 프롬프트 초안 + 수정이력(초안→수정→최종)
├── bonus-code/
│   ├── index.html                  보너스① 시안 3화면 HTML/CSS 변환(클릭 전환 프로토타입)
│   └── README.md                   보너스 변환 로그(사용 도구·이미지↔코드 대응·학습 포인트)
└── design/
    ├── final/                      산출물① 최종 UI 이미지 3장(PNG) — screen01-main-final.png 등
    └── raw-logs/                   근거 raw 로그(생성 시도·실패·후가공 과정 전체 보존)
```

---

## 산출물 ① UI 디자인 이미지 — ✅ 완료

컨셉: 중고 책 교환 플랫폼 — 메인(홈) / 목록(카테고리별 리스트) / 상세(도서 정보·교환 신청) 3화면.
최종본: [`design/final/`](design/final/) (screen01-main-final.png · screen02-list-final.png · screen03-detail-final.png). 생성·후가공 전 과정은 [`design/raw-logs/`](design/raw-logs/)에 보존.

## 산출물 ② 작업 로그 문서 — ✅ 완료

프롬프트 초안→수정→최종 기록(도구 교체·실패 사례·저작권 이슈 발견/수정 포함). [`prompts/prompt-templates.md`](prompts/prompt-templates.md).

## 산출물 ③ Figma 프로토타입 — 🟡 진행 중 (프레임·이미지 배치 완료, Hotspot 2/5 연결)

우리 3화면에 맞춘 실행 가이드와 Hotspot 흐름(메인↔상세↔목록 왕복 5개 연결)을 설계해 뒀습니다 → [`figma-prototype-guide.md`](figma-prototype-guide.md). 파일 `Project A - BookSwap Prototype` 생성, 프레임 3개(01-main/02-List/03-Detail) 이미지 배치 완료, Hotspot 1·2번(메인↔상세 왕복 — 최소 요구사항 충족) 연결 완료. 남은 3개 연결(3·4·5번)과 Share 링크 확보는 다음 세션에 이어서 진행.

> **화면3 이미지 재생성**: Figma 배치 중 화면3(`screen03-detail-final.png`, 기존 v2)이 화면1·2와 달리 흰 배경 위 카드+그림자 형태(엣지투엣지 아님)임을 발견 → Gemini에서 v3로 재생성(엣지투엣지 명시 지시 추가)해 교체. 상세 이력은 [`prompts/prompt-templates.md`](prompts/prompt-templates.md) 화면3 v2/v3 참고, 신규 QnA는 [`QnA.md`](QnA.md) Q11.

## 보너스 ① 코드 변환 체험 — ✅ 완료

완성 시안 3화면을 HTML/CSS로 재현하고 화면 전환까지 클릭되게 구현: [`bonus-code/index.html`](bonus-code/index.html) (브라우저에서 바로 열림). 사용 도구·이미지↔코드 대응·학습 포인트는 [`bonus-code/README.md`](bonus-code/README.md).

---

## 과제 목표 (동료 평가 대비 — 스스로 설명 가능)

1. 텍스트 프롬프트의 구성 요소(스타일, 레이아웃, 색상 등)가 결과물에 미치는 영향
2. AI 생성 이미지의 문제점(텍스트 깨짐, 부자연스러운 요소) 식별·수정 방법
3. AI 생성 이미지의 일관성 유지 방법(시드 고정, 이미지 레퍼런스 등)
4. 기획 → 이미지 생성 → 후가공 → 프로토타입으로 이어지는 AI 협업 워크플로우

---

## 진행 상태

**✅ 예습에서 완료**
- [x] 요구사항 체크리스트 작성
- [x] 팀 역할 분배안(4개 트랙) + 킥오프 플랜
- [x] 4개 트랙 예습 브리핑
- [x] 서비스 컨셉 확정(중고 책 교환 플랫폼) + 화면 3개 정의
- [x] 프롬프트 초안(v1) 3화면분 작성
- [x] 이미지 생성 도구 확정 — Adobe Firefly 접속·크레딧 실측 확인
- [x] 화면 3개(메인/목록/상세) 생성 완료 — 수정 이력(초안→실패 시도→최종) 실측 기록. 상세 화면은 저작권 이슈(실존 도서 표지 재현) 발견 → 재생성, 이후 Firefly 크레딧 소진 → Gemini 웹으로 도구 교체해 최종 성공
- [x] 후가공 완료 — placeholder 제목 교체, Dune 상태값 모순 수정, 실존 도서 표지 재현 전면 교체(화면1·2 총 6개 카드, 미셸 오바마 초상권 이슈 포함) → `design/final/`에 최종 3장 확정

- [x] 보너스① 코드 변환 체험 — 시안 3화면 HTML/CSS 변환(`bonus-code/`)
- [x] 평가 대비 QnA 정리 — 과제 목표 4가지 + 심화 질문(저작권·도구 교체·텍스트 깨짐 원리) 모범답변
- [x] 화면3 이미지 엣지투엣지 재생성(v3) + QnA Q11 추가

**🟡 진행 중 — Figma 프로토타입**
- [x] Figma 파일 생성 + 프레임 3개 이미지 배치(768×1376 정확히 맞춤)
- [x] Hotspot 1번(메인→상세), 2번(상세→메인) 연결 — 최소 요구사항 충족
- [ ] **▶ 다음 시작 지점: Hotspot 3·4·5번 연결**(메인→목록, 목록→상세, 목록→메인) — [`figma-prototype-guide.md`](figma-prototype-guide.md) 3단계 참고
- [ ] Present 모드 최종 동작 확인 → Share 링크(Anyone with the link – can view) 확보 → README·체크리스트 갱신

**⏸️ 남은 단계**
- [ ] (평가 전) QnA 답변 소리내어 연습
