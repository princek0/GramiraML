# Desktop Text Improvement Assistant

## Overview
This project is a desktop assistant designed to help users improve the grammar, spelling, and fluency of any text they write across all applications. The assistant is intended to make text improvement seamless and universally accessible, without requiring users to switch apps or copy and paste their text.

## How It Works
- Users type their message anywhere—such as in chat apps, email, or social media—and append a simple command (like `@@fix`) at the end.
- By pressing a designated hotkey, the assistant will automatically detect this command, process the text, and replace it with a polished, corrected version in place.
- The system is designed to support additional commands, such as translating or summarizing text, triggered by similar suffixes.
- The tool runs locally on the user's machine to preserve privacy and avoid ongoing server costs.

> **Note:** The feature that allows the assistant to work anywhere you type (cross-application text replacement) is not yet implemented.

## Technology Stack
- **Backend:** Python with FastAPI
- **LLM:** Mistral 7B running locally via Ollama

## Features
- Detects special command suffixes (e.g., `@@fix`) in user input.
- Processes text to improve grammar, spelling, and fluency.
- Designed for extensibility to support additional commands (e.g., translation, summarization).
- Runs entirely on the user's local machine for privacy.

## Getting Started
1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd <your-repo-directory>
   ```
2. **Install dependencies:**
   Ensure you have Python 3.8+ installed. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```
3. **Set up Ollama and Mistral 7B:**
   - Follow the [Ollama documentation](https://ollama.com/) to install and run the Mistral 7B model locally.

4. **Run the FastAPI server:**
   ```bash
   uvicorn main:app --reload
   ```

## Usage
- Send text with a supported command suffix (e.g., `@@fix`) to the API endpoint.
- The backend will process the text and return the improved version.

## Roadmap
- [ ] Implement cross-application hotkey and text replacement functionality.
- [ ] Add more command suffixes for features like translation and summarization.
- [ ] Improve user interface and experience.

## Contributing
Contributions are welcome! Please open issues or submit pull requests for new features, bug fixes, or suggestions.

## License
This project is licensed under the MIT License.