import fastapi
import uvicorn
# from movie_data import get_movie
import movie_data
from models.movie_model import MovieModel

app = fastapi.FastAPI()


@app.get('/')
def index():
    return {
        "message": " Que onda wey",
        "usage": "Call /api/movie/{title} to use the API"
    }


@app.get('/api/movie/{title}', response_model=MovieModel)
async def movie_search(title: str):
    movie = await movie_data.get_movie(title)
    if not movie:
        raise fastapi.HTTPException(status_code=404)
    return movie.dict()

if __name__ == '__main__':
    uvicorn.run(app)
