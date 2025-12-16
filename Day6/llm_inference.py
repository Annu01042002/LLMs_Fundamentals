"""
Day 6 - LLM Inference & Parameters (Gemini)
Experiments:
1. max_output_tokens
2. deterministic vs creative
3. stop sequences
"""

import os
import google.generativeai as genai
from dotenv import load_dotenv

# ==============================
# 0. Setup
# ==============================

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("Please set GEMINI_API_KEY in your environment variables.")

genai.configure(api_key=GEMINI_API_KEY)

base_dir = os.path.dirname(os.path.abspath(__file__))

# -------------------- Output Folder --------------------
output_dir = os.path.join(base_dir, "llm_inference_outputs")
os.makedirs(output_dir, exist_ok=True)

def generate(
    prompt,
    temperature=0.7,
    max_tokens=200,
    top_p=None,
    stop_sequences=None
):
    generation_config = {
        "temperature": temperature,
        "max_output_tokens": max_tokens
    }

    if top_p is not None:
        generation_config["top_p"] = top_p

    if stop_sequences is not None:
        generation_config["stop_sequences"] = stop_sequences

    model = genai.GenerativeModel("gemini-2.5-flash")

    response = model.generate_content(
        prompt,
        generation_config=generation_config
    )

    # SAFE extraction
    if not response.candidates:
        return "[No candidates returned]"

    parts = response.candidates[0].content.parts
    if not parts:
        return "[No text returned by model]"

    return "".join(
        part.text for part in parts if hasattr(part, "text")
    )




BASE_PROMPT = "Explain what transformers are in machine learning for a beginner."


# ==============================
# 1. Experiment – max_output_tokens
# ==============================

def experiment_max_tokens():
    outputs = []
    for max_tokens in [20, 60, 200]:
        text = generate(
            BASE_PROMPT,
            max_tokens=max_tokens,
        )
        outputs.append(f"\n--- max_output_tokens = {max_tokens} ---\n{text}")

    file_path = os.path.join(output_dir, "1_max_output_tokens.txt")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write("\n".join(outputs))

    print(f"Saved → {file_path}")


# ==============================
# 2. Experiment – Deterministic vs Creative
# ==============================

def experiment_deterministic_vs_creative():
    outputs = []

    outputs.append("\n--- Deterministic (temperature=0.0, top_p=0.3) ---")
    for i in range(2):
        text = generate(
            BASE_PROMPT,
            temperature=0.0,
            top_p=0.3,
        )
        outputs.append(f"\nRun {i + 1}:\n{text}")

    outputs.append("\n--- Creative (temperature=0.9, top_p=0.95) ---")
    for i in range(2):
        text = generate(
            BASE_PROMPT,
            temperature=0.9,
            top_p=0.95,
        )
        outputs.append(f"\nRun {i + 1}:\n{text}")

    file_path = os.path.join(output_dir, "2_deterministic_vs_creative.txt")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write("\n".join(outputs))

    print(f"Saved → {file_path}")


# ==============================
# 3. Experiment - Stop Sequences
# ==============================

# def experiment_stop_sequences():
#     outputs = []

#     prompt = (
#         "Answer the question briefly, then write 'END'.\n"
#         "Question: What is a model in machine learning?"
#     )

#     outputs.append("\n--- Without stop_sequences ---")
#     outputs.append(generate(prompt, max_tokens=60))

#     outputs.append("\n--- With stop_sequences=['END'] ---")
#     outputs.append(
#         generate(
#             prompt,
#             max_tokens=60,
#             stop_sequences=["END"],
#         )
#     )

#     file_path = os.path.join(output_dir, "3_stop_sequences.txt")
#     with open(file_path, "w", encoding="utf-8") as f:
#         f.write("\n".join(outputs))

#     print(f"Saved → {file_path}")


# ==============================
# Run all experiments
# ==============================

if __name__ == "__main__":
    experiment_max_tokens()
    experiment_deterministic_vs_creative()
    # experiment_stop_sequences()

    print("\n✅ All Day 6 experiments completed.")
    print(f"📁 Outputs saved in → {output_dir}")
