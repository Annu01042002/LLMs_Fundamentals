import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load .env and API key
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env")

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-flash")

# --- PROMPTS FOR THE EXPERIMENT ---
prompts = [
    ("vague", "Explain how solar panels work."),
    
    ("detailed",
    """Explain how solar panels work in simple terms.
Include:
- what sunlight does,
- what photovoltaic cells do,
- how electricity is produced,
- and where this electricity goes in a home.
Limit to 6-8 sentences."""),

    ("structured",
    """Explain how solar panels work in this strict structure:

1. One sentence definition of a solar panel.
2. Two sentences explaining photovoltaic cells.
3. Two sentences describing how electricity is generated.
4. One sentence explaining how electricity enters a home system.
5. One example sentence.

Write clearly and simply."""
    )
]

# Create output directory
os.makedirs("prompt_quality_outputs", exist_ok=True)

# Loop through prompts
for label, prompt_text in prompts:
    print(f"\n=== Running prompt: {label} ===\n")
    try:
        response = model.generate_content(
            prompt_text,
            generation_config={"temperature": 0.7}
        )
        text = response.text if hasattr(response, "text") else ""
    except:
        text = ""

    print(text)

    # Save output
    filepath = f"prompt_quality_outputs/{label}.txt"
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"\nSaved → {filepath}")
