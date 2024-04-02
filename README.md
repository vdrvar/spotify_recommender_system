# Spotify Song Recommender System

This project aims to build a recommender system for songs using Spotify data obtained from Kaggle. The goal is to provide personalized song recommendations to users based on their listening history, preferences, and other relevant factors.

## Overview

The recommender system will leverage machine learning techniques to analyze Spotify data, including features such as song attributes, user listening behavior, and user profiles. It will then generate recommendations that are tailored to each user's taste in music.

## Dataset

This project aims to develop a recommender system for Spotify songs using datasets obtained from Kaggle. We are utilizing two primary datasets:

1. [Spotify Dataset](https://www.kaggle.com/datasets/vatsalmavani/spotify-dataset) by Vatsal Mavani
2. [Spotify Tracks Dataset](https://www.kaggle.com/datasets/maharshipandya/-spotify-tracks-dataset) by Maharshi Pandya

These datasets contain valuable information about Spotify tracks, including various features and attributes that can be used to build a recommendation engine.

For inspiration and guidance, we refer to the following notebook on Kaggle:

- [Simple Music Recommendation System](https://www.kaggle.com/code/akbareza/simple-music-recommendation-system) by Akbar Eza


## Project Structure

- `data/`: Contains the dataset files obtained from Kaggle.
- `notebooks/`: Jupyter notebooks for data exploration, preprocessing, model development, and evaluation.
- `src/`: Source code for the recommender system implementation.
- `docs/`: Documentation files.

## Usage

1. **Data Exploration**: Use the Jupyter notebooks in the `notebooks/` directory to explore the dataset, analyze song features, and understand user listening behavior.

2. **Preprocessing**: Preprocess the dataset to extract relevant features, handle missing values, and prepare the data for model training.

3. **Model Development**: Develop machine learning models, such as collaborative filtering, content-based filtering, or hybrid methods, to generate song recommendations.

4. **Evaluation**: Evaluate the performance of the recommender system using appropriate metrics, such as precision, recall, and mean average precision.

5. **Deployment**: Deploy the trained model as a web application or API for users to interact with and receive song recommendations.

## Contributors

- [Vjekoslav Drvar](https://github.com/vdrvar)

## Acknowledgments

- This project is inspired by the need for personalized music recommendations and the availability of Spotify data on Kaggle.
- Special thanks to Kaggle for providing the Spotify dataset used in this project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
