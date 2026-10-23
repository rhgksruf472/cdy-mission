# main.py
# FastAPI 앱을 생성하고, CORS 설정을 담당하는 진입점 파일
import os                       # 환경변수를 읽는 파이썬 기본 도구
from dotenv import load_dotenv  # .env 파일을 읽는 도구
load_dotenv()                   # .env 내용을 환경변수로 등록 (Render에는 .env가 없어도 에러 없이 넘어감)

from routers import data as data_router
from routers import conversations as conversations_router
from fastapi import FastAPI
from routers import chat as chat_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="AI 비서 API")  # FastAPI 앱 인스턴스 생성, title은 Swagger 문서 제목에 쓰임

# CORS: 다른 주소(프론트엔드)에서 오는 요청을 이 API가 허용하도록 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=os.getenv("ALLOWED_ORIGINS", "*").split(","),  # 환경변수에서 허용 주소를 읽음(없으면 "*"=전체 허용), 쉼표로 여러 주소 구분
    allow_methods=["*"],   # GET/POST/PUT/DELETE 등 모든 HTTP 메서드 허용
    allow_headers=["*"],   # 모든 요청 헤더 허용
)

@app.get("/")              # 서버가 정상 동작하는지 확인하는 헬스체크 엔드포인트
def read_root():
    return {"status": "ok"}
app.include_router(data_router.router)
app.include_router(conversations_router.router)
app.include_router(chat_router.router)