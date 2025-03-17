import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config(object):
    # Set database type based on way of running project.
    if os.getenv("DOCKERIZED") == "1":
        SQLALCHEMY_DATABASE_URI = os.getenv(
            "DATABASE_URL", "mysql+pymysql://projectuser:onecomplexpasswrd@db:3306/flask_proj_db"
        )
    else:
        SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "app.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv("SECRET_KEY", "supersecretkey")
    DEBUG = True