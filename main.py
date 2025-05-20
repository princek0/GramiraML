from fastapi import FastAPI, Request
from pydantic import BaseModel
from command_parser import parse
from ollama_client import query
import uvicorn

app = FastAPI()

class TextRequest(BaseModel):
    input: str

@app.post("/process")
def process_text(request: TextRequest):
    parsed_prompt = parse(request.input)
    result = query(parsed_prompt)
    return {"output": result}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

