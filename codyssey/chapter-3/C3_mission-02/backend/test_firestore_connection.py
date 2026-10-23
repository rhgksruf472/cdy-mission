# test_firestore_connection.py
# Firestore 연결이 실제로 되는지 확인하기 위한 1회성 테스트 스크립트

from services.firestore_service import db  # 방금 만든 서비스에서 db 객체를 가져옴

# data 컬렉션과 섞이지 않도록 별도의 테스트용 컬렉션에 문서 1개 저장
doc_ref = db.collection("_connection_test").document("ping")
doc_ref.set({"message": "Firestore 연결 테스트 성공"})

# 방금 저장한 문서를 다시 읽어와서 화면에 출력 (쓰기+읽기 둘 다 확인)
print("Firestore 응답:", doc_ref.get().to_dict())
