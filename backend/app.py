from fastapi import FastAPI
from backend.ollama_client import ask_ollama
from pydantic import BaseModel
app = FastAPI(
    title="MathBot API",
    description="Offline AI Math Tutor using Ollama",
    version="1.0.0"
)

class ChatRequest(BaseModel):
    message: str
@app.get("/")
def home():
    return {
        "message": "Welcome to MathBot!",
        "status": "Server is running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }

@app.post("/chat")
def chat(request: ChatRequest):

    answer = ask_ollama(request.message)

    return {
        "question": request.message,
        "answer": answer
    }