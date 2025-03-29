import pandas as pd

def recommend_movies(target_user, num_recommendations=5):
    # Load Data
    user_movie_matrix = pd.read_csv("user_movie_matrix.csv", index_col=0)
    user_similarity_df = pd.read_csv("user_similarity_matrix.csv", index_col=0)

    # Convert index to string (if needed)
    user_movie_matrix.index = user_movie_matrix.index.astype(str)
    user_similarity_df.index = user_similarity_df.index.astype(str)

    # Ensure target_user exists in dataset
    if str(target_user) not in user_similarity_df.index:
        print(f"⚠️ User {target_user} not found. Suggesting popular movies.")
        return get_most_popular_movies(num_recommendations)

    # Get Similar Users (excluding self)
    similar_users = user_similarity_df.loc[str(target_user)].sort_values(ascending=False)[1:6]

    weighted_scores = {}
    total_similarity = {}

    # Movies already watched by the target user
    watched_movies = set(user_movie_matrix.loc[str(target_user)][user_movie_matrix.loc[str(target_user)] > 0].index)

    # Compute Weighted Movie Scores from Similar Users
    for user, similarity in similar_users.items():
        if str(user) in user_movie_matrix.index:
            user_ratings = user_movie_matrix.loc[str(user)]
            for movie, rating in user_ratings.items():
                if movie not in watched_movies and rating > 0:  # Recommend only unwatched movies
                    if movie not in weighted_scores:
                        weighted_scores[movie] = 0
                        total_similarity[movie] = 0
                    weighted_scores[movie] += rating * similarity
                    total_similarity[movie] += similarity

    # Normalize Scores
    recommendations = []
    for movie in weighted_scores:
        if total_similarity[movie] > 0:
            recommendations.append((movie, weighted_scores[movie] / total_similarity[movie]))

    # Sort movies by score (descending)
    recommendations.sort(key=lambda x: x[1], reverse=True)

    # If no personalized recommendations found, return popular movies
    return recommendations[:num_recommendations] if recommendations else get_most_popular_movies(num_recommendations)

def get_most_popular_movies(num_movies=5):
    """Fallback function to return most popular movies if no recommendations found."""
    df = pd.read_csv("cleaned_movie_data.csv")
    popular_movies = df.groupby("title")["rating"].count().sort_values(ascending=False).head(num_movies).index
    return [(movie, None) for movie in popular_movies]  # No score for popular movies

# Example Test
user_id = 18
recommendations = recommend_movies(user_id, 5)
print(f"\n🎬 **Top 5 Recommended Movies for User {user_id}:**")
for movie, score in recommendations:
    print(f"✅ {movie} (Score: {round(score, 2) if score else 'N/A'})")
