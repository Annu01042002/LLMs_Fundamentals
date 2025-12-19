from fastapi import FastAPI, UploadFile, File
import tempfile
import os

from app.resume_parser import extract_text_from_pdf
from app.analyser import ResumeAnalyzer

app = FastAPI(title="AI Resume Analyzer")

analyzer = ResumeAnalyzer()


@app.post("/analyze-resume/")
async def analyze_resume(file: UploadFile = File(...)):
    if not file.filename.endswith(".pdf"):
        return {"error": "Only PDF files are supported"}

    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp:
        temp.write(await file.read())
        temp_path = temp.name

    try:
        resume_text = extract_text_from_pdf(temp_path)
        result = analyzer.analyze(resume_text)
        return {"analysis": result}

    finally:
        os.remove(temp_path)
