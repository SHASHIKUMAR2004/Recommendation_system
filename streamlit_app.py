import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/recommend"

st.title("🎥 Movie Recommendation System")
user_id = st.number_input("Enter User ID:", min_value=1, max_value=943, value=1)
num_recommendations = st.slider("Number of Recommendations:", 1, 10, 5)

if st.button("Get Recommendations"):
    try:
        response = requests.get(f"{API_URL}/{user_id}?num_recommendations={num_recommendations}")
        data = response.json()
        
        if data["recommendations"]:
            st.subheader(f"🎬 Top {num_recommendations} Movies for User {user_id}")
            for rec in data["recommendations"]:
                st.write(f"✅ **{rec['title']}** (Score: {rec['score'] if rec['score'] else 'N/A'})")
        else:
            st.warning("⚠️ No recommendations found.")
    except requests.exceptions.RequestException:
        st.error("⚠️ Backend is not running. Please start FastAPI first.")
