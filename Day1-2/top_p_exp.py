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

prompt = "Write a short story about a robot who learns emotions."

# Experiments
top_p_values = [0.1, 0.5, 0.9]

output_dir = "top_p_outputs"
os.makedirs(output_dir, exist_ok=True)

summary = []

for top_p in top_p_values:
    try:
        print(f"\n--- top_p = {top_p} ---\n")
        response = model.generate_content(
            prompt,
            generation_config={"top_p": top_p}
        )
        text = response.text or ""
        # Save file
        safe_top_p = str(top_p).replace(".", "_")
        filename = f"top_p_{safe_top_p}.txt"
        filepath = os.path.join(output_dir, filename)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(text)
        print(text)
        print(f"\nSaved to: {filepath}")

        # Collect metadata for summary
        summary.append({
            "top_p": top_p,
            "file": filepath,
            "length_chars": len(text),
            "length_words": len(text.split()),
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
        })

    except Exception as e:
        print(f"Error for top_p={top_p}: {e}")
        summary.append({
            "top_p": top_p,
            "file": None,
            "error": str(e),
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
        })

# Save summary JSON
summary_path = os.path.join(output_dir, "summary.json")
with open(summary_path, "w", encoding="utf-8") as sf:
    json.dump(summary, sf, indent=2)
print(f"\nSummary saved to: {summary_path}")
