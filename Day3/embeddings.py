import google.generativeai as genai
from dotenv import load_dotenv
import os
from numpy import dot
from numpy.linalg import norm

# -----------------------------
# 1. Load API Key
# -----------------------------
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("Set GEMINI_API_KEY in your .env file!")

genai.configure(api_key=api_key)

# Embedding model
EMBED_MODEL = "models/text-embedding-004"

# -----------------------------
# 2. Helper: Cosine Similarity
# -----------------------------
def cosine_similarity(a, b):
    return dot(a, b) / (norm(a) * norm(b))

# -----------------------------
# 3. Sentences for testing
# -----------------------------
sent1 = "The weather is nice today."
sent2 = "It is a beautiful sunny day."
sent3 = "Quantum computers use qubits."

# -----------------------------
# 4. Get embeddings
# -----------------------------
def get_embedding(text):
    result = genai.embed_content(
        model=EMBED_MODEL,
        content=text
    )
    return result["embedding"]

emb1 = get_embedding(sent1)
emb2 = get_embedding(sent2)
emb3 = get_embedding(sent3)

# -----------------------------
# 5. Similarity scores
# -----------------------------
sim_12 = cosine_similarity(emb1, emb2)
sim_13 = cosine_similarity(emb1, emb3)

# -----------------------------
# 6. Print results
# -----------------------------
print("\n=== DAY 3 — Tokenization + Embeddings Practice ===\n")

print("Sentence 1:", sent1)
print("Sentence 2:", sent2)
print("Sentence 3:", sent3)

print("\nCosine Similarities:")
print(f"1 ↔ 2 (similar meaning): {sim_12:.4f}")
print(f"1 ↔ 3 (different meaning): {sim_13:.4f}")

# -----------------------------
# 7. Save output to folder
# -----------------------------
output_dir = "Day3/embedding_outputs"
os.makedirs(output_dir, exist_ok=True)

output_file = os.path.join(output_dir, "embedding_results.txt")

with open(output_file, "w", encoding="utf-8") as f:
    f.write("=== DAY 3 — Embedding Output ===\n\n")
    f.write(f"Sentence 1: {sent1}\n")
    f.write(f"Sentence 2: {sent2}\n")
    f.write(f"Sentence 3: {sent3}\n\n")
    f.write("Cosine Similarities:\n")
    f.write(f"1 ↔ 2 (similar meaning): {sim_12:.4f}\n")
    f.write(f"1 ↔ 3 (different meaning): {sim_13:.4f}\n")

print(f"\nSaved output to: {output_file}")
print("Done!")
