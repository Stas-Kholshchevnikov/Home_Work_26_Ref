from dao.model.movie import Movie


class MovieDAO:
    """
    Слой DAO для объетов класса Movie (таблица movie в БД)
    """
    def __init__(self, session):
        """
        Контруктор для MovieDAO
        :param session:
        """
        self.session = session

    def get_one(self, mid):
        """
        Получение одного объекта Movie
        :param mid:
        :return:
        """
        return self.session.query(Movie).get(mid)

    def get_all(self):
        """
        Получение всех объектов Movie
        :return:
        """
        return self.session.query(Movie).all()

    def get_all_by_director(self, director_id):
        """
        Получение всех объектов Movie по заданному director_id
        :param director_id:
        :return:
        """
        return self.session.query(Movie).filter(Movie.director_id == director_id).all()

    def get_all_by_genre(self, genre_id):
        """
        Получение всех объектов Movie по заданному genre_id
        :param genre_id:
        :return:
        """
        return self.session.query(Movie).filter(Movie.genre_id == genre_id).all()


    def get_all_by_year(self, year_id):
        """
        Получение всех объектов Movie по заданному year_id
        :param year_id:
        :return:
        """
        return self.session.query(Movie).filter(Movie.year == year_id).all()

    def create(self, data):
        """
        Создание нового объекта Movie
        :param data:
        :return:
        """
        new_movie = Movie(**data)
        self.session.add(new_movie)
        self.session.commit()
        return new_movie

    def update(self, mid, data):
        """
        Обновление значений заданного объекта Movie
        :param mid:
        :param data:
        :return:
        """
        self.session.query(Movie).filter(Movie.id == mid).update(data)
        self.session.commit()
        return self.get_one(mid)

    def delete(self, mid):
        """
        Удаление заданного объекта Movie
        :param mid:
        :return:
        """
        movie = self.session.query(Movie).get(mid)
        self.session.delete(movie)
        self.session.commit()
        return
