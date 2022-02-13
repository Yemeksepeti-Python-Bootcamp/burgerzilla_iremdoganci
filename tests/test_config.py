import unittest
import os

from flask import current_app
from app import create_app
from config import basedir

class TestDevelopmentConfig(unittest.TestCase):
    def test_app_is_development(self):
        """ Check if application is running in development mode """
        app = create_app("development") # uyg dev başlatabiliyor muyum

        self.assertFalse(app.config["SECRET_KEY"] == "GahNooSlasHLinUcks") # dev başlattığım uygulamada secret key şuna sahip mi
        self.assertTrue(app.config["DEBUG"]) # dev başlattığım uygulamada debug true mi
        self.assertFalse(current_app is None) # dev başlattığım uygulamada current_app null mı
        self.assertTrue(
            app.config["SQLALCHEMY_DATABASE_URI"]
            ==  "postgresql+psycopg2://user:123456@localhost:5432/burgerzilla"
        )


class TestProductionConfig(unittest.TestCase):
    def test_app_is_production(self):
        """ Check if application is running in production mode """
        app = create_app("production")

        self.assertTrue(app.config["DEBUG"] is False)
