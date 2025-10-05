# Gemini-Powered Code Assistant Agent (AI Agent CLI Tool)

A **command-line AI agent** that leverages **Google's Gemini API** to act as an autonomous code assistant for **Python code analysis, debugging, and improvement**.  
The agent can **read Python files**, **detect issues**, **generate fixes**, and **execute code** to verify solutions, providing an automated approach to software debugging and code quality enhancement.


---

## Features
- **LLM-Powered Python Management**: The tool leverages a **Large Language Model (LLM)** to:
  - Read existing Python files
  - Modify and improve code
  - Create new Python files
  - Execute scripts safely within a controlled directory
- **Configurable Working Directory**: Set your preferred working folder in `config.py` using `WORKING_DIR`.
- **Secure Environment**: All operations are sandboxed to avoid accidental modifications outside the intended directory.
- **Customizable System Prompt**: The `sys_prompt.py` file defines how the LLM behaves when processing user commands.
- **API Key Management**: Uses a `.env` file to pass your Gemini API key securely.
- **Environment Setup with `uv`**: Lightweight, modern environment management for Python.

---

## Key Technologies
- **Python** – Core programming language
- **Google Gemini API** – Large Language Model integration
- **Environment Management:** [uv](https://github.com/astral-sh/uv)
- **CLI Development** – Command-line interface design
- **File I/O Operations** – Reading and writing Python files
- **Subprocess Management** – Code execution and verification
- **Prompt Engineering** – Crafting effective AI instructions
- **API Integration** – RESTful API communication
- **Error Handling** – Robust exception management

---

## My Contributions
- Designed and implemented the **core agent logic** for autonomous code analysis and modification
- Built **file operation handlers** for reading, writing, and managing Python source files
- Developed **prompt engineering strategies** for effective communication with the Gemini API
- Created **execution pipeline** for running and testing code changes automatically
- Implemented **error handling** for API calls, file operations, and code execution
- Designed a **user-friendly CLI interface** with clear feedback and progress indicators

---

## Key Features & Accomplishments
- **Autonomous Bug Detection**: Analyzes Python code for logical errors, syntax issues, and runtime problems
- **Automated Code Fixes**: Generates and applies fixes directly to source files
- **Verification System**: Executes modified code to validate solutions
- **Interactive CLI**: Simple, clean command-line interface for easy interaction
- **Real-world Application**: Successfully debugged and fixed a calculator application
- **Extensible Architecture**: Modular design for supporting additional LLM providers in the future

---


## ⚙️ Configuration

### **WORKING_DIR**
In `config.py`, set:
```python
WORKING_DIR = "./calculator"
```

### **SET UP .ENV FILE**
Create `.env` file, and set:
```python
GEMINI_API_KEY=your_api_key_here
```
---

## ▶️ How to Run the Project

1. **Install `uv`** (if not already installed):
   ```bash
   pip install uv
   ```
2. **Set up environment**:
   ```bash
   uv venv
   ```
3. **Run the app**:
   ```bash
   uv run main.py "Your prompt here"
   
---

## 🧠 How It Works

- **sys_prompt.py**: Contains the system prompt that defines the LLM's behavior and rules for processing user input.

- **Gemini API**: Handles LLM operations such as reading, running, modifying, and creating Python files.

- **WORKING_DIR**: Ensures all actions are restricted to a specific folder for safety.

---

## ✅ Practical Applications

- **Functional Tool**: Even if simple, it demonstrates real-world integration with an LLM.

- **Modern Tech**: Showcases concepts like AI agents, LLMs, API integration, and Python CLI development.

- **Portfolio Value**: Highlights initiative, problem-solving, and technical skills.

- **Skills Demonstrated**:

  - Python scripting

  - API integration

  - Secure environment setup

  - Prompt engineering

  - CLI tool design

---

## 🙌 Credit

**Special thanks to [Boot.dev](https://www.boot.dev) for helping me learn Python and back-end fundamentals.**

---

## ⚠️ Disclaimer

**Educational purposes only, do not run this with untrusted inputs or in production environments. Use with caution. Restrict the working directory to avoid unintentional file modifications.**












