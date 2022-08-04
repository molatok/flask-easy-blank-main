from dao.movie import MovieDAO
from dao.model.movies import Movie

class MovieService:
    def __init__(self, movie_dao: MovieDAO):
        self.movie_dao = movie_dao
        
    def get_movies(self, mid=None):
        return self.movie_dao.get(mid)
    
    def create_movie(self, data):
        return self.movie_dao.create(data)
        
    def update_movie_full(self, movie_id, data):
        movie = self.get_movies(movie_id)
        movie.title = data['title']
        movie.description = data['description']
        movie.trailer = data['trailer']
        movie.year = data['year']
        movie.rating = data['rating']
        movie.genre_id = data['genre_id']
        movie.director_id = data['director_id']
        self.movie_dao.update(movie)
        return movie
        
    
    def delete(self, movie_id):
        self.movie_dao.delete(movie_id)
    
    