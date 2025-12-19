"""
Run Resume Analyzer in terminal
"""

import os
from app.resume_parser import extract_text_from_pdf
from app.analyser import ResumeAnalyzer


def main():
    # Base directory (project root)
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # Resume path inside data folder
    resume_path = os.path.join(base_dir, "resumes", "anonymous_resume.pdf")

    if not os.path.exists(resume_path):
        print(f"❌ Resume not found at: {resume_path}")
        return

    print("📄 Parsing resume...")
    resume_text = extract_text_from_pdf(resume_path)

    analyzer = ResumeAnalyzer()

    print("🤖 Analyzing resume...\n")
    result = analyzer.analyze(resume_text)

    # -------------------- Save Output --------------------
    output_dir = os.path.join(base_dir, "outputs")
    os.makedirs(output_dir, exist_ok=True)

    output_file = os.path.join(output_dir, "resume_analysis.txt")

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(result)

    # -------------------- Print Output --------------------
    print("✅ Resume Analysis:\n")
    print(result)

    print(f"\n💾 Output saved to: {output_file}")


if __name__ == "__main__":
    main()
