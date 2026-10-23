# seed_data.py
# data/results/usd_krw_fx_data.json의 실측 환율 데이터 281개를
# Firestore "data" 컬렉션에 한 번에 적재하는 1회성 스크립트

import json
from services.firestore_service import db

# data 폴더는 backend의 한 단계 위(../data)에 있음
with open("../data/results/usd_krw_fx_data.json", encoding="utf-8") as f:
    records = json.load(f)

collection = db.collection("data")
batch = db.batch()  # 여러 쓰기를 한 번에 묶어 보내는 배치 객체 (최대 500건까지 가능)

for record in records:
    doc_ref = collection.document()   # Firestore가 고유 id를 자동 생성
    batch.set(doc_ref, record)        # 배치에 쓰기 작업 추가 (아직 서버로 전송 안 됨)

batch.commit()  # 여기서 한 번에 전송 — 요청 281번 대신 1번

print(f"{len(records)}개 데이터 적재 완료")
