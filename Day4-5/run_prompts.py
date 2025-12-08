import google.generativeai as genai
from dotenv import load_dotenv
import os
import json

# -------------------- Load API Key --------------------
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("API key not found. Set GEMINI_API_KEY in .env")

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-flash")  # using your same model

# -------------------- Load Input Text --------------------

base_dir = os.path.dirname(os.path.abspath(__file__))        # current script folder
input_path = os.path.join(base_dir, "input.txt")             

with open(input_path, "r", encoding="utf-8") as f:
    TEXT = f.read()

# -------------------- Prompt Variations --------------------
prompts = {
    "role_based.txt": f"You are an expert academic summarizer.\nSummarize the text:\n\n{TEXT}",

    "structured.txt": f"Summarize the text in **exactly 3 bullet points**:\n\n{TEXT}",

    "delimited.txt": f"""Summarize ONLY the text inside the ### markers.
###
{TEXT}
###""",

    "json_output.txt": f"""Summarize the text and return output strictly in JSON format:
{{
  "summary": ""
}}
TEXT:
{TEXT}""",

    "few_shot.txt": f"""Examples:

Text: "Plants convert sunlight into energy."
Summary: "Plants turn sunlight into usable energy."

Text: "The Earth orbits the Sun yearly."
Summary: "Earth completes one revolution around the Sun each year."

Now summarize this text similarly:
{TEXT}
"""
}

print("🚀 Starting prompt executions...")

# print(prompts.items())

# -------------------- Output Folder --------------------
output_dir = os.path.join(base_dir, "prompt_outputs")
os.makedirs(output_dir, exist_ok=True)

summary = {}

# -------------------- Run Prompts --------------------
for filename, prompt in prompts.items():
    print(f"\nRunning prompt → {filename}\n")

    response = model.generate_content(prompt)
    out = response.text.strip()

    # Save to /prompt_outputs/filename
    filepath = os.path.join(output_dir, filename)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(out)

    summary[filename] = out
    print(f"Saved → {filepath}")

# -------------------- Save summary.json --------------------
summary_path = os.path.join(output_dir, "summary.json")
with open(summary_path, "w", encoding="utf-8") as f:
    json.dump(summary, f, indent=2)

print("\n🎉 All prompts executed successfully!")
print(f"📁 Outputs saved inside → {output_dir}")
