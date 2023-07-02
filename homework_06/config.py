from os import getenv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DEFAULT_DB_URL = "postgresql://username:passwd@localhost:5432/postgres"

SQLALCHEMY_DATABASE_URI = getenv("SQLALCHEMY_DATABASE_URI", DEFAULT_DB_URL)


class Config:
    TESTING = False
    DEBUG = False
    SECRET_KEY = "b17fb87500a32fbb24888e8cea0bb4c8"
    SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI


class ProductionConfig(Config):
    SECRET_KEY = "a951fad8d8369f41236a024ec6d65c7a"


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True