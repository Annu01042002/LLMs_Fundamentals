import streamlit as st
import tempfile
import os

from app.resume_parser import extract_text_from_pdf
from app.analyser import ResumeAnalyzer

st.title("📄 AI Resume Analyzer")

uploaded_file = st.file_uploader("Upload your resume (PDF)", type=["pdf"])

if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp:
        temp.write(uploaded_file.read())
        temp_path = temp.name

    try:
        st.info("Analyzing resume...")
        resume_text = extract_text_from_pdf(temp_path)

        analyzer = ResumeAnalyzer()
        result = analyzer.analyze(resume_text)

        st.success("Analysis complete!")
        st.text_area("Resume Feedback", result, height=400)

    finally:
        os.remove(temp_path)
