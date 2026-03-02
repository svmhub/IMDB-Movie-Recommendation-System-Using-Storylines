# 05_IMDb_MOVIE_RECOMMENDATION_SYSTEM/sentence_vectorizer.py

from sentence_transformers import SentenceTransformer
import numpy as np


class SentenceEmbeddingModel:
    """
    Generates semantic embeddings using pre-trained transformer model.
    """

    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)

    def encode_corpus(self, corpus):
        """
        Converts list of texts into embeddings.
        """
        embeddings = self.model.encode(
            corpus,
            convert_to_numpy=True,
            show_progress_bar=True
        )
        return embeddings

    def encode_query(self, query: str):
        """
        Converts single user query into embedding.
        """
        embedding = self.model.encode(
            query,
            convert_to_numpy=True
        )
        return embedding.reshape(1, -1)