
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Load original dataset
df = pd.read_csv("data/dataset.csv")

print("Original shape:", df.shape)

# Remove unnecessary index column
df = df.drop(columns=["index"])

# Remove rows missing essential song details
df = df.dropna(
    subset=["track_name", "artists", "album_name"]
).copy()

# Remove only exact duplicate rows
df = df.drop_duplicates()

# Reset row numbering
df = df.reset_index(drop=True)

# Save cleaned dataset
df.to_csv("data/spotify_cleaned.csv", index=False)

print("Cleaned shape:", df.shape)
print("Missing values:", df.isnull().sum().sum())
print("Exact duplicate rows:", df.duplicated().sum())
print("Unique track IDs:", df["track_id"].nunique())

print("\nCleaned dataset saved successfully!")



# Load cleaned data for analysis
df = pd.read_csv("data/spotify_cleaned.csv")

# Convert duration to minutes
df["duration_min"] = df["duration_ms"] / 60000

# 1. Most popular tracks
print("\n--- TOP 10 POPULAR TRACKS ---")

top_tracks = (
    df.sort_values("popularity", ascending=False)
    .drop_duplicates(subset="track_id")
    .head(10)
)

print(
    top_tracks[["track_name", "artists", "popularity"]]
    .to_string(index=False)
)

# 2. Genre analysis
print("\n--- TOP 10 GENRES BY AVERAGE POPULARITY ---")

genre_popularity = (
    df.groupby("track_genre")["popularity"]
    .mean()
    .sort_values(ascending=False)
    .head(10)
)

print(genre_popularity.round(2))

plt.figure(figsize=(10, 6))
genre_popularity.sort_values().plot(kind="barh")
plt.title("Top 10 Genres by Average Popularity")
plt.xlabel("Average Popularity")
plt.ylabel("Genre")
plt.tight_layout()
plt.savefig("data/top_genres.png", dpi=300)
plt.show()

# 3. Music feature correlation
features = [
    "popularity", "danceability", "energy",
    "valence", "acousticness", "tempo"
]

plt.figure(figsize=(9, 6))
sns.heatmap(
    df[features].corr(),
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)
plt.title("Correlation Between Music Features")
plt.tight_layout()
plt.savefig("data/feature_correlation.png", dpi=300)
plt.show()

# 4. Audio feature averages
print("\n--- AVERAGE AUDIO FEATURES ---")
print(
    df[["danceability", "energy", "valence",
        "acousticness", "tempo"]].mean().round(2)
)

print("\nEDA completed successfully!")
