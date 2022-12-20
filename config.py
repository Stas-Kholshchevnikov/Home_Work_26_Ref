# Класс настроек основного приложения app


class Config(object):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///hw_18.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    RESTX_JSON = {'ensure_ascii': False}
