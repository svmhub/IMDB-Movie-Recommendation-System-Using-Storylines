# 05_IMDB_MOVIE_RECOMMENDATION_SYSTEM/vectorizer.py

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD
from sklearn.pipeline import Pipeline


class MovieVectorizer:

    def __init__(self):
        self.pipeline = Pipeline([
            ('tfidf', TfidfVectorizer(
                max_features=10000,
                ngram_range=(1, 3),     # add trigrams
                min_df=2,               # ignore rare words
                max_df=0.8              # ignore the common words
            )),
            ('svd', TruncatedSVD(n_components=300))
        ])

    def fit_transform(self, corpus):
        return self.pipeline.fit_transform(corpus)

    def transform(self, text):
        return self.pipeline.transform([text])