import requests
import time

def query(prompt: str, model: str = "mistral") -> str: 
    start_time = time.time()
    
    response = requests.post(f"http://localhost:11434/api/generate", json={
        "model": model, 
        "prompt": prompt,
        "stream": False
    })
    
    result = response.json()["response"]
    end_time = time.time()
    
    print(f"[DEBUG] {model} inference took: {(end_time - start_time)*1000:.2f}ms")
    return result


# Sends prompt to local Mistral model and returns response