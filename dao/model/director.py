from marshmallow import Schema, fields
from setup_db import db


class Director(db.Model):
    """
        Модель для таблицы director в БД
    """
    __tablename__ = 'director'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))

class DirectorSchema(Schema):
    """
        Schema для модели Director
    """
    id = fields.Int(dump_only=True)
    name = fields.Str()
