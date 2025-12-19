"""
Core resume analysis logic
"""

from app.model import get_gemini_client
from app.prompts import RESUME_ANALYSIS_PROMPT
from app.config import TEMPERATURE, MAX_OUTPUT_TOKENS, GEMINI_MODEL_NAME

class ResumeAnalyzer:
    def __init__(self):
        self.client = get_gemini_client()

    def analyze(self, resume_text: str) -> str:
        if not resume_text.strip():
            raise ValueError("Resume text is empty")

        prompt = RESUME_ANALYSIS_PROMPT.format(resume_text=resume_text)

        try:
            response = self.client.models.generate_content(
                model=GEMINI_MODEL_NAME,
                contents=prompt,
                config={
                    "temperature": TEMPERATURE,
                    "max_output_tokens": MAX_OUTPUT_TOKENS,
                },
            )
            # Log finish reason for debugging
            candidate = response.candidates[0]
            print("Finish reason:", candidate.finish_reason)

            return response.text
            


        except Exception as e:
            raise RuntimeError(f"Resume analysis failed: {e}")
