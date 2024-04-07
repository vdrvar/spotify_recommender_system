import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics.pairwise import cosine_similarity, rbf_kernel
import random

def make_encoded_dataset(df):
    # Genre Encoding
    # Crosstab Genre and Song

    xtab_song = pd.crosstab(
        df['track_id'], 
        df['track_genre']
    )

    xtab_song = xtab_song*2

    df = df.sort_values('track_id')
    df = df.reset_index(drop=True)

    xtab_song.reset_index(inplace=True)
    data_encoded = pd.concat([df, xtab_song], axis=1)

    # Identify all columns in the DataFrame
    columns = list(data_encoded.columns)

    # Find all occurrences of 'track_id'
    track_id_occurrences = [i for i, col in enumerate(columns) if col == 'track_id']

    # Create a new DataFrame without the duplicate 'track_id' columns
    # Keep the first occurrence of 'track_id' and remove the others
    if len(track_id_occurrences) > 1:
        # Construct a new list of column indices to keep: all indices except the duplicate 'track_id' indices
        columns_to_keep_indices = set(range(len(columns))) - set(track_id_occurrences[1:])
        
        # Sort indices to maintain original order
        sorted_columns_to_keep_indices = sorted(list(columns_to_keep_indices))
        
        # Select columns by index
        data_encoded = data_encoded.iloc[:, sorted_columns_to_keep_indices]

    # Verify the columns in the modified DataFrame
    # print(data_encoded.columns)

    # display(data_encoded.head(),len(data_encoded))
        
    # Get the list of column names
    columns = list(data_encoded.columns)

    # Count occurrences of "track_id"
    track_id_count = columns.count("track_id")



    #scaling numerical features
    numerical_features = ['explicit', 'danceability', 'energy', 'loudness', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence','year']
    scaler = MinMaxScaler()
    data_encoded[numerical_features] = scaler.fit_transform(data_encoded[numerical_features])

    # Select the relevant columns for computing item similarities
    calculatied_features = numerical_features + list(xtab_song.drop(columns='track_id').columns)

    return data_encoded

def make_similarities(df, de, cos_ratio=0.5, rbf_ratio=0.5):

    xtab_song = pd.crosstab(
        df['track_id'], 
        df['track_genre']
    )

    xtab_song = xtab_song*2
    xtab_song.reset_index(inplace=True)

    numerical_features = ['explicit', 'danceability', 'energy', 'loudness', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence','year']

    # Select the relevant columns for computing item similarities
    calculatied_features = numerical_features + list(xtab_song.drop(columns='track_id').columns)
    cosine_sim = cosine_similarity(de[calculatied_features])
    # Apply RBF kernel
    # gamma is a parameter of the RBF kernel. Adjust it based on your dataset.
    gamma = 1.0 / de[calculatied_features].shape[1]
    rbf_sim = rbf_kernel(de[calculatied_features], gamma=gamma)

    combined_sim = (cos_ratio*cosine_sim + rbf_ratio*rbf_sim)

    return combined_sim

def get_recommendations(track_id_list, data, similarity_matrix, N=5):
    """
    Get song recommendations based on a list of track IDs, selecting N random songs from the top 100 matches.
    
    Parameters:
    - track_id_list (list): A list of track IDs to find recommendations for.
    - data (pd.DataFrame): DataFrame containing song data.
    - similarity_matrix (np.array): A precomputed similarity matrix for songs.
    - N (int): The number of random recommendations to return from the top 100. Default is 5.
    
    Returns:
    - list: A list of dictionaries with recommended song details and similarity scores. Returns an error message if any track is not found.
    """
    # Define indices mapping track_id to index in 'data'
    indices = pd.Series(data.index, index=data['track_id']).drop_duplicates()
    
    # Verify all track IDs are in the dataset
    missing_tracks = [track_id for track_id in track_id_list if track_id not in indices]
    if missing_tracks:
        return f"Tracks not found in the dataset: {missing_tracks}"
    
    # Get indices of the tracks
    idx_list = indices[track_id_list].values
    
    # Calculate average similarity scores across specified tracks for each potential recommendation
    avg_sim_scores = np.mean(similarity_matrix[idx_list], axis=0)
    
    # Sort the tracks based on the average similarity score, in descending order
    sorted_sim_scores_indices = np.argsort(-avg_sim_scores)
    
    # Filter out indices of the input tracks to avoid recommending the input tracks themselves
    filtered_indices = [idx for idx in sorted_sim_scores_indices if idx not in idx_list]
    
    # Select the top 100 matches, or all matches if there are less than 100
    top_matches = filtered_indices[:100]
    
    # Randomly choose N songs from the top 100 matches
    random_indices = random.sample(top_matches, min(len(top_matches), N))
    
    # Get recommended tracks' details
    recommended_tracks = data.iloc[random_indices]
    recommended_tracks = recommended_tracks[['track_id', 'track_name', 'artists', 'album_name']]
    
    # Prepare the final recommended list with similarity scores
    recommended_list = recommended_tracks.to_dict(orient='records')
    for i, idx in enumerate(random_indices):
        recommended_list[i]['similarity_score'] = avg_sim_scores[idx]
    
    return recommended_list

def get_popular_songs(data_encoded, seen_track_ids, N=5):
    # Ensure data_encoded is not modified
    data = data_encoded.copy()
    
    # Exclude songs that have already been seen
    data = data[~data['track_id'].isin(seen_track_ids)]
    
    # Invert the popularity score if higher scores indicate higher popularity
    max_popularity = data['popularity'].max()
    data['inverse_popularity'] = max_popularity - data['popularity']
    
    # Normalize the inverse popularity scores to sum to 1 (to use as probabilities)
    data['inverse_popularity'] /= data['inverse_popularity'].sum()
    
    # It's possible that after filtering, fewer than N songs remain
    num_songs_to_select = min(N, len(data))
    
    # Select N songs randomly, weighted by the inverse of their popularity
    selected_indices = np.random.choice(data.index, size=num_songs_to_select, replace=False, p=data['inverse_popularity'].values)
    selected_songs = data.loc[selected_indices]
    
    # Format the selected songs in the desired output format
    recommended_songs = selected_songs[['track_id', 'track_name', 'artists', 'album_name']]
    recommended_list = recommended_songs.to_dict(orient='records')
    
    # Add a placeholder similarity score since it's not applicable in this context
    for song in recommended_list:
        song['similarity_score'] = None
    
    return recommended_list
    
def update_seen_songs(seen_songs, new_songs):
    seen_songs.update(new_songs)
    session['seen_songs'] = seen_songs  # Update the session
