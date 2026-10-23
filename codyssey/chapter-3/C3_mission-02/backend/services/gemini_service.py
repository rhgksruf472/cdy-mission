# services/gemini_service.py
# Gemini API 호출을 담당하는 서비스 계층 (최신 google-genai SDK 사용)

import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))  # .env의 키로 클라이언트 생성

def ask_gemini(system_prompt: str, user_message: str) -> str:
    response = client.models.generate_content(
        model="gemini-3.6-flash",                                   # 저렴하고 빠른 모델
        contents=user_message,                                       # 사용자 질문
        config=types.GenerateContentConfig(system_instruction=system_prompt),  # 시스템 프롬프트 주입
    )
    return response.text
