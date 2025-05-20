# Desktop Text Improvement Assistant

## Overview
This project is a desktop assistant that automatically improves grammar, spelling, and fluency of text across any Windows application. Simply type your text followed by "@@fix" and the assistant will instantly replace it with a corrected version.

## Features
- **Cross-Application Support**: Works in any Windows application where you can type text
- **Instant Correction**: Type "@@fix" after your text to get immediate grammar and spelling corrections
- **Smart Text Processing**: Uses Mistral 7B (via Ollama) for intelligent text improvement
- **Background Operation**: Runs silently in the background, requiring no manual intervention
- **Privacy-Focused**: All processing happens locally on your machine

## How It Works
1. The application runs in the background with administrator privileges
2. When you type text followed by "@@fix" (e.g., "can u fix me@@fix")
3. The application:
   - Detects the trigger
   - Sends the text to the local API
   - Processes it through Mistral 7B
   - Automatically replaces the original text with the corrected version
4. The buffer is cleared after each correction, ready for the next text

## Requirements
- Windows 10 or later
- Python 3.8 or later
- Ollama with Mistral 7B model installed
- Administrator privileges (required for global keyboard monitoring)

## Installation
1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd <your-repo-directory>
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up Ollama:**
   - Install Ollama from [ollama.com](https://ollama.com)
   - Pull the Mistral model:
     ```bash
     ollama pull mistral
     ```

4. **Start the API server:**
   ```bash
   uvicorn main:app --reload
   ```

5. **Run the monitor:**
   ```bash
   python run_monitor.py
   ```

## Usage
1. Start both the API server and the monitor as described above
2. Type your text in any application
3. Add "@@fix" at the end of your text
4. The text will be automatically replaced with a corrected version

Example:
```
Original: "can u fix me@@fix"
Corrected: "Can you fix it for me?"
```

## Technical Details
- Uses `keyboard` library for global keyboard monitoring
- Implements UI Automation for text replacement
- FastAPI backend for text processing
- Mistral 7B model for intelligent text correction
- Clipboard fallback for applications with limited UI Automation support

## Troubleshooting
- If the application doesn't start, ensure you're running it with administrator privileges
- If text replacement doesn't work in some applications, try using a different text field
- Make sure both the API server and monitor are running
- Check `gramira_ml.log` for detailed error information

## Contributing
Contributions are welcome! Please open issues or submit pull requests for:
- Bug fixes
- Feature enhancements
- Additional command triggers
- UI/UX improvements

## License
This project is licensed under the MIT License.