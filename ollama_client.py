import requests

def query(prompt: str, model: str= "mistral") -> str: 
    response = requests.post(f"http://localhost:11434/api/generate", json={
        "model": model, 
        "prompt": prompt,
        "stream": False
    })

    return response.json()["response"]


# Sends prompt to local Mistral model and returns response