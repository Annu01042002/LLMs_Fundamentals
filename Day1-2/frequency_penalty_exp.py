# frequency_penalty_exp.py
import google.generativeai as genai
from dotenv import load_dotenv
import os
import time
import json
import re
from collections import Counter

# Load env
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("API key not found. Set GEMINI_API_KEY in .env")

# Configure client
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-2.5-flash")

prompt = "Explain AI in 3 sentences."

# frequency_penalty values to test
fp_values = [0, 1]

output_dir = "frequency_outputs"
os.makedirs(output_dir, exist_ok=True)

def analyze_text(text):
    # simple word tokenization (alphanumeric)
    words = re.findall(r"\w+", text.lower())
    total_words = len(words)
    unique_words = len(set(words))
    repetition_ratio = 0.0
    top_repeats = []
    if total_words > 0:
        repetition_ratio = (total_words - unique_words) / total_words
        counts = Counter(words)
        top_repeats = counts.most_common(10)
    return {
        "total_words": total_words,
        "unique_words": unique_words,
        "repetition_ratio": repetition_ratio,
        "top_repeats": top_repeats
    }

summary = []

for fp in fp_values:
    try:
        print(f"\n--- frequency_penalty = {fp} ---\n")
        response = model.generate_content(
            prompt,
            generation_config={"frequency_penalty": fp}
        )
        text = response.text or ""
        print(text)

        # save to file
        safe_fp = str(fp).replace(".", "_")
        filename = f"frequency_{safe_fp}.txt"
        filepath = os.path.join(output_dir, filename)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(text)

        # analyze repetition
        analysis = analyze_text(text)

        entry = {
            "frequency_penalty": fp,
            "file": filepath,
            "length_chars": len(text),
            "length_words": analysis["total_words"],
            "unique_words": analysis["unique_words"],
            "repetition_ratio": round(analysis["repetition_ratio"], 4),
            "top_repeats": analysis["top_repeats"],
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
        }
        summary.append(entry)
        print(f"\nSaved to: {filepath}")
        print("Analysis:", json.dumps(entry, indent=2))

    except Exception as e:
        print(f"Error for frequency_penalty={fp}: {e}")
        summary.append({
            "frequency_penalty": fp,
            "file": None,
            "error": str(e),
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
        })

# Save summary JSON
summary_path = os.path.join(output_dir, "summary.json")
with open(summary_path, "w", encoding="utf-8") as sf:
    json.dump(summary, sf, indent=2)
print(f"\nSummary saved to: {summary_path}")
