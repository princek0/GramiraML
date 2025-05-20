import ctypes
import sys
import os
import logging
import traceback
import time
import pythoncom
import win32com.client

# Configure logging with both file and console output
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('gramira_ml.log'),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except Exception as e:
        logger.error(f"Error checking admin status: {str(e)}")
        return False

def run_as_admin():
    """Relaunch the script with admin privileges"""
    try:
        if not is_admin():
            logger.info("Requesting admin privileges...")
            # Re-run the program with admin rights
            ctypes.windll.shell32.ShellExecuteW(
                None, 
                "runas", 
                sys.executable, 
                " ".join(sys.argv), 
                None, 
                1
            )
            sys.exit(0)
        else:
            logger.info("Running with admin privileges")
    except Exception as e:
        logger.error(f"Error requesting admin privileges: {str(e)}")
        logger.error(traceback.format_exc())
        input("Press Enter to exit...")
        sys.exit(1)

def main():
    """Main function with error handling"""
    try:
        # Ensure we're running as admin
        run_as_admin()
        
        # Initialize COM
        logger.info("Initializing COM...")
        pythoncom.CoInitialize()
        
        # Start the keyboard monitor
        logger.info("Starting GramiraML monitor...")
        from keyboard_monitor import run_monitor
        run_monitor()
        
    except Exception as e:
        logger.error(f"Critical error in main: {str(e)}")
        logger.error(traceback.format_exc())
        print("\nAn error occurred. Check gramira_ml.log for details.")
        input("Press Enter to exit...")
        sys.exit(1)
    finally:
        try:
            pythoncom.CoUninitialize()
        except:
            pass

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logger.info("Program terminated by user")
        print("\nProgram terminated by user")
        input("Press Enter to exit...")
    except Exception as e:
        logger.error(f"Unhandled exception: {str(e)}")
        logger.error(traceback.format_exc())
        print("\nAn unexpected error occurred. Check gramira_ml.log for details.")
        input("Press Enter to exit...")
        sys.exit(1) 