from dao.model.director import Director


class DirectorDAO:
    """
    Слой DAO для объетов класса Director (таблица director в БД)
    """
    def __init__(self, session):
        """
        Конструктор для DirectorDAO
        :param session:
        """
        self.session = session

    def get_one(self, did):
        """
        Получение одного объекта director
        :param did:
        :return:
        """
        return self.session.query(Director).get(did)

    def get_all(self):
        """
        Получение всех объектов director
        :return:
        """
        return self.session.query(Director).all()
