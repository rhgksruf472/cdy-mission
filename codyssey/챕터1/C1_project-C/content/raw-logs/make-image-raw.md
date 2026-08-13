# 대표 이미지 생성 시도 — 실측 raw 로그 (도구 스펙 함정 발견)

- **주제**: 2026년 직장인 AI 생산성 도구 트렌드
- **실측 구분**: 개인 예습 — Make 이미지 모듈 실행 시도 (실패 기록, 도구 비교 자료로 보존)
- **재현성 정보**: Make(make.com) · Google Gemini AI › **Generate an Image** 모듈 · 모델 **Nano Banana 2 (Gemini 3.1 Flash Image)** = `gemini-3.1-flash-image` · 2026-07-20
- **용도**: 워크플로우 내 이미지 자동 생성이 무료 티어로 가능한지 실제 실행으로 검증

---

## 1. 모듈 옵션 실측 (스펙 확인 결과)

| 확인 항목 | 실제 UI |
|-----------|---------|
| 이미지 모델 | **Nano Banana 2 (Gemini 3.1 Flash Image)** (드롭다운) |
| 종횡비/사이즈 옵션 | **없음** — Aspect ratio/size 지정 칸 미제공 (프롬프트 내부에 `square 1:1` 문구로만 유도 가능) |
| Image prompt 입력 | 정상 (설계한 영문 프롬프트 붙여넣기 성공) |
| 출력 방식 | 확인 불가 (실행 실패로 결과 미도달) |
| 1회 생성 장수 | 확인 불가 (실행 실패) |

## 2. 실행 결과 — 429 RateLimitError (실패)

```
[429] You exceeded your current quota, please check your plan and billing details.
* Quota exceeded for metric: generativelanguage.googleapis.com/generate_content_free_tier_input_token_count, limit: 0, model: gemini-3.1-flash-image
* Quota exceeded for metric: generativelanguage.googleapis.com/generate_content_free_tier_requests, limit: 0, model: gemini-3.1-flash-image
Please retry in 1.063717386s.
Code: RateLimitError
Origin: Google Gemini AI
```

## 3. 원인 분석

- **`limit: 0`** = 소진된 쿼터가 아니라 **무료 티어 요청 한도 자체가 0**. 즉 `gemini-3.1-flash-image`(Nano Banana 2)는 **결제 활성화 없이는 이미지를 1장도 생성할 수 없는 유료 전용 모델**이다.
- 같은 커넥션의 **텍스트 모델(Gemini 3.5 Flash, `Generate a response`)은 무료로 정상 작동**했다(`make-run-raw.md`). → 무료/유료 경계가 **텍스트 vs 이미지**에서 갈린다.

## 3b. 모든 이미지 모델 무료 티어 0 확정 (2차 실측)

드롭다운의 이미지 모델 전체 목록:
- Nano Banana 2 (Gemini 3.1 Flash Image) — `gemini-3.1-flash-image`, **free limit 0**
- Nano Banana 2 Lite (Gemini 3.1 Flash Lite Image)
- Nano Banana Pro (Gemini 3 Pro Image)
- Nano Banana (Gemini 2.5 Flash Image) — `gemini-2.5-flash-preview-image`, **free limit 0** (교체 후 재시도 → 동일 429)

→ **구형 모델(2.5)로 낮춰도 `limit: 0` 동일**. 이 계정의 Gemini **이미지 생성은 모델 무관 전면 유료 전용**임이 실측으로 확정됨. (텍스트는 무료 정상)

## 4. 학습 포인트 (도구 스펙 확인 원칙)

- `workflow/workflow-spec.md`는 "Gemini 2.5 Flash Image 하루 ~500장 무료"라고 가정했으나, **실제로는 2.5·3.1 등 모든 이미지 모델이 무료 티어 0**(유료 전용). → **가정과 실제 스펙이 정반대였다.** 신규 도구(특히 이미지)는 반드시 실행 실측으로 무료 여부를 확인해야 한다는 원칙을 다시 입증.
- **텍스트/이미지 무료 경계**: 같은 Gemini 커넥션이라도 **텍스트=무료, 이미지=유료**로 갈린다. "Gemini 무료니까 이미지도 무료"라는 추론은 틀렸다.
- **결정된 해결 경로**: 무료 구형 모델이 없으므로 → **무료 이미지 API(Pollinations/Flux)를 Make HTTP `Download a file` 모듈로 연동**해 자동화를 유지(결제 불필요). 엔드포인트 실측 검증: HTTP 200 + JPEG 768~1024px 반환(키 불필요). 설계 반영: `workflow/workflow-spec.md`, `workflow/build-guide.md` Phase 5.

## 5. 빌드 진행 상태 (2026-07-20 · 재개 지점)

- HTTP `Download a file` 모듈 추가 + Pollinations URL(`encodeURL(...)`) 입력 완료.
- **매핑 이슈**: URL의 주제 태그가 존재하지 않는 module ID 1을 참조("references non-existing module") → 트리거 모듈에서 주제 필드를 **재매핑** 필요(검은 깨진 태그 삭제 후 실제 트리거 필드 클릭).
- **마지막 실행 결과**: Operation 1(Gemini **텍스트** 모듈)에서 `[503] high demand`(구글 서버 일시 과부하) → 이미지 모듈까지 도달 못 함. **코드·설정 문제 아님, 비용 문제 아님**(과금 0, Make operation 소량만 소모). 잠시 후 재시도 시 해소 예상.
- **다음 재개 시 할 일**: ①주제 태그 재매핑 확정 → ②Run once로 텍스트 3종 + 이미지까지 통과 확인 → ③노션 `대표이미지`(Files) 속성 연결(외부 URL 첨부 지원 여부 UI 확인) → ④실행/노션 결과 스크린샷.

## 6. Make 무료 크레딧 소진 (2026-07-20 · 실행 제약)

- Gemini 텍스트 모듈에서 반복 `503 high demand` → 안정 모델로 교체하려 재실행하던 중 **Make Free plan 크레딧 소진** 안내: "reached the limit of **1,000 credits or 0.5 GB** data transfer in the Free plan".
- **원인**: 월 1,000 operations 한도가 미션 03 + 본 프로젝트 반복 테스트로 누적 소진. 이미지 다운로드는 데이터 전송(0.5GB)도 소모. **과금 아님**(무료 할당량 소진, 다음 결제 주기에 리셋).
- **503과의 관계**: 503은 구글 서버 과부하(모델 교체로 완화 가능)였고, 크레딧 소진은 별개의 Make 플랫폼 한도. 두 제약이 겹쳐 예습 단계 풀 실행을 여기서 중단.
- **예습 단계 판단**: 텍스트 자동화는 실측 성공(`make-run-raw.md`), 이미지 연동은 설계+무료 API 검증 완료. **풀 실행(텍스트+이미지+노션 동시)은 크레딧 리셋 후 또는 팀 실전(팀원 계정)에서 완료**. 대표 이미지 asset 자체는 Pollinations URL을 브라우저로 직접 호출해 확보(도구·프롬프트 재현성 유지).
- **학습 포인트**: 노코드 자동화 플랫폼은 **월 실행 크레딧 한도**가 있어, 반복 테스트가 많은 개발 단계에서 소진되기 쉽다. 실측 테스트는 **성공 1회를 확실히 캡처**하고 불필요한 반복 실행을 줄이는 운영이 필요하다.
