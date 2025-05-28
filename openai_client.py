import time
from openai import OpenAI
from dotenv import load_dotenv
import os
import sys
from typing import Generator

load_dotenv()

def get_api_key():
    """
    Get the OpenAI API key from environment variables.
    Raises a helpful error if the key is not found.
    """
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        print("\n[ERROR] OpenAI API key not found!")
        print("Please set your OpenAI API key using one of these methods:")
        print("\n1. Temporary (current session only):")
        print("   Windows PowerShell:")
        print("   $env:OPENAI_API_KEY='your-api-key-here'")
        print("   Linux/macOS:")
        print("   export OPENAI_API_KEY='your-api-key-here'")
        print("\n2. Permanent (recommended):")
        print("   Create a .env file in the application directory with:")
        print("   OPENAI_API_KEY=your-api-key-here")
        print("\nGet your API key from: https://platform.openai.com/api-keys")
        sys.exit(1)
    return api_key

# Initialize the OpenAI client
client = OpenAI(api_key=get_api_key())

def query_stream(prompt: str, model: str = "gpt-4.1-nano") -> Generator[str, None, None]:
    """
    Stream a query to the OpenAI API.
    
    Args:
        prompt (str): The prompt to send to the model
        model (str): The model to use
        
    Yields:
        str: The model's response chunks
    """
    start_time = time.time()
    
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant that improves text by fixing grammar, spelling, style, tone, language, punctuation, and other errors while maintaining the original meaning."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,
            max_tokens=1000,
            stream=True  # Enable streaming
        )
        
        collected_chunks = []
        for chunk in response:
            if chunk.choices[0].delta.content is not None:
                content = chunk.choices[0].delta.content
                collected_chunks.append(content)
                yield content
        
        end_time = time.time()
        print(f"[DEBUG] OpenAI {model} streaming completed in: {(end_time - start_time)*1000:.2f}ms")
        
    except Exception as e:
        print(f"[ERROR] OpenAI API streaming failed: {str(e)}")
        raise

# Keep the original query function for non-streaming use cases
def query(prompt: str, model: str = "gpt-4.1-nano") -> str:
    """
    Query the OpenAI API with the given prompt (non-streaming version).
    """
    return ''.join(query_stream(prompt, model)) 