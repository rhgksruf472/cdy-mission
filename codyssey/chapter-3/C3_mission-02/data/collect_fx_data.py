# data/collect_fx_data.py
# 목적: Frankfurter 공개 API에서 USD -> KRW 일별 환율을 가져와
#       (date, value, memo) 레코드로 변환해 JSON 파일로 저장한다.

import json                            # 결과를 JSON 파일로 저장하기 위해 사용
import os                              # 저장 폴더(results)가 없으면 만들기 위해 사용
import urllib.request                  # 표준 라이브러리만으로 HTTP 요청을 보내기 위해 사용
from datetime import date, timedelta   # 오늘 날짜 기준으로 수집 기간을 자동 계산하기 위해 사용

# 수집 기간: 어제까지 ~ 약 400일 전부터 (평일에만 값이 있어 100개 이상 확보하려고 넉넉히 잡음)
end_date = date.today() - timedelta(days=1)
start_date = end_date - timedelta(days=400)

# Frankfurter는 API 키 없이 무료로 쓸 수 있는 공개 환율 API
url = f"https://api.frankfurter.dev/v1/{start_date}..{end_date}?from=USD&to=KRW"

# API 호출 후 응답 본문(JSON)을 파이썬 딕셔너리로 변환
# 수정: User-Agent 헤더를 붙인 요청 객체를 먼저 만들고 그걸로 요청
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
with urllib.request.urlopen(req) as response:
    raw = json.loads(response.read())


# raw["rates"]는 {"2025-01-02": {"KRW": 1467.23}, ...} 형태
# -> 미션이 요구하는 (date, value, memo) 형태의 리스트로 한 건씩 변환
records = []
for record_date, rate_info in sorted(raw["rates"].items()):
    records.append({
        "date": record_date,
        "value": rate_info["KRW"],
        "memo": "USD/KRW 환율 (Frankfurter API)",
    })

print(f"수집된 데이터 개수: {len(records)}")

# results 폴더가 없으면 자동 생성 후 그 안에 저장 (Firestore에 넣을 원본 + raw 로그 역할)
os.makedirs("results", exist_ok=True)
with open("results/usd_krw_fx_data.json", "w", encoding="utf-8") as f:
    json.dump(records, f, ensure_ascii=False, indent=2)
