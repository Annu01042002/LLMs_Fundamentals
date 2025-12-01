# top_k_exp.py
import google.generativeai as genai
from dotenv import load_dotenv
import os
import time
import json

# Load environment variables from .env
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("API key not found. Set GEMINI_API_KEY in .env")

# Configure Gemini client
genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-flash")
prompt = "Write a short story about a robot who learns emotions."

# Values for top-k experiment
top_k_values = [10, 50, 100]

output_dir = "top_k_outputs"
os.makedirs(output_dir, exist_ok=True)

summary = []

for k in top_k_values:
    try:
        print(f"\n--- top_k = {k} ---\n")

        response = model.generate_content(
            prompt,
            generation_config={"top_k": k}
        )

        text = response.text or ""
        print(text)

        safe_k = str(k)
        filename = f"top_k_{safe_k}.txt"
        filepath = os.path.join(output_dir, filename)

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(text)

        print(f"\nSaved to: {filepath}")

        summary.append({
            "top_k": k,
            "file": filepath,
            "length_chars": len(text),
            "length_words": len(text.split()),
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
        })

    except Exception as e:
        print(f"Error for top_k={k}: {e}")
        summary.append({
            "top_k": k,
            "file": None,
            "error": str(e),
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
        })

# Save summary
summary_path = os.path.join(output_dir, "summary.json")
with open(summary_path, "w", encoding="utf-8") as sf:
    json.dump(summary, sf, indent=2)

print(f"\nSummary saved to: {summary_path}")
