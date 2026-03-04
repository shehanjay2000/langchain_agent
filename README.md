# Personal Finance Assistant (CLI)

An AI-powered **command line personal finance assistant** built with **LangChain**, **SQLite**, and **Pandas**.
Ask questions in natural language and get answers directly from your financial data.

Examples:

* What are my unpaid bills?
* What bills are due this month?
* What are my income sources?
* How much did I spend on entertainment?
* Give me saving tips

---

# Features

* Natural language financial queries
* Bill tracking (paid, unpaid, upcoming)
* Budget monitoring
* Expense analysis
* Income summaries
* SQLite database storage
* Tool-based LangChain agent
* Conversation memory in CLI
* Offline knowledge search (RAG)

---

# Tech Stack

* LangChain
* SQLite
* Pandas
* Python
* Google Gemini (LLM)

---

# Project Structure

```
project/
│
├── agent_setup.py        # Agent + tools configuration
├── cli.py               # Command line interface
├── finance.db           # SQLite database
├── .env                 # API keys
│
├── tools/
│   ├── bill_tool.py
│   ├── budget_tool.py
│   ├── income_tool.py
│   ├── transactions_tool.py
│
├── rag/
│   ├── rag_setup.py     # ChromaDB + embeddings
│   ├── rag_tool.py      # Knowledge search tool
│   └── chroma_db/       # Vector store (auto created)
│
├── knowledge/
│   ├── budgeting.txt
│   ├── investing.txt
│   └── savings_tips.txt
│
├── requirements.txt
└── README.md
```

---

# Installation

## 1. Clone the repository

```bash
git clone <your-repo-url>
cd <project-folder>
```

---

## 2. Create virtual environment

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

# requirements.txt (example)

```
langchain
langchain-community
langchain-core
langchain-google-genai
chromadb
pandas
python-dotenv
sqlite3
sentence-transformers
```

---

# Environment Setup

Create `.env` file:

```
GEMINI-API-KEY=your_api_key_here
```

---

# Database Setup

Place:

```
finance.db
```

inside project root.

### Example tables

## bills

| Bill Name | Amount | Due Date   | Status |
| --------- | ------ | ---------- | ------ |
| Gas       | 400    | 2026-03-05 | Unpaid |

## income

| Source | Amount |

## budgets

| Category | Budget |

## transactions

| Category | Amount | Date |

---

# Run the Assistant

```bash
python cli.py
```

Output:

```
Personal Finance Assistant
Type 'exit' to quit

You:
```

---

# Example Usage

```
You: what are my unpaid bills
Assistant: Total unpaid bills: $13223.87. Unpaid bills: Water, Gas, Rent

You: what are my income sources
Assistant: Rental, Job, Investment, Freelance

You: what is my budget for food
Assistant: Your budget for Food & Drinks is $410.01

You: give me saving tips
Assistant: (retrieved advice from knowledge base)
```

---

# Tools Overview

## Bill Tool

Handles:

* unpaid bills
* paid bills
* monthly bills
* weekly bills

Queries SQLite and returns totals.

---

## Budget Tool

Handles:

* category budgets
* spending comparison
* over/under budget alerts

---

## Income Tool

Handles:

* income sources
* totals
* summaries

---

## Transactions Tool

Handles:

* category expenses
* spending analytics

---

## RAG Knowledge Tool

Provides:

* saving tips
* investing advice
* budgeting guidance

Uses:

* text files in `/knowledge`
* embeddings
* Chroma vector store

---

# How the System Works

```
User Question
     ↓
LangChain Agent
     ↓
Selects Tool
     ↓
SQLite / RAG
     ↓
Tool Result
     ↓
Final Answer
```

---

# Future Improvements

* Web dashboard (Streamlit/React)
* Charts & graphs
* Bill reminders
* Notifications
* CSV import/export
* Cloud deployment
* Authentication system

---

# License

MIT License

---

# Author

Shehan Jay
IT Undergraduate — AI/ML Learner & AI Projects
