import os
from datetime import timedelta

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    # Change the secret key in production run.
    SECRET_KEY = os.environ.get("SECRET_KEY", os.urandom(24))
    DEBUG = False

    # JWT Extended config
    JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY", os.urandom(24)) # 'aC\xb0M\rK\x9d\xdb\xe5\xc1\xd7R8]\x94\x8f{\xe6\x05\xaf\x054\xa8\x1d'
    ## Set the token to expire every week 
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=7)

# database url gelmezse sqlite ile bağlanır 
class DevelopmentConfig(Config):
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://user:123456@localhost:5432/burgerzilla"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True

    # Add logger


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    # In-memory SQLite for testing
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL", "sqlite:///" + os.path.join(basedir, "data.sqlite")
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False


config_by_name = dict(
    development=DevelopmentConfig,
    testing=TestingConfig,
    production=ProductionConfig,
    default=DevelopmentConfig,
)
