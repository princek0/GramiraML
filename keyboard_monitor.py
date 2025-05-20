import keyboard
import logging
from typing import Optional, Callable
import uiautomation as auto
import pyautogui
import time
import threading
from main import process_text, TextRequest
from queue import Queue
import win32com.client
import pythoncom
import traceback

# Configure logging with both file and console output
logging.basicConfig(
    level=logging.DEBUG,  # Changed to DEBUG level
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('gramira_ml.log'),
        logging.StreamHandler()  # Add console output
    ]
)
logger = logging.getLogger(__name__)

class KeyboardMonitor:
    def __init__(self):
        self.buffer = ""
        self.trigger = "@@fix"
        self.text_queue = Queue()
        self.processing = False
        self.last_key_time = time.time()
        self.key_timeout = 0.5  # Time in seconds to consider a new word
        logger.info("KeyboardMonitor initialized with trigger: '%s'", self.trigger)
        
    def start_monitoring(self):
        """Start monitoring keyboard input globally"""
        logger.info("Starting keyboard monitoring")
        
        # Start the text processing thread
        self.processing_thread = threading.Thread(target=self._process_queue, daemon=True)
        self.processing_thread.start()
        logger.info("Processing thread started")
        
        # Start keyboard monitoring
        keyboard.on_press(self._on_key_press)
        logger.info("Keyboard hook installed")
        keyboard.wait()

    def _on_key_press(self, event):
        """Handle key press events"""
        try:
            current_time = time.time()
            logger.debug(f"Key pressed: '{event.name}' (scan_code: {event.scan_code})")
            
            # Handle special keys
            if event.name == 'backspace':
                if self.buffer:
                    self.buffer = self.buffer[:-1]
                    logger.debug(f"Buffer after backspace: '{self.buffer}'")
                return
            
            # Handle space and regular characters
            if event.name == 'space' or len(event.name) == 1:
                # Add character to buffer immediately
                char_to_add = ' ' if event.name == 'space' else event.name
                self.buffer += char_to_add
                logger.debug(f"Buffer after adding '{char_to_add}': '{self.buffer}'")
                
                # Check for trigger after adding the character
                if self.buffer.endswith(self.trigger):
                    # Get text before trigger
                    text_before_trigger = self.buffer[:-len(self.trigger)].strip()
                    logger.debug(f"Trigger detected. Full buffer: '{self.buffer}'")
                    logger.debug(f"Text before trigger: '{text_before_trigger}'")
                    
                    if text_before_trigger:  # Only process if there's actual text
                        logger.info(f"Trigger detected! Text to process: '{text_before_trigger}'")
                        self.text_queue.put(text_before_trigger)
                    else:
                        logger.info("Trigger detected but no text to process (buffer: '%s')", self.buffer)
                    self.buffer = ""  # Clear buffer after processing
                    return
                
                # Update last key time after processing
                self.last_key_time = current_time
                
                # Only clear buffer on timeout if we haven't just processed a trigger
                if current_time - self.last_key_time > self.key_timeout:
                    if self.buffer:  # Only log if buffer was not empty
                        logger.debug(f"Buffer cleared due to timeout. Previous buffer: '{self.buffer}'")
                    self.buffer = ""
                
        except Exception as e:
            logger.error(f"Error in key press handler: {str(e)}")
            logger.error(traceback.format_exc())

    def _process_queue(self):
        """Process text from the queue in a separate thread"""
        logger.info("Starting queue processing thread")
        # Initialize COM for this thread
        pythoncom.CoInitialize()
        
        while True:
            try:
                if not self.text_queue.empty():
                    text_to_correct = self.text_queue.get()
                    logger.info(f"Processing text from queue: '{text_to_correct}'")
                    self._process_text(text_to_correct)
                time.sleep(0.1)  # Small sleep to prevent CPU overuse
            except Exception as e:
                logger.error(f"Error in processing thread: {str(e)}")
                logger.error(traceback.format_exc())

    def _process_text(self, text_to_correct: str):
        """Process the text and replace it in the current text field"""
        try:
            if not text_to_correct or not text_to_correct.strip():
                logger.info("Empty text, skipping processing")
                return

            # Add the trigger back to the text before sending to API
            text_with_trigger = f"{text_to_correct}@@fix"
            logger.info(f"Making API call for text: '{text_with_trigger}'")
            
            # Get correction from API
            try:
                response = process_text(TextRequest(input=text_with_trigger))
                corrected_text = response["output"]
                logger.info(f"API Response: '{corrected_text}'")
            except Exception as e:
                logger.error(f"API call failed: {str(e)}")
                logger.error(traceback.format_exc())
                corrected_text = text_to_correct
            
            # If the API returns a generic response or error, use the original text
            if (not corrected_text or 
                "It seems like you accidentally" in corrected_text or 
                len(corrected_text) > len(text_to_correct) * 2 or
                "@@fix" in corrected_text):  # Also check if trigger is in response
                logger.info("Using original text due to invalid API response")
                corrected_text = text_to_correct
            
            logger.info(f"Final text to use: '{corrected_text}'")
            
            # Get the focused element using UI Automation
            logger.info("Getting focused element")
            focused_element = auto.GetFocusedControl()
            
            if focused_element:
                logger.info(f"Found focused element: {focused_element}")
                try:
                    # Try to get the actual edit control
                    if hasattr(focused_element, 'GetEditControl'):
                        edit_control = focused_element.GetEditControl()
                        if edit_control:
                            logger.info("Found edit control, attempting direct replacement")
                            edit_control.SetValue(corrected_text)
                            self.buffer = ""  # Clear buffer after successful replacement
                            return
                    
                    # If no edit control, try clipboard method
                    logger.info("Using clipboard method for text replacement")
                    self._replace_text_clipboard(corrected_text)
                    self.buffer = ""  # Clear buffer after successful replacement
                except Exception as e:
                    logger.error(f"Text replacement failed: {str(e)}")
                    logger.error(traceback.format_exc())
            else:
                logger.warning("No focused element found")
                
        except Exception as e:
            logger.error(f"Error in text processing: {str(e)}")
            logger.error(traceback.format_exc())

    def _replace_text_clipboard(self, new_text: str):
        """Replace text using clipboard as fallback"""
        try:
            logger.info(f"Starting clipboard replacement with text: '{new_text}'")
            
            # Clear any existing selection
            pyautogui.press('escape')
            time.sleep(0.2)  # Increased delay
            
            # Select all text
            pyautogui.hotkey('ctrl', 'a')
            time.sleep(0.3)  # Increased delay for selection
            
            # Delete selected text
            pyautogui.press('backspace')
            time.sleep(0.3)  # Increased delay for deletion
            
            # Type new text
            pyautogui.write(new_text)
            logger.info("Clipboard replacement completed")
            
        except Exception as e:
            logger.error(f"Clipboard replacement failed: {str(e)}")
            logger.error(traceback.format_exc())

def run_monitor():
    """Run the keyboard monitor"""
    try:
        # Initialize COM for the main thread
        pythoncom.CoInitialize()
        logger.info("COM initialized in main thread")
        
        monitor = KeyboardMonitor()
        monitor.start_monitoring()
    except Exception as e:
        logger.error(f"Error in run_monitor: {str(e)}")
        logger.error(traceback.format_exc())
        raise
    finally:
        try:
            pythoncom.CoUninitialize()
            logger.info("COM uninitialized")
        except:
            pass

if __name__ == "__main__":
    run_monitor() 