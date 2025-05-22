import keyboard
import time
from text_processor import select_and_copy_text, paste_text
from api_client import process_text
from collections import deque

# Buffer to store last few characters
CHAR_BUFFER_SIZE = 5
char_buffer = deque(maxlen=CHAR_BUFFER_SIZE)

def check_for_trigger():
    """Check if the buffer contains @@fix"""
    buffer_str = ''.join(char_buffer)
    return buffer_str.endswith('@@fix')

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
        if check_for_trigger():
            print("\n[DEBUG] @@fix detected in buffer!")
            # Clear the buffer
            char_buffer.clear()
            # Process the text
            process_trigger()

def process_trigger():
    """
    Handles the @@fix trigger sequence:
    1. Select and copy current text
    2. Process text through API
    3. Paste processed text back
    """
    print("[DEBUG] Starting text processing...")
    
    # Get current text
    print("[DEBUG] Attempting to select and copy text...")
    original_text = select_and_copy_text()
    if not original_text:
        print("[ERROR] Failed to get text from clipboard")
        return
    print(f"[DEBUG] Successfully copied text: {original_text[:50]}...")
    
    # Process text through API
    print("[DEBUG] Sending text to API...")
    processed_text = process_text(original_text)
    if not processed_text:
        print("[ERROR] Failed to get response from API")
        return
    print(f"[DEBUG] Received processed text: {processed_text[:50]}...")
    
    # Paste processed text
    print("[DEBUG] Attempting to paste processed text...")
    paste_text(processed_text)
    print("[DEBUG] Paste operation completed")

def main():
    print("Starting @@fix monitor...")
    print("Press Ctrl+C to exit")
    print("[DEBUG] Starting keyboard monitoring...")
    
    # Register the keyboard hook
    keyboard.hook(on_key_event)
    print("[DEBUG] Keyboard hook registered successfully")
    
    # Keep the program running
    keyboard.wait('ctrl+c')

if __name__ == "__main__":
    main()

