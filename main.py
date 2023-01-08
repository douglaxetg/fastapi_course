from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from jwt_manager import create_token
from config.database import engine, Base
from models.movie import Movie as MovieModel
from middlewares.error_handler import ErrorHandler
from routes.movie import movie_router
from routes.user import user_router

app = FastAPI()
app.title = "My app with FastAPI"
app.version = "0.0.1"

app.add_middleware(ErrorHandler)
app.include_router(movie_router)
app.include_router(user_router)

Base.metadata.create_all(bind=engine)

movies = [
    {
        'id': 1,
        'title': 'Avatar',
        'overview': "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        'year': '2009',
        'rating': 7.8,
        'category': 'Accion'    
    },
    {
        'id': 2,
        'title': 'Avatar2',
        'overview': "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...2",
        'year': '2010',
        'rating': 7.8,
        'category': 'Accion2'
    } 
]

@app.get('/', tags=['home'])
def message():
    return HTMLResponse('<h1>Hello world</h1>')

        
