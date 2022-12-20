from constants import DATA_DB
from setup_db import db

from dao.model.movie import Movie
from dao.model.director import Director
from dao.model.genre import Genre



def create_db():
    """
    Функция для создания БД и задания начальных значений
    :return:
    """
    db.drop_all()
    db.create_all()


    for movie in DATA_DB["movies"]:
        m = Movie(
            id=movie["pk"],
            title=movie["title"],
            description=movie["description"],
            trailer=movie["trailer"],
            year=movie["year"],
            rating=movie["rating"],
            genre_id=movie["genre_id"],
            director_id=movie["director_id"],
        )
        with db.session.begin():
            db.session.add(m)

    for director in DATA_DB["directors"]:
        d = Director(
            id=director["pk"],
            name=director["name"],
        )
        with db.session.begin():
            db.session.add(d)

    for genre in DATA_DB["genres"]:
        d = Genre(
            id=genre["pk"],
            name=genre["name"],
        )
        with db.session.begin():
            db.session.add(d)
