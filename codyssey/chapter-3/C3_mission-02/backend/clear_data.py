# clear_data.py
# "data" 컬렉션의 모든 문서를 삭제하는 1회성 스크립트
# (seed_data.py가 두 번 실행돼 데이터가 중복 적재된 것을 정리하기 위함)

from services.firestore_service import db

collection = db.collection("data")
docs = list(collection.stream())
print(f"삭제 대상: {len(docs)}개")

# 배치는 한 번에 최대 500건까지만 처리 가능하므로 500개씩 나눠서 삭제
for i in range(0, len(docs), 500):
    batch = db.batch()
    for doc in docs[i:i + 500]:
        batch.delete(doc.reference)
    batch.commit()

print("삭제 완료")
