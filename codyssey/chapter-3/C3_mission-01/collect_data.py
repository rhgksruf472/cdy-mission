# collect_data.py — Open-Meteo에서 서울 일별 기온 10년치를 받아 CSV로 저장한다

import requests        # 인터넷으로 데이터를 요청하는 도구
import pandas as pd    # 표 형태 데이터를 다루는 도구 (pd라는 별명으로 부름)
import os              # 폴더 만들기 같은 운영체제 작업용

# 1) API에 보낼 조건들 — 어디의, 언제부터 언제까지, 무슨 값을 원하는지
URL = "https://archive-api.open-meteo.com/v1/archive"
params = {
    "latitude": 37.5665,          # 서울 위도
    "longitude": 126.9780,        # 서울 경도
    "start_date": "2016-01-01",   # 분석 시작일
    "end_date": "2025-12-31",     # 분석 종료일
    "daily": "temperature_2m_mean,temperature_2m_max,temperature_2m_min",  # 일평균/최고/최저 기온
    "timezone": "Asia/Seoul",     # 하루의 기준 시각을 한국 시간으로
}

# 2) 실제 요청을 보내고 응답을 받는다
print("데이터 요청 중...")
response = requests.get(URL, params=params)   # GET 방식으로 조회 요청
response.raise_for_status()                   # 응답이 정상(200)이 아니면 여기서 에러를 내고 멈춤
data = response.json()                        # JSON 문자열을 파이썬 딕셔너리로 변환

# 3) 응답 안의 daily 부분만 꺼내서 표(DataFrame)로 만든다
df = pd.DataFrame(data["daily"])

# 4) 컬럼 이름을 짧게 바꾸고, 날짜를 '문자열'이 아닌 '날짜 타입'으로 변환
df = df.rename(columns={
    "time": "date",
    "temperature_2m_mean": "temp_mean",
    "temperature_2m_max": "temp_max",
    "temperature_2m_min": "temp_min",
})
df["date"] = pd.to_datetime(df["date"])

# 5) data 폴더를 만들고 CSV로 저장 (index=False: 판다스가 붙이는 순번은 저장 안 함)
os.makedirs("data", exist_ok=True)
df.to_csv("data/seoul_temperature_2016_2025.csv", index=False, encoding="utf-8")

# 6) 제대로 받았는지 바로 확인 — 요구사항 '100개 이상'을 여기서 검증한다
print("저장 완료:", len(df), "일치")
print("기간:", df["date"].min().date(), "~", df["date"].max().date())
print(df.head())
