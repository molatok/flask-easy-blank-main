from flask_restx import Resource, Namespace

directors_ns = Namespace('genres')

@directors_ns.route('/')
class DirectorsViews(Resource):
    def get(self):
        return '', 200


@directors_ns.route('/<int:gid>')
class DirectorViews(Resource):
    def get(self, did):
        return '', 200
