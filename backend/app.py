from fastapi import FastAPI

app = FastAPI(
    title="MathBot API",
    description="Offline AI Math Tutor using Ollama",
    version="1.0.0"
)


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