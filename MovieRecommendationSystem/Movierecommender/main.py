# Importing the streamlit package
import streamlit as st
import pickle
import pandas as pd

# Reading the pickle file using pickle load function
movie_dict = pickle.load(open('movies.pkl', 'rb'))

# Converting the dictionary back to dataframe
movies = pd.DataFrame(movie_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

# Creating the title and select box on the webpage
st.title('Movie Recommendation System')
selected_movie = st.selectbox('Select a movie for recommendation', movies['title'].values)

# This is the same function which we used in the Jupyter notebook to get the recommended movies


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distance = similarity[movie_index]
    movie_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []

    for i in movie_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

# Creating a button named Recommend which will trigger the recommend function and show the recommended movie list


if st.button('Recommend'):
    recommendation = recommend(selected_movie)
    for i in recommendation:
        st.write(i)
