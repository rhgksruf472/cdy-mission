# analysis.py — 서울 기온 시계열 분석 (Q1: 연평균 추세)

import pandas as pd
import matplotlib.pyplot as plt
import os

# 그래프에 한글이 깨지지 않게 폰트 지정 (Windows 기본 한글 폰트)
plt.rcParams["font.family"] = "Malgun Gothic"
plt.rcParams["axes.unicode_minus"] = False  # 마이너스 기호(-) 깨짐 방지

os.makedirs("images", exist_ok=True)  # 그래프 저장할 폴더 준비

# 데이터 불러오기 + 혹시 모를 순서 뒤섞임 방지로 날짜순 재정렬
df = pd.read_csv("data/seoul_temperature_2016_2025.csv", parse_dates=["date"])
df = df.sort_values("date").reset_index(drop=True)

# ===== Q1: 서울 연평균 기온은 지난 10년간 상승 추세인가? =====

# [기법 1] 연도별 집계 — 날짜에서 연도만 뽑아 그룹으로 묶고 평균 계산
df["year"] = df["date"].dt.year
yearly_mean = df.groupby("year")["temp_mean"].mean()
print("=== 연도별 평균 기온(℃) ===")
print(yearly_mean)

change = yearly_mean.iloc[-1] - yearly_mean.iloc[0]
print(f"\n2016년 대비 2025년 변화: {change:+.2f}℃")

# [기법 2] 이동평균 — window=365: 매일, 그 날 기준 최근 365일 평균을 다시 계산
# center=True: 계산된 평균값을 window 중앙 날짜에 표시 (그래프가 좌우로 안 밀리게)
df["rolling_365d"] = df["temp_mean"].rolling(window=365, center=True).mean()

# 시각화 1 — 일별 원본(연하게, 노이즈 그대로) + 365일 이동평균(진하게, 추세만)
# [보강] 2016 vs 2025 두 해만 비교하면 그 해의 우연에 좌우된다.
# 그래서 앞 3개년 평균 vs 뒤 3개년 평균으로 비교해 더 안정적인 추세를 본다.
first3 = yearly_mean.loc[2016:2018].mean()
last3 = yearly_mean.loc[2023:2025].mean()
print(f"\n2016~2018 평균: {first3:.2f}℃")
print(f"2023~2025 평균: {last3:.2f}℃")
print(f"변화: {last3 - first3:+.2f}℃")

# 시각화 1 — 위: 전체 범위(일별+이동평균, 스케일 때문에 평평해 보임)
#          아래: 연평균만 확대(스케일 문제 해소, 추세가 실제로 보임)
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))

ax1.plot(df["date"], df["temp_mean"], alpha=0.2, color="gray", label="일별 평균 기온(원본)")
ax1.plot(df["date"], df["rolling_365d"], color="red", linewidth=2, label="365일 이동평균(추세)")
ax1.set_title("서울 일별 기온 (2016~2025) — 전체 범위 (스케일 때문에 추세가 평평해 보임)")
ax1.set_ylabel("기온(℃)")
ax1.legend()

ax2.plot(yearly_mean.index, yearly_mean.values, marker="o", color="red")
ax2.set_title("연평균 기온 확대판 — 같은 데이터, y축 범위만 좁힘")
ax2.set_xlabel("연도")
ax2.set_ylabel("연평균 기온(℃)")

plt.tight_layout()
plt.savefig("images/01_yearly_trend.png", dpi=150)
plt.close()
print("\n저장 완료: images/01_yearly_trend.png (2단 그래프)")


# ===== Q2: 여름과 겨울 중 어느 쪽이 더 빠르게 더워지고 있는가? =====

df["month"] = df["date"].dt.month

# [기법] 계절 배정 — 12월은 "다음 해 겨울"로 묶는다 (지난 학습에서 정한 기준)
# winter_year: 기본은 그 해 연도, 12월이면 연도+1
df["winter_year"] = df["year"].where(df["month"] != 12, df["year"] + 1)

summer = df[df["month"].isin([6, 7, 8])]
winter = df[df["month"].isin([12, 1, 2])]

# [기법] 계절별·연도별 집계 — 여름은 year 기준, 겨울은 winter_year 기준으로 그룹화
summer_yearly = summer.groupby("year")["temp_mean"].mean()
winter_yearly = winter.groupby("winter_year")["temp_mean"].mean()

# 2016~2025 둘 다 온전한 해만 비교 (겨울은 12월 있는 마지막 해 2025의 winter_year=2026이라 데이터가 없어 자동 제외됨)
print("=== 여름 연도별 평균(℃) ===")
print(summer_yearly)
print("\n=== 겨울 연도별 평균(℃) ===")
print(winter_yearly)

# [기법] 변화율 — 각 계절의 첫 3개년 대비 마지막 3개년 평균 차이 (Q1과 같은 방식으로 통일)
summer_change = summer_yearly.loc[2023:2025].mean() - summer_yearly.loc[2016:2018].mean()
winter_change = winter_yearly.loc[2023:2025].mean() - winter_yearly.loc[2017:2019].mean()
print(f"\n여름 변화(2016~18 대비 2023~25): {summer_change:+.2f}℃")
print(f"겨울 변화(2017~19 대비 2023~25): {winter_change:+.2f}℃")

# 시각화 2 — 여름/겨울 각각의 연도별 추이를 한 그래프에
plt.figure(figsize=(10, 5))
plt.plot(summer_yearly.index, summer_yearly.values, marker="o", color="orangered", label="여름(6~8월) 평균")
plt.plot(winter_yearly.index, winter_yearly.values, marker="o", color="steelblue", label="겨울(12~2월) 평균")
plt.title("서울 여름·겨울 평균 기온 추이 (2016~2025)")
plt.xlabel("연도")
plt.ylabel("기온(℃)")
plt.legend()
plt.tight_layout()
plt.savefig("images/02_summer_winter.png", dpi=150)
plt.close()
print("\n저장 완료: images/02_summer_winter.png")

# ===== Q3: 일최고기온 33℃ 이상 폭염일이 매년 늘고 있는가? =====

# [기법] 조건부 카운트 — temp_max >= 33 이 True/False로 계산되고, True=1이라 sum()하면 개수가 됨
df["is_heatwave"] = df["temp_max"] >= 33
heatwave_yearly = df.groupby("year")["is_heatwave"].sum()

print("=== 연도별 폭염일수(일) ===")
print(heatwave_yearly)

# 변화 비교 — Q1·Q2와 같은 방식(첫 3개년 vs 마지막 3개년)으로 통일
heatwave_change = heatwave_yearly.loc[2023:2025].mean() - heatwave_yearly.loc[2016:2018].mean()
print(f"\n폭염일수 변화(2016~18 평균 대비 2023~25 평균): {heatwave_change:+.1f}일")

# 시각화 3 — 연도별 폭염일수 막대그래프
plt.figure(figsize=(10, 5))
plt.bar(heatwave_yearly.index, heatwave_yearly.values, color="crimson")
plt.title("서울 연도별 폭염일수(일최고기온 33℃ 이상) 2016~2025")
plt.xlabel("연도")
plt.ylabel("폭염일수(일)")
plt.tight_layout()
plt.savefig("images/03_heatwave_days.png", dpi=150)
plt.close()
print("\n저장 완료: images/03_heatwave_days.png")

# [검증] 극단치(2018, 2025)에 덜 흔들리는 중앙값으로도 같은 방향인지 확인
heatwave_median_change = heatwave_yearly.loc[2023:2025].median() - heatwave_yearly.loc[2016:2018].median()
print(f"폭염일수 변화(중앙값 기준): {heatwave_median_change:+.1f}일")
