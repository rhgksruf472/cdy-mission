# Codyssey Mission 01 (Course 2) — Python & Git 기초

> 과제 원문: [`codyssey.md`](codyssey.md)

## 미션 요약

이전 미션들에서 쌓인 프롬프트를 관리하는 **콘솔 기반 파이썬 프로그램**을 만들고, 그 개발 과정을 **Git으로 버전 관리**하며 **GitHub에 공개**하는 미션입니다. 이번 미션의 핵심은 AI 활용이 아니라 Python 기초 문법과 Git 명령어(`init/add/commit/push/pull/checkout/clone/merge`)를 직접 손으로 익히는 것입니다.

- 프롬프트 추가 / 목록 보기 / 카테고리별 조회 / 검색 / 상세 보기 / 즐겨찾기 6가지 핵심 기능
- 이전 미션(mission-01, mission-02)에서 실제로 작성한 프롬프트 4개를 기본 데이터로 재사용
- "목록 보기" 기능은 별도 브랜치에서 작업 후 main으로 병합
- **보너스 1**: 프롬프트를 JSON으로 저장/불러오기, 카테고리별 Markdown 내보내기
- **보너스 2**: 프롬프트 수정/삭제(CRUD), 조회수 기록, 조회수 Top 정렬

## 저장소 구조 (이 미션만 예외)

이번 미션은 "GitHub 저장소 1개"가 별도 산출물이기 때문에, 실제 프로그램 코드는 이 `cdy` 저장소가 아니라 **독립된 별도 GitHub 저장소**에 있습니다.

- **GitHub 저장소 URL**: https://github.com/rhgksruf472/Prompt-manager
- 로컬 경로: `Desktop/vs code folder/prompt-manager/`

```
codyssey/C2_mission-01/
├── codyssey.md                  과제 원문
├── requirements-checklist.md    요구사항 체크리스트 (비공개)
└── README.md                    이 문서 — 평가자용 미션 요약
```

## 프로그램 기능

| 번호 | 기능 |
|---|---|
| 1 | 프롬프트 추가 (제목/내용/카테고리, 빈 값 재입력 요청) |
| 2 | 프롬프트 목록 (번호·카테고리·즐겨찾기 표시) |
| 3 | 카테고리별 조회 |
| 4 | 프롬프트 검색 (제목+내용) |
| 5 | 프롬프트 상세 보기 |
| 6 | 즐겨찾기 추가/해제 |
| 7 | 즐겨찾기 목록 |
| 8 | 프롬프트 수정 (보너스) |
| 9 | 프롬프트 삭제 (보너스) |
| 10 | 조회수 Top 목록 (보너스) |
| 11 | JSON으로 저장 (보너스) |
| 12 | JSON 불러오기 (보너스) |
| 13 | 카테고리별 Markdown 내보내기 (보너스) |

전 기능을 스크립트 입력으로 시나리오 테스트하여 정상 동작을 확인했습니다(카테고리에 결과가 없을 때 안내 메시지, 검색 결과 없음 안내, 잘못된 번호 입력 처리 등 예외 케이스 포함).

## 기본 등록 프롬프트 (이전 미션 재사용)

과제 요구사항("이전 미션에서 작성한 프롬프트를 최소 3개 이상 기본 데이터로 등록")에 따라, 새로 지어내지 않고 이전 미션에서 실제로 작성했던 프롬프트를 그대로 가져와 등록했습니다.

| 제목 | 카테고리 | 출처 |
|---|---|---|
| 비즈니스 메일 작성 코치 (다은) 시스템 프롬프트 | 페르소나 | [mission-01 system-design.md](../mission-01/system-design/system-design.md) (v2 단계적 추론 유도 프롬프트) |
| CraftFit 광고 씬1 이미지 생성 프롬프트 (GPT Image 2) | 이미지 생성 | [mission-02 storyboard.md](../mission-02/storyboard/storyboard.md) |
| CraftFit 광고 씬1 영상 생성 프롬프트 v2 (Sora 2 Pro) | 영상 생성 | [mission-02 storyboard.md](../mission-02/storyboard/storyboard.md) |
| LLM 모델 비교 결과 인포그래픽 프롬프트 | 이미지 생성 | [mission-01 bonus-2-visualization-prompt.md](../mission-01/bonus/bonus-2-visualization-prompt.md) |

## Git 작업 기록

- 로컬 저장소 초기화: `git init -b main` (기본 브랜치 main)
- 기능 단위 커밋 15개 (병합 커밋 1개 포함) — `.gitignore` → README → 기본 데이터/메뉴 → 기능 6종 → 보너스 4종 → README 갱신 순
- "프롬프트 목록" 기능은 `feature/show-list` 브랜치에서 작업 후 `git merge --no-ff`로 main에 병합
- 공개 샘플 저장소(`octocat/Hello-World`)를 clone하여 구조·커밋 로그를 확인 후 삭제
- 원격 저장소 연결 후 `main`·`feature/show-list` 브랜치 모두 push, `git pull`로 동기화 확인 완료

```
* Update README with feature list, usage, and category info
* Add view count tracking and Top-viewed sorting (bonus 2)
* Add edit_prompt and delete_prompt functions (bonus 2)
* Add category-wise Markdown export function (bonus 1)
* Add JSON save/load functions (bonus 1)
* Add toggle_favorite and show_favorites functions
* Add show_detail function with number validation
* Add search_prompt function (title/content keyword search)
* Add show_by_category function
* Add add_prompt function with empty-input validation and category selection
*   Merge branch 'feature/show-list' into main
|\
| * Add show_list function on feature/show-list branch
|/
* Add base prompt data and menu skeleton
* Add .gitignore
* Add README with project title
```

## 재현성 기록

| 항목 | 값 |
|---|---|
| Python 버전 | 3.11.9 |
| Git 버전 | 2.54.0.windows.1 |
| 외부 라이브러리 | 없음 (표준 라이브러리 `json`, `os`만 사용) |
| 로컬 저장소 경로 | `Desktop/vs code folder/prompt-manager/` |
