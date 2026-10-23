# routers/data.py
# /api/data 관련 엔드포인트 5개 — 라우터는 "요청을 받아 서비스(Firestore)를 호출하고 응답을 돌려주는" 역할만 한다

from fastapi import APIRouter, HTTPException
from schemas import DataItem
from services.firestore_service import db

router = APIRouter(prefix="/api/data", tags=["data"])  # 이 라우터의 모든 경로 앞에 /api/data가 자동으로 붙음
collection = db.collection("data")  # Firestore의 "data" 컬렉션 참조

@router.post("")  # POST /api/data : 새 데이터 추가
def create_data(item: DataItem):
    doc_ref = collection.document()      # Firestore가 고유 id를 자동 생성
    doc_ref.set(item.model_dump())       # Pydantic 모델을 dict로 바꿔 저장
    return {"id": doc_ref.id, **item.model_dump()}

@router.get("")  # GET /api/data : 데이터 목록 조회
def list_data():
    docs = collection.stream()
    return [{"id": doc.id, **doc.to_dict()} for doc in docs]

from services.analysis_service import get_summary as calculate_summary  # 파일 상단 import에 추가

@router.get("/summary")  # GET /api/data/summary : 데이터 요약(프롬프트 주입용)
def get_summary():
    return calculate_summary()  # 실제 계산은 서비스 계층에 위임


@router.put("/{item_id}")  # PUT /api/data/{id} : 데이터 수정
def update_data(item_id: str, item: DataItem):
    doc_ref = collection.document(item_id)
    if not doc_ref.get().exists:
        raise HTTPException(status_code=404, detail="데이터를 찾을 수 없습니다")
    doc_ref.set(item.model_dump())
    return {"id": item_id, **item.model_dump()}

@router.delete("/{item_id}")  # DELETE /api/data/{id} : 데이터 삭제
def delete_data(item_id: str):
    doc_ref = collection.document(item_id)
    if not doc_ref.get().exists:
        raise HTTPException(status_code=404, detail="데이터를 찾을 수 없습니다")
    doc_ref.delete()
    return {"deleted_id": item_id}
