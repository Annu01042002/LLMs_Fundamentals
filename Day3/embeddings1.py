from sentence_transformers import SentenceTransformer, util

# Load a pre-trained sentence embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Define sample sentences for embedding
sentences = [
    "Cats are great pets.",
    "Dogs are friendly animals.",
    "The stock market crashed today."
]

# Encode sentences into embeddings (convert to tensor for similarity calculations)
emb = model.encode(sentences, convert_to_tensor=True)

# Calculate and print cosine similarity between sentence pairs
print("Sim 1-2:", util.cos_sim(emb[0], emb[1]))  # Similar sentences (both about animals)
print("Sim 1-3:", util.cos_sim(emb[0], emb[2]))  # Dissimilar sentences (animals vs finance)
