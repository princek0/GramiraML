import pyautogui
import pyperclip
import time

def select_and_copy_text():
    """
    Selects all text in the current text box and copies it to clipboard.
    Returns the copied text or None if operation fails.
    """
    try:
        print("[DEBUG] Pressing Ctrl+A...")
        pyautogui.hotkey('ctrl', 'a')
        time.sleep(0.1)  # Small delay to ensure selection
        print("[DEBUG] Ctrl+A completed")
        
        print("[DEBUG] Pressing Ctrl+C...")
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(0.1)  # Small delay to ensure copy
        print("[DEBUG] Ctrl+C completed")
        
        print("[DEBUG] Reading from clipboard...")
        text = pyperclip.paste()
        print(f"[DEBUG] Clipboard content length: {len(text) if text else 0} characters")
        return text
    except Exception as e:
        print(f"[ERROR] Error in select_and_copy_text: {str(e)}")
        return None

def paste_text(text: str):
    """
    Pastes the given text into the current text box.
    """
    try:
        print(f"[DEBUG] Copying text to clipboard (length: {len(text)})...")
        pyperclip.copy(text)
        time.sleep(0.1)  # Small delay to ensure copy
        print("[DEBUG] Text copied to clipboard")
        
        print("[DEBUG] Pressing Ctrl+V...")
        pyautogui.hotkey('ctrl', 'v')
        print("[DEBUG] Ctrl+V completed")
    except Exception as e:
        print(f"[ERROR] Error in paste_text: {str(e)}") 