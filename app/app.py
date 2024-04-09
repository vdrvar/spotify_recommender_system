from flask import Flask, render_template, redirect, url_for, session, request


import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics.pairwise import cosine_similarity, rbf_kernel
import random

import os, sys

# Determine the directory path of the currently executing script
dir_path = os.path.dirname(os.path.realpath(__file__))

# Include the 'code' directory to the system path to import custom utility functions
sys.path.append(os.path.join(dir_path, '../code'))

# Import custom utility functions from utils.py
from utils import *

# Construct the absolute path to the dataset
data_file_path = os.path.join(dir_path, '../data/complete_dataset.csv')
# Load the dataset into a pandas DataFrame
df = pd.read_csv(data_file_path)

# Preprocess the dataset to encode categorical features and scale numerical features
data_encoded = make_encoded_dataset(df)

# Calculate the combined similarity matrix based on cosine and RBF kernel similarities
combined_sim = make_similarities(df=df, de=data_encoded, cos_ratio=0.2, rbf_ratio=0.8)

# Initialize the Flask application
app = Flask(__name__)
# Set a secret key for session management. Replace 'your secret key' with a real secret key for production.
app.secret_key = 'your secret key'

# Define the route for the home page
@app.route('/')
def home():
    if 'favorites' not in session:
        session['favorites'] = []  # Initialize an empty favorites list
    # Render the index.html template for the home page
    return render_template('index.html')

@app.route('/explore')
def explore():
    # Ensure 'seen_songs' is initialized in the session
    if 'seen_songs' not in session:
        session['seen_songs'] = []

    # Convert the list of seen song IDs from the session into a set for efficient lookup
    seen_songs = set(session['seen_songs'])

    # Fetch 6 popular songs, excluding those that have been seen
    N = 6
    popular_songs = get_popular_songs(data_encoded, seen_songs, N)

    # Update the set of seen songs with the IDs of the newly fetched songs
    for song in popular_songs:
        seen_songs.add(song['track_id'])

    # Update the session. Convert the set back into a list since session data must be serializable
    session['seen_songs'] = list(seen_songs)

    # Render the explore.html template, passing the popular_songs to the template
    return render_template('explore.html', songs=popular_songs)

@app.route('/add_favorites', methods=['POST'])
def add_favorites():
    track_ids = request.form.getlist('track_ids')
    if 'favorites' not in session:
        session['favorites'] = []

    for track_id in track_ids:
        if track_id not in session['favorites']:
            session['favorites'].append(track_id)
    session.modified = True

    return redirect(url_for('explore'))


@app.route('/recommend')
def recommend():
    # Check if 'favorites' exists in session and is not empty
    if 'favorites' not in session or not session['favorites']:
        # If there are no favorites, render a specific template or return a custom message
        # This uses a custom template 'no_favorites.html' for displaying the message
        return render_template('no_favorites.html')
    else:
        # If there are favorites, proceed to fetch and display recommendations
        # This part requires your logic to fetch recommendations based on favorites
        # For demonstration, it's just rendering recommend.html
        # Replace the following line with your recommendation fetching and rendering logic
        return render_template('recommend.html')


@app.route('/reset')
def reset_data():
    # Reset the 'seen_songs' in the session
    session['seen_songs'] = []
    session['favorites'] = []
    # Redirect to the home page or another page as needed
    return redirect(url_for('home'))

# The entry point for running the Flask app
if __name__ == '__main__':
    app.run(debug=True)
