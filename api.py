# 라이브러리 설치
# pip install google-generativeai python-dotenv

import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

# API 키 설정
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

# 모델 초기화
model = genai.GenerativeModel('gemini-2.0-flash-lite')

# 대화형 채팅 시작
chat = model.start_chat(history=[])

print("Gemini AI와 채팅을 시작합니다. 'quit'라고 입력하면 종료됩니다.")

while True:
    user_input = input("You: ")
    if user_input.lower() == 'quit':
        print("채팅을 종료합니다.")
        break
    response = chat.send_message(user_input)
    print("Gemini:", response.text)