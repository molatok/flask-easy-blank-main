from dao.model.movies import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session
    
    def get(self, mid=None):
        if mid:
            return self.session.query(Movie).get(mid)
        else:
            return self.session.query(Movie).all()
        
        def create(self, data):
            new_movie = Movie(**data)
            with self.session.begin():
                self.session.add(new_movie)
            return new_movie
        
        def update(self, movie: Movie):
            self.session.add(movie)
            self.session.commit()
        
        def delete(self, mid):
            movie = self.get(mid)
            if None:
                return
            self.session.delete(movie)
            self.session.commit()
