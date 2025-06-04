# Gramira - Global Text Transformation Tool

<div align="center">

![Version](https://img.shields.io/badge/version-1.0.1-blue.svg)
![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green.svg)

</div>

Gramira is a powerful Python application that provides instant text transformation and correction anywhere on your system. Simply type any of the supported triggers (e.g., "@@fix", "@@spanish", "@@formal") after any text to get AI-powered transformations powered by OpenAI's GPT-4.

## ✨ Features

- 🎯 **Global Text Transformation**: Works in any text input field across your system
- ⚡ **Multiple Triggers**: Use various triggers for different text transformations
- 🤖 **AI-Powered**: Utilizes OpenAI's GPT-4 for high-quality text processing
- 🔄 **Smart Selection**: Automatically selects and replaces text with transformed version
- 🛡️ **Secure**: Your API key is stored locally and never shared
- 📝 **Universal Compatibility**: Works in browsers, applications, and any text input field
- 🌍 **Language Support**: Translate text to different languages
- 🎨 **Style Transformations**: Convert text to different writing styles and tones

## 🎮 Available Triggers

### Text Correction
- `@@fix` - Improve grammar and spelling of the provided text

### Language Translation
- `@@spanish` - Translate the text to Spanish

### Writing Style
- `@@formal` - Convert the text to formal language
- `@@casual` - Convert the text to casual language
- `@@technical` - Convert the text to technical language
- `@@genz` - Convert the text to GenZ slang

## 📋 Prerequisites

- Python 3.8 or higher
- OpenAI API key
- Administrator privileges (required for global keyboard monitoring)
- Windows 10/11 (currently Windows-only due to UI automation requirements)

## 🚀 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/GramiraML.git
   cd GramiraML
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your OpenAI API key:**

   Choose one of the following methods:

   a. Using a .env file (recommended):
   ```bash
   # Copy the template file
   cp .env.template .env
   
   # Edit .env with your API key
   OPENAI_API_KEY=your-api-key-here
   ```

   b. Using environment variables:
   ```bash
   # Windows PowerShell
   $env:OPENAI_API_KEY="your-api-key-here"
   
   # Linux/macOS
   export OPENAI_API_KEY="your-api-key-here"
   ```

   Get your API key from: [OpenAI API Keys](https://platform.openai.com/api-keys)

## 💻 Usage

1. **Start the application:**
   ```bash
   python main.py
   ```

2. **Using the transformation tool:**
   - Type any text in any application
   - Add any of the supported triggers (e.g., "@@fix", "@@spanish", "@@formal") at the end of the text
   - The application will automatically:
     - Select the text
     - Send it to OpenAI for transformation
     - Replace it with the transformed version

## 📦 Project Structure

```
GramiraML/
├── main.py              # Main application entry point
├── text_processor.py    # Text processing and correction logic
├── command_parser.py    # Command parsing and handling
├── openai_client.py     # OpenAI API integration
├── text_streamer.py     # Text streaming and monitoring
├── requirements.txt     # Project dependencies
└── .env.template       # Environment variables template
```

## 🔧 Dependencies

- `openai>=1.12.0`: OpenAI API client
- `keyboard==0.13.5`: Global keyboard monitoring
- `uiautomation==2.0.18`: Windows UI automation
- `pyautogui==0.9.54`: GUI automation
- `python-dotenv>=1.0.0`: Environment variable management
- `pywin32==310`: Windows API integration
- `pyperclip==1.8.2`: Clipboard management
- Additional dependencies in `requirements.txt`

## 📦 Distribution

To distribute this application to other users:

1. **Create a release package:**
   ```bash
   # Create a zip file with the necessary files
   zip -r GramiraML.zip main.py text_processor.py command_parser.py openai_client.py text_streamer.py requirements.txt .env.template README.md
   ```

2. **User Setup Instructions:**
   - Extract the zip file
   - Install Python 3.8 or higher
   - Run `pip install -r requirements.txt`
   - Copy `.env.template` to `.env` and add their API key
   - Run `python main.py`

> **Note:** Each user needs their own OpenAI API key. The application will guide them through the setup process if the key is missing.

## 🔒 Security

- Your OpenAI API key is stored locally in the `.env` file
- The application never transmits your API key to any third-party services
- All text processing is done through secure OpenAI API endpoints
- No data is stored locally beyond the API key

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## ⚠️ Known Limitations

- Currently Windows-only due to UI automation requirements
- Requires administrator privileges for global keyboard monitoring
- Internet connection required for OpenAI API access
- May have slight delays depending on API response time

## 🆘 Troubleshooting

If you encounter any issues:

1. Ensure you have administrator privileges
2. Verify your OpenAI API key is correctly set in the `.env` file
3. Check your internet connection
4. Ensure all dependencies are installed correctly
5. Check the application logs for detailed error messages

## 📞 Support

For support, please open an issue in the GitHub repository or contact the maintainers.
