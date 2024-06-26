from flask import Flask, render_template, redirect, url_for, session, request


import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics.pairwise import cosine_similarity, rbf_kernel
import random

import os, sys

from redis import Redis
import pickle
import time

import uuid

from prometheus_flask_exporter import PrometheusMetrics

# Initialize Redis
redis_client = Redis(host='redis', port=6379, db=0, decode_responses=False)

# Determine the directory path of the currently executing script
dir_path = os.path.dirname(os.path.realpath(__file__))

# Include the 'code' directory to the system path to import custom utility functions
# sys.path.append(os.path.join(dir_path, '../code'))

# Import custom utility functions from utils.py
from utils import *

# Construct the absolute path to the dataset
data_file_path = os.path.join(dir_path, 'complete_dataset.csv')
# Load the dataset into a pandas DataFrame
df = pd.read_csv(data_file_path)

# Preprocess the dataset to encode categorical features and scale numerical features
data_encoded = make_encoded_dataset(df)

# Calculate the combined similarity matrix based on cosine and RBF kernel similarities
combined_sim = make_similarities(df=df, de=data_encoded, cos_ratio=0.2, rbf_ratio=0.8)

# Initialize the Flask application
app = Flask(__name__)

metrics = PrometheusMetrics(app)

# static information as metric
metrics.info('app_info', 'Application info', version='1.0.3')

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

@app.before_request
def ensure_session_id():
    if 'session_id' not in session:
        # Generate a new session ID and store it in the session
        session['session_id'] = uuid.uuid4().hex

@app.route('/add_favorites', methods=['POST'])
def add_favorites():
    track_ids = request.form.getlist('track_ids')
    updated = False

    if 'favorites' not in session:
        session['favorites'] = []

    for track_id in track_ids:
        if track_id not in session['favorites']:
            session['favorites'].append(track_id)
            updated = True

    if updated:
        session.modified = True
        # Generate new recommendations and cache them
        favorites = session['favorites']
        recommendations = get_recommendations(favorites, data_encoded, combined_sim, N=6)
        # Cache the recommendations with a timestamp key to manage freshness
        redis_client.set(f'recommendations_{session["session_id"]}', pickle.dumps(recommendations), ex=3600)  # Expires in 1 hour

    return redirect(request.referrer or url_for('home'))



@app.route('/recommend')
def recommend():
    if 'favorites' not in session or not session['favorites']:
        return render_template('no_favorites.html')
    else:
        session_id = session.get('session_id')
        pickled_recommendations = redis_client.get(f'recommendations_{session_id}')
        if pickled_recommendations:
            recommendations = pickle.loads(pickled_recommendations)
        else:
            favorites = session['favorites']
            recommendations = get_recommendations(favorites, data_encoded, combined_sim, N=6)
            # Make sure to store the pickled data correctly
            redis_client.set(f'recommendations_{session_id}', pickle.dumps(recommendations), ex=3600)  # Cache for 1 hour

        return render_template('recommendations.html', songs=recommendations)






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
