import argparse
from datetime import datetime
import json
import os
import requests
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
KAKAO_REST_API_KEY = os.environ.get("KAKAO_REST_API_KEY")

GEMINI_MODEL = "gemini-3.7-flash"
GEMINI_URL = f"https://generativelanguage.googleapis.com/v1beta/models/{GEMINI_MODEL}:generateContent"
KAKAO_URL = "https://dapi.kakao.com/v2/local/search/keyword.json"


def check_api_keys():
    if not GEMINI_API_KEY or not KAKAO_REST_API_KEY:
        print("오류: API 키가 설정되지 않았습니다.")
        print(".env 파일에 GEMINI_API_KEY, KAKAO_REST_API_KEY를 설정해주세요.")
        exit(1)


def call_gemini(prompt):
    response = requests.post(
        GEMINI_URL,
        headers={"x-goog-api-key": GEMINI_API_KEY},
        json={"contents": [{"parts": [{"text": prompt}]}]},
    )
    response.raise_for_status()
    data = response.json()
    return data["candidates"][0]["content"]["parts"][0]["text"]



def get_recommendation(date):
    prompt = f"""당신은 국내 여행 추천 전문가입니다.
{date}에 여행하기 좋은 국내 여행지를 2~3곳 추천해주세요.

아래 형식의 JSON만 출력하세요. 설명 문장이나 코드블록 표시 없이 JSON 그 자체만 출력합니다.

{{
  "recommended_cities": ["도시 이름 1", "도시 이름 2", "도시 이름 3"],
  "weather": "{date} 무렵의 일반적인 날씨 요약",
  "events": ["행사/축제 이름 1~3개"],
  "reason": "추천 근거 2~4문장 (각 지역을 왜 골랐는지 포함)"
}}"""
    text = call_gemini(prompt)
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        print("  - JSON 파싱 실패. 1회만 재요청합니다...")
        retry_prompt = prompt + "\n\n앞선 응답이 JSON으로 파싱되지 않았습니다. 설명 없이 JSON만 다시 출력하세요."
        return json.loads(call_gemini(retry_prompt))


    
def search_restaurants(city, size=5):
    response = requests.get(
        KAKAO_URL,
        headers={"Authorization": f"KakaoAK {KAKAO_REST_API_KEY}"},
        params={"query": f"{city} 맛집", "size": size},
    )
    response.raise_for_status()
    documents = response.json()["documents"]

    restaurants = []
    for doc in documents:
        restaurants.append({
            "name": doc["place_name"],
            "address": doc["road_address_name"] or doc["address_name"],
            "category": doc["category_name"],
            "url": doc["place_url"],
            "x": float(doc["x"]),
            "y": float(doc["y"]),
        })
    return restaurants

   
def generate_report(date, recommendation, restaurants_by_city, errors):
    region_blocks = []
    for entry in restaurants_by_city:
        city = entry["city"]
        city_restaurants = entry["restaurants"]
        if city_restaurants:
            items = "\n".join(
                f"  - {r['name']} ({r['category']}) - {r['address']}" for r in city_restaurants
            )
        else:
            items = "  - 데이터 없음"
        region_blocks.append(f"[{city}]\n{items}")
    restaurant_lines = "\n".join(region_blocks)

    events_lines = "\n".join(f"- {e}" for e in recommendation["events"])

    if errors:
        errors_lines = "\n".join(f"- [{e['step']}] {e['type']}: {e['message']}" for e in errors)
    else:
        errors_lines = "없음"

    cities_text = ", ".join(recommendation["recommended_cities"])

    prompt = f"""당신은 여행 리포트 작성 전문가입니다. 아래 정보를 바탕으로 Markdown 형식의 국내 여행 추천 리포트를 작성하세요.

날짜: {date}
추천 지역(복수): {cities_text}
추천 이유: {recommendation['reason']}
날씨 요약: {recommendation['weather']}
행사/축제:
{events_lines}
맛집 목록(지역별):
{restaurant_lines}
오류 요약: {errors_lines}

아래 섹션을 모두 포함한 Markdown 리포트를 작성하세요. "맛집 추천" 섹션은 지역별로 소제목을 나눠 정리하세요. 설명 문장 없이 Markdown 본문만 출력합니다.

# {date} 국내 여행 추천 리포트
## 추천 지역
## 추천 이유
## 날씨 요약
## 행사/축제
## 맛집 추천
## 1일 일정 제안
## 오류 요약
"""
    return call_gemini(prompt)



def save_results(date, recommendation, restaurants, errors, report):
    os.makedirs("results", exist_ok=True)
    json_path = f"results/{date}_travel_data.json"
    md_path = f"results/{date}_travel_plan.md"

    data = {
        "recommendation": recommendation,
        "restaurants": restaurants,
        "errors": errors,
    }
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    with open(md_path, "w", encoding="utf-8") as f:
        f.write(report)

    return json_path, md_path


def parse_args():
    parser = argparse.ArgumentParser(description="국내 여행지 추천 프로그램")
    parser.add_argument("-date", required=True, help='여행 날짜 (형식: "YYYY-MM-DD")')
    args = parser.parse_args()

    try:
        datetime.strptime(args.date, "%Y-%m-%d")
    except ValueError:
        parser.print_usage()
        print('오류: 날짜 형식이 올바르지 않습니다. 예: -date "2026-03-15"')
        exit(1)

    return args.date


if __name__ == "__main__":
    travel_date = parse_args()
    check_api_keys()

    cache_path = f"results/{travel_date}_travel_data.json"
    if os.path.exists(cache_path):
        print(f"[캐시] {cache_path} 발견 — API 호출을 건너뛰고 저장된 데이터를 재사용합니다.")
        with open(cache_path, "r", encoding="utf-8") as f:
            cached = json.load(f)
        recommendation = cached["recommendation"]
        restaurants_by_city = cached["restaurants"]
        errors = cached["errors"]
    else:
        print("[1/3] 1차 추천 생성 중(LLM)...")
        recommendation = get_recommendation(travel_date)
        print(f"  - recommended_cities: {recommendation['recommended_cities']}")

        errors = []
        print("[2/3] 맛집 검색 중(지도/장소 API)...")
        restaurants_by_city = []
        for city in recommendation["recommended_cities"]:
            try:
                restaurants = search_restaurants(city)
                restaurants_by_city.append({"city": city, "restaurants": restaurants})
                print(f"  - {city} 맛집 {len(restaurants)}곳 검색 완료")
            except requests.exceptions.RequestException as e:
                restaurants_by_city.append({"city": city, "restaurants": []})
                errors.append({"step": "place_search", "type": "API_ERROR", "message": f"{city}: {e}"})
                print(f"  - 오류: {city} 맛집 검색 실패({e}). '데이터 없음'으로 처리하고 계속 진행합니다.")

    print("[3/3] 최종 리포트 생성 중(LLM)...")
    report = generate_report(travel_date, recommendation, restaurants_by_city, errors)
    print("  - 리포트 생성 완료")
    json_path, md_path = save_results(travel_date, recommendation, restaurants_by_city, errors, report)
    print(f"완료! {md_path} 를 확인하세요.")



