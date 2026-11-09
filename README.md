# 🤖 AI Research Agent

An AI-powered research assistant built using **Python, LangChain, and Groq**. It researches user queries using external tools, generates structured responses, and saves research findings to a text file.

## ✨ Features

- AI-powered research using Groq LLM.
- Web search using DuckDuckGo.
- Wikipedia integration for background information.
- Dynamic tool selection using LangChain Agents.
- Structured output validation using Pydantic.
- Save research results with timestamps.

## 🛠️ Tech Stack

- Python
- LangChain
- Groq (GPT-OSS-20B)
- DuckDuckGo Search
- Wikipedia API
- Pydantic

## 📂 Project Structure

```text
AI-Research-Agent/
├── main.py
├── tools.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## ⚙️ Setup & Installation

**1. Clone the repository**

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
cd YOUR_REPOSITORY
```

**2. Create and activate a virtual environment**

```bash
python -m venv venv
venv\Scripts\activate
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

**4. Configure API key**

Create a `.env` file using `.env.example` and add your Groq API key:

```env
GROQ_API_KEY=your_groq_api_key_here
```

Get your API key from [Groq Console](https://console.groq.com/keys).

**5. Run the application**

```bash
python main.py
```

## 💡 Example Query

- Research the history of artificial intelligence.
- What is the capital of India?

The agent selects relevant tools, gathers information, and generates a structured research response.

## 📄 Output

The agent generates a structured research response containing:

- Topic
- Summary
- Source URLs (when available)
- Tools used

Research results can also be saved to `research_output.txt`
with timestamps when requested.`

## ⚠️ Limitations

- Web search availability depends on network connectivity.
- Source URLs may not be available for every research query.
- Response quality depends on the LLM and retrieved information.

## 👩‍💻 Author

**Ruchika Vispute**

GitHub: [@ruchiii-codes](https://github.com/ruchiii-codes)

---

⭐ If you find this project useful, consider giving it a star!