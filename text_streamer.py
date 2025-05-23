import pyautogui
import keyboard
from typing import Optional

class TextStreamer:
    def __init__(self):
        self._is_streaming = False
        self._original_text: Optional[str] = None
        # List of keys to ignore when checking for interruption
        self._ignore_keys = {'ctrl', 'shift', 'alt', 'win'}
    
    def _simulate_key(self, text: str) -> bool:
        """
        Write text immediately, handling special cases.
        Returns True if successful, False if interrupted.
        """
        try:
            if self._check_interruption():
                return False
                
            # Handle newlines specially
            if '\n' in text:
                parts = text.split('\n')
                for i, part in enumerate(parts):
                    if part:  # Write non-empty parts
                        pyautogui.write(part)
                    if i < len(parts) - 1:  # Add shift+enter between parts
                        pyautogui.hotkey('shift', 'enter')
            else:
                pyautogui.write(text)
            return True
            
        except Exception as e:
            print(f"[ERROR] Text simulation failed: {str(e)}")
            return False
    
    def _check_interruption(self) -> bool:
        """Check if user has started typing (any key pressed)."""
        # Check all possible keys except ignored ones
        for key in keyboard._pressed_events:
            if key not in self._ignore_keys and keyboard.is_pressed(key):
                return True
        return False
    
    @property
    def is_streaming(self) -> bool:
        return self._is_streaming
    
    @property
    def original_text(self) -> Optional[str]:
        return self._original_text 