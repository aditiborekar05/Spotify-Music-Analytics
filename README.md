# Spotify Music Analytics & Recommendation Dashboard

## Project Overview
This project analyzes Spotify music data to understand track popularity, music genres, and audio features. It also includes a content-based music recommendation system that suggests similar songs using their audio characteristics.

## Objectives
- Analyze Spotify tracks and music genres.
- Identify genres with higher average popularity.
- Explore audio features such as energy, danceability, valence, and acousticness.
- Visualize insights using charts and a Power BI dashboard.
- Recommend similar songs using content-based filtering.

## Technologies Used
- Python
- Pandas and NumPy
- Matplotlib and Seaborn
- Scikit-learn
- Microsoft Power BI
- Visual Studio Code

## Project Structure
- `data/` — Original dataset, cleaned dataset, and generated charts.
- `notebooks/` — Notebook workspace.
- `powerbi/` — Power BI dashboard.
- `spotify_analysis.py` — Data cleaning and exploratory data analysis.
- `recommendations.py` — Content-based music recommendation system.
- `check_data.py` — Dataset inspection and validation.

## Methodology
1. Load and inspect the Spotify dataset.
2. Clean records with missing essential song details and remove exact duplicate rows.
3. Perform exploratory data analysis.
4. Generate visualizations of genre popularity and audio-feature relationships.
5. Build a content-based recommendation model using standardized audio features and cosine similarity.
6. Present insights through a Power BI dashboard.

## Key Findings
The analysis identifies the top genres by average popularity and compares audio features across tracks. The dashboard includes summary metrics, a genre slicer, genre popularity, average audio features, and a popularity-versus-danceability scatter plot.

## Recommendation System
The recommendation system uses audio features such as danceability, energy, acousticness, instrumentalness, valence, speechiness, liveness, tempo, and loudness. StandardScaler normalizes the features, and cosine similarity ranks tracks by audio-feature similarity. A genre bonus is also used in the current ranking logic.

Recommendation scores are ranking estimates, not probabilities that a listener will enjoy a song.

## How to Run
1. Install the required Python libraries:
   `pip install pandas numpy matplotlib seaborn scikit-learn`
2. Run the analysis:
   `python spotify_analysis.py`
3. Run the recommendation system:
   `python recommendations.py`
4. Open the `.pbix` file in Microsoft Power BI Desktop to explore the dashboard.

## Conclusion
This project combines data cleaning, exploratory data analysis, content-based recommendations, and interactive visualization to explore patterns in Spotify music data.

## Project Inspiration
Inspired by Spotify's music discovery and recommendation concepts. This is an educational project and does not reproduce Spotify's production recommendation system.
