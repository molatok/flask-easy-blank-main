from dao.movie import MovieDAO


class MovieService:
    def __init__(self, dao: MovieDAO):
        self.dao = dao
    
    def get_movies(self, mid=None, **kwargs):
        return self.dao.get(mid, **kwargs)
    
    def create_movie(self, data):
        return self.dao.create(data)
    
    def update(self, movie_id, data):
        movie = self.get_movies(movie_id)
        movie.title = data['title']
        movie.description = data['description']
        movie.trailer = data['year']
        movie.rating = data['rating']
        movie.genre_id = data['genre_id']
        movie.director_id = data['director_id']
        self.dao.update(movie)
        return movie
    
    def delete(self, mid):
        self.dao.delete(mid)