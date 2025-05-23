import time
from openai import OpenAI
import os
import sys

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

def query(prompt: str, model: str = "gpt-4.1-nano") -> str:
    """
    Query the OpenAI API with the given prompt.
    
    Args:
        prompt (str): The prompt to send to the model
        model (str): The model to use (defaults to GPT-4)
        
    Returns:
        str: The model's response
    """
    start_time = time.time()
    
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant that improves text by fixing grammar, spelling, and style while maintaining the original meaning."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,  # Lower temperature for more consistent corrections
            max_tokens=1000
        )
        
        result = response.choices[0].message.content.strip()
        end_time = time.time()
        
        print(f"[DEBUG] OpenAI {model} inference took: {(end_time - start_time)*1000:.2f}ms")
        return result
        
    except Exception as e:
        print(f"[ERROR] OpenAI API call failed: {str(e)}")
        raise 