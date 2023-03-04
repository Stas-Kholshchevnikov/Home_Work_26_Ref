# Класс настроек основного приложения app


class Config(object):
    DB_USER: str = 'db_user'
    DB_PASSWORD: str = 'db_password'
    DB_NAME: str = 'db_name'
    DB_HOST: str = 'db'
    DB_PORT: int = 5432
    DEBUG = True
    #SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:password_26@localhost/home_work_26'
    SQLALCHEMY_DATABASE_URI = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    RESTX_JSON = {'ensure_ascii': False}
