from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from llama_index import SimpleDirectoryReader, GPTVectorStoreIndex
from langchain.chat_models import ChatOpenAI
from langchain.chains.question_answering import load_qa_chain
import openai
import os

# ChatGPT API 키 설정
openai.api_key = "your_openai_api_key"

# FastAPI 애플리케이션 초기화
app = FastAPI()

# 정적 파일 및 템플릿 설정
app.mount("/static", StaticFiles(directory="static"), name="static")

# 코드 색인화 (초기화 시 한 번 실행)
documents = SimpleDirectoryReader('path/to/your/code').load_data()
index = GPTVectorStoreIndex.from_documents(documents)
openai_api = ChatOpenAI(api_key=openai.api_key)

# 요청 모델
class QueryRequest(BaseModel):
    question: str

# HTML 페이지 반환
@app.get("/", response_class=HTMLResponse)
async def get_chat_interface():
    with open("templates/index.html") as f:
        return HTMLResponse(content=f.read())

# 질문-응답 API
@app.post("/query")
async def query_code(request: QueryRequest):
    try:
        query = request.question
        result = index.query(query)
        context = result if result else "정보를 찾을 수 없습니다."

        # ChatGPT에 전달하여 응답 생성
        response_chain = load_qa_chain(openai_api)
        response = response_chain(query=query, context=context)
        return {"answer": response["output_text"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
