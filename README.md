# Agentic AI Projects

A collection of Agentic AI practice implementations built with Python and Agno. Each project focuses on a different agent pattern and is organized as an independent runnable example.

## Projects

### 01. Travel Agent

Demonstrates a web-enabled travel assistant that can answer travel questions with current information. Uses Agno, Groq, and DuckDuckGo tools.

Run with:

```bash
python 01-travel-agent/main.py
```

### 02. Finance Agent

Demonstrates an investment research agent that combines stock data and web search for prices, fundamentals, and analyst recommendations. Uses Agno, Google Gemini, YFinance, and DuckDuckGo tools.

Run with:

```bash
python 02-finance-agent/main.py
```

### 03. Agentic Memory

Demonstrates persistent user memory backed by SQLite, allowing an agent to recall information across interactions. Uses Agno, Groq, SQLite, and Rich.

Run with:

```bash
python 03-agentic-memory/main.py
```

The SQLite database is local-only and ignored by Git.

### 04. Multi-Agent Team

Demonstrates a team of specialized language agents coordinated by a team leader. Uses Agno and Google Gemini.

Run with:

```bash
python 04-multi-agent-team/main.py
```

### 05. YouTube Analyzer

Demonstrates a YouTube video analysis agent and a Streamlit interface for submitting video URLs. Uses Agno, Groq, YouTube tools, and Streamlit.

Run the backend example with:

```bash
python 05-youtube-analyzer/youtube_analyzer.py
```

Run the Streamlit UI with:

```bash
streamlit run 05-youtube-analyzer/app.py
```

## Setup

1. Create and activate a virtual environment.
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Copy `.env.example` to `.env` and add your own API credentials locally.

Never commit `.env`, API keys, generated caches, virtual environments, or local database files.