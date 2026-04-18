# Syntra.AI — AI Microservice

FastAPI-based AI microservice for Syntra.AI graduation project.

## Features
| # | Feature | Approach | Endpoint |
|---|---------|----------|----------|
| 02 | Mini Learning Paths | Few-Shot | `POST /api/ai/mini-path` |
| 07 | AI Analysis & Recommendations | Few-Shot + Prompt Engineering | `POST /api/ai/analyze` |
| 08 | Auto Documentation & Reporting | Few-Shot | `POST /api/ai/document` |

## Setup

### 1. Create virtual environment
```bash
python -m venv venv
source venv/bin/activate        # Mac/Linux
venv\Scripts\activate           # Windows
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Create .env file
```bash
cp .env.example .env
# Then add your Gemini API Key inside .env
```

### 4. Run the server
```bash
uvicorn app.main:app --reload
```

### 5. Open API docs
```
http://localhost:8000/docs
```

## Project Structure
```
syntra-ai/
├── app/
│   ├── api/v1/routes/       ← FastAPI endpoints
│   ├── services/            ← Business logic
│   ├── chains/              ← LangChain logic
│   ├── prompts/             ← Few-Shot prompts
│   ├── models/              ← Pydantic models
│   ├── core/                ← Config, LLM, Exceptions
│   └── main.py
├── tests/
├── requirements.txt
└── .env.example
```

## Model
- **Gemini 2.5 Flash** via `langchain-google-genai`
