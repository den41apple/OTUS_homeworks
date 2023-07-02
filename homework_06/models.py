from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, declared_attr, relationship
from flask_sqlalchemy import SQLAlchemy
from typing import TYPE_CHECKING

db = SQLAlchemy()

# class Base(db.Model):
#     @declared_attr
#     def __tablename__(cls):
#         return f"{cls.__name__.lower()}s"
#
#     @declared_attr
#     def id(self):
#         return Column(Integer, primary_key=True)
#
#

# Base = declarative_base(cls=Base)


if TYPE_CHECKING:
    from flask_sqlalchemy.query import Query


class Post(db.Model):
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    body = Column(String(1_000), nullable=False)

    if TYPE_CHECKING:
        query: Query

    def __str__(self):
        return f"{self.__class__.__name__}(user_id={self.user_id}, title={self.title})"

    def __repr__(self):
        return str(self)
