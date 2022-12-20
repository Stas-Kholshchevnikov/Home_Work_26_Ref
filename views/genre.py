from flask_restx import Resource, Namespace

from dao.model.genre import GenreSchema
from implemented import genre_service

genre_ns = Namespace('genres')
genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)

@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        """
        Представление всех записей для get запроса
        :return:
        """
        genre = genre_service.get_all()
        return genres_schema.dump(genre), 200


@genre_ns.route('/<int:gid>')
class GenreView(Resource):
    def get(self, gid):
        """
        Представление одной записи для get запроса
        :param gid:
        :return:
        """
        result = genre_service.get_one(gid)
        return genre_schema.dump(result), 200

