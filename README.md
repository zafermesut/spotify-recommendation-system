# Spotify Recommendation System

This project is a Spotify song recommendation system built using a dataset of tracks and Streamlit for the user interface. The system allows users to select a song from a dropdown menu, and based on the song's features, it suggests similar tracks.

## Dataset

The dataset used for this recommendation system can be found on Kaggle:

[Spotify Tracks Dataset](https://www.kaggle.com/datasets/maharshipandya/-spotify-tracks-dataset)

The dataset contains features like danceability, energy, and tempo, which are used to calculate the similarity between tracks and provide recommendations.

## Live Demo

A live demo of the project is available on Hugging Face Spaces. You can try it out by selecting a song and getting recommendations based on the song's features.

[Live Demo on Hugging Face](https://huggingface.co/spaces/zafermbilen/spotify-recommendation-system)

## How it Works

1. Select a song from the dropdown menu.
2. Adjust the number of recommendations you want to see.
3. Click "Recommend" to get a list of similar songs based on the audio features in the dataset.

The recommendation is calculated using the Euclidean distance between the features of the selected song and other tracks in the dataset.

## Technologies Used

- **Streamlit** for the web interface
- **Pandas** and **NumPy** for data manipulation
- **TQDM** for progress tracking in calculations
- **Hugging Face Spaces** for deployment
