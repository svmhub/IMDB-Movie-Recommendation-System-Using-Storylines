# 05_IMDB_MOVIE_RECOMMENDATION/recommender.py

from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


class SenMovieRecommender:

    def __init__(self, movie_names, embeddings):
        self.movie_names = movie_names
        self.embeddings = embeddings

    def recommend(self, query_embedding, top_n=5):

        similarity_scores = cosine_similarity(
            query_embedding,
            self.embeddings
        ).flatten()

        top_indices = similarity_scores.argsort()[::-1][:top_n]

        results = [
            {
                "movie": self.movie_names[i],
                "score": float(similarity_scores[i])
            }
            for i in top_indices
        ]

        return results