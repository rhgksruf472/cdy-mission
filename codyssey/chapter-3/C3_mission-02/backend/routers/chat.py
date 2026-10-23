# routers/chat.py
# POST /api/chat : 요약 조회 -> 시스템 프롬프트 주입 -> Gemini 호출 -> 대화 자동 저장

from fastapi import APIRouter
from datetime import datetime, timezone
from pydantic import BaseModel
from services.analysis_service import get_summary
from services.gemini_service import ask_gemini
from services.firestore_service import db

router = APIRouter(prefix="/api/chat", tags=["chat"])
conversations = db.collection("conversations")

class ChatRequest(BaseModel):
    message: str                         # 사용자 질문
    conversation_id: str | None = None   # 기존 대화에 이어붙일 id (없으면 새 대화 생성)

@router.post("")
def chat(req: ChatRequest):
    summary = get_summary()  # 1) 데이터 요약 조회

    # 2) 요약을 시스템 프롬프트에 삽입
    system_prompt = (
        "당신은 데이터 분석 비서입니다.\n\n"
        f"[사용자 데이터 요약]\n"
        f"- 데이터 기간: {summary['period']}\n"
        f"- 총 레코드: {summary['count']}개\n"
        f"- 주요 지표: {summary['metrics']}\n"
        f"- 최근 트렌드: {summary['trend']}\n\n"
        "위 데이터를 기반으로 맞춤형 답변을 제공하세요."
    )

    reply = ask_gemini(system_prompt, req.message)  # 3) Gemini API 호출

    # 4) 대화 내용을 conversations에 저장(자동 저장)
    now = datetime.now(timezone.utc).isoformat()
    new_messages = [
        {"role": "user", "content": req.message},
        {"role": "assistant", "content": reply},
    ]

    if req.conversation_id:
        doc_ref = conversations.document(req.conversation_id)
        doc = doc_ref.get()
        existing = doc.to_dict().get("messages", []) if doc.exists else []
        title = doc.to_dict().get("title", "새 대화") if doc.exists else req.message[:20]
        created_at = doc.to_dict().get("created_at", now) if doc.exists else now
        doc_ref.set({"title": title, "messages": existing + new_messages, "created_at": created_at})
        conversation_id = req.conversation_id
    else:
        doc_ref = conversations.document()
        doc_ref.set({"title": req.message[:20], "messages": new_messages, "created_at": now})
        conversation_id = doc_ref.id

    return {"reply": reply, "conversation_id": conversation_id}
