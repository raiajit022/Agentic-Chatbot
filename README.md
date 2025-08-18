# 🤖 LangGraph Agentic AI Chatbot

[![Python 3.13](https://img.shields.io/badge/python-3.13-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/streamlit-1.28+-red.svg)](https://streamlit.io/)
[![LangChain](https://img.shields.io/badge/langchain-latest-green.svg)](https://langchain.com/)
[![LangGraph](https://img.shields.io/badge/langgraph-latest-orange.svg)](https://langchain-ai.github.io/langgraph/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> **An advanced conversational AI system built with LangGraph and Streamlit, featuring stateful conversation management and modular agentic architecture.**

## 🌟 Features

- **🔄 Stateful Conversations**: Persistent chat history with session management
- **🎯 Modular Architecture**: Clean separation of concerns with dedicated modules
- **🌐 Web Interface**: Beautiful Streamlit-based UI with real-time chat
- **🔧 Configurable**: Easy configuration through INI files
- **🚀 Multiple LLM Support**: Currently supports Groq with easy extensibility
- **📊 Graph-Based Processing**: Powered by LangGraph for complex AI workflows
- **🔒 Secure**: API key management with environment variable support

## 🏗️ Architecture

```
AgenticChatbot/
├── 📱 app.py                          # Streamlit application entry point
├── 📋 requirements.txt                # Python dependencies
├── 📂 src/langgraphagenticai/
│   ├── 🧠 main.py                     # Core application logic
│   ├── 🤖 LLMS/                       # Language model integrations
│   │   └── groqllm.py                 # Groq LLM implementation
│   ├── 📊 graph/                      # LangGraph components
│   │   └── graph_builder.py           # Graph construction logic
│   ├── 🔗 nodes/                      # Processing nodes
│   │   └── basic_chatbot_node.py      # Basic chatbot node
│   ├── 🏪 state/                      # State management
│   │   └── state.py                   # Graph state definitions
│   ├── 🛠️ tools/                      # AI tools and utilities
│   └── 🎨 ui/                         # User interface components
│       ├── uiconfigfile.ini           # UI configuration
│       ├── uiconfigfile.py            # Configuration loader
│       └── streamlitui/               # Streamlit UI components
│           ├── loadui.py              # UI loader and controls
│           └── display_result.py      # Result display logic
```

## 🚀 Quick Start

### Prerequisites

- Python 3.13+
- Conda or pip package manager
- Groq API key ([Get one here](https://console.groq.com/keys))

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/raiajit022/Agentic-Chatbot.git
   cd AgenticChatbot
   ```

2. **Create and activate a virtual environment**
   ```bash
   # Using conda
   conda create -n agentic-chatbot python=3.13
   conda activate agentic-chatbot
   
   # Or using venv
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   streamlit run app.py
   ```

5. **Configure your API key**
   - Open the Streamlit interface in your browser
   - Enter your Groq API key in the sidebar
   - Select your preferred model and use case
   - Start chatting!

## 🎯 Usage

### Basic Chat

1. **Launch the app**: `streamlit run app.py`
2. **Configure settings** in the sidebar:
   - Select LLM provider (Groq)
   - Choose your model (llama3-8b-8192, llama3-70b-8192, gemma2-9b-it)
   - Enter your API key
   - Select use case (Basic_Chatbot)
3. **Start chatting** using the input box at the bottom
4. **Clear history** anytime using the sidebar button

### Environment Variables

For production use, set your API key as an environment variable:

```bash
export GROQ_API_KEY="your_api_key_here"
```

## 🔧 Configuration

### UI Configuration (`src/langgraphagenticai/ui/uiconfigfile.ini`)

```ini
[DEFAULT]
PAGE_TITLE = LangGraph: Build Stateful Agentic AI Graph
LLM_OPTIONS = Groq
USECASE_OPTIONS = Basic_Chatbot
GROQ_MODEL_OPTIONS = llama3-8b-8192, llama3-70b-8192, gemma2-9b-it
```

### Adding New LLM Providers

1. Create a new class in `src/langgraphagenticai/LLMS/`
2. Implement the `get_llm_model()` method
3. Update the configuration files
4. Add UI components in `loadui.py`

### Adding New Use Cases

1. Create new node classes in `src/langgraphagenticai/nodes/`
2. Add graph-building logic in `graph_builder.py`
3. Update the configuration file
4. Implement display logic in `display_result.py`

## 📦 Dependencies

| Package | Purpose | Version |
|---------|---------|---------|
| `langchain` | LLM framework | Latest |
| `langgraph` | Graph-based AI workflows | Latest |
| `langchain_groq` | Groq integration | Latest |
| `streamlit` | Web interface | Latest |
| `langchain_core` | Core LangChain components | Latest |
| `langchain_community` | Community integrations | Latest |
| `faiss-cpu` | Vector database | Latest |
| `tavily-python` | Search API | Latest |

## 🧪 Development

### Project Structure

- **Modular Design**: Each component has a specific responsibility
- **Configuration-Driven**: Easy to modify behaviour without code changes
- **Type Safety**: Uses TypedDict for state management
- **Error Handling**: Comprehensive exception handling throughout

### Code Style

- Follow PEP 8 guidelines
- Use type hints where applicable
- Document functions and classes
- Keep functions focused and small

### Testing

```bash
# Run tests (when available)
python -m pytest tests/

# Code formatting
black src/
flake8 src/
```

## 🤝 Contributing

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. **Commit your changes**
   ```bash
   git commit -m 'Add amazing feature'
   ```
4. **Push to the branch**
   ```bash
   git push origin feature/amazing-feature
   ```
5. **Open a Pull Request**

### Contribution Guidelines

- Ensure your code follows the project structure
- Add appropriate documentation
- Test your changes thoroughly
- Update the README if needed

### Common Issues

**"streamlit: command not found"**
```bash
# Make sure you're in the correct environment
conda activate agentic-chatbot
# Or reinstall streamlit
pip install streamlit
```

**"'GroqLLM' object has no attribute 'get_llm_model'"**
- This was a known issue that has been fixed in the latest version

**"No use case selected"**
- Ensure you've selected a use case in the sidebar before sending messages

**API Key Issues**
- Verify your Groq API key is valid
- Check if you've entered it correctly in the sidebar
- Ensure you have credits available

### Getting Help

- 📝 [Open an issue](https://github.com/raiajit022/Agentic-Chatbot/issues)
- 💬 Check existing issues for solutions

## 🗺️ Roadmap

- [ ] **Multi-Agent Support**: Add support for multiple specialized agents
- [ ] **Tool Integration**: Add function calling capabilities
- [ ] **Memory Systems**: Implement long-term memory
- [ ] **API Endpoints**: REST API for integration
- [ ] **Docker Support**: Containerization
- [ ] **More LLM Providers**: OpenAI, Anthropic, local models
- [ ] **Advanced Use Cases**: RAG, code generation, data analysis
- [ ] **Authentication**: User management system
- [ ] **Monitoring**: Logging and analytics
- [ ] **Testing Suite**: Comprehensive test coverage

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **LangChain Team** for the amazing framework
- **LangGraph** for graph-based AI workflows
- **Streamlit** for the beautiful web interface
- **Groq** for fast inference capabilities
- **Open Source Community** for inspiration and support

## 📈 Project Status

![GitHub last commit](https://img.shields.io/github/last-commit/raiajit022/Agentic-Chatbot)
![GitHub issues](https://img.shields.io/github/issues/raiajit022/Agentic-Chatbot)
![GitHub stars](https://img.shields.io/github/stars/raiajit022/Agentic-Chatbot)

**Current Version**: 1.0.0  
**Status**: Active Development  
---

<div align="center">

**⭐ Star this repo if you find it helpful!**

Made with ❤️ by [Ajit Rai](https://github.com/raiajit022)

</div>
