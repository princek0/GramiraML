import requests

API_URL = "http://localhost:8000/process"

def process_text(text: str) -> str:
    """
    Sends text to the API for processing and returns the response.
    Returns None if the API call fails.
    """
    try:
        print(f"[DEBUG] Sending POST request to {API_URL}")
        print(f"[DEBUG] Request payload: {{'input': '{text[:50]}...'}}")
        
        response = requests.post(API_URL, json={"input": text})
        print(f"[DEBUG] API Response status code: {response.status_code}")
        
        response.raise_for_status()  # Raises an exception for bad status codes
        result = response.json()["output"]
        print(f"[DEBUG] API Response content: {result[:50]}...")
        return result
    except requests.exceptions.ConnectionError:
        print("[ERROR] Failed to connect to API. Is the server running at http://localhost:8000?")
        return None
    except Exception as e:
        print(f"[ERROR] Error in process_text: {str(e)}")
        return None 