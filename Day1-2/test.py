# top_p_exp.py
import google.generativeai as genai
from dotenv import load_dotenv
import os
import time
import json

# Load env
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("API key not found. Set GEMINI_API_KEY in .env")

# Configure client
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-2.5-flash")

prompt = "What is the color of the sky on a clear day?"

# Experiments
top_p_values = [0.1, 0.5, 0.9]

output_dir = "top_p_outputs"
os.makedirs(output_dir, exist_ok=True)

summary = []

for top_p in top_p_values:
    print(f"\n--- top_p = {top_p} ---\n")
    response = model.generate_content(
        prompt,
        generation_config={"top_p": top_p}
    )
    # print("Response:", response)
    text = response.text or ""
    print(text)



