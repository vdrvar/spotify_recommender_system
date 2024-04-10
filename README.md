# Spotify Recommender System

## Overview
The Spotify Recommender System is a Flask-based web application designed to provide personalized song recommendations. This system leverages a recommendation algorithm that utilizes both cosine similarity and radial basis function (RBF) similarity to analyze user preferences and interaction history. By integrating these similarity measures, the system can curate a list of songs that users might enjoy, tailoring recommendations to match their unique musical tastes accurately.


## Features
- **Explore Songs**: Browse through a curated list of songs.
- **Personalized Recommendations**: Receive song recommendations tailored to your musical taste.
- **Favorites**: Add songs to your favorites list for personalized recommendations.
- **Responsive Design**: Enjoy a seamless experience across different devices.

## Technologies Used
- Flask: A lightweight WSGI web application framework.
- Python: The backend programming language.
- PostgreSQL (Planned): For persistent storage of user data and preferences.
- HTML/CSS: For the frontend design.
- JavaScript (Planned): To enhance interactivity and user experience.

## Getting Started

### Prerequisites
- Ensure you have Python 3.6+ installed on your system. Flask can be installed and run on Windows, macOS, and Linux environments.
- Docker installed on your system if you wish to run the application in a container.

#### Running Locally
1. Clone the repository:
git clone https://github.com/vdrvar/spotify-recommender-system.git

2. Navigate to the project directory:
cd spotify-recommender-system

3. Install the required packages:
pip install -r requirements.txt

4. Run the Flask application:
flask run

#### Running with Docker
1. Build the Docker image:
docker build -t spotify-recommender-system .

2. Run the Docker container:
docker run -p 5000:5000 spotify-recommender-system

After running the application, visit `http://127.0.0.1:5000/` in your web browser to start exploring songs and receiving recommendations.

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
X - [@v_drvar](https://twitter.com/v_drvar)

Github: [https://github.com/vdrvar/spotify-recommender-system](https://github.com/vdrvar/spotify-recommender-system)

## Acknowledgements
- [Flask](https://flask.palletsprojects.com/)
- [Python](https://www.python.org/)


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
Your Name - [@v_drvar](https://twitter.com/yourtwitter)

Project Link: [https://github.com/vdrvar/spotify-recommender-system](https://github.com/vdrvar/spotify-recommender-system)

## Acknowledgements
- [Flask](https://flask.palletsprojects.com/)
- [Python](https://www.python.org/)
