
import os
import google.generativeai as genai
from dotenv import load_dotenv


load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("Please set GEMINI_API_KEY in your environment variables.")

genai.configure(api_key=GEMINI_API_KEY)

model=genai.GenerativeModel("gemini-2.5-flash")

prompt="What is Generative AI."
response = model.generate_content(prompt)
print(response.text)