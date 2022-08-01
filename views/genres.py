from flask_restx import Resource, Namespace

genres_ns = Namespace('genres')

@genres_ns.route('/')
class GenresViews(Resource):
    def get(self):
        return '', 200


@genres_ns.route('/<int:gid>')
class GenreViews(Resource):
    def get(self, gid):
        return '', 200
