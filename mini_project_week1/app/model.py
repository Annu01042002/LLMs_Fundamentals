"""
Gemini model initialization (no wrapper, clean & simple)
"""

from google import genai
from app.config import GEMINI_API_KEY, GEMINI_MODEL_NAME



def get_gemini_client():
    """
    Return Gemini client instance.
    """
    # Create a single reusable client
    client = genai.Client(api_key=GEMINI_API_KEY)
    return client
