import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


class Config:
    SECRET_KEY = "snazzy"

    SQLALCHEMY_DATABASE_URI = (
        "mysql+mysqlconnector://snazzy:snazzy@{}:{}/snazzy".format(
            os.getenv("MYSQL_HOST", "localhost"),
            os.getenv("MYSQL_PORT", 3306),
        )
    )
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_MAX_OVERFLOW = 100
    SQLALCHEMY_TRACK_MODIFICATIONS = False


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db = SQLAlchemy(app)

    return app, db


app, db = create_app()
from app import routes, models

# TODO: to support postsgres in the future
with app.app_context():
    db.create_all()
