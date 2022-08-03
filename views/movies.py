from flask import request
from flask_restx import Resource, Namespace
from implemented import movie_service
from setup_db import db

movie_ns = Namespace('movie')


@movie_ns.route('/')
class MovieView(Resource):
    def get(self):
        return movie_service.get_movies()
    
    def post(self):
        new_movie = movie_service.create_movie(request.json)
        return '', 201, {'location': f"{movie_ns.patch}/{new_movie.id}"}


@movie_ns.route('/<int:movie_id>')
class MovieView(Resource):
    def get(self, movie_id: int):
       return movie_service.get_movies(movie_id)

    def put(self, movie_id: int):
        return movie_service.update_movie_full(movie_id, request.json)
    
    
    def delete(self, movie_id):
        movie_service.delete(movie_id)
        return '', 204