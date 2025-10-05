# Insight Project

새로운 프로젝트입니다.

## 시작하기

이 프로젝트에 대한 설명을 여기에 작성하세요.

## 환경 설정

1. Python 3.13 이상이 설치되어 있는지 확인하세요.

2. 필요한 패키지를 설치하세요:

   ```shell
   pip install -r requirements.txt
   ```

3. 환경 변수 설정:

   - `.env.example` 파일을 복사하여 `.env` 파일을 생성하세요:

     ```shell
     cp .env.example .env
     ```

   - `.env` 파일을 열고 `GOOGLE_API_KEY`에 실제 Google Generative AI API 키를 입력하세요.

## 사용법

`api.py`를 실행하여 Gemini AI와 채팅을 시작하세요:

```shell
python api.py
```

채팅 중 'quit'라고 입력하면 종료됩니다.
