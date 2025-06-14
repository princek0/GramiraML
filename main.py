import keyboard
import time
from text_processor import select_and_copy_text
from openai_client import query_stream
from command_parser import parse
from collections import deque
from dotenv import load_dotenv
import os
from text_streamer import TextStreamer
import pyautogui

# Load environment variables from .env file
load_dotenv()

# Buffer to store last few characters
CHAR_BUFFER_SIZE = 10  # Increased to accommodate longer trigger words
char_buffer = deque(maxlen=CHAR_BUFFER_SIZE)

# List of valid trigger words
TRIGGERS = ['@@fix', '@@spanish', '@@genz', '@@formal', '@@casual', '@@technical', '@@shorten', '@@expand', '@@summarize', '@@paraphrase']

# Initialize text streamer
text_streamer = TextStreamer()

def check_for_trigger() -> str | None:
    """
    Check if the buffer contains any of the valid trigger words.
    Returns the detected trigger word if found, None otherwise.
    """
    buffer_str = ''.join(char_buffer)
    for trigger in TRIGGERS:
        if buffer_str.endswith(trigger):
            return trigger
    return None

def on_key_event(event):
    """
    Handle each key press event
    """
    if event.event_type == keyboard.KEY_DOWN:
        # Add character to buffer
        if event.name == 'space':
            char_buffer.append(' ')
        elif len(event.name) == 1:  # Single character
            char_buffer.append(event.name)
        elif event.name == '@':
            char_buffer.append('@')
        
        # Check for trigger
        detected_trigger = check_for_trigger()
        if detected_trigger:
            print(f"\n[DEBUG] {detected_trigger} detected in buffer!")
            # Clear the buffer
            char_buffer.clear()
            # Process the text
            process_trigger()

def process_trigger():
    """
    Handles the @@fix and other triggers sequence:
    1. Select and copy current text 
    2. Stream processed text through OpenAI in real-time
    3. Type each chunk as it arrives
    """
    print("[DEBUG] Starting text processing...")
    
    # Get current text
    print("[DEBUG] Attempting to select and copy text...")
    original_text = select_and_copy_text()
    if not original_text:
        print("[ERROR] Failed to get text from clipboard")
        return
    print(f"[DEBUG] Successfully copied text: {original_text[:50]}...")
    
    # Process text through OpenAI
    print("[DEBUG] Sending text to OpenAI...")
    try:
        parsed_prompt = parse(original_text)
        
        # Select all text first, before starting the stream
        pyautogui.hotkey('ctrl', 'a')
        time.sleep(0.1)  # Small delay to ensure selection
        
        # Stream and type in real-time
        print("[DEBUG] Starting real-time streaming...")
        for chunk in query_stream(parsed_prompt):
            # Type each chunk as it arrives
            if not text_streamer._simulate_key(chunk):
                print("[DEBUG] Streaming interrupted by user")
                return
                
        print("[DEBUG] Streaming completed successfully")
        
    except Exception as e:
        print(f"[ERROR] Failed to process text with OpenAI: {str(e)}")
        return

def main():
    print("Starting monitor...")
    print("Press Ctrl+C to exit")
    print("[DEBUG] Starting keyboard monitoring...")
    
    # Register the keyboard hook
    keyboard.hook(on_key_event)
    print("[DEBUG] Keyboard hook registered successfully")
    
    # Keep the program running
    keyboard.wait('ctrl+c')

if __name__ == "__main__":
    main()

