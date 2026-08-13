# 보너스 2 — 멀티모달 확장 (모델 비교 결과 시각화)

`model-comparison/model-comparison.md`의 평가 축 점수표(Claude Sonnet 4.6 25점 / Gemini 3.5 Flash 20점 / ChatGPT 15점, 5개 평가 축)를 인포그래픽 이미지로 시각화한다.

## 이미지 생성 프롬프트 (DALL·E / Midjourney 등에 입력)

```
A clean, modern business infographic comparing 3 AI language models on an
email-drafting task, in a flat vector illustration style with a soft blue
and white corporate color palette.

Title at top: "LLM Model Comparison — Email Drafting Task"

A horizontal bar chart showing total scores out of 25:
- Claude Sonnet 4.6: 25 points (longest bar, highlighted in green, label "Winner")
- Gemini 3.5 Flash: 20 points (medium bar, blue)
- ChatGPT: 15 points (shortest bar, gray)

Below the chart, 5 small icons representing the evaluation criteria:
format compliance, tone fit, instruction accuracy, natural language,
extra detail — each as a simple labeled icon in a row.

Minimalist, presentation-ready, no real logos or brand marks, plenty of
white space, sans-serif typography, 16:9 aspect ratio.
```

## 사용 방법
1. 위 프롬프트를 ChatGPT(DALL·E), Midjourney, Gemini 등 이미지 생성 AI에 그대로 입력
2. 생성된 이미지를 이 폴더(`bonus/`)에 `bonus-2-result.png`로 저장 (완료됨)
3. Notion 산출물 섹션에도 기록 (완료됨)

## 참고: 실제 데이터 (이미지에 반영된 수치)
| 모델 | 형식준수 | 톤적합성 | 지시반영 | 자연스러움 | 추가디테일 | 합계 |
|---|---|---|---|---|---|---|
| Claude Sonnet 4.6 | 5 | 5 | 5 | 5 | 5 | 25 |
| Gemini 3.5 Flash | 5 | 5 | 5 | 5 | 0 | 20 |
| ChatGPT | 4 | 3 | 3 | 5 | 0 | 15 |
