Movie Recommender
A modern Streamlit-based web app for movie recommendations and personal watchlist management.
Choose your favourite movies, get smart recommendations, build your watchlist, and explore trending picks in a clean, interactive gallery/grid.

Features-
Trending Now: Browse popular movies in a responsive grid—see more rows with a click.
Smart Recommendations: Select any movie and instantly view recommended titles using the built-in recommender.
Watchlist: Add any movie to your personal watchlist to revisit later—see all your picks in an organized gallery.
Movie Details: Click any movie name to view details, including genres and quick back navigation.
Top Picks: Discover top suggestions curated just for you.

Prerequisites-
Python 3.8+
pip
Streamlit

Installation-
Clone the repository
git clone https://github.com/yourusername/movie-recommender.git
cd movie-recommender

Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate     # On Windows

Install required packages
pip install -r requirements.txt

Prepare dataset files
movie.csv
tmdb_5000_movies.csv
movie_redefined.csv

Interact with UI-
Select movies from drop-downs or the trending grid.
Click to add/remove movies to your watchlist.
View recommended movies and details pages.

Code Structure-
frontend3.py - Main Streamlit app and UI logic
movie_recommender_py.py - Recommender model functions
movie.csv / tmdb_5000_movies.csv / movie_redefined.csv - Movie datasets
watchlist.json - User’s persistent watchlist
images.png - Poster images in grid/gallery

Customization-
To add movie-specific images: update code to map each movie to its unique poster file.
To change grid size: update grid_cols variable in the app.

Troubleshooting-
Virtualenv issues: Be sure to activate your environment and install packages within it.
CSV/file errors: Make sure all dataset files exist and have the correct format.
Streamlit/settings: Use latest Streamlit for full compatibility with modern UI features.

I'm stil working on the project, so this is a temporary readme.
