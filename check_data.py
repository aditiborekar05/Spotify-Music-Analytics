
import pandas as pd

df = pd.read_csv("data/dataset.csv")

print("Original rows:", len(df))
print("Unique track IDs:", df["track_id"].nunique())
print("Rows with repeated track IDs:",
      df.duplicated(subset=["track_id"], keep=False).sum())

print("\n--- EXAMPLE REPEATED TRACK IDs ---")
repeated = df[df.duplicated(subset=["track_id"], keep=False)]

print(
    repeated[
        ["track_id", "track_name", "artists", "track_genre"]
    ].head(12).to_string(index=False)
)

print("\n--- LONGEST TRACKS ---")
df["duration_min"] = df["duration_ms"] / 60000

print(
    df.nlargest(10, "duration_min")[
        ["track_name", "artists", "duration_min", "track_genre"]
    ].to_string(index=False)
)
