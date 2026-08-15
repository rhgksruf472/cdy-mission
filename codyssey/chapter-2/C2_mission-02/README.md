# 🗺️ Mission 02 - API 활용 국내 여행지 추천 프로그램

LLM API(Google Gemini)와 지도/장소 검색 API(Kakao Local)를 조합해, 입력한 날짜에 어울리는 국내 여행지를 추천하고 맛집까지 찾아 하나의 여행 리포트로 만들어주는 CLI 프로그램입니다.

## 요약

| 항목 | 내용 |
|---|---|
| 실행 파일 | `travel_planner.py` |
| 실행 명령 | `python travel_planner.py -date "YYYY-MM-DD"` |
| LLM API | Google Gemini (`gemini-3.7-flash`) |
| 지도/장소 검색 API | Kakao Local (키워드 장소 검색) |
| 결과물 | `results/{date}_travel_data.json`, `results/{date}_travel_plan.md` |
| 보너스 구현 | 복수 지역 추천(2~3곳), 결과 캐싱 |

## 목차

- [프로그램 개요](#프로그램-개요)
- [실행 방법](#실행-방법)
- [API 키 설정 방법](#api-키-설정-방법)
- [결과물 확인 방법](#결과물-확인-방법)
- [기능 요약](#기능-요약)
- [에러 처리 정책](#에러-처리-정책)
- [과제 목표 대응표](#과제-목표-대응표)
- [저장소 구조](#저장소-구조)
- [보안 주의사항](#보안-주의사항)

## 프로그램 개요

`-date "YYYY-MM-DD"`를 입력하면 아래 순서로 동작합니다.

1. **1차 추천 (LLM)**: 입력한 날짜를 Gemini에 보내 여행하기 좋은 국내 지역 2~3곳과 날씨 요약, 행사/축제, 추천 이유를 JSON으로 받습니다.
2. **맛집 검색 (지도 API)**: 추천받은 지역마다 Kakao Local API로 맛집을 최대 5곳씩 검색합니다.
3. **최종 리포트 생성 (LLM)**: 1·2단계 결과를 다시 Gemini에 보내 사람이 읽기 좋은 Markdown 리포트로 정리합니다.
4. **결과 저장**: 원본 데이터(JSON)와 최종 리포트(Markdown)를 `results/` 폴더에 저장합니다.

같은 날짜로 다시 실행하면, 이미 저장된 JSON이 있을 경우 1·2단계(추천·맛집 검색) API 호출은 건너뛰고 저장된 데이터로 리포트만 다시 생성합니다(비용/속도 절약).

## 실행 방법

1. 가상환경 생성 및 활성화 (Windows PowerShell 기준)

   ```
   python -m venv venv
   venv\Scripts\activate
   ```

2. 패키지 설치

   ```
   pip install -r requirements.txt
   ```

3. `.env` 파일 준비 — [API 키 설정 방법](#api-키-설정-방법) 참고

4. 실행

   ```
   python travel_planner.py -date "2026-03-15"
   ```

   실행 중 진행 로그(`[1/3]`~`[3/3]`)가 출력되고, 완료되면 결과 파일 경로가 안내됩니다.

## API 키 설정 방법

이 프로젝트 폴더(`C2_mission-02/`)에 `.env` 파일을 만들고 아래 두 줄을 작성합니다.

```
GEMINI_API_KEY=발급받은_Gemini_API_키
KAKAO_REST_API_KEY=발급받은_Kakao_REST_API_키
```

- **Gemini 키**: [Google AI Studio](https://ai.google.dev)에서 API 키를 생성합니다.
- **Kakao 키**: [Kakao Developers](https://developers.kakao.com) 콘솔에서 애플리케이션을 만들고 REST API 키를 확인합니다. 이때 앱의 제품 설정에서 **"카카오맵" 서비스를 반드시 활성화**해야 합니다 — 활성화하지 않으면 키가 유효해도 맛집 검색이 403(권한 없음)으로 거부됩니다.

`.env` 파일이 없거나 두 키 중 하나라도 비어있으면, 프로그램은 API를 전혀 호출하지 않고 즉시 안내 메시지를 출력한 뒤 종료합니다.

## 결과물 확인 방법

실행할 때마다 `results/` 폴더에 아래 두 파일이 생성됩니다 (파일명은 입력한 날짜 기준).

| 파일 | 내용 |
|---|---|
| `{date}_travel_data.json` | 1차 추천 JSON(`recommendation`), 지역별 맛집 검색 결과(`restaurants`), 오류 요약(`errors`) |
| `{date}_travel_plan.md` | 추천 지역·이유, 날씨, 행사/축제, 지역별 맛집, 1일 일정 제안, 오류 요약이 담긴 최종 리포트 |

`{date}_travel_plan.md`를 열어보면 사람이 읽기 좋은 완성된 리포트를 바로 확인할 수 있습니다.

## 기능 요약

| 기능 | 설명 |
|---|---|
| CLI 인터페이스 | `argparse`로 `-date` 필수 옵션 처리, 날짜 형식이 틀리면 사용법 출력 후 종료 |
| 복수 지역 추천 (보너스) | 1차 추천에서 `recommended_cities` 배열로 2~3개 지역을 받음 |
| 지역별 맛집 검색 (보너스) | 지역마다 반복문으로 Kakao Local을 호출해 지역별 맛집 리스트 구성 |
| 결과 캐싱 (보너스) | 같은 날짜의 원본 JSON이 있으면 추천·맛집 검색 API 호출을 건너뛰고 재사용 |
| 에러 처리 | API 키 미설정/지도 API 실패/JSON 파싱 실패를 모두 처리하며 프로그램이 중단되지 않음 |

## 에러 처리 정책

| 상황 | 처리 방식 |
|---|---|
| API 키 미설정 | 즉시 종료 + `.env` 설정 안내 출력 |
| 지도 API 실패 (401/403/네트워크 등) | 해당 지역 맛집을 "데이터 없음"으로 처리하고 나머지 지역·리포트 생성은 계속 진행 |
| 맛집 검색 0건 | 예외 없이 빈 리스트로 처리, 리포트에 "데이터 없음"으로 표기 |
| LLM JSON 파싱 실패 | 1회 재요청 후 재시도 (무한 재시도 없음) |

모든 실패는 `errors` 리스트(`{"step", "type", "message"}`)에 기록되어 원본 JSON과 최종 리포트의 "오류 요약" 섹션에 남습니다.

## 과제 목표 대응표

| 과제 목표 | 저장소 내 근거 |
|---|---|
| REST API 요청/응답 구조, GET/POST 차이 | `call_gemini()`는 `requests.post`(본문에 프롬프트), `search_restaurants()`는 `requests.get`(쿼리스트링에 검색어) |
| LLM JSON 출력을 다음 단계 입력으로 활용 | `get_recommendation()`이 반환한 `recommended_cities`를 `search_restaurants()`의 입력으로 그대로 사용 |
| 외부 API 오류 유형과 대응 원칙 | `check_api_keys()`(키 미설정), `try/except requests.exceptions.RequestException`(지도 API 실패), `try/except json.JSONDecodeError`(파싱 재시도) |
| API 키를 `.env`로 관리하는 이유 | `load_dotenv()` + `os.environ.get()`으로만 키를 읽으며, 코드 어디에도 키 값을 직접 작성하지 않음 |

## 저장소 구조

```
C2_mission-02/
├── codyssey.md              # 과제 원문
├── README.md                # 이 문서
├── requirements.txt         # requests, python-dotenv
├── travel_planner.py        # 메인 프로그램
└── results/                 # 실행 결과 (날짜별 JSON + Markdown)
```

`.env`, `venv/`, `requirements-checklist.md`, `QnA.md`는 저장소 루트 `.gitignore`에 등록되어 있어 GitHub에 올라가지 않습니다.

## 보안 주의사항

- API 키는 코드에 직접 작성하지 않고 `.env` → `os.environ.get()`으로만 읽습니다.
- `.env`는 `.gitignore`에 등록되어 git에 커밋되지 않습니다.
- 인증은 쿼리파라미터가 아닌 **헤더**로 전송합니다(`x-goog-api-key`, `Authorization: KakaoAK ...`). 개발 중 실제로 Gemini 키를 쿼리파라미터(`?key=`)로 보냈다가 에러 메시지의 URL에 키가 그대로 노출된 적이 있어, 이후 헤더 인증 방식으로 변경했습니다.
- 이 문서와 `results/`의 결과 파일 어디에도 실제 API 키 값은 포함되어 있지 않습니다.
