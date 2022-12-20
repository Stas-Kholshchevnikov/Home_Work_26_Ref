from dao.genre import GenreDAO


class GenreService:
    """
    Класс слоя Service для Genre
    """
    def __init__(self, dao: GenreDAO):
        self.dao = dao

    def get_one(self, gid):
        """
        ПОлучение одной записи
        :param gid:
        :return:
        """
        return self.dao.get_one(gid)

    def get_all(self):
        """
        Получение всех записей
        :return:
        """
        return self.dao.get_all()
