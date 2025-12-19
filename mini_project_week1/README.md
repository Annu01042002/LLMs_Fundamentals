# 🧠 AI Resume Analyzer (GenAI Fundamentals – Mini Project)

A simple, clean GenAI-powered resume analyzer built to strengthen core LLM fundamentals:

- Prompt engineering
- Inference control
- Safety-aware design
- Real-world debugging

This project uses Gemini 2.5 Flash via the new `google.genai` SDK and includes:

- CLI usage
- FastAPI endpoint
- Streamlit UI

---

## 🎯 Project Goal

The goal is not to build a production ATS, but to deeply understand:

- How LLM inference works in practice
- How prompts affect model behavior
- How safety mechanisms influence generation
- Why real-world GenAI systems require orchestration

---

## 🏗️ Project Structure

mini_project_week1/
- app/
  - config.py        # Config, env variables, model name
  - model.py         # Gemini client initialization (google.genai)
  - resume_parser.py # PDF → text extraction
  - prompts.py       # Prompt templates
  - analyser.py      # ResumeAnalyzer logic

- outputs/           # Output after evaluation
- resumes/           # Resumes to evaluate(pdf files)
- cli.py             # CLI runner
- streamlit_app.py   # Streamlit UI
- main.py            # FastAPI app entry
- key_takeaways.md   # Takeaways from the project
- README.md

---

## ⚙️ Tech Stack

- Python
- Gemini 2.5 Flash
- google.genai (new SDK)
- FastAPI
- Streamlit
- PyPDF2

---

## 🚀 Setup Instructions

1) Create & activate virtual environment

```bash
python -m venv venv
venv\Scripts\Activate.ps1    # Windows PowerShell
```

2) Install dependencies

```bash
pip install -r requirements.txt
```

3) Set environment variable (your Gemini API key)

PowerShell (session):

```powershell
$env:GEMINI_API_KEY = "your_api_key_here"
```

Persistent (Windows):

```powershell
setx GEMINI_API_KEY "your_api_key_here"
```

---

## ▶️ How to Run

- CLI Mode

```bash
python app/cli.py 
```

- FastAPI

```bash
uvicorn main:app --reload
# then open: http://127.0.0.1:8000/docs
```

- Streamlit UI

```bash
streamlit run app/streamlit_app.py
```

---

## 🧠 High-Level Flow

PDF Resume
  ↓
Text Extraction (PyPDF2)
  ↓
Fixed Evaluation Prompt
  ↓
Gemini 2.5 Flash Inference
  ↓
Structured Resume Feedback

---

## ⚠️ Important Limitation (Key Learning)

One-shot generation is not always reliable for real resumes. During development we observed early stops when the model produced long, critical, or reputational analysis even with high `max_output_tokens`. This is due to built-in safety heuristics.

### 🔍 finish_reason values (observed meaning)

| Code | Meaning |
|------|---------|
| 0    | STOP – model completed normally |
| 1    | MAX_TOKENS – hit output token limit |
| 2    | SAFETY / other stop condition |
| 3    | POLICY / recitation |
| 4    | ERROR |

In this project we observed `finish_reason = 2` when producing long, critical analysis of real individuals — this is safety behavior, not a token-limit bug.

### Design implication

One-shot prompting works for simple/resume-like inputs. Complex or real resumes require multi-step (agentic) orchestration and continuation logic.

This project intentionally keeps a single-call design to surface this limitation for learning.

---

## 🧩 Future Improvements

- Convert analyzer into agentic multi-step flow
- Auto-continue generation when stopped by safety/limit
- Emit structured JSON output + validation schema
- Resume anonymization option
- Add an evaluation rubric & scoring logic

---

## 🧠 Key Learnings

- `max_output_tokens` does not guarantee full output
- Prompt tone influences safety behavior
- Safety is a system design concern, not an edge case
- Observability (finish_reason) is critical for debugging
- One-shot prompting does not scale to real-world use cases

---

## 📌 Disclaimer

This project is for learning and experimentation only. It is not intended for production use without additional safety, evaluation, and robustness improvements.

---

## 👤 Author

Built as part of GenAI Fundamentals – Week 1 learning journey by Annu.
