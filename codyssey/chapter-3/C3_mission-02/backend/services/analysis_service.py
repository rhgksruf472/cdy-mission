# services/analysis_service.py
# 시계열 데이터 요약 계산 로직 — data 라우터와 chat 라우터가 공통으로 호출하기 위해 서비스로 분리

from services.firestore_service import db

def get_summary() -> dict:
    docs = list(db.collection("data").stream())
    if not docs:
        return {"period": None, "count": 0, "metrics": {}, "trend": "데이터 없음"}

    records = [doc.to_dict() for doc in docs]
    records.sort(key=lambda r: r["date"])   # 날짜순 정렬
    values = [r["value"] for r in records]

    trend = "유지"
    if values[-1] > values[0]:
        trend = "상승"
    elif values[-1] < values[0]:
        trend = "하락"

    return {
        "period": f"{records[0]['date']} ~ {records[-1]['date']}",
        "count": len(records),
        "metrics": {
            "average": round(sum(values) / len(values), 2),
            "max": max(values),
            "min": min(values),
        },
        "trend": trend,
    }
