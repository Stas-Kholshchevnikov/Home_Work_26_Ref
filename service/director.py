from dao.director import DirectorDAO


class DirectorService:
    """
    Класс слоя Service для Director
    """
    def __init__(self, dao: DirectorDAO):
        self.dao = dao

    def get_one(self, did):
        """
        Получение одной записи
        :param did:
        :return:
        """
        return self.dao.get_one(did)

    def get_all(self):
        """
        ПОлучение всех записей
        :return:
        """
        return self.dao.get_all()

