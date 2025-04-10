# NeuroSearch - Semantic Search for News Articles

This project lets users upload news articles and search them using semantic meaning instead of keywords. It uses sentence-transformers to create embeddings and stores them in FAISS or Chroma for fast similarity search.

## Features

- Upload and store news articles
- Generate embeddings using sentence-transformers
- Store and search with FAISS or Chroma vector DB
- Django API for querying with semantic meaning
- Optional: Response latency tracking & vector caching

## Requirements

- Python 3.8+
- Django
- sentence-transformers
- faiss-cpu or chromadb
- numpy
- pandas

Install dependencies:

```bash
pip install -r requirements.txt
