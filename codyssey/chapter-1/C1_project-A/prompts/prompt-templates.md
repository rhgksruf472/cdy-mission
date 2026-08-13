# Project A — 프롬프트 템플릿 문서 (초안)

> 컨셉: **중고 책 교환 플랫폼** — 메인 / 목록 / 상세 3화면.
> 이미지 생성 도구(최종, 2개 사용 — 원문 요구 "1개 이상" 충족, 각각 이름 명시):
> 1. **Adobe Firefly**(firefly.adobe.com, Creative Cloud 구독 계정) — 모델 **Gemini 3 (w/ Nano Banana Pro)**. 화면 1(메인)·2(목록) 생성에 사용. 파트너 모델 목록 중 텍스트 렌더링·종합 품질 최상위로 확인돼 채택(웹 조사 근거, 2026-07-22).
> 2. **Google Gemini 웹**(gemini.google.com, 무료 플랜) — 모델 **Nano Banana 2**. Firefly의 Nano Banana Pro 무료 체험 크레딧이 소진돼 화면 3(상세) 생성에 한해 교체 사용. 무료 플랜 하루 약 20장 한도(2026-07-22 웹 조사 근거).
> ⚠️ 참고: 두 모델 모두 Adobe 자체 모델(Firefly Image 5 등)에 붙는 "상업적으로 안전함" 태그가 없는 파트너/외부 모델 — 원문 제약사항(저작권 문제 해결된 툴)과 관련해 작업 로그에 선택 이유·발견된 저작권 이슈(화면3 v1 사례)와 수정 과정을 명시해 둠.
> 아래는 **초안(v1)** — 실제 생성 결과를 아직 반영하지 않은 상태. 생성 후 결과에 따라 v2(수정)·최종본을 이 문서에 이어서 기록한다(임의 결과 기재 금지 — [[실증 데이터 원칙]]).
> ✅ 확인 완료: Firefly "더 보기"에서 화면 비율·해상도 직접 설정 가능(2026-07-22 실측). 생성 시 **비율 9:16**으로 UI에서 지정하고 진행한다.

---

## 공통 스타일 베이스 (3화면 공통 적용 — 일관성 유지용)

```
Mobile app UI design, secondhand book exchange service, minimal flat design,
warm pastel palette (beige, brown, soft green accent), clean sans-serif labels,
high fidelity, Figma-style UI mockup, 9:16 vertical mobile ratio, no long readable text blocks
```

- **스타일**: 미니멀 플랫 디자인
- **색상**: 베이지·브라운 메인 + 그린 포인트
- **비율**: 9:16 (모바일) — 팀 회의에서 데스크탑(16:9)으로 바뀌면 전 화면 동시 수정
- **텍스트 깨짐 방지**: "no long readable text blocks"로 과도한 텍스트 생성 억제 → 라벨은 후가공(C 트랙)에서 실제 텍스트로 보정 전제

---

## 화면 1 — 메인 (홈)

**역할**: 서비스 진입 + 추천 도서 탐색

### 초안 v1
```
[공통 스타일 베이스] + home screen, top search bar, category icons row,
featured book cards in vertical scroll list, each card shows book cover thumbnail
and simple placeholder label, bottom navigation bar with 4 icons
```

### 수정 이력
| 단계 | 프롬프트 | 결과 및 개선점 |
|------|----------|----------------|
| 초안 v1 | (위) | **실측 결과**([`design/raw-logs/screen01-main-firefly-v1.png`](../design/raw-logs/screen01-main-firefly-v1.png), Firefly·Gemini 3 w/ Nano Banana Pro, 768×1376≈9:16): 검색창·카테고리 아이콘 4개(Fiction/Non-Fiction/Academic/Kids&YA)·추천 도서 카드 리스트·하단 내비게이션 4개 모두 요구사항대로 생성됨. 텍스트 렌더링 전반적으로 매우 깨끗함(모델 선택 효과로 판단). **발견된 문제 1건**: 4번째 도서 카드 제목이 "The Book"이라는 일반적 placeholder로 생성됨(부자연스러운 요소) → 후가공에서 실제 도서 제목으로 교체 필요 |

**학습 포인트**: 텍스트 렌더링 특화 모델(Nano Banana Pro)을 쓰면 "글자 깨짐" 문제는 크게 줄지만, "의미 없는 플레이스홀더 텍스트" 같은 다른 유형의 부자연스러움은 여전히 발생 → 후가공 검수는 글자 모양뿐 아니라 내용 타당성까지 봐야 함.

### 후가공 — "The Book" placeholder 수정
| 방법 | 결과 |
|------|------|
| Gemini 웹(Nano Banana 2)에 원본 첨부 + "4번째 카드 제목만 실제 책 제목으로 바꿔줘, 나머지는 그대로" 지시(인페인팅 대체) | **성공**([`design/raw-logs/screen01-main-gemini-v2.png`](../design/raw-logs/screen01-main-gemini-v2.png)): 4번째 카드 제목이 표지 삽화에 이미 그려져 있던 "THE PICTURES"와 맞춰 "The Pictures"로 수정됨. 나머지 요소(검색창·카테고리·다른 카드 3개·하단 내비)는 원본과 동일하게 유지 — 국소 편집 성공. **채택**</br>⚠️ 단, 첫 번째 카드 "The Great Gatsby" 썸네일이 여전히 실제 표지 디자인을 재현 중 — 아래 "저작권 재검토" 참고 |

---

## 화면 2 — 목록 (카테고리별 도서 리스트)

**역할**: 필터링 + 리스트 탐색

### 초안 v1
```
[공통 스타일 베이스] + book list screen, filter chips row at top (genre, region),
grid or list of book items with thumbnail + condition tag, bottom navigation bar
```

### 수정 이력
| 단계 | 프롬프트 | 결과 및 개선점 |
|------|----------|----------------|
| 초안 v1 (참조 이미지: 화면1 첨부) | (위) | **실측 결과**([`design/raw-logs/screen02-list-firefly-v1.png`](../design/raw-logs/screen02-list-firefly-v1.png), 768×1376≈9:16, 동일 모델·참조 이미지 사용): 필터 칩(Genre/Region/Condition) + 도서 리스트(썸네일+상태 태그) + 하단 내비게이션 모두 요구사항 충족. **참조 이미지 덕분에 화면1과 팔레트·카드 스타일·폰트가 실제로 일치**(일관성 유지 전략 효과 확인). 이번엔 도서 제목도 실제 책 제목(1984·Becoming·Dune·Atomic Habits)이 나와 화면1보다 개선됨. **발견된 문제 2건**: ①Dune 카드 — 우측 태그는 "Acceptable"인데 저자 줄 텍스트는 "Good Condition"으로 서로 다른 상태값이 동시 표기됨(내용 모순, 부자연스러운 요소) ②5번째(최하단) 카드 제목이 화면1과 동일하게 "The Book"이라는 일반 placeholder로 반복 생성됨 — 리스트 끝쪽 항목에서 모델이 제목을 대충 채우는 패턴으로 추정 |

**학습 포인트**: 레퍼런스 이미지를 붙이면 스타일 일관성은 잘 유지되지만, **각 카드의 정보 값 자체(상태 태그 vs 본문 텍스트 일치 여부)까지는 보장 안 됨** → 후가공 단계에서 텍스트 렌더링뿐 아니라 "표시된 정보끼리 모순 없는지"도 함께 검수해야 함. 또한 리스트 끝부분 placeholder 문제가 화면1·2에서 반복 관찰돼, 후가공 시 우선순위로 처리.

---

## 화면 3 — 상세 (도서 정보 / 교환 신청)

**역할**: 개별 도서 정보 확인 + 교환 신청 액션

### 초안 v1
```
[공통 스타일 베이스] + book detail screen, large book cover image at top,
short description area below, condition and location tags, prominent
"request exchange" action button at bottom, no bottom navigation bar
```

### 수정 이력
| 단계 | 프롬프트 | 결과 및 개선점 |
|------|----------|----------------|
| 초안 v1 (참조 이미지: 화면1 첨부) | (위) | **실측 결과**([`design/raw-logs/screen03-detail-firefly-v1.png`](../design/raw-logs/screen03-detail-firefly-v1.png), 768×1376≈9:16): 상세 정보(제목·저자·설명·상태/위치/커버 태그)·"Request Exchange" 버튼·하단 내비게이션 없음까지 요구사항대로 나옴. 텍스트 렌더링도 깨끗함. **발견된 문제(중대)**: 상단 도서 표지 이미지가 실제 출판된 『The Great Gatsby』의 유명한 원조 커버 디자인("Celestial Eyes" — 눈·입술·도시 야경 일러스트, 1925년 Francis Cugat 작)을 거의 그대로 재현함. 화면1 리스트의 "The Great Gatsby" 항목을 참조 이미지로 넣었더니 AI가 실제 유명 삽화를 학습 데이터에서 그대로 복원한 것으로 추정됨. **원문 제약사항("저작권 문제가 해결된 툴 사용", "레퍼런스 출처 기록")과 직접 충돌 위험** → 그대로 제출 불가, v2로 재생성 필요 |
| v1-b (도구 교체 시도, 실패) | 동일 도구(Firefly)의 무료 모델 **Firefly Image 4**로 재시도 — Nano Banana Pro 무료 체험 크레딧 소진으로 부득이 교체 | **실패**([`design/raw-logs/screen03-detail-firefly4-v1-failed.jpg`](../design/raw-logs/screen03-detail-firefly4-v1-failed.jpg), 2304×1792, 가로형): 제목·부제·본문·버튼 텍스트가 전부 판독 불가 수준으로 깨짐("Book ЯOW" 등). 게다가 요청한 "플랫 UI 화면"이 아니라 스마트폰 목업 프레임 안의 감성 사진(책+찻잔)으로 나왔고 비율도 9:16 지시를 무시하고 가로형으로 생성됨 — Firefly Image 4는 구세대 디퓨전 모델이라 텍스트·복잡한 레이아웃 지시에 약함. 도구 비교 실측 자료로 raw-logs에 원본 그대로 보존(삭제 안 함) |
| v2 (도구 교체: Gemini 웹) | 도구를 **gemini.google.com**(무료 플랜, Nano Banana 2 모델)으로 교체. 화면2 참조 이미지 첨부 + 프롬프트에 "flat 2D app screen only, NOT a phone device mockup photo, NOT a photograph, vector-style UI illustration" 부정 지시 추가 + "generic original book cover illustration ... not based on any existing published book cover" 저작권 회피 지시 유지 | **부분 성공, 이후 Figma 배치 단계에서 문제 재발견**([`design/raw-logs/screen03-detail-gemini-v2.png`](../design/raw-logs/screen03-detail-gemini-v2.png), 768×1376≈9:16): 텍스트 전부 깨짐 없이 깨끗하게 렌더링됨("Book Detail", "The Whispering Woods", "By Eleanor Vance" 등). 표지도 가상의 창작 일러스트로 나와 저작권 문제는 해결됨. **당시엔 "폰 목업/사진 이탈 문제 해결"로 판단해 최종 채택했으나, Figma 프로토타입 제작 중 실제로는 흰 배경 위에 그림자 있는 둥근 카드가 떠 있는 형태(엣지투엣지 아님)임을 재확인** — 화면1·2는 상태바가 이미지 최상단 모서리부터 시작하는 완전 풀블리드인데, 화면3은 여백 있는 "카드형" 목업으로 나와 스타일이 실제로는 불일치했음. "NOT a phone mockup photo" 지시가 사실적 3D 폰 케이스는 막았지만, 카드+그림자 형태의 목업 프레젠테이션까지는 막지 못한 것으로 추정 |
| **v3 (동일 도구 재시도, 채택)** | 프롬프트에 **참조 이미지(화면1 최종본)를 직접 첨부**하고 "screen content fills the ENTIRE canvas edge-to-edge, ZERO margin, do NOT render as a floating rounded card, do NOT add a drop shadow, do NOT show any white/blank space around the screen" 등 여백·카드·그림자를 구체적으로 금지하는 부정 지시를 추가 | **성공**([`design/raw-logs/screen03-detail-gemini-v3.png`](../design/raw-logs/screen03-detail-gemini-v3.png), 768×1376 — 화면1과 픽셀 크기 완전 동일): 화면1과 동일한 상단 상태바(10:30 AM·신호·와이파이·배터리)까지 포함해 완전 풀블리드로 생성됨. 가상 도서 "Whispering Summits"(저자 Elara Vance, 산 일러스트 표지)로 저작권 문제 없음. 태그(Very Good Condition/Seattle, WA/Fiction·Adventure/Year Pub. 2018)·REQUEST EXCHANGE 버튼 정상. **화면1·2와 완전히 일치하는 엣지투엣지 스타일 확보 → 최종 채택**. Figma에 배치 시 프레임(768×1376)에 크롭·리사이즈 없이 그대로 꽉 참 |

### 후가공 — Dune 상태값 모순 + "The Book" placeholder 수정
| 방법 | 결과 |
|------|------|
| Gemini 웹에 원본 첨부 + "Dune 카드 저자 줄에서 모순된 'Good Condition' 텍스트 제거, 마지막 카드 제목을 실제 책 제목으로 교체, 나머지는 그대로" 지시 | **성공**([`design/raw-logs/screen02-list-gemini-v2.png`](../design/raw-logs/screen02-list-gemini-v2.png)): Dune 카드가 "Frank Herbert"만 남아 우측 태그("Acceptable")와 모순 없어짐. 마지막 카드는 "The Silent Patient"로 교체됨. 나머지 카드·필터 칩·내비는 원본과 동일 유지 |

### ⚠️ 저작권 재검토 — 실존 도서 재현 문제가 화면1·2에도 반복됨
화면3(상세)에서 발견했던 "실존 저작물 표지 재현" 문제가 **화면1·2의 축소 썸네일에도 동일하게 나타남**을 후가공 검토 중 확인:
- 화면1: "The Great Gatsby" 썸네일이 1925년 원조 커버("Celestial Eyes")를 축소 재현
- 화면2: "1984"(Orwell 스타일 표지), "Dune"(실제 최근 판본과 유사한 디자인), "Atomic Habits"(실제 커버 디자인과 유사), 그리고 **"Becoming" 썸네일은 마이클 오바마의 실제 저서 표지를 사진 수준으로 재현하면서 실존 인물(미셸 오바마)의 얼굴까지 그대로 그려냄** — 표지 디자인 저작권뿐 아니라 실존 인물 초상권까지 걸리는 더 심각한 사례로 판단됨

**원인**: 프롬프트에 실제 책 제목을 예시로 넣지 않았는데도, "book exchange app에 표지가 필요하다"는 맥락만으로 모델이 유명 도서의 실제 표지를 학습 데이터에서 자동으로 소환한 것으로 추정(화면3에서도 동일 패턴 확인됨 → 3화면 모두에서 반복 관찰된 재현 가능한 현상).

### 후가공 — 실존 표지 전면 교체
| 방법 | 결과 |
|------|------|
| Gemini 웹에 화면1 v2 첨부 + "1번 카드(Gatsby)를 완전 가상의 책(제목·저자·추상 표지)으로 교체, 나머지 동일 유지" 지시 | **성공**([`design/raw-logs/screen01-main-gemini-v3.png`](../design/raw-logs/screen01-main-gemini-v3.png)): "The Great Gatsby" → 가상의 "Patterns of Infinity"(저자 Kaelen Mercer, 추상 라인아트 표지)로 교체. 나머지 카드(Sapiens·Educated·The Pictures)는 이미 가상이라 그대로 유지. **화면1 전체가 실존 저작물 재현 없음 — 최종 채택** |
| Gemini 웹에 화면2 v2 첨부 + "1984·Becoming·Dune·The Silent Patient 4장을 가상 표지로 교체(실존 인물 얼굴 금지), Atomic Habits는 사진 초상 없으면 유지 가능" 지시 | **부분 성공**([`design/raw-logs/screen02-list-gemini-v3.png`](../design/raw-logs/screen02-list-gemini-v3.png)): "1984"→"Patterns of Resonance"(Alistair Grey), "Becoming"→"Echoes of the Machine"(Sylvia Vance) — **미셸 오바마 얼굴 완전히 제거됨**, "Dune"→"Whispers of the Sand"(Kaelen Chen), "The Silent Patient"→"The Fractured Code"로 전부 가상 교체 성공. **다만 "Atomic Habits"(James Clear)는 실제 도서 그대로 남아있음** — 지시가 조건부("사진 없으면 유지")였는데 모델이 유지를 택함. 사용자가 "전부 가상 표지로 교체"를 선택했으므로 **한 번 더 국소 편집 필요** |
| Gemini 웹에 화면2 v3 첨부 + "Atomic Habits 카드만 가상 표지로 교체, 나머지 동일 유지" 지시 | **성공**([`design/raw-logs/screen02-list-gemini-v4.png`](../design/raw-logs/screen02-list-gemini-v4.png)): "Atomic Habits"→가상의 "A Distant Whisper"(저자 Anya Petrova, 추상 곡선 패턴 표지)로 교체. 5개 카드 전부 가상 도서로 확인됨. **화면2 전체가 실존 저작물 재현 없음 — 최종 채택** |

### ✅ 최종 채택본
| 화면 | 파일 | 사용 도구·모델 |
|------|------|----------------|
| 1. 메인 | [`design/final/screen01-main-final.png`](../design/final/screen01-main-final.png) | Firefly(Nano Banana Pro) 생성 → Gemini(Nano Banana 2)로 후가공 2회(placeholder 제목·저작권 표지 교체) |
| 2. 목록 | [`design/final/screen02-list-final.png`](../design/final/screen02-list-final.png) | Firefly(Nano Banana Pro) 생성 → Gemini(Nano Banana 2)로 후가공 3회(상태값 모순·placeholder 제목·저작권 표지 4장 교체) |
| 3. 상세 | [`design/final/screen03-detail-final.png`](../design/final/screen03-detail-final.png) | Firefly(Nano Banana Pro, 저작권 문제로 폐기) → Firefly Image 4(텍스트 깨짐으로 폐기) → Gemini(Nano Banana 2) v2(카드+여백 형태로 재확인돼 폐기) → Gemini v3(엣지투엣지 명시 지시로 재생성, 최종 채택) |

**학습 포인트**:
1. 이미지 생성 AI에 실존하는 유명 저작물의 제목·맥락을 입력하면(직접 캡처하지 않아도) 학습 데이터에 있는 실제 커버 디자인을 거의 그대로 재현할 수 있음 — "타인의 작업물을 캡처하여 제출하는 행위 금지" 조항의 취지를 지키려면 **AI가 재현한 결과물도 기존 저작물과의 유사성을 직접 검수**해야 한다는 것을 실측으로 확인. "실존 표지 재현 금지" 같은 부정 지시가 예방책.
2. **같은 "AI 이미지 생성"이어도 모델 세대에 따라 텍스트 렌더링 품질 차이가 매우 큼**(Nano Banana 계열 vs 구세대 디퓨전 모델인 Firefly Image 4) — 유료 크레딧이 소진돼 급하게 하위 모델로 바꾸면 텍스트 깨짐이 재발할 수 있음을 실측으로 확인.
3. **부정 지시는 "무엇을 막을지" 구체적이어야 효과가 있다**: "NOT a phone mockup photo, flat 2D UI only"만으로는 3D 폰 케이스·사진은 막았지만, **흰 배경 위에 그림자 있는 "카드형" 목업 프레젠테이션까지는 막지 못함**(화면3 v2 — 텍스트·저작권만 검수하고 "완료"로 판단했다가 Figma 배치 단계에서 뒤늦게 발견). "screen fills the ENTIRE canvas edge-to-edge, ZERO margin, do NOT add a drop shadow, do NOT render as a floating card"처럼 **원치 않는 형태를 명시적으로 나열**하고서야 v3에서 해결됨.
4. **완성 선언 후에도 실제 사용 맥락(Figma 배치)에서 재검수가 필요하다**: 화면3 v2는 텍스트 깨짐·저작권 기준으로는 통과해 한 차례 "최종 채택"됐지만, 다른 화면과 나란히 배치해보니(Figma 프레임 채우기) 비로소 엣지투엣지 불일치가 드러남 — 개별 이미지 검수만으로는 "화면 간 스타일 일관성" 문제를 못 잡을 수 있음.
5. **동일 도구 안에서 크레딧이 소진돼도, 다른 서비스(Gemini 웹)의 같은 계열(Nano Banana) 무료 모델로 갈아타면 스타일 일관성을 크게 해치지 않고 이어갈 수 있음** — 참조 이미지 재사용이 도구를 넘나들 때도 유효했음.

---

## 일관성 유지 전략 (과제 목표 3번)

- 3화면 모두 **공통 스타일 베이스 문장을 그대로 재사용**하고, 화면별 레이아웃 설명만 교체.
- 도구가 **시드(seed) 고정**을 지원하면 화면 1 생성 시 나온 시드값을 화면 2·3에도 동일 적용.
- 시드 미지원 시 **화면 1 결과 이미지를 레퍼런스 이미지로 업로드**해 화면 2·3 생성 시 참조하도록 설정(도구가 이미지 레퍼런스 입력을 지원하는 경우).

---

## 학습 포인트 (실행 후 채움)
*생성·수정 과정을 거친 뒤, 프롬프트 요소(스타일/레이아웃/색상)가 결과에 미친 영향과 배운 점을 정리.*
