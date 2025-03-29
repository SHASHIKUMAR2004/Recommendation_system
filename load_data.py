import pandas as pd

# Load dataset
columns = ["user_id", "movie_id", "rating", "timestamp"]
ratings = pd.read_csv("ml-100k/u.data", sep="\t", names=columns, usecols=["user_id", "movie_id", "rating"])

movies = pd.read_csv("ml-100k/u.item", sep="|", encoding="latin-1", usecols=[0, 1], names=["movie_id", "title"])

# Merge ratings and movie titles
df = ratings.merge(movies, on="movie_id")

# Save cleaned data
df.to_csv("cleaned_movie_data.csv", index=False)
print("✅ Data saved as cleaned_movie_data.csv")
