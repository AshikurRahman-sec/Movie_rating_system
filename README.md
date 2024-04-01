# Movie Rating System using FastAPI

## Language and Database

- **Language**: Python
- **Database**: No database is used in this implementation. Data is stored in memory using Python lists.

## Setup Instructions

1. Clone the repository:

    ```bash
    git clone <repository-url>
    ```

2. Install the required dependencies:

    ```bash
    pip install fastapi uvicorn
    ```

2. Navigate to the project directory:

    ```bash
    cd Movie_rating_system
    ```

3. Run the FastAPI server:

    ```bash
    uvicorn main:app --reload
    ```

4. The server will start running at `http://127.0.0.1:8000` by default.
5. Swager url `http://127.0.0.1:8000/docs`

## Problem Solved

- User can log in.
- User can add movies.
- User can view a list of all movies.
- User can rate a movie.
- User can search for a specific movie and see its details along with the average rating.


