# GramiraML - Global Text Correction Tool

A Python application that provides instant grammar and text correction anywhere on your system. Simply type "@@fix" after any text to get AI-powered corrections.

## Features

- Global keyboard monitoring for "@@fix" trigger
- Instant text selection and replacement
- AI-powered text correction using Ollama
- Works in any text input field (browsers, applications, etc.)
- Direct integration with Ollama for fast processing

## Prerequisites

- Python 3.8+
- [Ollama](https://ollama.ai/) installed and running locally
- Administrator privileges (required for global keyboard monitoring)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/GramiraML.git
cd GramiraML
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Start the Ollama service (if not already running):
```bash
ollama serve
```

2. Start the keyboard monitor:
```bash
python main.py
```

3. Use the tool:
   - Type any text followed by "@@fix" in any text input field
   - The text will be automatically selected, processed, and replaced with the corrected version
   - Example: "this is a test @@fix" → "This is a test."

## Project Structure

- `main.py` - Keyboard monitoring and main application logic
- `text_processor.py` - Text selection and clipboard operations
- `command_parser.py` - Text parsing and prompt formatting
- `ollama_client.py` - Direct Ollama API integration

## How It Works

1. **Keyboard Monitoring**: The application monitors all keyboard input globally using the `keyboard` library
2. **Trigger Detection**: When "@@fix" is detected, the current text is selected and copied
3. **Text Processing**: The text is parsed and sent directly to Ollama for processing
4. **Text Replacement**: The corrected text is pasted back into the original location

## Requirements

```
requests
keyboard==0.13.5
uiautomation==2.0.18
pyautogui==0.9.54
python-logging-loki==0.3.1
pywin32==310
pyperclip==1.8.2
```

## Troubleshooting

- If the keyboard monitor doesn't work, try running it with administrator privileges
- Ensure Ollama is running and accessible at `http://localhost:11434`
- Verify all dependencies are installed correctly

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details. 