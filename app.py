from flask import Flask
from flask_restx import Api
from setup_db import db
from config import Config
from views.directors import director_ns
from views.genres import genres_ns
from views.movies import movie_ns


def create_app(config_object):
    application = Flask(__name__)
    application.config.from_object(config_object)
    register_extensions(application)
    return application


def create_data(application, database):
    with application.app_context():
        database.create_all()


def register_extensions(application):
    db.init_app(application)
    api = Api(application)
    api.add_namespace(movie_ns)
    api.add_namespace(genres_ns)
    api.add_namespace(director_ns)
    create_data(application, db)


app = create_app(Config())

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
