from dao.movie import MovieDAO
#from service.movie import MovieDAO
from setup_db import db

movie_dao = MovieDAO(db.session)
movie_service = MovieDAO(movie_dao)

