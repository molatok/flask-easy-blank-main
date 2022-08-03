from flask import Flask
from flask_restx import Api
#
from config import Config
# from models import Review, Book
from setup_db import db
# from views.books import book_ns
# from views.reviews import review_ns
#
# функция создания основного объекта app
from views.movies import movie_ns


def create_app(config_object):
     application = Flask(__name__)
     application.config.from_object(config_object)
     register_extensions(application)
     return application
#
#
def register_extensions(application):
    db.init_app(application)
    api = Api(application)
    api.add_namespace(movie_ns)
    
    
app = create_app(Config())

if __name__ == '__main__':
    app.run()



