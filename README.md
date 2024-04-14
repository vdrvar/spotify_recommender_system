# Spotify Recommender System

## Overview
The Spotify Recommender System is a Flask-based web application designed to provide personalized song recommendations. This system leverages a recommendation algorithm that utilizes both cosine similarity and radial basis function (RBF) similarity to analyze user preferences and interaction history. By integrating these similarity measures, the system can curate a list of songs that users might enjoy, tailoring recommendations to match their unique musical tastes accurately.

## Features
- **Explore Songs**: Browse through a curated list of songs.
- **Personalized Recommendations**: Receive song recommendations tailored to your musical taste.
- **Favorites**: Add songs to your favorites list for personalized recommendations.

## Screenshots

### Home Page
![image](https://github.com/vdrvar/spotify_recommender_system/assets/48907543/8a98c2b3-4121-46c0-b904-0fc41d3ff5a1)


### Explore Songs


### Recommendations


## Technologies Used
- Flask: A lightweight WSGI web application framework.
- Python: The backend programming language.
- Redis: For caching data such as session states and recommendations.
- Prometheus: For monitoring the application's performance and health.
- HTML/CSS: For the frontend design.

## Getting Started

### Prerequisites
- Ensure you have Python 3.6+ installed on your system. Flask can be installed and run on Windows, macOS, and Linux environments.
- Docker and Docker Compose installed on your system if you wish to run the application in a containerized environment.

### Running with Docker Compose
To run the application using Docker Compose, which sets up both the application and its dependencies like Redis and Prometheus:

1. **Clone the repository:**
git clone https://github.com/vdrvar/spotify-recommender-system.git

2. **Navigate to the app directory:**
cd spotify-recommender-system/app


3. **Build and start the services:**
docker-compose up --build


This command builds the necessary Docker images and starts the services defined in the `docker-compose.yml` file. It includes your Flask application, Redis, and Prometheus.

4. **Access the application:**
After running the Docker Compose command, visit `http://localhost:5000/` in your web browser to start exploring songs and receiving recommendations.

### Shutting Down
To stop and remove the containers set up by Docker Compose:
docker-compose down


This command stops all the running containers and removes them along with their network, but keeps your data intact.

### Cleaning Up
To remove everything, including any volumes created by Docker Compose:
docker-compose down -v


This will remove the containers, network, and all data associated with the application's Docker Compose setup.

## Contributing
Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License
Distributed under the MIT License. See `LICENSE` for more information.

## Contact
Vjekoslav Drvar - [@VjekoslavDrvar](https://twitter.com/v_drvar)

Project Link: [https://github.com/vdrvar/spotify-recommender-system](https://github.com/vdrvar/spotify-recommender-system)

## Acknowledgements
- [Flask](https://flask.palletsprojects.com/)
- [Python](https://www.python.org/)
- [Redis](https://redis.io/)
- [Prometheus](https://prometheus.io/)





