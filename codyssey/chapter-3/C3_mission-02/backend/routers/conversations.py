# routers/conversations.py
# /api/conversations 관련 엔드포인트 — 대화 저장/목록/상세조회/삭제

from fastapi import APIRouter, HTTPException
from datetime import datetime, timezone
from schemas import ConversationCreate
from services.firestore_service import db

router = APIRouter(prefix="/api/conversations", tags=["conversations"])
collection = db.collection("conversations")

@router.post("")  # POST /api/conversations : 대화 저장
def create_conversation(conversation: ConversationCreate):
    doc_ref = collection.document()
    data = conversation.model_dump()
    data["created_at"] = datetime.now(timezone.utc).isoformat()  # 생성 시각 기록
    doc_ref.set(data)
    return {"id": doc_ref.id, **data}

@router.get("")  # GET /api/conversations : 대화 목록 조회 (가벼운 요약만)
def list_conversations():
    docs = collection.stream()
    result = []
    for doc in docs:
        d = doc.to_dict()
        result.append({
            "id": doc.id,
            "title": d.get("title", "새 대화"),
            "created_at": d.get("created_at"),
            "message_count": len(d.get("messages", [])),  # 메시지 전체 대신 개수만 노출
        })
    return result

@router.get("/{conversation_id}")  # GET /api/conversations/{id} : 특정 대화 전체 메시지 조회
def get_conversation(conversation_id: str):
    doc_ref = collection.document(conversation_id)
    doc = doc_ref.get()
    if not doc.exists:
        raise HTTPException(status_code=404, detail="대화를 찾을 수 없습니다")
    return {"id": doc.id, **doc.to_dict()}

@router.delete("/{conversation_id}")  # DELETE /api/conversations/{id} : 대화 삭제
def delete_conversation(conversation_id: str):
    doc_ref = collection.document(conversation_id)
    if not doc_ref.get().exists:
        raise HTTPException(status_code=404, detail="대화를 찾을 수 없습니다")
    doc_ref.delete()
    return {"deleted_id": conversation_id}
