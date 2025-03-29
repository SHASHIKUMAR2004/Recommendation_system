 Movie Recommendation System

This is a **User-Based Collaborative Filtering** Movie Recommendation System built using **FastAPI** for the backend and **Streamlit** for the frontend. The system suggests personalized movie recommendations based on user preferences and similarities.

---

Features**
✅ User-based collaborative filtering  
✅ Personalized movie recommendations  
✅ FastAPI-powered backend  
✅ Interactive Streamlit frontend  
✅ Uses MovieLens dataset  

---

Movie Recommendation System  

The **Movie Recommendation System** is an advanced application that suggests movies to users based on their past viewing history and preferences. This system leverages **User-Based Collaborative Filtering**, where similar users are identified to generate personalized movie recommendations. If personalized recommendations are not available, the system suggests popular movies instead. The project is built using **FastAPI** for the backend and **Streamlit** for the frontend, providing a seamless and interactive user experience.  

The core functionality of the system is driven by **data preprocessing, user similarity calculations, and recommendation generation**. It processes the **MovieLens dataset**, which contains user ratings for movies, and structures it into a **User-Item Matrix**. Using **cosine similarity**, the system calculates relationships between users to find similar viewers. Once similar users are identified, movies watched and rated highly by them are suggested to the target user.  

The backend is implemented with **FastAPI**, exposing an API endpoint (`/recommend/{user_id}`) that returns recommendations based on user similarity. This allows for efficient and scalable communication between the database and client applications. The frontend, built with **Streamlit**, provides an easy-to-use interface where users can input their **User ID** and instantly receive recommendations. The interface is designed to be intuitive, making it accessible to users with minimal technical knowledge.  

For deployment, the project can be hosted on platforms like **Render, AWS, or Hugging Face Spaces**. Additionally, it can be containerized using **Docker** to ensure consistent performance across different environments. The system is modular and extendable, allowing for future enhancements such as **content-based filtering** or **hybrid recommendation models**.  

By implementing this **Movie Recommendation System**, users can easily discover new movies that match their tastes, improving their overall viewing experience. This project serves as a solid foundation for further exploration in the field of **recommendation systems and machine learning**.
