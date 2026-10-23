# schemas.py
# API 요청/응답에 사용할 Pydantic 모델 — 형식이 안 맞으면 FastAPI가 자동으로 422 에러를 응답한다

from pydantic import BaseModel

class DataItem(BaseModel):
    date: str        # "YYYY-MM-DD" 형식의 날짜 문자열
    value: float      # 환율처럼 숫자로 다뤄야 하는 값
    memo: str = ""    # 메모, 값을 안 보내면 빈 문자열이 기본값이 됨
# 대화 기록 API에서 사용할 모델

class Message(BaseModel):
    role: str       # "user" 또는 "assistant"
    content: str    # 메시지 내용

class ConversationCreate(BaseModel):
    title: str = "새 대화"       # 값을 안 보내면 기본 제목 사용
    messages: list[Message] = []  # 값을 안 보내면 빈 대화로 생성
