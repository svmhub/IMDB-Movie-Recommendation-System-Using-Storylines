# 05_IMDB_MOVIE_RECOMMENDATATION_SYSTEM/recommender.py

from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


class MovieRecommender:

    def __init__(self, movie_names, movie_vectors):
        self.movie_names = movie_names
        self.movie_vectors = movie_vectors

    def recommend(self, user_vector, top_n=5):
        similarity_scores = cosine_similarity(
            user_vector,
            self.movie_vectors
        )

        scores = similarity_scores.flatten()
        top_indices = np.argsort(scores)[::-1][1:top_n + 1]

        return [(self.movie_names[i], scores[i]) for i in top_indices]