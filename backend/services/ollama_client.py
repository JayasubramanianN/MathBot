import requests

from backend.config import OLLAMA_URL, MODEL_NAME


def ask_ollama(prompt: str):

    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(
        OLLAMA_URL,
        json=payload,
        timeout=120
    )

    response.raise_for_status()

    return response.json()["response"]