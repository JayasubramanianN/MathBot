from fastapi import APIRouter

from backend.models.schemas import ChatRequest
from backend.services.ollama_client import ask_ollama
from backend.services.solver import solve_expression

router = APIRouter(prefix="/api", tags=["Chat"])


@router.post("/chat")
def chat(request: ChatRequest):

    # Try solving with SymPy first
    result = solve_expression(request.message)

    if result is not None:
        return {
            "source": "SymPy",
            "question": request.message,
            "answer": result
        }

    # Otherwise ask Ollama
    answer = ask_ollama(request.message)

    return {
        "source": "Ollama",
        "question": request.message,
        "answer": answer
    }