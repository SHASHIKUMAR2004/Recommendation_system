import pandas as pd

# Load cleaned data
df = pd.read_csv("cleaned_movie_data.csv")

# Create User-Item Matrix
user_movie_matrix = df.pivot(index="user_id", columns="title", values="rating").fillna(0)

# Save User-Item Matrix
user_movie_matrix.to_csv("user_movie_matrix.csv")

print("✅ User-Item Matrix saved as user_movie_matrix.csv")
