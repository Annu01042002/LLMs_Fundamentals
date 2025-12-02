# Day 3: Embeddings Exploration

This folder contains experiments comparing different embedding approaches using Google Gemini API and Hugging Face SentenceTransformers.

## Files

- **embeddings.py** - Google Gemini embedding implementation
- **embeddings1.py** - Hugging Face SentenceTransformers implementation
- **experiment.txt** - Experiment details
- **visualize_embedd.txt** - Embedding visualization reference

## Overview

This project demonstrates two different approaches to sentence embeddings:

### 1. Google Gemini Embeddings (embeddings.py)
- Uses Google's `text-embedding-004` model via Gemini API
- Requires API key configuration
- Calculates cosine similarity between sentence pairs
- Saves results to output file

### 2. Hugging Face SentenceTransformers (embeddings1.py)
- Uses pre-trained `all-MiniLM-L6-v2` model
- Lightweight, local implementation
- No API key required
- Quick semantic similarity comparisons

## Getting Started

Install dependencies:
```bash
pip install google-generativeai python-dotenv numpy sentence-transformers
```

For Gemini embeddings, set up your `.env` file:
```
GEMINI_API_KEY=your_api_key_here
```

Run either script:
```bash
python embeddings.py
python embeddings1.py
```

## Key Concepts

- **Embeddings**: Convert text into numerical vectors capturing semantic meaning
- **Cosine Similarity**: Measure similarity between embeddings (0-1 range)
- **API-based vs Local**: Compare cloud-based vs local embedding models