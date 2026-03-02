# 05_IMDB_MOVIE_RECOMMENDATION/preprocess.py

# Import required packages

import os
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

class TextPreprocessor:

    def __init__(self):
        nltk_data_path = os.path.join(os.getcwd(), "nltk_data")
        if not os.path.exists(nltk_data_path):
            os.makedirs(nltk_data_path)

        nltk.data.path.append(nltk_data_path)
        nltk.download('punkt', download_dir=nltk_data_path)
        nltk.download('punkt_tab', download_dir=nltk_data_path)
        nltk.download('stopwords', download_dir=nltk_data_path)
        nltk.download('wordnet', download_dir=nltk_data_path)

        self.stop_words = set(stopwords.words("english"))
        self.lemmatizer = WordNetLemmatizer()

    def clean_text(self, text: str) -> str: # Clean the text from the user input
        text = text.lower()
        text = re.sub(r"[^a-zA-Z\s]", "", text)

        tokens = word_tokenize(text)
        tokens = [
            self.lemmatizer.lemmatize(word)
            for word in tokens
            if word not in self.stop_words and len(word) > 2
        ]

        return " ".join(tokens)