# Codyssey Mission 02 — 멀티모달 콘텐츠 제작

> 과제 원문: [`codyssey/mission-02/codyssey.md`](codyssey/mission-02/codyssey.md)
> 요구사항 1:1 체크리스트: [`codyssey/mission-02/requirements-checklist.md`](codyssey/mission-02/requirements-checklist.md)

## 미션 요약

가상 브랜드 1개를 선정해 스토리보드(기획 문서)를 작성하고, 이미지·비디오·오디오 생성 AI를 각 1종 이상 사용해 10초 이내의 AI 기반 광고 영상을 완성하는 미션입니다. 기획 의도가 프롬프트를 거쳐 최종 영상으로 구현되기까지의 파이프라인을 직접 설계하고, 그 과정에서 발생한 도구 전환·프롬프트 실패·재시도를 전부 실측 기록으로 남겼습니다.

- **브랜드**: CraftFit — 사용자가 인터페이스를 직접 설계하는 커스터마이징 헬스케어 앱
- **핵심 메시지**: "헬스케어, 당신 손으로 조립하세요."
- **씬 구성**: 4씬 · 10초, 기승전결(문제 제시 → 전환 → 해결 → 브랜드 인지) 구조
- **사용 도구**: 이미지 GPT Image 2 / 영상 Google Vids(Veo 3.1) / 음성 ElevenLabs(Eleven Multilingual v2)

---

## 저장소 구조

```
codyssey/mission-02/
├── codyssey.md                    과제 원문
├── requirements-checklist.md      요구사항 원문 1:1 대조 체크리스트
└── storyboard/
    ├── storyboard.md              기획 문서(스토리보드) — 씬 구성·프롬프트·실측 결과 전체 기록
    ├── CraftFit_ad_final.mp4      최종 광고 영상 — 16:9 (필수 산출물)
    ├── CraftFit_ad_final_9x16.mp4 최종 광고 영상 — 9:16 (보너스 3)
    ├── CraftFit_ad_final_1x1.mp4  최종 광고 영상 — 1:1 (보너스 3)
    ├── image/                     최종 채택 이미지 4장 (GPT Image 2)
    ├── video/                     최종 채택 씬별 영상 4개 (Google Vids·Veo 3.1)
    ├── voice/                     나레이션 음성 4개 + 원본(raw) (ElevenLabs)
    ├── bonus1/                    보너스 1 — 립싱크 인물 사진·음성·영상
    ├── scene01-video-v1/v2.mp4    Sora 2 Pro 시도분(도구 비교 실측 자료, 보너스 2 근거)
    └── scene0*-video-vids-v*.mp4  씬별 영상 반복 버전(실패·중간본, 프롬프트 수정 근거)
```

최종 채택 파일은 `image/`·`video/`·`voice/` 폴더에 정리했고, 실패·중간 버전은 `storyboard/` 루트에 그대로 남겨 프롬프트 수정 전/후 비교의 원본 증거로 사용합니다.

---

## 산출물 1 — 스토리보드(기획) 문서

📄 최종 문서: [`storyboard/storyboard.pdf`](codyssey/mission-02/storyboard/storyboard.pdf) (PDF, 필수 산출물) · 원본: [`storyboard/storyboard.md`](codyssey/mission-02/storyboard/storyboard.md)

브랜드 아이덴티티, 캠페인 목표/핵심 메시지, 씬별 필수 필드(길이/목표 메시지/화면 구성/내레이션/사용 도구/입력 프롬프트/출력 요약/파일명)를 전부 포함합니다.

| 씬 | 길이 | 내용 | 카피 |
|---|---|---|---|
| 1 (문제 제시) | 2.47초 | 복잡하고 화려한 기존 헬스앱 UI | "난잡한 헬스케어 앱, 이제 지겨우시죠!" |
| 2 (전환) | 1.87초 | 유리 파편 전환 → 미니멀 그리드 UI 등장 | "그런 앱, 저희가 다 부쉈습니다!" |
| 3 (해결) | 2.43초 | 위젯을 직접 배치·색상 지정 | "자신에게 맞는 스타일로 앱을 만들어보세요!" |
| 4 (브랜드 인지) | 3.23초 | 완성된 대시보드 + "CraftFit" 워드마크 | "헬스케어, 단 하나뿐인 당신을 위한 앱, CraftFit" |

### 도구 선택과 전환 이력

| 유형 | 최종 도구 | 전환 이력 |
|---|---|---|
| 이미지 | GPT Image 2 | (전환 없음) |
| 영상 | Google Vids (Veo 3.1) | Sora 2 Pro(텍스트 전용) 시도 → 이미지-영상 화풍 불일치·UI 텍스트 깨짐 확인 → image-to-video를 지원하는 Google Vids로 전환 |
| 음성 | ElevenLabs (Eleven Multilingual v2) | OpenAI TTS-1 HD(nova, 인위적 AI톤 문제) → Typecast(무료 플랜 다운로드 불가 확인) → ElevenLabs(voice: Yooni, 사용자 직접 청취 후 선정)로 최종 전환 |

**대체 도구(제약 사항 "도구 접근성 대응")**: 이미지(Midjourney/Firefly, 미사용 후보) / 영상(Sora 2 Pro, 실사용 이력) / 음성(Typecast·TTS-1 HD, 실사용 이력) — 상세는 [`storyboard.md` 4번 섹션](codyssey/mission-02/storyboard/storyboard.md).

### 프롬프트 수정 전/후 — 대표 사례 2건

1. **씬4 이미지 — 워드마크 누락** ([상세](codyssey/mission-02/storyboard/storyboard.md#씬-4-프롬프트-수정-전후-과제-요구사항-최소-1개-씬-프롬프트-수정-전후-대응)): 워드마크 위치를 구체적으로 지정하지 않아 누락 → "화면 최상단 별도 헤더 영역"으로 위치를 명시하자 해결.
2. **씬2 영상 — v1~v4 4회 반복** ([상세](codyssey/mission-02/storyboard/storyboard.md#씬-2-프롬프트-수정-전후--빈-흰-화면-문제)): 빈 화면(아이콘 목록 미명시) → 아이콘 등장했으나 폰 베젤 소실("shatter" 적용 범위 미지정) → 베젤 복구했으나 워드마크 중복("유지하라" 지시가 원본 복제와 별도 처리됨) → 개수 제약(exactly ONE)으로 최종 해결.

---

## 산출물 2 — 광고 영상 (필수: 16:9 / 보너스 3: 9:16·1:1)

| 파일 | 화면비 | 스펙 |
|---|---|---|
| [`CraftFit_ad_final.mp4`](codyssey/mission-02/storyboard/CraftFit_ad_final.mp4) | 16:9 | 1920x1080 / H.264 / 30fps / AAC / 10.000초 |
| [`CraftFit_ad_final_9x16.mp4`](codyssey/mission-02/storyboard/CraftFit_ad_final_9x16.mp4) | 9:16 | 1080x1920 / H.264 / 30fps / AAC / 10.000초 |
| [`CraftFit_ad_final_1x1.mp4`](codyssey/mission-02/storyboard/CraftFit_ad_final_1x1.mp4) | 1:1 | 1080x1080 / H.264 / 30fps / AAC / 10.000초 |

**통합 편집 방식**: ffmpeg로 씬별 영상을 나레이션 길이에 맞춰 트림 → 원본 앰비언트 오디오를 나레이션으로 교체 → 4씬 concat. 9:16·1:1 버전은 새로 생성하지 않고 16:9 소스를 중앙 크롭해서 제작(사전에 각 씬 프레임을 확인해 "CraftFit" 워드마크 등 핵심 요소가 잘리지 않는지 검증). 상세 과정은 [`storyboard.md` 9번 섹션](codyssey/mission-02/storyboard/storyboard.md)에 기록.

**편집 중 발견/수정한 문제**:
- 필러박스 크롭 계획 정정 — 실제 프레임 확인 결과 검은 영역이 여백이 아니라 워드마크 등 실제 콘텐츠였음을 발견, 크롭 없이 원본 그대로 사용.
- 씬4 나레이션 오류 수정 — 통합본 v1에서 씬4에 잘못된 음성이 배치된 것을 사용자가 발견 → 올바른 대사로 교체했으나 길이가 길어져(3.99초) 10초 제한 초과 → atempo 1.2343배속 적용 + 씬1~3 길이 최소화로 정확히 10.000초 재조정.

---

## 보너스 과제

| # | 내용 | 결과 |
|---|---|---|
| 보너스 1 — 립싱크 | 별도 인물 발화 씬 추가: GPT Image 2(인물 사진) + ElevenLabs(음성) + Magic Hour Talking Photo(립싱크) | [`bonus1/`](codyssey/mission-02/storyboard/bonus1/) — 640x640 / 7.848초, 프레임별 입 모양 변화로 립싱크 작동 확인 |
| 보너스 2 — 다른 도구로 재제작 | 씬1을 Sora 2 Pro와 Google Vids 두 도구로 각각 제작해 비교 | [`storyboard.md` 11번](codyssey/mission-02/storyboard/storyboard.md) — image-to-video 지원 여부가 화풍 일관성·텍스트 정확도를 좌우함을 확인 |
| 보너스 3 — 화면비 버전 추가 | 16:9(필수) 외 9:16·1:1 버전 추가 제작 | 위 "산출물 2" 표 참고 |

---

## 재현성 기록

| 항목 | 내용 |
|---|---|
| 이미지 | GPT Image 2 / 코디세이 부트캠프 웹사이트 / 1024x1536 / 2026-07-04 |
| 영상 | Google Vids(Veo 3.1) / 9:16 세로 모드 / 2026-07-04 · Sora 2 Pro(도구 비교용) / 720x1280 / 2026-07-04 |
| 음성 | ElevenLabs / Eleven Multilingual v2 / voice: Yooni(Natural & clear) / 2026-07-06 |
| 립싱크 | Magic Hour Talking Photo(무료 플랜, 워터마크 포함) / 2026-07-06 |
| 통합 편집 | ffmpeg 명령줄(컷 편집·오디오 트랙 교체·크롭 용도로만 사용) |

## 안전/윤리 준수

- 실존 인물을 모방하지 않은, AI 생성 가상 인물만 사용(딥페이크 아님)
- 직접 촬영/유료 스톡 영상 소스 미사용 — 모든 시각·청각 소스는 생성형 AI 결과물
- 혐오/선정성/폭력 콘텐츠 생성 시도 없음
- 영상 편집(ffmpeg)은 컷 편집·오디오 교체·크롭 등 "통합 편집" 용도로만 제한적으로 사용, 핵심 비주얼/오디오는 AI 생성 결과물을 주된 소스로 유지
