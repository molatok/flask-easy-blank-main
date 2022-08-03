from typing import List

from dao.movie import MovieDAO

class MovieService:
    def __init__(self, movie_dao: MovieDAO):
        self.book_dao = movie_dao
        
    def get_movies(self, mid=None):
        return self.movie_dao.get(mid)
    
    def create_movie(self, data):
        self.movie_dao.create()
        
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
        
    
    # def update_movie_partial(self, data):
    #     movie = self.get_movies(data['movie_id'])
    #
    #     if not movie:
    #         return 'не нашли', 404
    #     movie.title = data['title']
    #     movie.description = data['description']
    #     movie.trailer = data['trailer']
    #     movie.year = data['year']
    #     movie.rating = data['rating']
    #     movie.genre_id = data['genre_id']
    #     movie.director_id = data['director_id']
    #     self.movie_dao.update(movie)
    #     return movie
    
    def delete(self, movie_id):
        try:
            movie_service.delete(movie_id)
            return 204
        except Exception as e:
            print(e)
            return 500
    
    