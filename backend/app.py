from fastapi import FastAPI
from backend.ollama_client import ask_ollama
from pydantic import BaseModel
from backend.solver import solve_expression

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

    result = solve_expression(request.message)

    if result is not None:
        return {
            "source": "SymPy",
            "question": request.message,
            "answer": result
        }

    answer = ask_ollama(request.message)

    return {
        "source": "Ollama",
        "question": request.message,
        "answer": answer
    }