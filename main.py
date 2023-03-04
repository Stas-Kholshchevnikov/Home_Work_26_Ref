from flask import Flask
from flask_restx import Api

from config import Config
from create_data_db import create_db
from views.genre import genre_ns
from views.director import director_ns
from views.movie import movie_ns
from setup_db import db


# функция создания основного объекта app
def create_app(app_config):
    app = Flask(__name__)
    app.config.from_object(app_config)
    app.app_context().push()
    register_extensions(app)
    return app


# функция подключения расширений (Flask-SQLAlchemy, Flask-RESTx, ...)
def register_extensions(app):
    db.init_app(app)
    api = Api(app)
    api.add_namespace(genre_ns)
    api.add_namespace(director_ns)
    api.add_namespace(movie_ns)
    create_db()


app = create_app(Config())
app.debug = True

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
