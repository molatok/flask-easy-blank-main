from flask_restx import Resource, Namespace

genres_ns = Namespace('genre')


@genres_ns.route('/')
class BooksView(Resource):
     def get(self):
         return "", 200

     def post(self):
         return "", 201