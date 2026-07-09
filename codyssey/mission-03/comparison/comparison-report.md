# 프로젝트 1 — 자동화 도구 비교 분석 보고서

## 사용한 도구

- **Make** (make.com)
- **Zapier** (zapier.com)

## 동일 워크플로우

"문의 접수 시트에 새 행이 추가되면, 우선순위(높음/보통)에 따라 담당자에게 다른 방식으로 알림을 보낸다"

- Trigger: Google Sheets 새 행 감지
- 조건 분기: 우선순위 값 (높음 / 보통)
- Action: 높음 → Gmail 발송 / 보통 → Webhook(webhook.site) POST

설계 상세는 [`workflow-spec.md`](workflow-spec.md) 참고. 구현 캡처는 [`make/`](make/), [`zapier/`](zapier/) 폴더.

## 구현 과정 요약

**Make**: Google Sheets "Watch Rows" Trigger → Router(필터 2개 경로) → Gmail "Send an Email" / HTTP "Make a request" Action 순서로 구성. Trigger 설정 시 "Choose where to start"를 **All**로 선택해, 이미 입력해둔 테스트 행(높음/보통)을 그대로 재사용해 "Run once" 한 번으로 두 분기를 모두 검증할 수 있었다. Webhook Action의 Body를 "JSON string" 모드로 직접 타이핑하는 과정에서 문법 오류를 2차례 겪었다 — 1차로 중괄호·콤마·값 따옴표를 모두 빠뜨려 "not valid JSON" 오류, 수정 후에도 속성 사이 콤마를 빠뜨려 "Expected ',' or '}'" 오류가 재발했고, 콤마를 추가한 뒤에야 정상 실행됐다.

**Zapier**: Google Sheets "New Spreadsheet Row" Trigger → Paths(Path A / Path B, 각각 "Only continue if" 규칙) → Gmail "Send Email" / Webhooks by Zapier "POST" Action 순서로 구성. Webhook Action은 Payload Type을 **Json**으로 선택하면 key-value 표에 필드를 채우는 것만으로 Zapier가 유효한 JSON을 자동 생성해줘서, Make에서 겪었던 문법 오류 없이 한 번에 성공했다. 다만 Zapier에는 Make의 "All(백로그 재처리)" 같은 옵션이 없어, 이미 있던 테스트 행은 인식하지 못했고 시트에 새 행(높음 1개, 보통 1개)을 추가로 입력한 뒤 자동 폴링으로 실행되는 것을 확인했다.

## 비교 항목

| 비교 항목 | Make | Zapier |
|---|---|---|
| **UI/UX 방식** | 캔버스형 시각적 노드(원형 모듈+연결선), 확대/축소로 전체 흐름이 한눈에 보임 | 세로 트리형 리스트 + 우측 설정 패널, 스텝을 하나씩 클릭해 들어가는 방식 |
| **조건 분기 설계** | Router 하나에 경로를 자유롭게 추가하고, 각 경로 선 위의 필터 아이콘을 클릭해 조건 입력 | "Paths" 앱을 추가해 Path A/B 단위로 관리, 각 Path 내부의 "Only continue if"에 필드·연산자·값 입력 |
| **Webhook Body 작성 난이도** | "JSON string" 모드는 중괄호·콤마·따옴표를 직접 타이핑해야 해서 실제로 문법 오류를 2회 겪음 | "Json" Payload Type 선택 시 key-value 표 입력만으로 자동 생성 — 문법 오류 없이 한 번에 성공 |
| **테스트/실행 방식** | "Run once" 버튼으로 즉시 수동 실행, "Choose where to start=All"로 기존 데이터도 소급 재처리 가능 | 발행(Publish) 후 자동 폴링이 기본이라 결과 확인까지 대기 시간 발생, 새로 추가된 행만 감지(백로그 재처리 불가) |
| **실행 로그 확인 방식** | 캔버스 위에 모듈별 처리 건수·성공 배지가 바로 표시되고, Router 경로마다 "1st/2nd + 처리건수"로 분기별 실행 여부를 한눈에 확인 | Zap History에서 실행별 상세 로그 확인, 조건 불일치로 스킵된 경로는 "Path did not run as the rule conditions were not met"처럼 사유를 명시적으로 알려줌 |
| **필드 매핑 방식** | 매핑 가능한 필드가 초록 칩으로 표시되고 클릭해 삽입 | 필드 칩에 "스텝 번호 + 필드명"이 함께 표시되어(예: `1. 우선순위`) 어느 스텝에서 온 데이터인지 더 명확 |

## 각 도구의 장단점

**Make**
- 장점: 전체 워크플로우를 캔버스 하나로 조망할 수 있어 구조 파악이 빠르다. "Run once"로 즉시 반복 테스트가 가능하고, 기존 데이터를 백로그로 재처리할 수 있어 디버깅 속도가 빠르다.
- 단점: Webhook처럼 raw 형식으로 값을 입력해야 하는 Action에서는 사용자가 직접 문법(중괄호·콤마·따옴표)을 맞춰야 해서 실수 위험이 크다 — 이번 구현에서도 실제로 2차례 오류를 겪었다.

**Zapier**
- 장점: JSON payload를 key-value 표로 자동 생성해주기 때문에 문법 오류 위험이 낮다. Path 조건 설정 UI가 필드/연산자/값으로 딱 나뉘어 있어 구조가 명확하다.
- 단점: 즉시 실행 버튼이 없어 자동 폴링을 기다려야 하고, 기존 시트 데이터를 재사용하지 못해 테스트할 때마다 새 행을 추가해야 하는 번거로움이 있다.

## 어떤 상황에서 적합한가

- **Make**: 여러 갈래로 분기가 많거나 구조를 한눈에 보면서 설계해야 하는 경우, 혹은 설계 중 반복적으로 즉시 테스트하며 디버깅해야 하는 프로토타이핑 단계에 유리하다.
- **Zapier**: JSON/API 연동처럼 문법 실수가 발생하기 쉬운 Action을 초보자가 다뤄야 하는 경우, 또는 실행 이력을 텍스트 로그로 명확하게 남기고 싶은 경우에 더 안전하고 직관적이다.

## 무료 플랜 관련 참고

원문 예시에는 "Make 1,000 Ops/월 / Zapier 100 Tasks/월"이라는 수치가 있었지만, 이는 원문에 "참고 예시"로만 명시된 값이라 그대로 인용하지 않았다. 정확한 현재 한도는 각 계정의 대시보드(Make: 좌측 More → Billing, Zapier: 설정 → Billing)에서 직접 확인하는 것을 권장한다.
