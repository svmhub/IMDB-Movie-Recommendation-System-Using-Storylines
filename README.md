# IMDB-Movie-Recommendation-System-Using-Storylines
This project scrapes IMDb for 2024 movies' names &amp; storylines using Selenium. Preprocesses text with NLP (TF-IDF/CountVectorizer), computes cosine similarity for recommendations. Interactive Streamlit UI lets users input a storyline &amp; get top 5 similar movies.

## _Requirements of the project_

* The whole project is developed by Python-3.10.5 Version
* The each file has been treated in the VS Code Editor
* I have creaed a Python virtual environment.
      - The packages are in the requirements.txt file installed on the virtual environment.
      - The same environment has been used throughout the project completion.

## _Approaches of the project_

## TASK 1:- Data Scraping and Storage:

* Data Source: IIMDb 2024 Movies page (link).
* Scraping Method: Use Selenium to extract the following data:
    - Movie Name
    - Storyline (Plot Summary)
* Data Storage: Save the extracted movie data into a CSV file for further analysis.
    - Columns:
    - Movie Name
    - Storyline
* CSV Storage: Save the data in a CSV format for easy data manipulation.

## TASK 2: Data Preprocessing and Analysis:

* Text Cleaning (NLP):
    - Preprocess the storyline text by removing stop words, punctuation, and unnecessary characters.
    - Tokenize the story text for further analysis.
* Text Representation:
    - Use TF-IDF Vectorizer or Count Vectorizer to convert the movie storylines into numerical vectors.
* Cosine Similarity:
    - Calculate the Cosine Similarity between the movie storylines to find the most similar movies.
    - Rank the movies based on similarity scores.

## TASK 3: Recommendation System:

* ***Algorithm:*** Use Cosine Similarity or other ML algorithms to find the top 5 most similar movies based on a user’s input.
* ***User Input:*** Users will be able to input a movie storyline into the Streamlit app, and the system will output the top 5 recommended movies based on storyline similarity.

## Business Use Cases:
* ***Movie Recommendation:*** Users can input a movie storyline, and the system will suggest the top 5 most similar movies based on storyline similarity.
* ***Entertainment Suggestions:*** Provide personalized movie recommendations based on story preferences.

> _I have done these steps in the web_scraper.jpynb file at my repository._
>
> Also, the class based codes are available in this repository. So that you can reuse and reproduce it in your own way. The main aim of the code is to create a package for this project.

### Hence this project has been completed successfully 😎🙏🏾
