# GramiraML - Global Text Correction Tool

A Python application that provides instant grammar and text correction anywhere on your system. Simply type "@@fix" after any text to get AI-powered corrections.

## Features

- Global keyboard monitoring for "@@fix" trigger
- Instant text selection and replacement
- AI-powered text correction using OpenAI's GPT-4
- Works in any text input field (browsers, applications, etc.)
- High-quality text correction with OpenAI's advanced language models

## Prerequisites

- Python 3.8+
- OpenAI API key
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

3. Set up your OpenAI API key (choose one method):

   a. Using a .env file (recommended):
   ```bash
   # Copy the template file
   cp .env.template .env
   
   # Edit .env with your API key
   # Replace 'your-api-key-here' with your actual OpenAI API key
   ```

   b. Using environment variables (temporary):
   ```bash
   # Windows PowerShell
   $env:OPENAI_API_KEY="your-api-key-here"
   
   # Linux/macOS
   export OPENAI_API_KEY="your-api-key-here"
   ```

   Get your API key from: https://platform.openai.com/api-keys

## Distribution

To distribute this application to other users:

1. Create a release package:
   ```bash
   # Create a zip file with the necessary files
   zip -r GramiraML.zip main.py text_processor.py command_parser.py openai_client.py requirements.txt .env.template README.md
   ```

2. Users should:
   - Extract the zip file
   - Install Python 3.8 or higher
   - Run `pip install -r requirements.txt`
   - Copy `.env.template` to `.env` and add their API key
   - Run `python main.py`

Note: Each user needs their own OpenAI API key. The application will guide them through the setup process if the key is missing.

## Usage

1. Start the keyboard monitor:
```