from dao.model.genre import Genre


class GenreDAO:
    """
    Слой DAO для объетов класса Genre (таблица genre в БД)
    """
    def __init__(self, session):
        """
        Конструктор для GenreDAO
        :param session:
        """
        self.session = session

    def get_one(self, gid):
        """
        Получение одного объекта genre
        :param gid:
        :return:
        """
        return self.session.query(Genre).get(gid)

    def get_all(self):
        """
        Получение всех объектов genre
        :return:
        """
        return self.session.query(Genre).all()
