# explore_data.py — 수집한 데이터의 기본 정보와 결측치/이상치 여부를 확인한다

import pandas as pd

# 1) 저장해둔 CSV를 다시 불러온다 (parse_dates: date 컬럼을 처음부터 날짜 타입으로 읽음)
df = pd.read_csv("data/seoul_temperature_2016_2025.csv", parse_dates=["date"])

# 2) 데이터 기본 정보 — 기간, 행/열 개수, 컬럼별 타입
print("=== 기본 정보 ===")
print("행 개수:", len(df))
print("기간:", df["date"].min().date(), "~", df["date"].max().date())
print(df.info())

# 3) 결측치 확인 — 컬럼별로 비어있는 값이 몇 개인지 센다
print("\n=== 결측치 개수 ===")
print(df.isnull().sum())

# 4) 날짜 누락 확인 — 10년치라면 3653일이 '연속으로' 다 있어야 함
expected_days = (df["date"].max() - df["date"].min()).days + 1
print("\n=== 날짜 누락 확인 ===")
print("실제 행 수:", len(df), "/ 기대 일수:", expected_days)

# 5) 이상치 후보 확인 — 기술통계로 최소/최대값이 물리적으로 말이 되는지 눈으로 점검
print("\n=== 기술 통계 (이상치 후보 점검용) ===")
print(df[["temp_mean", "temp_max", "temp_min"]].describe())

# 6) 논리 오류 확인 — 최저기온이 최고기온보다 높은 날이 있으면 데이터 자체가 잘못된 것
bad_rows = df[df["temp_min"] > df["temp_max"]]
print("\n=== temp_min > temp_max인 이상 행 수:", len(bad_rows))
