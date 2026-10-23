# services/firestore_service.py
# Firestore 연결을 담당하는 서비스 계층 — 라우터 파일들이 여기서 db 객체를 가져다 쓴다

import os
from dotenv import load_dotenv
import firebase_admin
from firebase_admin import credentials, firestore

load_dotenv()  # backend/.env 파일의 환경변수를 읽어와 os.environ에 등록

cred_path = os.getenv("FIREBASE_SERVICE_ACCOUNT_PATH")  # .env에서 키 파일 경로를 읽어옴
cred = credentials.Certificate(cred_path)                # 그 경로의 JSON으로 인증 정보 생성
firebase_admin.initialize_app(cred)                       # Firebase 앱 초기화 (앱 전체에서 1번만 실행)

db = firestore.client()  # Firestore 클라이언트 — 다른 파일에서 import해서 재사용
