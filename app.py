import streamlit as st
import pandas as pd
from spotify_recommendation import Spotify_Recommendation

st.title("Spotify Song Recommendation")

df = pd.read_csv('data/dataset.csv')

recommender = Spotify_Recommendation(df)

song_list = df['track_name'].unique()

song_name = st.selectbox("Select a Track", options=song_list)

num_recommendations = st.slider("How many suggestions do you want to see?", 1, 20, 10)

if st.button("Recommend"):
    recommendations = recommender.recommend(song_name, num_recommendations)
    
    if not recommendations.empty:
        st.write(f"Recommended songs for : '{song_name}'")
        st.dataframe(recommendations)
    else:
        st.write(f"No recommendations found for '{song_name}' !")
