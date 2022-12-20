from dao.movie import MovieDAO


class MovieService:
    """
    Класс слоя Service для Movie
    """

    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_one(self, mid):
        """
        Получение одной записи
        :param mid:
        :return:
        """
        return self.dao.get_one(mid)

    def get_all(self):
        """
        Получить все записи
        :return:
        """
        return self.dao.get_all()

    def get_all_by_director(self, director_id):
        """
        Получение всех записей соответвующих director_id
        :param director_id:
        :return:
        """
        return self.dao.get_all_by_director(director_id)

    def get_all_by_genre(self, genre_id):
        """
        Получение всех записей соответвующих genre_id
        :param genre_id:
        :return:
        """
        return self.dao.get_all_by_genre(genre_id)

    def get_all_by_year(self, year_id):
        """
        Получение всех записей соответвующих year_id
        :param year_id:
        :return:
        """
        return self.dao.get_all_by_year(year_id)

    def create(self, data):
        """
        Создание записи
        :param data:
        :return:
        """
        return self.dao.create(data)

    def update(self, mid, data):
        """
        Обновление значений заданной записи
        :param mid:
        :param data:
        :return:
        """
        return self.dao.update(mid, data)

    def delete(self, mid):
        """
        Удаление заданной записи
        :param mid:
        :return:
        """
        return self.dao.delete(mid)
