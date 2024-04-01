from fastapi import FastAPI, HTTPException, Depends
from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()

# Example data
users = [
    {"id": 1, "name": "John Doe", "phone": "11111111111", "password": "pass1", "email": "john_doe@gmail.com"},
    {"id": 2, "name": "Jane Doe", "phone": "22222222222", "password": "pass2", "email": "jane_doe@gmail.com"},
    {"id": 3, "name": "Mark Doe", "phone": "3333333333", "password": "pass3", "email": "mark_doe@gmail.com"},
    {"id": 4, "name": "Macy Doe", "phone": "4444444444", "password": "pass4", "email": "macy_doe@gmail.com"}
]

movies = [
    {"id": 1, "name": "Home Alone", "genre": "Comedy", "rating": "PG", "release_date": "01-04-1996"},
    {"id": 2, "name": "The Godfather", "genre": "Crime", "rating": "R", "release_date": "01-04-1972"},
    {"id": 3, "name": "Avengers: Endgame", "genre": "Action", "rating": "PG", "release_date": "01-04-2019"}
]

ratings = [
    {"id": 1, "user_id": 1, "movie_id": 1, "rating": 5.0},
    {"id": 2, "user_id": 1, "movie_id": 2, "rating": 4.0},
    {"id": 3, "user_id": 1, "movie_id": 3, "rating": 3.3},
    {"id": 4, "user_id": 2, "movie_id": 1, "rating": 5.0},
    {"id": 5, "user_id": 2, "movie_id": 3, "rating": 4.5},
    {"id": 6, "user_id": 3, "movie_id": 1, "rating": 1.6},
    {"id": 7, "user_id": 3, "movie_id": 2, "rating": 0.0},
    {"id": 8, "user_id": 3, "movie_id": 3, "rating": 3.4},
    {"id": 9, "user_id": 4, "movie_id": 2, "rating": 4.5}
]


# Models
class User(BaseModel):
    id: int
    name: str
    phone: str
    email: str


class Movie(BaseModel):
    id: int
    name: str
    genre: str
    rating: str
    release_date: str


class Rating(BaseModel):
    id: int
    user_id: int
    movie_id: int
    rating: float


# Routes
@app.get("/")
def read_root():
    return {"message": "Welcome to the Movie Rating System!"}


@app.post("/login/")
def login(username: str, password: str):
    for user in users:
        if user["email"] == username and user["password"] == password:
            return {"message": "Login successful", "user_id": user["id"]}
    raise HTTPException(status_code=401, detail="Invalid credentials")


@app.get("/movies/")
def get_movies():
    return movies


@app.post("/movies/")
def add_movie(movie: Movie):
    movies.append(movie)
    return {"message": "Movie added successfully"}


@app.get("/ratings/")
def get_ratings():
    return ratings


@app.post("/ratings/")
def rate_movie(rating: Rating):
    ratings.append(rating)
    return {"message": "Rating added successfully"}


@app.get("/movies/{movie_id}")
def get_movie(movie_id: int):
    movie = next((m for m in movies if m["id"] == movie_id), None)
    if movie is None:
        raise HTTPException(status_code=404, detail="Movie not found")
    
    movie_ratings = [r["rating"] for r in ratings if r["movie_id"] == movie_id]
    average_rating = sum(movie_ratings) / len(movie_ratings) if movie_ratings else 0
    
    return {"movie_details": movie, "average_rating": average_rating}


# Run the app
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
