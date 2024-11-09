
# CodeGPT 🎉

CodeGPT은 ChatGPT와 유사한 UI로 코드를 질문하고, 답변을 받는 웹 기반 애플리케이션입니다. LlamaIndex와 ChatGPT API를 연동하여 사용자가 코드베이스에 대한 질의를 할 수 있도록 구성되었습니다.

![Python](https://img.shields.io/badge/Python-3.7%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.85.0-green)
![ChatGPT API](https://img.shields.io/badge/ChatGPT%20API-OpenAI-yellow)
![JavaScript](https://img.shields.io/badge/JavaScript-ES6+-yellow)
![HTML](https://img.shields.io/badge/HTML-5-orange)
![CSS](https://img.shields.io/badge/CSS-3-blue)

## 📝 프로젝트 개요
CodeGPT은 ChatGPT와 같은 대화형 인터페이스를 통해 코드베이스에 대한 질문과 답변을 주고받을 수 있도록 만든 프로젝트입니다. 사용자는 질문을 입력하고, 코드베이스의 특정 부분에 대한 검색 결과와 함께 ChatGPT API를 통해 응답을 받을 수 있습니다.

## 🚀 주요 기능
- **질문-응답 형식의 채팅 인터페이스**: 사용자가 질문을 입력하고, 응답을 받을 수 있는 UI 제공
- **코드 검색 기능**: LlamaIndex를 활용하여 코드베이스를 색인화하고 특정 정보를 쿼리 가능
- **ChatGPT API 연동**: 코드 검색 결과를 바탕으로 ChatGPT의 자연어 처리 능력 활용

## 📂 폴더 구조
```
project_root/
├── main.py                 # FastAPI 백엔드 서버 및 API 구현
├── templates/
│   └── index.html          # HTML 템플릿
├── static/
│   ├── styles.css          # CSS 파일 (스타일 시트)
│   └── script.js           # JavaScript 파일 (프론트엔드 로직)
└── README.md               # 프로젝트 설명 파일
```

## 🛠️ 사용된 기술
- **언어**: Python, JavaScript, HTML, CSS
- **프레임워크 및 라이브러리**:
  - [FastAPI](https://fastapi.tiangolo.com/): 웹 서버 및 API 구현
  - [LlamaIndex](https://github.com/jerryjliu/llama_index): 코드 색인화 및 검색
  - [LangChain](https://github.com/hwchase17/langchain): ChatGPT API와 LlamaIndex의 연동을 위한 라이브러리
  - [OpenAI ChatGPT API](https://platform.openai.com/): 자연어 응답 생성

## ⚙️ 설치 방법

1. **Python 3.7+ 설치**
   - [Python 공식 사이트](https://www.python.org/downloads/)에서 Python 3.7 이상 버전을 설치합니다.

2. **프로젝트 클론 및 가상 환경 생성**
   ```bash
   git clone https://github.com/enyoares/CodeGPT.git
   cd CodeGPT
   python -m venv venv
   ```

3. **가상 환경 활성화**
   - **Windows**:
     ```bash
     venv\Scripts\activate
     ```
   - **Mac/Linux**:
     ```bash
     source venv/bin/activate
     ```

4. **필요 패키지 설치**
   ```bash
   pip install --upgrade llama-index fastapi uvicorn langchain openai
   ```

5. **OpenAI API 키 설정**
   - OpenAI 계정에서 API 키를 발급받고, `main.py` 파일에 키를 추가합니다.
     ```python
     openai.api_key = "your_openai_api_key"
     ```

6. **서버 실행**
   ```bash
   uvicorn main:app --reload
   ```

7. **브라우저에서 실행**
   - 브라우저에서 `http://localhost:8000`으로 접속하여 ChatGPT 스타일의 채팅 인터페이스를 통해 질문을 입력하고 답변을 받아보세요.

## 📸 화면 예시
![screenshot](https://via.placeholder.com/800x400.png?text=CodeGPT+Screenshot)

## 🤝 기여 방법
1. 이 리포지토리를 포크합니다.
2. 기능을 추가하거나 수정한 후 커밋합니다.
3. 새로운 브랜치를 만듭니다 (`git checkout -b feature/YourFeature`).
4. 변경 사항을 커밋합니다 (`git commit -am 'Add some feature'`).
5. 브랜치에 푸시합니다 (`git push origin feature/YourFeature`).
6. Pull Request를 생성합니다.

## 📄 라이센스
이 프로젝트는 MIT 라이센스를 따릅니다. 자세한 내용은 `LICENSE` 파일을 참조하세요.

---

여러분의 코드베이스 질의응답이 더욱 편리해지기를 바랍니다! 😊
