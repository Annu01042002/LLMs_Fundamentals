import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load .env variables
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("API key not found. Set GEMINI_API_KEY in .env")

# Configure Gemini
genai.configure(api_key=api_key)

prompt = "Write a short story about a robot who learns emotions."
model = genai.GenerativeModel("gemini-2.5-flash")

# Folder to save outputs
output_dir = "temperature_outputs"
os.makedirs(output_dir, exist_ok=True)

for temp in [0.1, 0.7, 1.2]:
    print(f"\n--- Temperature = {temp} ---\n")

    response = model.generate_content(
        prompt,
        generation_config={"temperature": temp}
    )

    story = response.text
    print(story)

    # Save to file
    filename = f"temp_{temp}.txt"
    filepath = os.path.join(output_dir, filename)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(story)

    print(f"\nSaved to: {filepath}")
