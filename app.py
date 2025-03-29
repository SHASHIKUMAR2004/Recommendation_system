from fastapi import FastAPI
import pandas as pd
from recommend_movies import recommend_movies

app = FastAPI()

@app.get("/recommend/{user_id}")
def get_recommendations(user_id: int, num_recommendations: int = 5):
    recommendations = recommend_movies(user_id, num_recommendations)
    return {"user_id": user_id, "recommendations": [{"title": movie, "score": score} for movie, score in recommendations]}
