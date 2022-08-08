from dao.model.directors import Director
from dao.model.movies import Movie
from dao.model.genres import Genre

class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_movies(self, mid=None):
       return self.dao.get(mid)

    def create_movie(self, data):
        new_movie = Movie(**data)
        with self.session.begin():
            self.session.add(new_movie)
        return new_movie

    def update_movie(self, mid):
        movie = self.get(mid)
        self.session.add(movie)
        self.session.commit()


    def delete(self, mid):
        movie = self.get(mid)
        if not movie:
            return
        self.session.delete(movie)

    def filter_by_genre(self, genre_id):
        movies = self.get_movies()
        result = []
        for movie in movies:
            if movie.genre_id == genre_id:
                result.append(movie)

        return result