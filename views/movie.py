from flask import request
from flask_restx import Resource, Namespace

from dao.model.movie import MovieSchema
from implemented import movie_service

movie_ns = Namespace('movies')
movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        """
        Представление все записей для get запроса
        :return:
        """
        #Проверка наличия дополнительных аргументов в get запросе
        director_id = request.args.get("director_id")
        genre_id = request.args.get("genre_id")
        year_id = request.args.get("year_id")

        if director_id is not None:
            all_movie = movie_service.get_all_by_director(director_id)
        elif genre_id is not None:
            all_movie = movie_service.get_all_by_genre(genre_id)
        elif year_id is not None:
            all_movie = movie_service.get_all_by_year(year_id)
        else:
            all_movie = movie_service.get_all()
        return movies_schema.dump(all_movie), 200

    def post(self):
        """
        Представление для создания записи по post запросу
        :return:
        """
        data = request.json
        result = movie_service.create(data)
        return movie_schema.dump(result), 201



@movie_ns.route('/<int:mid>')
class MovieView(Resource):
    def get(self, mid):
        """
        Представление одной записи для get запроса
        :param mid:
        :return:
        """
        movie = movie_service.get_one(mid)
        return movie_schema.dump(movie), 200

    def put(self, mid):
        """
        Представление для обновления данных выбранной записи по put запросу
        :param mid:
        :return:
        """
        data = request.json
        result = movie_service.update(mid, data)
        return movie_schema.dump(result), 204


    def delete(self, mid):
        """
        Представление для удаления выбранной записи по delete запросу
        :param mid:
        :return:
        """
        movie_service.delete(mid)
        return "Deleted", 204

