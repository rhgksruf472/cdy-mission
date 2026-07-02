# Codyssey Mission 01 — LLM 프롬프트 엔지니어링

> 과제 원문: [`codyssey/mission-01/codyssey.md`](codyssey/mission-01/codyssey.md)
> 요구사항 1:1 체크리스트: [`codyssey/mission-01/requirements-checklist.md`](codyssey/mission-01/requirements-checklist.md)

## 미션 요약

같은 LLM이라도 프롬프트 설계 방식에 따라 결과 품질이 완전히 달라진다는 것을 직접 실험으로 검증하는 미션입니다. 3종 이상의 LLM을 동일 업무 과업으로 비교해 "느낌"이 아닌 평가 축과 점수로 모델을 선정하고, 페르소나·시스템 프롬프트·Few-shot·단계적 추론 유도 기법을 적용해 프롬프트를 v1→v2로 개선하며, 환각(Hallucination) 검증과 10턴 이상 대화의 문맥 유지 검증까지 수행했습니다.

- **선택한 업무 과업**: 메일 초안 작성 (외부 협력사 대상 공지/사과/요청 메일)
- **최종 선정 모델**: Claude Sonnet 4.6 (5개 평가축 25점 만점)
- **페르소나**: "다은" — 10년차 사내 커뮤니케이션 담당자 출신, 비즈니스 메일 작성 코치

---

## 저장소 구조

```
codyssey/mission-01/
├── codyssey.md                    과제 원문
├── requirements-checklist.md      요구사항 원문 1:1 대조 체크리스트
├── QnA.md                         예상 질문 자체 답변 연습 기록
├── model-comparison/              산출물 1 — 모델 비교·선정 보고서
├── system-design/                 산출물 2 — 시스템 설계 문서
├── execution-log/                 산출물 3 — 실행 로그(10턴 대화)
└── bonus/                         보너스 1·2
```

각 폴더는 "최종 문서 + 그 문서가 인용하는 원본 실측 로그"를 함께 담고 있습니다. 즉 문서에 적힌 모든 AI 응답·점수는 같은 폴더 안의 raw 파일로 재현 가능합니다.

---

## 산출물 1 — LLM 모델 비교·선정 보고서

📄 최종 문서: [`model-comparison/model-comparison.md`](codyssey/mission-01/model-comparison/model-comparison.md)
📄 테스트 설계: [`model-comparison/model-comparison-test-design.md`](codyssey/mission-01/model-comparison/model-comparison-test-design.md)
📄 모델별 원본 출력: [`model-comparison/model-outputs-raw.md`](codyssey/mission-01/model-comparison/model-outputs-raw.md)

동일한 메일 초안 작성 프롬프트를 3개 모델에 입력하고, 5개 평가 축(형식준수 / 톤 적합성 / 지시사항 반영 / 한국어 자연스러움 / 추가 디테일)으로 채점했습니다.

| 모델 | 요금제 | 환경 | 형식준수 | 톤적합성 | 지시반영 | 자연스러움 | 추가디테일 | **합계** |
|---|---|---|---|---|---|---|---|---|
| **Claude Sonnet 4.6** | 유료 | 웹 채팅 | 5 | 5 | 5 | 5 | 5 | **25** |
| Gemini 3.5 Flash | 무료 | 웹 채팅 | 5 | 5 | 5 | 5 | 0 | 20 |
| ChatGPT | 무료 | 웹 채팅 | 4 | 3 | 3 | 5 | 0 | 15 |

**최종 선정: Claude Sonnet 4.6.** 5개 축 전부 만점을 받았고, 특히 "추가 디테일" 축에서 별도 지시 없이도 제출 일정·프로젝트명 등 빈 정보를 구체화하도록 자발적으로 제안한 점이 결정적 차별 요인이었습니다. (근거 상세는 최종 보고서 6번 항목 참고)

---

## 산출물 2 — 시스템 설계 문서

📄 최종 문서: [`system-design/system-design.md`](codyssey/mission-01/system-design/system-design.md)

| 구성 요소 | 내용 |
|---|---|
| 문제 정의 | 업무용 이메일 표현/형식을 매번 고민하는 직장인을 위한 메일 초안 자동화 |
| 타겟 사용자 | 협력사/고객 대응 이메일을 자주 작성하는 직장인 |
| 입력 템플릿 | `[목적] [대상] [상황] [핵심 포인트] [톤] [금지어] [필수 포함 항목]` |
| 페르소나 | "다은" — 이름/직무/전문분야/말투/금지사항/우선순위(정확성 > 정중함 > 간결함) 명시 |
| 시스템 프롬프트 | 역할·목표 / 출력형식규칙 / 안전장치 / 사실·정책·수치 처리 규칙 4요소 포함 |
| Few-shot 예시 | 정상 입력 2개 + 모호한 입력 1개(AI가 되물어야 하는 케이스) |

### 단계적 추론 유도 (v1 → v2) — 실측 비교

같은 모호한 입력(Few-shot 예시 3)을 v1(간단 지시)과 v2(단계적 추론 유도)에 각각 실제로 적용해 비교했습니다.

| 버전 | 실측 결과 | 근거 |
|---|---|---|
| v1 (간단 지시) | 확인 질문 없이 톤·형식을 임의로 가정해 메일 2버전을 바로 완성 | [`v1-test-raw.md`](codyssey/mission-01/system-design/v1-test-raw.md) |
| v2 (단계적 추론 유도) | 확인 질문 3개를 먼저 제시하고 멈춤(임의로 완성하지 않음) | [`v2-example3-raw.md`](codyssey/mission-01/system-design/v2-example3-raw.md) |

재현성: 둘 다 Claude Sonnet 4.6 / 유료 / 2026-07-02 / 작업량 낮음 조건으로 실측. (v2는 Claude Projects "다은" 봇의 Knowledge에 올라간 Few-shot 예시 검색 효과가 결과에 일부 섞였을 가능성을 문서에 한계로 명시)

### 환각(Hallucination) 검증 — 6문항 실측

📄 원본 대화: [`hallucination-test-raw.md`](codyssey/mission-01/system-design/hallucination-test-raw.md)

| # | 질문 유형 | 판정 |
|---|---|---|
| 1 | 확인 안 된 사내 규정 | Pass (B — 확인 필요 명시) |
| 2 | 임의 이름/직급 요청 | Pass (B) |
| 3 | 확인 안 된 계약서 조항 | Pass (B) |
| 4 | 날짜 계산(검증 가능) | Pass (A — 정답+근거 제시) |
| 5 | 확인 안 된 과거 사례 | Pass (B) |
| 6 (추가) | 확정 안 된 보상 방침 | Pass (B) |

재현성: Claude Sonnet 4.6 / 유료 / Claude Projects "다은" 봇 / 2026-07-02 / 작업량 낮음.

---

## 산출물 3 — 실행 로그 (10턴 대화)

📄 정리본: [`execution-log/execution-log.md`](codyssey/mission-01/execution-log/execution-log.md)
📄 원본 전문: [`execution-log/conversation-log-raw.md`](codyssey/mission-01/execution-log/conversation-log-raw.md)

"다은"(시스템 프롬프트 v2) 페르소나로 10턴 대화를 수행하며 아래 상황을 모두 포함시켰습니다.

- **조건 변경**: 4턴 "유쾌한 톤" → 5턴 "격식 있는 톤"으로 변경 요청 — 변경된 부분만 반영, 나머지 확정 내용 유지
- **늦은 정보 제공**: 6턴에서 뒤늦게 보안 사고 사유 추가 — 민감 정보를 그대로 쓰지 않고 완곡한 대안 제시
- **미확정 사실 처리**: 8턴 보상 약속 요청 — 확정 안 된 보상을 단정하지 않고 확인 질문 후 완곡한 표현으로 반영

**결과**: 문맥 유지 Pass (확정 요구사항 10턴 내내 유지 + 조건 변경 시 변경분만 반영), 환각 방지 Pass.

---

## 보너스

| # | 내용 | 근거 |
|---|---|---|
| 보너스 1 | Claude Projects에 "다은" 페르소나를 커스텀 인스트럭션으로 배포, 실사용 테스트 완료 | [배포 가이드](codyssey/mission-01/bonus/bonus-1-bot-deployment.md) / [실측 로그](codyssey/mission-01/bonus/bonus-1-result.md) |
| 보너스 2 | 모델 비교 점수를 인포그래픽으로 시각화 | [생성 프롬프트](codyssey/mission-01/bonus/bonus-2-visualization-prompt.md) / [결과 이미지](codyssey/mission-01/bonus/bonus-2-result.png) |

---

## 재현성 기록

모든 실측은 아래 조건에서 진행되었으며, 무료 버전 사용 시 한계점을 각 문서에 1줄로 명시했습니다.

| 항목 | 내용 |
|---|---|
| 모델명 | Claude Sonnet 4.6 / Gemini 3.5 Flash / ChatGPT (각 문서에 상세 기재) |
| 요금제 | Claude: 유료 / Gemini·ChatGPT: 무료 |
| 사용 채널 | 웹 채팅 (일부는 Claude Projects) |
| 사용 날짜 | 2026-06-25 ~ 2026-07-02 |
| 주요 설정 | Claude: 작업량 낮음 / 그 외: 기본값(웹 UI 특성상 temperature 등 직접 설정 불가) |

## 안전/윤리 준수

- 실명·전화번호·주소 등 개인정보는 전부 `[협력사명]`, `[이름]` 같은 플레이스홀더로 처리
- 폭력적/선정적 콘텐츠 생성 시도 없음
- 사실/정책/수치가 포함되는 답변은 "근거 제시 또는 확인 필요" 규칙 전 구간 적용

## 산출물 자체 검증 (재감사)

산출물을 완료 처리한 뒤에도, 문서에 적힌 AI 행동 서술이 실제 raw 로그로 뒷받침되는지 재검토하는 과정을 별도로 거쳤습니다. 이 과정에서 근거 없이 서술되어 있던 3곳(v1 문제점 서술, 환각 검증 5문항, v2-예시3 출력 비교)을 발견해 전부 실제 재테스트 결과로 교체했습니다. 이 재검증 과정 자체가 미션 목표 5번("생성 결과를 테스트로 검증하고, 프롬프트를 반복 개선하는 과정을 재현 가능하게 설명할 수 있다")에 해당하는 실습이었습니다. 상세 이력은 [`system-design/system-design.md`](codyssey/mission-01/system-design/system-design.md)의 "수정" 표기 부분을 참고하세요.
