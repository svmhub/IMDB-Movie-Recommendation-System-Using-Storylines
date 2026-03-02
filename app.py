import streamlit as st
import pandas as pd

from preprocess import TextPreprocessor
from vectorizer import MovieVectorizer
from recommender import MovieRecommender
from sentence_vectorizer import SentenceEmbeddingModel
from sentence_recommender import SenMovieRecommender


st.markdown("## 🎬 IMDb Storyline Movie Recommender")

@st.cache_resource
def load_embedding_model():
    return SentenceEmbeddingModel()

@st.cache_data
def load_data():
    return pd.read_csv("imdb_2024_movies.txt", sep="\t")
st.divider()

# Generate embeddings once
@st.cache_data
def compute_embeddings(corpus):
    return embedding_model.encode_corpus(corpus)

df = load_data()
if not df.empty:
    st.success('Data loaded successfully!')
else:
    st.failure('Data loading got failed!')

preprocessor = TextPreprocessor()
df["clean_story"] = df["Storyline"].apply(preprocessor.clean_text)

vectorizer = MovieVectorizer()
movie_vectors = vectorizer.fit_transform(df["clean_story"])

embedding_model = load_embedding_model()
movie_embeddings = compute_embeddings(df["clean_story"])

recommender = MovieRecommender(
    df["Movie Name"].values,
    movie_vectors
)

sen_recommender = SenMovieRecommender(
    df["Movie Name"].values,
    movie_embeddings
)

user_input = st.text_area("Enter a movie storyline:")

if st.button("Recommend"):
    clean_input = preprocessor.clean_text(user_input)

    user_vector = vectorizer.transform(clean_input)
    recommendations = recommender.recommend(user_vector)

    query_embedding = embedding_model.encode_query(clean_input)
    sen_recommendations = sen_recommender.recommend(query_embedding)

    st.subheader("Top 5 Recommendations using TF-IDF + SVD:")
    for movie, score in recommendations:
        st.write(f"🎬 **{movie}** (Similarity: {score:.2f})")

    st.subheader("Top 5 Recommendations using Sentence-Transformers:")
    for rec in sen_recommendations:
        st.markdown(f"🎬 **{rec['movie']}** (Similarity Score: {rec['score']:.2f})")
        # st.write(f"Similarity Score: {rec['score']:.2f}")
        st.progress(min(rec['score'], 1.0))