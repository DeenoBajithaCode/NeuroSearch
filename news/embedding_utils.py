from sentence_transformers import SentenceTransformer
import numpy as np
import faiss

from .models import Article

# Load pre-trained model
model = SentenceTransformer('all-MiniLM-L6-v2')

class VectorStore:
    def __init__(self):
        # Index for 384-dimensional vectors (MiniLM model output)
        self.index = faiss.IndexFlatL2(384)
        self.article_ids = []

    def add_articles(self, articles):
        texts = [article.content for article in articles]
        embeddings = model.encode(texts, show_progress_bar=False)
        self.index.add(np.array(embeddings, dtype='float32'))
        self.article_ids.extend([article.id for article in articles])

    def search(self, query, top_k=5):
        query_embedding = model.encode([query])
        D, I = self.index.search(np.array(query_embedding, dtype='float32'), top_k)
        return [self.article_ids[i] for i in I[0] if i < len(self.article_ids)]
