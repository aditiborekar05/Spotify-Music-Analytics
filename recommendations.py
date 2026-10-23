
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.metrics.pairwise import cosine_similarity

# 1. Load cleaned dataset
df = pd.read_csv("data/spotify_cleaned.csv")

# 2. Select important audio features
features = [
    "danceability",
    "energy",
    "acousticness",
    "instrumentalness",
    "valence",
    "speechiness",
    "liveness",
    "tempo",
    "loudness"
]

# 3. Prepare and scale the audio features
X = df[features].fillna(df[features].median())

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

print("Music recommendation model is ready!")


def recommend_songs(song_name, number=5):

    # 4. Find the requested song
    exact = df[
        df["track_name"].fillna("").str.casefold()
        == song_name.strip().casefold()
    ]

    if exact.empty:
        matches = df[
            df["track_name"].fillna("").str.contains(
                song_name, case=False, regex=False
            )
        ]

        if matches.empty:
            print("Song not found. Try another name.")
            return

        print("\nMatching songs found:")
        print(
            matches[
                ["track_name", "artists", "popularity"]
            ].drop_duplicates().head(10).to_string(index=False)
        )

        # Use the most popular matching track
        song_index = matches["popularity"].idxmax()

    else:
        # If several records match, select the most popular one
        song_index = exact["popularity"].idxmax()

    song = df.loc[song_index]
    query_vector = X_scaled[song_index].reshape(1, -1)

    # 5. Compare the selected song with all tracks
    similarities = cosine_similarity(
        query_vector, X_scaled
    )[0]

    # 6. Convert cosine similarity to a 0-100 scale
    audio_score = (similarities + 1) / 2 * 100

    results = df[
        ["track_id", "track_name", "artists",
         "track_genre", "popularity"]
    ].copy()

    results["audio_similarity"] = audio_score

    # 7. Give a small preference to the same genre
    same_genre = (
        results["track_genre"] == song["track_genre"]
    )

    results["genre_bonus"] = same_genre.astype(float) * 5

    results["match_score"] = (
    results["audio_similarity"]
    + results["genre_bonus"]
)

    # 8. Exclude the selected track itself
    results = results[
        results["track_id"] != song["track_id"]
    ].copy()

    # 9. Rank tracks, then remove repeated track IDs
    results = results.sort_values(
        "match_score", ascending=False
    )

    results = results.drop_duplicates(
        subset="track_id", keep="first"
    )

    # 10. Display recommendations
    print("\nRecommendations for:")
    print(song["track_name"], "-", song["artists"])
    print("Reference genre:", song["track_genre"])

    print(
        results[
            ["track_name", "artists", "track_genre",
             "audio_similarity", "match_score"]
        ].head(number).round(2).to_string(index=False)
    )

    print(
        "\nScores are model-based ranking estimates, "
        "not probabilities of liking a song."
    )


# Try a song
recommend_songs("Unholy", 5)
