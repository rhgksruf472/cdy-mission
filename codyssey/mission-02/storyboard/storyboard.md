# CraftFit — 스토리보드(기획) 문서

> 요구사항 근거: [`../codyssey.md`](../codyssey.md) 2번(최종 결과물)·4번(기능 요구 사항) / 대조: [`../requirements-checklist.md`](../requirements-checklist.md)
>
> **폴더 구조 안내**: 최종 채택 산출물은 `image/`(이미지) · `video/`(최종 영상) · `voice/`(나레이션 음성) 폴더에 정리되어 있다. 각 씬의 실패·중간 버전(예: 씬4 이미지 v1, Sora 시도분, 씬2 영상 v1~v3)은 도구 비교·프롬프트 수정 학습 근거(CLAUDE.md 2번 원칙)로 이 폴더(`storyboard/`) 루트에 그대로 보존한다.

## 1. 브랜드 아이덴티티

| 항목 | 내용 |
|---|---|
| 브랜드명 | **CraftFit** |
| 서비스 | 사용자가 인터페이스를 직접 설계하는 커스터마이징 헬스케어 앱 |
| 타겟 | 정형화된 UI에 답답함을 느끼고, 자기만의 방식으로 도구를 쓰고 싶어하는 자기주도형 사용자(미니멀·커스터마이징 취향의 얼리어답터 포함) |
| 톤앤매너 | 미니멀, 절제된 색감, 눈에 편안한 여백감, 능동적인 "메이커(제작자)" 느낌 — 화려함을 지양 |
| USP | 카테고리/기능의 배치·크기·색상·배경을 사용자가 직접 조립하는 유일한 헬스케어 앱. "무에서 유를 창조"하는 자유도 자체가 제품 |

### 배경(문제 정의 → 해결 → USP 연결)

기존 헬스케어 앱들은 임의로 정해진 인터페이스에 불필요한 기능까지 얹어, 사용자가 효율적으로 쓰기 어렵고 화려한 UI 탓에 눈이 쉽게 피로해지는 문제가 있었다. CraftFit은 반대로 완성된 인터페이스를 주지 않고 "도구"만 제공한다 — 사용자가 카테고리·기능의 배치와 크기, 색상과 배경을 직접 구성해 자신만의 헬스케어 앱을 만든다. 이 덕분에 사용자는 자신이 설계한 인터페이스로 더 빠르게 사용 숙련도를 쌓고, 남들과 다른 자기만의 앱을 갖게 된다.

## 2. 캠페인 목표 / 핵심 메시지

- **광고 목적**: 인지(Awareness) — "정해진 대로 쓰는 헬스앱"이 아니라 "내가 조립하는 헬스앱"이라는 새로운 카테고리를 각인시키고, 마지막에 다운로드(CTA)로 유도
- **핵심 메시지(한 문장)**: "헬스케어, 당신 손으로 조립하세요."

## 3. 씬 구성 (초안 — 총 4씬, 10초, 기승전결 구조)

> **상태: 초안(draft)**. 아래 표의 "필요 도구(유형)"는 기능적 필요만 표시한 것이고, 실제 도구명·프롬프트 원문·출력 결과 요약·파일명은 도구 선정 후 실제 생성 결과로 채운다(임의로 지어내지 않음 — CLAUDE.md 2번 원칙).

| 씬 | 길이 | 목표 메시지 | 화면 구성 | 내레이션/카피 | 필요 도구(유형) |
|---|---|---|---|---|---|
| 1 (문제 제시) | 2초 | 기존 헬스 앱의 답답함(정형화·과한 기능·화려한 UI로 인한 피로) | 아이콘·그래프가 빽빽하게 뒤섞인 화려하고 복잡한 헬스앱 UI, 사용자가 미간을 찌푸리며 스와이프 | "난잡한 헬스케어 앱, 이제 지겨우시죠!" | 이미지 생성(UI 목업) + 비디오 변환 |
| 2 (전환) | 2초 | 딱딱한 화면이 걷히고 미니멀한 CraftFit 빈 캔버스/블록 UI 등장 | 화면이 정리되며 빈 그리드/블록 형태 UI로 부드럽게 전환 | "그런 앱, 저희가 다 부쉈습니다!" | 비디오 변환(트랜지션) |
| 3 (해결) | 3초 | 사용자가 직접 블록을 배치·색상 지정해 자신만의 인터페이스 완성 | 손(또는 커서)이 기능 블록을 원하는 위치로 옮기고 색상 팔레트에서 톤 선택, 차분한 화면 완성 | "자신에게 맞는 스타일로 앱을 만들어보세요!" | 이미지 생성(블록 목업 시퀀스) + 비디오 변환(드래그 모션) |
| 4 (마무리/브랜드 인지) | 3초 | 완성된 미니멀 인터페이스 + 브랜드 인지 장치(로고/슬로건/CTA) | 완성된 CraftFit 화면 위로 로고·태그라인 오버레이, 하단 다운로드 CTA | "헬스케어, 단 하나뿐인 당신을 위한 앱, CraftFit" | 이미지 생성(로고/타이포) + 오디오(사운드 로고) |

전체 배경음악/효과음은 오디오 생성 도구 1종으로 전체 씬에 이어서 깔고, 4씬에서 마무리 사운드 로고로 강조하는 방향.

합계: 2+2+3+3 = **10초** (요구사항 충족).

## 4. 사용 도구 목록

| 유형 | 도구 | 사용 목적 | 선택 이유 |
|---|---|---|---|
| 이미지 생성 | GPT Image 2 | UI 목업, 블록 목업 시퀀스, 로고/타이포 생성 | 사용자 지정 |
| 음성 생성 | ~~OpenAI TTS-1 HD (nova)~~ → ~~Typecast~~ → **ElevenLabs** | 나레이션(씬 1~4 카피) | 최초엔 TTS-1 HD(nova)로 계획했으나 nova 톤이 인위적인 AI 느낌이 강하다고 판단해 Typecast로 변경. 이후 Typecast는 **무료 플랜에서 음성 파일 다운로드가 불가**하고 유료 결제 시에만 가능하다는 것이 확인되어(사용자 실사용 확인), 무료 플랜에서도 다운로드 가능한 ElevenLabs(Eleven Multilingual v2 모델)로 재전환 |
| 비디오 생성/변환 | ~~Sora 2 Pro~~ → **Google Vids (Veo 3.1)** | 이미지→모션/트랜지션 변환(전 씬) | 최초엔 Sora 2 Pro 선택(사전 Veo 3.1 테스트에서 화질 낮음 확인, 토큰 재충전 가능해 Pro 우선). 그런데 부트캠프 Sora 2 Pro가 **텍스트 전용**이라 이미지-영상 간 화풍 불일치·UI 텍스트 깨짐 문제가 실측으로 확인됨(6번 섹션 참고). Google Vids는 이미지+프롬프트를 함께 입력하는 image-to-video를 무료로 지원 — 이전에 Veo 3.1 품질이 낮았던 테스트도 Google Vids였지만, 그때는 텍스트만으로 생성한 경우였고 이번엔 이미지를 기준으로 준다는 점이 달라 재테스트 가치가 있다고 판단해 전환 |

**접속 경로**: 이미지(GPT Image 2)는 코디세이 부트캠프 웹사이트(등록 계정) / 영상(Google Vids·Veo 3.1)은 구글 계정 필요, 부트캠프 외부 무료 도구 / 음성(ElevenLabs)도 부트캠프 외부, 별도 가입 필요한 무료 플랜 도구 — 과제 원문은 특정 플랫폼을 요구하지 않고 "생성형 AI 결과물"만 요구하므로 무관. API/MCP 전부 아님 — 실제 생성 시 프롬프트 원문·출력 파일·재현성 정보(도구명/날짜/설정)는 씬별로 이 폴더에 raw 로그로 남긴다.
**Sora 2 Pro 결과 처리**: 삭제하지 않고 6번 섹션에 그대로 유지 — 보너스 2("동일 스토리보드, 다른 도구로 재제작") 및 과제 목표 3("동일 요구를 여러 도구로 시도했을 때 결과 차이 비교")에 해당하는 실측 비교 자료로 활용.

**대체 도구 준비(제약 사항 "도구 접근성 대응" 대응)**: 특정 도구가 대기열/플랜 제한으로 막힐 경우를 대비해 유형별 대체 도구를 아래와 같이 준비해둔다(도구명만 기록).

| 유형 | 주 도구 | 대체 도구(실사용 근거) |
|---|---|---|
| 이미지 생성 | GPT Image 2 | Midjourney, Adobe Firefly (미사용, 후보로만 기록) |
| 비디오 생성/변환 | Google Vids (Veo 3.1) | **Sora 2 Pro** — 실제로 씬1을 시도했다가 텍스트 전용 한계로 전환한 이력이 있어(6번 섹션), 이미 검증된 대체 경로임 |
| 오디오 생성(음성) | ElevenLabs | **Typecast**, **OpenAI TTS-1 HD** — 둘 다 실제로 검토·시도했던 이력이 있음(도구 전환 이력 참고) |

## 5. 씬별 입력 프롬프트 (이미지 생성 — GPT Image 2)

> **상태: 씬 1~4 실제 생성 완료.** 재현성: GPT Image 2 / 코디세이 부트캠프 웹사이트 / 1024x1536 / 2026-07-04. 일관성 유지를 위해 모든 씬에 아래 **공통 스타일 앵커**를 프롬프트 앞에 고정해서 사용했다(제약사항 "일관성 유지 팁" 대응).

**이미지 생성 크기**: GPT Image 2 제공 옵션(1024x1024 / 1536x1024 / 1024x1536) 중 세로형인 **1024x1536**로 확정. 단, 이는 2:3 비율(0.667)이라 최종 영상 목표 비율인 9:16·1080x1920(0.5625, 과제 원문 보너스 3 기준)보다 덜 길쭉하다. Sora 2 Pro로 영상 변환 시 위아래가 잘리거나 확장될 수 있으므로, 로고·CTA·인물 등 핵심 요소는 프레임 중앙에 여유 여백을 두고 배치해 잘려도 안전하게 설계한다(아래 프롬프트에 반영).

**공통 스타일 앵커(모든 씬 프롬프트 앞에 고정)**
```
Minimalist flat UI mockup on a modern smartphone screen, consistent clean sans-serif typography, calm color palette (sage green #8FA998 accent, off-white #F5F3EE background, charcoal #2B2B2B text), soft even studio lighting, high detail, 1024x1536 portrait composition with key elements centered and generous top/bottom safe margin (composition must survive cropping to a taller 9:16 frame), no watermark.
```

| 씬 | 입력 프롬프트(원문, 스타일 앵커 뒤에 이어붙임) | 출력 결과 요약 | 결과 파일명 |
|---|---|---|---|
| 1 | Smartphone screen mockup showing an overwhelming, cluttered fitness/health app home screen: dozens of overlapping colorful widgets, neon gradient buttons, small crowded icons, multiple pop-up notification badges, busy overlapping charts and graphs, garish clashing colors (hot pink, neon yellow, electric blue). A hand holds the phone, slightly blurred, with a faint reflection of a squinting, fatigued face on the glossy screen glass. Mood: visual overload, eye strain. | 의도대로 매우 복잡하고 화려한 헬스앱 UI 생성됨(점수/칼로리/수분/심박/수면/체중/식사/업적/친구목록/PRO 업그레이드 등 위젯 15개 이상 과밀). 네온 핑크·옐로우·블루 색 충돌도 잘 표현됨. 화면 뒤로 흐릿한 인물 얼굴(눈 감은 피곤한 표정)이 겹쳐 보여 "피로감" 연출도 의도에 부합. | [scene01-image.png](image/scene01-image.png) |
| 2 | Smartphone screen mid-transition: left half still shows fading fragments of the cluttered colorful UI from scene 1, right half has already turned into a clean empty grid canvas with soft dotted-outline placeholder blocks on an off-white background, sage green glow along the transition seam, small "CraftFit" wordmark fading in faintly at the top in charcoal sans-serif. Calm, hopeful mood, soft diagonal light sweep. | 화면 좌측은 복잡한 기존 UI, 우측은 빈 아이콘 placeholder 그리드로 정확히 절반씩 전환되는 구도로 생성됨. "CraftFit" 워드마크가 우측 상단에 선명하게(의도보다 더 또렷하게) 표시됨 — 라틴 문자 렌더링은 안정적임을 확인. | [scene02-image.png](image/scene02-image.png) |
| 3 | Smartphone screen showing a minimal custom health app interface being assembled: a rounded rectangular widget block labeled "걸음 수" is being dragged by a stylized fingertip cursor into an empty grid slot, two other widget blocks already neatly placed nearby, a small circular color-palette selector floating to the side with a fingertip choosing a soft sage-green swatch. Orderly, spacious, calm, satisfying "assembling" feeling. | 의도대로 "걸음 수" 위젯 카드를 손 커서가 빈 점선 슬롯 쪽으로 드래그하는 장면과, 우측 하단 원형 색상 선택 UI(초록 선택 중)가 정확히 생성됨. **한글 타이포("내 건강 대시보드", "위젯을 드래그하여 나만의 대시보드를 만들어보세요.", "수면 시간", "걸음 수" 등)가 전부 정확하게 렌더링됨** — 사전에 우려했던 한글 깨짐 리스크가 이 씬에서는 발생하지 않음(아래 갱신 노트 참고). | [scene03-image.png](image/scene03-image.png) |
| 4 (v2, 최종 채택) | *(v1 프롬프트 + 아래 수정 전/후 참고의 추가 지시문)* | 톤앤매너(세이지그린·오프화이트, 여백감, 프리미엄한 느낌)는 v1과 동일하게 유지되면서, **"CraftFit" 워드마크가 화면 최상단 별도 헤더 영역에 명확하게 렌더링됨** — 위젯 그리드와 분리되어 씬 2와 동일한 배치 방식으로 잘 나옴. 수정 프롬프트 의도가 그대로 재현됨. | [scene04-image-v2.png](image/scene04-image-v2.png) |

### 씬 4 프롬프트 수정 전/후 (과제 요구사항 "최소 1개 씬 프롬프트 수정 전/후" 대응)

- **수정 전(v1) 프롬프트**: Smartphone screen showing the finished custom minimal health app home screen with neatly arranged personalized widget blocks in soft sage-green and off-white tones, calm and premium product-shot feel.
- **v1 결과**: 톤앤매너는 의도대로 나왔으나 **"CraftFit" 워드마크가 화면에 전혀 나타나지 않음** ([scene04-image-v1.png](scene04-image-v1.png)).
- **문제 원인 추정**: 워드마크 위치를 구체적으로 지정하지 않고 "브랜드 워드마크만 포함"이라고만 지시해, 다른 디테일(위젯 배치·색감)에 밀려 무시된 것으로 보임(씬 2에서는 워드마크가 화면의 명확히 분리된 상단 영역에 배치되도록 구도가 설계돼 있어 잘 나온 것과 대비됨).
- **수정 후(v2) 프롬프트**: v1 프롬프트 끝에 다음을 추가 — `"CraftFit" wordmark must appear clearly at the very top of the screen in charcoal sans-serif, in its own clear header area separate from the widget grid below it (same placement style as scene 2).`
- **v2 결과**: 의도한 대로 화면 최상단 별도 헤더 영역에 "CraftFit" 워드마크가 명확하게 렌더링됨 ([scene04-image-v2.png](image/scene04-image-v2.png)). **위치를 구체적으로(화면 최상단, 별도 헤더 영역, 씬 2와 동일 배치) 명시하면 요소 누락이 해결된다는 것을 확인** — 이번 미션의 "프롬프트 설계·수정" 학습 목표(과제 목표 2번)에 해당하는 실측 사례.
- **최종 채택**: v2를 씬 4 최종 산출물로 사용.

### 실증 결과 반영 — 한글 텍스트 처리 전략 갱신

애초에 "한글 타이포는 깨질 위험이 있다"고 예상해 태그라인/CTA를 편집 단계 자막으로 미루기로 했었는데, **씬 3 실제 결과에서는 한글이 전부 정확하게 렌더링됨**. 즉 위험이 아예 없는 건 아니지만(씬 4의 워드마크 누락처럼 다른 방식의 실패는 발생), 최소한 "한글이 깨져서 나온다"는 우려는 이번 실측에서는 재현되지 않았다. 그래도 최종 광고에 들어갈 정확한 문구(태그라인/CTA)는 실패 시 재생성 크레딧 낭비를 막기 위해 기존 계획대로 편집 단계 자막으로 유지하는 것을 권장한다 — 다만 사용자가 원하면 씬 4 재생성 시 한글 태그라인을 직접 넣어 테스트해봐도 된다(허용된 실험).

## 6. 씬별 입력 프롬프트 (영상 변환 — Sora 2 Pro, 1차 시도·도구 비교용)

> **상태: 씬 1만 실제 시도(v1/v2) 후 도구 전환. 씬 2~4는 생성하지 않음.** 이미지 입력이 안 되는 텍스트 전용 구조 때문에 화풍 불일치·UI 텍스트 깨짐 문제가 씬 1에서 반복 확인돼, 최종 영상 생성 도구를 7번 섹션의 Google Vids(Veo 3.1, 이미지+텍스트 입력)로 전환했다. 이 섹션은 삭제하지 않고 **보너스 2("동일 스토리보드, 다른 도구로 재제작") 및 과제 목표 3(도구 간 결과 비교)의 실측 근거**로 남겨둔다.
>
> **도구 제약 확인(설계 변경)**: 당초 씬 이미지를 입력으로 넣는 image-to-video 방식으로 설계했으나, 실제 부트캠프 Sora 2 Pro 화면은 **이미지 입력이 불가하고 텍스트 프롬프트만으로 생성**되는 것으로 확인됨. 그래서 아래 프롬프트는 이미지 참조 없이 장면을 처음부터 전부 텍스트로 서술하도록 다시 설계했다. 이로 인해 이미지(씬 1~4 PNG)와 영상이 서로 다른 모델의 독립 생성물이 되어 **완전한 픽셀 단위 일치는 보장되지 않는다** — 이는 과제 원문 1번(미션 소개)이 명시한 "멀티모달 제작에서 빈번히 발생하는 문제(캐릭터/화풍 불일치)"에 해당하는 실제 사례다. 동일한 공통 스타일 앵커(색상 팔레트·타이포·레이아웃 서술)를 이미지·영상 프롬프트 모두에 반복 적용해 화풍 일관성을 최대한 유지하는 방식으로 대응한다.
>
> **해상도**: Sora 2 Pro는 비율 입력이 없고 해상도만 선택 가능(1280x720 / 720x1280 중 택1). **720x1280**로 확정 — 정확히 9:16 비율(0.5625)이며, 과제 원문의 "저사양/제약 허용: 해상도 720p 이상" 조항에 해당해 요구사항에 부합한다.
>
> **영상 길이**: 4초/8초/12초 중 택1만 가능(임의 길이 불가). 씬별 목표 길이(2/2/3/3초)를 직접 만들 수 없으므로, **모든 씬을 최소 단위인 4초로 생성한 뒤, 편집 단계에서 각 씬의 목표 길이만큼 컷 편집으로 잘라 쓴다**(제약사항에서 명시적으로 허용된 "컷 편집" 범위 내 — AI 생성물이 주 소스라는 원칙도 그대로 유지됨).

| 씬 | 목표 길이(편집 후) | 생성 길이 | 입력 프롬프트(원문) | 출력 결과 요약 | 결과 파일명 |
|---|---|---|---|---|---|
| 1 (문제 제시, v1 시도) | 2초 | 4초 | *(이 시도는 위 프롬프트가 아니라 5번 섹션의 씬 1 **이미지 생성용** 프롬프트를 그대로 재사용해서 생성됨 — 아래 "씬 1 v1 결과 및 재시도 필요성" 참고)* | 재현성: Sora 2 Pro / 코디세이 부트캠프 웹사이트 / 2026-07-04. 실제 확인 결과 **해상도 1280x720(가로형)**로 생성됨 — 목표였던 720x1280(세로형)과 반대. 화면 내용은 복잡하고 화려한 헬스앱 UI(네온 핑크·그린·블루, 걸음수 12,492, 심박 98bpm 등 위젯 다수)로 "과부하" 컨셉 자체는 잘 표현됨. 다만 **8프레임을 살펴본 결과 4초 내내 손·화면이 거의 정지 상태 — 요청했던 알림 배지 깜빡임, 카메라 미세 흔들림, 반사된 피곤한 얼굴 등 모션·디테일이 전혀 나타나지 않음.** 이미지용 프롬프트에는 애초에 모션 지시가 없어서 정지 영상처럼 나온 것으로 추정. | [scene01-video-v1.mp4](scene01-video-v1.mp4) |
| 1 (문제 제시, v2) | 2초 | 4초 | A modern smartphone screen mockup, seen from a slight angle, held by a hand entering from the bottom-left with a subtle restless micro-jitter. The screen shows an overwhelming, cluttered fitness/health app home screen: dozens of overlapping colorful widgets (streak badge, score ring, calorie goal bar, water tracker, heart rate, sleep, weight, achievements, flash-sale banner, friends leaderboard), neon gradient buttons, small crowded icons, multiple notification badges pulsing rapidly, garish clashing colors (hot pink, neon yellow, electric blue, purple). Faintly visible through the glossy screen glass, a blurred reflection of a person's face, eyes closed, brow tightening as if wincing with fatigue over the 4 seconds. Camera: static handheld with subtle micro-shake, close-up product shot. Mood: visual overload, restless. Vertical 9:16 portrait composition, no watermark, no text overlays beyond the app UI itself. | 재현성: Sora 2 Pro / 코디세이 부트캠프 웹사이트 / 2026-07-04 / 해상도 720x1280 지정. **해상도 문제는 해결됨(720x1280 세로형으로 정확히 생성)**. 전체적으로 자주색·네온 톤의 빽빽한 위젯 화면(칼로리/체중/심박/수면/친구 목록 등)이라 "과부하" 컨셉 자체는 v1과 마찬가지로 잘 유지됨. 다만 (1) **화면 속 UI 텍스트 다수가 깨져서 나옴**("Alhorieboard"=Leaderboard 추정, "Add Wood"=의미불명, "Sleep 5h 112m"=수치 비정상, "3 soh/4 son/2 soh"=의미불명) — 영상 생성 모델이 이미지 생성 모델보다 상세 UI 텍스트 렌더링에 약하다는 실제 근거. (2) 8프레임을 비교해도 손·화면 구도에 뚜렷한 변화가 보이지 않아 **요청한 배지 깜빡임·카메라 흔들림·얼굴 반사 요소는 이번에도 명확히 확인되지 않음**(단, 프레임 샘플링이 2fps로 성글어 미세한 움직임까지는 못 잡았을 가능성 있음). | [scene01-video-v2.mp4](scene01-video-v2.mp4) |
| 2 (전환) | 2초 | 4초 | *(미실행 — 7번 섹션 Google Vids 방식으로 진행)* | 미실행 | — |
| 3 (해결) | 3초 | 4초 | *(미실행 — 7번 섹션 Google Vids 방식으로 진행)* | 미실행 | — |
| 4 (마무리/브랜드 인지) | 3초 | 4초 | *(미실행 — 7번 섹션 Google Vids 방식으로 진행)* | 미실행 | — |

씬 1만 v1/v2 두 번 실제 시도(위 결과 참고), 씬 2~4는 도구 전환으로 생성하지 않음.

### 씬 1 v1 결과 및 재시도 필요성 (프롬프트 수정 전/후 추가 사례)

- **v1(전) 프롬프트**: 5번 섹션의 GPT Image 2용 이미지 프롬프트를 그대로 Sora 2 Pro에 입력 — 화면 구성만 서술하고 카메라/모션 지시가 전혀 없음.
- **v1 결과**([scene01-video-v1.mp4](scene01-video-v1.mp4)): `watch` 스킬로 8프레임을 확인한 결과, 4.1초 내내 손과 화면이 사실상 완전히 정지된 이미지처럼 보임 — 요청했던 알림 배지 깜빡임·카메라 미세 흔들림·반사된 피곤한 얼굴 중 어느 것도 나타나지 않음. 해상도도 1280x720(가로형)으로 확인돼 목표(720x1280, 세로형)와 반대로 나옴.
- **문제 원인**: (1) 이미지 생성용 프롬프트는 "정지된 한 장면"을 묘사하는 문법이라 모션 동사가 없어 영상 도구가 애니메이션을 만들 근거가 없었음. (2) 해상도는 프롬프트 텍스트가 아니라 별도 선택 파라미터라 텍스트에 "vertical 9:16"이라고 써도 반영되지 않음 — 반드시 해상도 선택 UI에서 720x1280을 직접 골라야 함.
- **수정 후(v2) 대응**: 이미지 프롬프트와 별도로, 위 표의 "v2 재시도용" 프롬프트처럼 카메라 움직임·모션 지시(미세 흔들림, 배지 깜빡임, 표정 변화)를 명시적으로 추가. 생성 시 해상도 드롭다운에서 **720x1280을 직접 선택**.
- **학습 포인트**: 이미지 생성 프롬프트와 영상 생성 프롬프트는 문법이 다르다 — 정지 장면 묘사만으로는 영상 도구가 움직임을 만들지 않으므로, 반드시 시간 경과에 따른 변화(모션 동사·순서)를 프롬프트에 넣어야 한다. 또한 비율/해상도는 텍스트 프롬프트가 아니라 도구의 별도 설정값으로 제어된다.
- **v2 결과**([scene01-video-v2.mp4](scene01-video-v2.mp4)): 해상도 문제는 해결(720x1280 세로형 확정). 다만 새로운 문제 발견 — **화면 속 UI 텍스트가 다수 깨져서 나옴**(예: "Alhorieboard", "Add Wood", "Sleep 5h 112m" 등 의미 불명 문자열), 모션도 8프레임 비교상 여전히 뚜렷하게 확인되지 않음.
- **추가 학습 포인트**: 영상 생성 모델(Sora 2 Pro)은 이미지 생성 모델(GPT Image 2)보다 화면 속 상세 UI 텍스트를 정확히 렌더링하는 능력이 약하다는 것을 실측으로 확인 — 과제 목표 1번("텍스트/이미지/비디오/오디오 생성 도구의 역할과 차이(강점/약점)를 설명할 수 있다")에 해당하는 근거 사례로 기록.
- **현재 결정**: 씬 1은 "문제 제시" 장면이라 텍스트 정확도보다 전반적인 "복잡하고 화려해서 피로한 느낌"이 더 중요 — 텍스트가 완벽히 안 읽혀도 컨셉 전달에는 큰 지장이 없다고 보고, v2를 잠정 채택. 이후 씬 2~4에서도 비슷한 텍스트 깨짐이 나오는지 계속 관찰 필요(특히 씬 2의 "CraftFit" 워드마크, 씬 4의 브랜드 마크는 텍스트 정확도가 중요하므로 결과를 더 엄격히 확인할 것).

## 7. 씬별 입력 프롬프트 (영상 변환 — Google Vids / Veo 3.1, 이미지+텍스트)

> **상태: 설계 완료(입력 프롬프트) / 출력 결과 미실행.** Google Vids는 이미지 입력 + 텍스트 프롬프트를 함께 받는 image-to-video 방식을 무료로 지원해, 당초 설계(6번 섹션 이전 버전)대로 각 씬의 **최종 채택 이미지를 기준 프레임으로 직접 입력**하고 모션만 텍스트로 지시한다. 이 방식이 Sora 2 Pro의 텍스트 전용 방식보다 이미지-영상 간 일관성이 높을 것으로 기대되며, 씬 1은 이미 Sora로 시도한 적이 있어 직접적인 도구 비교가 가능하다.
>
> **해상도**: Google Vids는 가로 모드 / 9:16 세로 모드 중 선택. **9:16 세로 모드**로 확정(목표 비율과 일치).
> **영상 길이**: 실제 확인 결과 **8초 고정**(4초 아님 — 씬 1 실제 생성 후 정정). Vids 자체 편집 기능으로 자를 수 있어, 8초로 생성한 뒤 각 씬 목표 길이(2/2/3/3초)로 트리밍한다.
> **재현성 메모**: 이전에 Google Vids의 Veo 3.1을 텍스트만으로 생성했을 때는 품질이 낮았던 적이 있음(사용자 실사용 경험) — 이번엔 이미지를 기준 프레임으로 제공한다는 차이가 있어 재테스트하는 것이며, 같은 품질 문제가 재현되는지도 함께 확인 대상이다.

| 씬 | 입력 이미지 | 목표 길이(편집 후) | 생성 길이 | 모션 프롬프트(원문) | 출력 결과 요약 | 결과 파일명 |
|---|---|---|---|---|---|---|
| 1 (문제 제시) | [scene01-image.png](image/scene01-image.png) | 2초 | 8초 | Animate this UI mockup image with extremely subtle handheld camera micro-jitter, as if held by a slightly restless hand. Notification badges softly pulse/flicker in quick succession (2-3 pulses) to suggest sensory overload. The blurred reflected face's brow tightens slightly as if wincing. Keep the exact same color palette, layout, and composition as the source image — do not add or remove any UI elements. Mood: overwhelming, restless. | 재현성: Google Vids(Veo 3.1) / 2026-07-04 / 9:16 세로 모드 지정. **화면 구도·색감·소품 배치가 원본 scene01-image.png와 매우 유사하게 유지됨** — Sora 시도 때보다 이미지-영상 일관성이 뚜렷하게 좋음(이미지 기준 프레임 입력의 효과로 보임). 12프레임 비교 결과 **빨간 알림/경고 아이콘들이 시간에 따라 화면 전체에 나타났다 옅어지는 펄스 효과가 실제로 관찰됨** — 요청했던 "알림 배지 깜빡임"이 부분적으로 재현됨. 다만 손·카메라 미세 흔들림과 반사된 얼굴 요소는 이번에도 확인되지 않음. **주의(기술적 이슈)**: 출력 파일 자체는 1920x1080(가로 컨테이너)이고 그 안에 세로 영상이 좌우 검은 여백과 함께 담긴 필러박스 상태 — 최종 편집 시 검은 여백을 크롭해서 순수 세로 프레임만 남겨야 함. | [scene01-video-vids-v1.mp4](video/scene01-video-vids-v1.mp4) |
| 2 (전환, v1) | [scene02-image.png](image/scene02-image.png) | 2초 | 8초 | Animate this UI transition image: the cluttered fragments on the left continue dissolving and fading away while the clean empty grid on the right expands smoothly to fill the entire frame by the end of the clip. A soft sage-green light sweep travels left to right across the screen during the wipe. The "CraftFit" wordmark at the top gently settles and stabilizes as the transition completes. Keep the same color palette and style as the source image. Mood: calm, hopeful release. | 재현성: Google Vids(Veo 3.1) / 2026-07-04 / 9:16 세로 모드. **"CraftFit" 워드마크는 상단에 정확하고 안정적으로 렌더링·유지됨(성공).** 전환 연출은 "좌우 분할 와이프" 대신 **화면이 깨진 유리처럼 산산조각나며 사라지는 연출**로 대체 해석됨(초록빛 스윕도 대각선으로 함께 나타남 — 컨셉 자체는 크게 벗어나지 않음). **다만 사용자가 확인한 대로, 전환이 끝난 뒤 목적지 화면이 요청한 "점선 아이콘 placeholder 그리드"가 아니라 완전히 빈 흰 화면으로만 나옴** — 8초 중 후반 5초 내내 흰 화면 유지. 또한 시작 프레임(전환 전) UI가 원본 scene02-image.png(헬스앱 스트릭·챌린지 위젯)와 다르게 메신저/채팅 앱 느낌의 UI로 나와 이미지 재현도가 씬 1보다 낮음. | [scene02-video-vids-v1.mp4](scene02-video-vids-v1.mp4) |
| 2 (전환, v2) | [scene02-image.png](image/scene02-image.png) | 2초 | 8초 | Animate this UI transition image: the cluttered fragments of the colorful health-tracking app UI (streak badge, points, daily challenge card) shatter and dissolve away like breaking glass, revealing a calm minimalist screen underneath. As the shards clear, the destination screen must fill with a clearly visible 2x3 grid of soft dotted-outline placeholder icon cards — a photo/image icon, a dumbbell icon, a fork-and-knife icon, a circular progress ring icon, a calendar icon, and a bar-chart icon — plus a circular "+" add button, all on an off-white background. The grid of icon placeholders must be clearly visible and must NOT be a blank empty white screen. A soft sage-green light sweep travels across the screen during the transition. The "CraftFit" wordmark stays fixed and clearly legible at the very top in its own header area throughout. Keep the same color palette and style as the source image. Mood: calm, hopeful release. | 재현성: Google Vids(Veo 3.1) / 2026-07-04 / 9:16 세로 모드. **아이콘 그리드 문제는 해결됨** — 이미지/덤벨/포크나이프/원형링/캘린더/막대그래프 아이콘과 "+" 버튼이 요청한 대로 정확히 렌더링됨(사진 아이콘엔 "Ph" 텍스트까지 정확히 표시). 다만 **새로운 문제 발견(사용자 확인)**: 유리 파편 연출이 지나가고 난 뒤, 아이콘 그리드가 **스마트폰 기기 베젤/프레임 없이 배경에 그대로 노출됨** — 앞부분(전환 전)에는 폰 베젤이 있었는데, 파편 효과 도중 폰 틀 자체가 함께 부서져 사라지고 화면 내용만 남은 것으로 보임. 이 때문에 다른 씬들과 달리 "폰 목업 안에 담긴 화면"이라는 일관된 프레이밍이 깨짐. | [scene02-video-vids-v2.mp4](scene02-video-vids-v2.mp4) |
| 2 (전환, v3) | [scene02-image.png](image/scene02-image.png) | 2초 | 8초 | Animate this UI transition image: the cluttered fragments of the colorful health-tracking app UI (streak badge, points, daily challenge card) shatter and dissolve away like breaking glass, revealing a calm minimalist screen underneath. **Throughout the entire clip, the smartphone device itself — its bezel, frame, and notch — must remain fully intact and visible; only the on-screen UI content shatters and changes, never the phone hardware.** As the shards clear, the destination screen (still framed inside the phone's screen area) must fill with a clearly visible 2x3 grid of soft dotted-outline placeholder icon cards — a photo/image icon, a dumbbell icon, a fork-and-knife icon, a circular progress ring icon, a calendar icon, and a bar-chart icon — plus a circular "+" add button, all on an off-white background, contained within the phone screen. A soft sage-green light sweep travels across the screen during the transition. The "CraftFit" wordmark stays fixed and clearly legible at the very top in its own header area (above the phone, as in the source image) throughout. Keep the same color palette and style as the source image. Mood: calm, hopeful release. | 재현성: Google Vids(Veo 3.1) / 2026-07-04 / 9:16 세로 모드. **폰 베젤 문제는 해결됨** — 클립 내내 스마트폰 프레임·노치가 온전히 유지된 채로 화면 내용만 파편 효과 후 바뀜(바닥에 은은한 반사 효과까지 추가돼 프리미엄한 느낌 오히려 강화). 아이콘도 덤벨·포크나이프·식사 아이콘·원형 링(막대그래프 포함)+초록 "+" 버튼으로 대체로 잘 나옴(2x3 대신 2x2+버튼 구성으로 약간 단순화됐지만 컨셉은 충족). **다만 새로운 문제 발견(사용자 확인): 상단 헤더에 "CraftFit" 워드마크가 두 줄로 중복 표시됨**("CraftFit" / "CraftFit™" 형태로 겹쳐 나옴) — 클립 전체 구간에서 계속 중복 상태 유지. | [scene02-video-vids-v3.mp4](scene02-video-vids-v3.mp4) |
| 2 (전환, v4, 최종 채택) | [scene02-image.png](image/scene02-image.png) | 2초 | 8초 | Animate this UI transition image: the cluttered fragments of the colorful health-tracking app UI (streak badge, points, daily challenge card) shatter and dissolve away like breaking glass, revealing a calm minimalist screen underneath. Throughout the entire clip, the smartphone device itself — its bezel, frame, and notch — must remain fully intact and visible; only the on-screen UI content shatters and changes, never the phone hardware. As the shards clear, the destination screen (still framed inside the phone's screen area) must fill with a clearly visible 2x3 grid of soft dotted-outline placeholder icon cards — a photo/image icon, a dumbbell icon, a fork-and-knife icon, a circular progress ring icon, a calendar icon, and a bar-chart icon — plus a circular "+" add button, all on an off-white background, contained within the phone screen. A soft sage-green light sweep travels across the screen during the transition. **There is exactly ONE "CraftFit" wordmark on screen at any time, shown once at the very top in its own header area — do not duplicate, repeat, or stack the wordmark text.** Keep the same color palette and style as the source image. Mood: calm, hopeful release. | 재현성: Google Vids(Veo 3.1) / 2026-07-04 / 9:16 세로 모드. **워드마크 중복 문제 해결** — "CraftFit"이 한 줄로 깔끔하게 한 번만 표시됨. 폰 베젤도 v3처럼 계속 유지됨. 목적지 아이콘은 정확히 6개(2x3)는 아니고 **4개(운동 관련 아이콘 2종 + 포크나이프 + 원형 링)+ "+" 버튼**으로 단순화돼 나왔지만, "빈 화면"이었던 v1과 달리 아이콘이 있는 그리드라는 컨셉 자체는 충족. 유리 파편 전환 연출도 그대로 유지. **최종 채택**: 3번의 반복 수정 끝에 핵심 문제(빈 화면·베젤 소실·워드마크 중복)가 모두 해결된 v4를 씬 2 최종본으로 확정. | [scene02-video-vids-v4.mp4](video/scene02-video-vids-v4.mp4) |
| 3 (해결, 최종 채택) | [scene03-image.png](image/scene03-image.png) | 3초 | 8초 | Animate this UI mockup image: the "걸음 수" widget card, currently held by the fingertip cursor, glides smoothly down and to the left into the empty dashed grid slot and snaps into place with a soft, satisfying bounce. Immediately after, the fingertip at the color-palette selector taps the sage-green swatch, and the just-placed widget's accent color subtly shifts to match sage green. Static camera, shallow depth of field, no new elements beyond the source image. Mood: satisfying, orderly assembly. | 재현성: Google Vids(Veo 3.1) / 2026-07-04 / 9:16 세로 모드. **1차 시도만에 성공.** "내 건강 대시보드" 타이틀, 부제, "수면 시간 7시간 30분", "오늘의 마음 좋음", "걸음 수 8,247 걸음" 등 **한글 텍스트가 전부 정확하게 유지됨**(씬 3 이미지 결과와 동일하게 이번에도 한글 렌더링 성공). 색상 팔레트 패널이 확장되며 손가락이 스와치를 탭하는 동작도 잘 나타났고, 마지막엔 팔레트가 사라지며 걸음 수 위젯에 작은 상승 그래프가 추가된 차분한 최종 화면으로 마무리됨. 이 씬은 원본 이미지 자체가 폰 베젤 없는 클로즈업 구도라 씬 1·2에서 있었던 "베젤 소실" 문제가 애초에 해당 없음. 유일한 사소한 흠은 위젯 카드가 슬롯으로 옮겨가는 중간 과정이 매끄러운 글라이드보다는 살짝 끊기듯(디졸브에 가깝게) 전환되는 정도 — 서사에 지장 없어 그대로 채택. | [scene03-video-vids-v1.mp4](video/scene03-video-vids-v1.mp4) |
| 4 (마무리/브랜드 인지, 최종 채택) | [scene04-image-v2.png](image/scene04-image-v2.png) | 3초 | 8초 | Animate this finished dashboard image with a slow, smooth cinematic push-in (Ken Burns zoom) moving toward a slightly closer framing centered on the "CraftFit" wordmark at the top. In the final half-second, add a soft, subtle glow/shimmer pulse behind the wordmark to draw attention to the brand mark. Keep the same layout, colors, and content as the source image — do not add any new text. Mood: calm, confident, premium. | 재현성: Google Vids(Veo 3.1) / 2026-07-04 / 9:16 세로 모드. **1차 시도만에 성공, 요청한 3가지가 전부 재현됨**: ① 완성된 대시보드(걸음 7,842·영양 1,650·운동·수면 7h 32m)가 원본 scene04-image-v2.png와 색감·레이아웃 모두 일치, ② 부드러운 켄번즈 줌인으로 "CraftFit" 워드마크에 점점 클로즈업, ③ 마지막 프레임에서 워드마크 뒤로 은은한 반짝임(glow/shimmer) 효과 확인. **"CraftFit" 워드마크는 최종적으로 한 번만, ® 마크와 함께 선명하게 표시됨** — 줌 전환 중간(4초 지점) 한 프레임에서 모션 블러로 텍스트가 살짝 겹쳐 보이는 순간이 있었지만 이는 카메라 무브먼트에 의한 일시적 잔상이고, 씬 2에서처럼 최종 상태까지 중복 유지되는 문제는 아님. 사소한 흠: 배경 라벨 중 "Steps Today"가 "Steps Turay"로 약간 오타처럼 나왔으나 곧 줌으로 가려져 눈에 크게 띄지 않음. | [scene04-video-vids-v1.mp4](video/scene04-video-vids-v1.mp4) |

**전 씬 영상 생성 완료** — 씬 1(Sora 폐기/Vids 채택)·2(v4)·3(v1)·4(v1) 전부 Google Vids(Veo 3.1)로 확정.

**크롭 계획 정정(9번 섹션 최종 편집 참고)**: 당초 4개 클립을 "1920x1080 필러박스, 좌우 검은 여백"으로 추정해 크롭이 필요하다고 적었으나, 최종 편집 단계에서 실제 프레임을 직접 열어 확인한 결과 이는 잘못된 추정이었다 — 검게 보였던 영역은 빈 여백이 아니라 "CraftFit" 워드마크·배경 연출이 들어간 실제 콘텐츠였다(자동 크롭 감지 결과도 전 프레임에서 크롭 불필요로 확인됨). 크롭했다면 오히려 워드마크가 잘릴 뻔했다. 과제 원문은 화면비를 고정하지 않으므로(9:16은 보너스 3에서만 필요) 원본 1920x1080(16:9) 그대로 사용하기로 변경.

합계(편집 후): 2+2+3+3 = **10초**(설계 목표) → 실제로는 나레이션 길이에 맞춰 2.57+1.97+2.53+2.93 = **정확히 10.00초**로 미세 조정(9번 섹션 참고). 생성은 씬당 8초 × 4씬, 편집에서 목표 길이로 트리밍.

### 씬 1 도구 비교 — Sora 2 Pro vs Google Vids(Veo 3.1)

| 항목 | Sora 2 Pro (v1/v2) | Google Vids (Veo 3.1) |
|---|---|---|
| 이미지 기준 입력 | 불가(텍스트 전용) | 가능 |
| 이미지-영상 화풍 일관성 | 낮음(독립 생성이라 구도·색감 다름) | 높음(원본 이미지와 매우 유사) |
| 요청한 모션(배지 깜빡임 등) | 거의 없음(정지 영상에 가까움) | 부분 재현(빨간 경고 아이콘 펄스 확인) |
| 카메라 흔들림·얼굴 반사 | 미확인 | 미확인 |
| 해상도 문제 | v1은 가로/세로 반대, v2에서 해결 | 세로 모드 선택했지만 1920x1080 필러박스로 출력(크롭 필요) |
| UI 텍스트 정확도 | 다수 깨짐("Alhorieboard" 등) | 씬 1은 상세 텍스트 요구가 적어 비교 애매 — 씬 2·4에서 "CraftFit" 유지 여부로 추가 확인 예정 |

**중간 결론**: 이미지 기준 입력 덕분에 Google Vids 쪽이 화풍 일관성·모션 재현에서 우세. 다만 필러박스 크롭이라는 새로운 후반작업 단계가 필요함. 씬 2~4 결과까지 보고 최종 채택 도구를 확정한다.

### 씬 2 프롬프트 수정 전/후 — "빈 흰 화면" 문제

- **v1 결과**([scene02-video-vids-v1.mp4](scene02-video-vids-v1.mp4)): "CraftFit" 워드마크는 성공적으로 유지됐지만, 전환 후 목적지 화면이 요청한 점선 아이콘 그리드가 아니라 **완전히 빈 흰 화면**으로 나옴(사용자 확인).
- **문제 원인 추정**: 프롬프트에서 목적지를 "a calm minimalist empty grid canvas... soft dotted-outline placeholder blocks"라고만 서술해, "empty"라는 단어에 모델이 이끌려 정말 아무것도 없는 흰 화면으로 단순하게 해석한 것으로 보임. 이미지에는 실제로 이미지/덤벨/식사/원형 진행률/캘린더/막대그래프 아이콘이 점선 카드 안에 배치돼 있었는데, 텍스트 프롬프트가 그 구체적인 아이콘 목록을 반복하지 않아 정보가 누락됨.
- **수정 후(v2) 대응**: 목적지 그리드에 들어갈 아이콘을 구체적으로 나열하고, "반드시 빈 화면이 아니어야 한다(must NOT be a blank empty white screen)"는 부정 지시를 명시적으로 추가. 시작 프레임도 원본 이미지의 실제 위젯(스트릭 배지·포인트·데일리 챌린지)을 다시 언급해 이미지 재현도를 높이려 시도.
- **학습 포인트**: 이미지-투-비디오에서도 이미지에 있는 세부 내용을 텍스트 프롬프트가 반복해서 강조하지 않으면 모델이 단순화(예: "그리드"→"빈 화면")해서 해석할 수 있다. 이미지 입력이 있다고 해서 텍스트 설명을 소홀히 하면 안 된다는 실측 근거.
- **v2 결과**([scene02-video-vids-v2.mp4](scene02-video-vids-v2.mp4)): **아이콘 그리드 문제는 해결** — 요청한 6개 아이콘 + "+" 버튼이 정확히 렌더링됨. 그런데 **새 문제 발생: 유리 파편 연출 도중 스마트폰 기기 베젤/프레임까지 함께 부서져 사라져서, 최종 화면에 아이콘 그리드만 배경에 노출되고 폰 목업이 없음**(사용자 확인).
- **문제 원인 추정 2**: "shatter and dissolve" 지시가 화면 내용뿐 아니라 이미지 전체(폰 포함)에 적용된 것으로 보임 — 프롬프트가 "무엇이 부서지는지"를 UI 내용으로 한정하지 않았음.
- **수정 후(v3) 대응**: "스마트폰 기기(베젤·프레임·노치)는 클립 내내 온전히 유지돼야 하고, 오직 화면 속 UI 콘텐츠만 부서지고 바뀐다"는 문장을 명시적으로 추가. 목적지 아이콘 그리드도 "폰 화면 영역 안에 담겨야 한다(contained within the phone screen)"고 재차 강조.
- **학습 포인트 2**: "화면이 부서진다(shatter)"처럼 파괴적 모션을 지시할 때는 그 효과의 적용 범위(화면 내용 vs 전체 이미지)를 명시하지 않으면 모델이 이미지 전체에 효과를 적용해버릴 수 있다 — 모션 지시는 항상 "무엇에" 적용되는지 범위를 같이 지정해야 한다.
- **v3 결과**([scene02-video-vids-v3.mp4](scene02-video-vids-v3.mp4)): **폰 베젤 문제 해결** — 클립 내내 폰 프레임이 온전히 유지됨(바닥 반사 효과까지 덤으로 추가돼 프리미엄한 느낌 강화). 아이콘 그리드도 대체로 잘 나옴. 그런데 **또 새 문제 발생: 상단 "CraftFit" 워드마크가 두 줄로 중복 표시됨**("CraftFit"과 "CraftFit™"가 겹쳐서 나옴, 사용자 확인).
- **문제 원인 추정 3**: 프롬프트에서 "the wordmark stays fixed... as in the source image"라고 써서, 모델이 (1) 원본 이미지에 이미 있던 "CraftFit" 텍스트를 그대로 복제하면서 (2) 프롬프트가 별도로 지시한 "워드마크를 유지하라"는 문장도 독립적으로 한 번 더 그려 넣어 결과적으로 두 벌이 생긴 것으로 추정.
- **수정 후(v4) 대응**: "화면에는 정확히 하나의 'CraftFit' 워드마크만 있어야 하며, 중복·반복·겹쳐 쓰지 말라"는 명시적 부정 지시(exactly ONE... do not duplicate)를 추가.
- **학습 포인트 3**: 이미지에 이미 있는 텍스트 요소를 "유지하라"고 다시 텍스트로 지시하면, 모델이 "원본 재현"과 "지시 이행"을 별개로 취급해 같은 요소를 중복 생성할 수 있다 — 이미 이미지에 있는 요소는 굳이 텍스트로 재차 강조하기보다 "정확히 1개만" 같은 개수 제약을 거는 편이 안전하다.
- **v4 결과**([scene02-video-vids-v4.mp4](video/scene02-video-vids-v4.mp4)): **워드마크 중복 해결** — "CraftFit"이 한 번만, 깔끔하게 표시됨. 폰 베젤 유지·아이콘 그리드도 함께 유지되어 v1→v4까지 발견된 3가지 문제(빈 화면/베젤 소실/워드마크 중복)가 모두 해결됨.
- **최종 채택**: v4를 씬 2 최종본으로 확정. 총 4번의 반복(v1~v4)에 걸쳐 "빈 화면 → 아이콘 등장(베젤 소실) → 베젤 복구(워드마크 중복) → 워드마크 정상화"로 문제를 하나씩 순차적으로 해결한 과정 자체가 과제 목표 2번("프롬프트를 어떻게 설계·수정했는지 설명")의 풍부한 실측 사례가 된다.

## 8. 나레이션 스크립트 (음성 생성 — ElevenLabs)

> **상태: 씬 1~4 실제 생성 완료.** 재현성: ElevenLabs / Eleven Multilingual v2 / voice: Yooni (Natural & clear) / 2026-07-06. 대사는 3번 섹션 씬 구성 표의 "내레이션/카피" 칸을 그대로 사용했다. 각 씬 영상 길이(2/2/3/3초)에 맞춰 최종 편집에서 배치 예정 — TTS가 말한 길이가 목표 길이와 정확히 안 맞으면 편집 단계에서 속도 조절 또는 무음 트림으로 맞춘다.
>
> **도구 전환 이력**: OpenAI TTS-1 HD(voice: nova) → 인위적인 AI 톤 문제로 Typecast로 변경 → Typecast는 무료 플랜에서 다운로드가 불가함을 확인해 ElevenLabs(Eleven Multilingual v2)로 재전환. 앞선 두 도구 모두 실제 생성을 시도하지 않은 계획 단계에서 교체된 것이라 별도 보존할 실측 결과물은 없음.
>
> **대사 개정**: 최초 대사(1인칭 혼잣말 → 브랜드 2인칭 초대·클로징 혼합 구조)에서, 사용자가 4줄 전부 "브랜드가 시청자에게 직접 말을 거는" 톤으로 재작성함.
>
> **Voice 선택(실제 사용)**: 사용자가 ElevenLabs 보이스 라이브러리에서 직접 청취해 **Yooni(Natural & clear)** 로 4줄 전부 통일 확정 — 앞서 AI가 추천했던 Salang 대신 사용자가 직접 들어보고 결정.

| 씬 | 목표 길이 | 대사(원문) | 톤 가이드 | 결과 파일명 |
|---|---|---|---|---|
| 1 | 2초 | "난잡한 헬스케어 앱, 이제 지겨우시죠!" | 시청자에게 공감을 구하는, 살짝 지친 듯한 질문형 톤 | [scene01-audio.mp3](voice/scene01-audio.mp3) |
| 2 | 2초 | "그런 앱, 저희가 다 부쉈습니다!" | 통쾌하고 자신감 있게 선언하는 톤 | [scene02-audio.mp3](voice/scene02-audio.mp3) |
| 3 | 3초 | "자신에게 맞는 스타일로 앱을 만들어보세요!" | 경쾌하고 초대하는 제안형 톤 | [scene03-audio.mp3](voice/scene03-audio.mp3) |
| 4 | 3초 | "헬스케어, 단 하나뿐인 당신을 위한 앱, CraftFit" | 차분하고 신뢰감 있는 브랜드 클로징 톤 | [scene04-audio.mp3](voice/scene04-audio.mp3) |

**출력 결과**: 4개 파일 모두 실제 생성 완료(사용자 확인). 각 파일 길이 — 씬1: 2.4555초 / 씬2: 1.8547초 / 씬3: 2.4033초 / 씬4: 2.8212초(ffprobe 확인). 전부 목표 길이(2/2/3/3초) 이내로, 9번 섹션 1차 통합 편집에서 대사를 한 글자도 자르지 않고 그대로 담을 수 있었다.

### 씬 4 오디오 교체 (파일 오류 수정)

- **문제**: 1차 통합본(`CraftFit_ad_final.mp4`)에서 씬4 구간에 실제로는 씬1 초안 대사("또 이 기능이야?")가 재생됨 — 사용자가 완성본을 확인하는 과정에서 발견. 원인은 통합 편집 시 잘못된 음성 파일이 씬4에 배치된 것.
- **조치**: 사용자가 ElevenLabs에서 올바른 씬4 대사("헬스케어, 단 하나뿐인 당신을 위한 앱, CraftFit")를 다시 생성해 전달(`voice/scene04-audio-raw.mp3`로 보존). 실제 발화 길이는 무음 구간 분석(ffmpeg silencedetect) 결과 약 **3.99초** — 기존 씬4 목표 길이(2.93초)보다 훨씬 길어, 전체 10초 제한을 맞추기 위한 추가 조정이 필요했다.
- **대응**: 사용자에게 (1) 전 씬 속도를 미세 조정 (2) 씬4만 속도 조정 (3) 직접 재녹음 중 선택지를 제시했고, 사용자는 **"씬4만 속도 조정"**을 선택. 이에 따라 씬4 오디오만 트림(무음 제거, 3.990748초) + atempo 1.2343배속 적용 → 3.233초로 압축, 씬1~3의 목표 길이도 프레임 단위로 최소화(2.4667/1.8667/2.4333초)해 합계 정확히 10.000초를 맞춤. 원본(속도 조정 전) 파일은 `scene04-audio-raw.mp3`로 보존.
- **학습 포인트**: 멀티모달 통합 편집에서 나레이션 하나만 교체해도 전체 씬 타이밍 예산이 연쇄적으로 재계산되어야 한다는 것을 실측으로 확인 — 특히 "10초 이내"처럼 하드 캡이 있는 요구사항에서는 개별 씬을 독립적으로 다루면 안 되고 항상 전체 합계 기준으로 재조정해야 한다.

## 9. 최종 통합 편집

> **상태: 완료.** 결과 파일: [`CraftFit_ad_final.mp4`](CraftFit_ad_final.mp4)

**편집 도구**: ffmpeg 명령줄(컷 편집·오디오 트랙 교체 용도로만 사용 — 제약사항 "편집 도구는 통합 편집 용도로만 제한적 사용" 준수. 새로운 AI 생성 없음).

**작업 내용 (v2, 씬4 오디오 교체 반영 최종본)**:
1. 씬별 길이를 나레이션 실제 길이에 맞춰 30fps 프레임 단위로 재계산: 씬1 2.4667초 / 씬2 1.8667초 / 씬3 2.4333초 / 씬4 3.2333초(씬4는 8번 섹션 "씬4 오디오 교체" 참고 — atempo 1.2343배속 적용 후 길이 기준). 합계 정확히 10.000초.
2. 각 씬 영상(8초 원본)을 위 길이로 트림.
3. 씬 영상의 원본 오디오(배경 앰비언트)는 제거하고, 대신 해당 씬 나레이션(ElevenLabs, voice: Yooni)을 씬 길이에 맞춰 무음 패딩 후 배치(대사 전체가 잘리지 않고 재생됨).
4. 씬 1→2→3→4 순서로 영상·오디오를 이어붙임(concat).
5. 크롭은 적용하지 않음(위 7번 섹션 "크롭 계획 정정" 참고) — 원본 1920x1080(16:9) 그대로 사용.

**v1(첫 통합본) 문제**: 씬4에 잘못된 음성 파일이 배치되어 있었음(8번 섹션 "씬4 오디오 교체" 참고). v2에서 올바른 음성으로 교체하고 씬별 길이를 재조정해 재생성.

**출력 스펙**: 1920x1080 / H.264 / 30fps / AAC / **정확히 10.000초** / 약 2.0MB (ffprobe로 확인, 재현성 확보). 요구사항의 "최대 인코딩 스펙(1080p·24~30fps·H.264·AAC)"과 "10초 이내"를 모두 충족.

**미반영 요소(선택 보완 가능)**: 전체를 아우르는 배경음악/효과음(3번 섹션에서 계획했던 "배경음악+씬4 사운드 로고")은 별도 생성이 필요해 이번 1차 통합본에는 포함하지 않음 — 나레이션만으로 "청각 요소 1개 이상 포함" 요구사항은 충족됨.

## 10. 보너스 1 — 립싱크(Lip-sync) 적용

> **상태: 완료.** 원문 요구사항: "인물 발화 장면 1개 이상을 추가하고, 입모양과 대사를 자연스럽게 맞춘다." 메인 광고(10초, UI 목업 중심)에는 사람이 등장하지 않으므로, 별도의 보너스 전용 씬을 하나 새로 설계해 추가했다(메인 10초 광고와는 별개 산출물).

**컨셉**: CraftFit을 실제로 쓰는 사용자의 짧은 후기(testimonial) 장면. 메인 광고의 기승전결(문제→전환→해결→브랜드) 구조를 한 사람의 목소리로 압축해 보여주는 보완 클립.

**대사(원문)**: "예전엔 복잡한 기능들 때문에 늘 헤맸는데, 이제는 제 방식대로 관리해요. CraftFit 덕분이에요."

**인물 이미지 생성 프롬프트 (GPT Image 2, 기존 공통 스타일 앵커의 색감만 재사용)**:
```
Minimalist portrait photo of a calm person in their late 20s, sitting in a softly lit modern living room, warm natural smile, looking directly at camera as if mid-conversation, wearing simple neutral-toned clothing, soft even studio lighting, shallow depth of field, calm color palette (sage green #8FA998 accent, off-white #F5F3EE background, charcoal #2B2B2B accents), photorealistic, high detail, portrait orientation, no text overlays, no watermark.
```

**진행 순서(실제 수행 완료)**:
1. 위 프롬프트로 GPT Image 2에서 인물 사진 1장 생성 → [bonus1-lipsync-image.png](bonus1/bonus1-lipsync-image.png) (1024x1024). 의도한 미니멀 거실 배경·세이지그린/오프화이트 톤·차분한 미소가 그대로 재현됨.
2. 위 대사를 ElevenLabs(Eleven Multilingual v2)로 음성 생성 → [bonus1-lipsync-audio.mp3](bonus1/bonus1-lipsync-audio.mp3) (7.837초).
3. 사진 + 음성을 **Magic Hour "Talking Photo" 도구**(magichour.ai, 무료 플랜)에 입력해 립싱크 영상 생성 → [bonus1-lipsync-video.mp4](bonus1/bonus1-lipsync-video.mp4).

**출력 결과**: 640x640 / H.264 / 25fps / AAC / 7.848초(음성 길이와 거의 일치). 프레임 확인 결과(t=2초, t=4초) 입 모양이 서로 다르게 나타나 실제로 음성에 맞춰 입이 움직이고 있음을 확인. 무료 플랜 사용으로 화면 우측 하단에 "Magic Hour" 워터마크가 포함됨(유료 전환 시 제거 가능하나 이번 과제 범위에서는 그대로 사용).

**파일명 컨벤션 수정**: 사용자가 전달한 원본 파일명(`bonus1 image.png` 등, 공백 포함)을 CLAUDE.md 컨벤션에 맞춰 위와 같이 재명명함.

## 12. 보너스 3 — 플랫폼별 화면 비율 버전 제작

> **상태: 완료.** 원문 요구사항: "동일 스토리보드로 화면 비율 버전 2개 이상을 제작한다. (예: 16:9(유튜브) + 9:16(숏폼/릴스 표준, 1080x1920) + 1:1(피드용))" 필수 산출물(16:9, `CraftFit_ad_final.mp4`)에 더해 **9:16**과 **1:1** 두 버전을 추가 제작 — 원문 예시의 3종을 모두 충족.

**방법**: 새로 영상을 생성하지 않고, 기존 4개 씬 원본(1920x1080)에서 중앙 영역을 크롭하는 방식으로 제작(편집 도구 사용 범위 내 — 새 AI 생성 없음). 크롭 전, 각 씬에서 "CraftFit" 워드마크나 핵심 UI 요소가 잘리지 않는지 프레임을 직접 추출해 4개 씬 전부 육안으로 확인한 뒤 진행.

- **9:16 (1080x1920)**: `crop=608:1080:656:0` (원본 중앙 608px 폭 추출, 9:16 비율) 후 `scale=1080:1920`으로 업스케일.
- **1:1 (1080x1080)**: `crop=1080:1080:420:0` (원본 중앙 1080px 정사각형 추출).
- 두 버전 모두 메인 영상과 동일한 씬별 트림 길이·나레이션 오디오를 그대로 사용해 합계 정확히 10.000초 유지.

**검증**: 크롭 전 4개 씬 모두에서 테스트 프레임을 추출해 확인 — 씬2·4의 "CraftFit" 워드마크는 9:16·1:1 모두에서 중앙에 온전히 유지됨. 좌우 가장자리의 부수적 요소(예: 씬2 하단 네비게이션 라벨 일부, 씬4 우측 아이콘 일부)만 일부 잘리고 핵심 콘텐츠는 보존됨.

**결과 파일**:
- [`CraftFit_ad_final_9x16.mp4`](CraftFit_ad_final_9x16.mp4) — 1080x1920 / H.264 / 30fps / AAC / 10.000초
- [`CraftFit_ad_final_1x1.mp4`](CraftFit_ad_final_1x1.mp4) — 1080x1080 / H.264 / 30fps / AAC / 10.000초
- (기존) [`CraftFit_ad_final.mp4`](CraftFit_ad_final.mp4) — 1920x1080(16:9), 필수 산출물

## 11. 보너스 2 — 동일 스토리보드, 다른 도구로 재제작

> **상태: 완료.** 원문 요구사항: "이미지 또는 비디오 생성 파트를 다른 도구로 바꿔 동일 씬 1~2개를 재제작한다." 별도 신규 작업 없이, 6번·7번 섹션에서 이미 실제로 진행했던 **씬 1 영상 재제작 실측 기록**을 이 섹션에서 공식 정리한다.

**무엇을 재제작했나**: 씬 1("문제 제시" — 복잡하고 화려한 기존 헬스앱 UI)을 동일한 소스 이미지([scene01-image.png](image/scene01-image.png))와 동일한 연출 의도(알림 배지 깜빡임, 카메라 미세 흔들림, 반사된 피곤한 얼굴)를 기준으로, **비디오 생성 도구 2종**으로 각각 독립 제작했다.

| 항목 | Sora 2 Pro (6번 섹션) | Google Vids · Veo 3.1 (7번 섹션, 최종 채택) |
|---|---|---|
| 입력 방식 | 텍스트 전용(이미지 입력 불가) | 이미지 + 텍스트(image-to-video) |
| 결과 파일 | [scene01-video-v1.mp4](scene01-video-v1.mp4) / [scene01-video-v2.mp4](scene01-video-v2.mp4) | [scene01-video-vids-v1.mp4](video/scene01-video-vids-v1.mp4) |
| 이미지-영상 화풍 일관성 | 낮음(독립 생성이라 구도·색감이 원본 이미지와 다름) | 높음(원본 이미지와 매우 유사) |
| 요청한 모션 재현 | 거의 없음(정지 영상에 가까움) | 부분 재현(알림 아이콘 펄스 효과 확인) |
| UI 텍스트 정확도 | 다수 깨짐("Alhorieboard", "Add Wood" 등 의미 불명 문자열) | 비교적 안정적 |
| 해상도 제어 방식 | 드롭다운에서 720x1280 직접 선택(텍스트 프롬프트에 명시해도 미반영 — v1 실패로 확인) | 9:16 세로 모드 선택(단, 실제 출력은 1920x1080 컨테이너) |

**결론**: 동일한 재현 의도로 두 도구에 각각 프롬프트를 설계해 실행한 결과, **이미지 기준 입력(image-to-video)을 지원하는 Google Vids 쪽이 원본 이미지와의 화풍 일관성·모션 재현·텍스트 안정성에서 전반적으로 우세**했다. Sora 2 Pro는 텍스트 전용 구조라 이미지 생성 단계의 결과물을 그대로 이어받지 못하고 매번 새로 해석해야 했고, 이 과정에서 UI 텍스트 왜곡이 반복적으로 발생했다. 이 비교 자체가 과제 목표 1번("생성 도구의 강점/약점 설명")과 3번("동일 요구를 여러 도구로 시도했을 때 결과 차이 비교")에 해당하는 실측 근거이며, Sora 결과물은 삭제하지 않고 그대로 보존해 이 비교의 원본 증거로 남겼다.
