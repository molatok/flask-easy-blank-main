from dao.model.movies import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session
    
    def get(self, mid=None, **kwargs):
        query = self.session.query(Movie)
        if kwargs:
            for key, value in kwargs.items():
                query = query.filter(eval(f'Movie.{key}') == int(value))
        if mid:
            return query.get(mid)
        else:
            return query.all()
        
        def create(self, data):
            new_movie = Movie(**data)
            with self.session.begin():
                self.session.add(new_movie)
            return new_movie
        
        def update(self, movie):
            self.session.add(movie)
            self.session.commit()
        
        def delete(self, mid):
            movie = self.get(mid)
            if None:
                return
            self.session.delete(movie)
            self.session.commit()
