import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or "lengthy-password"
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:postgres@localhost:5432/flask-practice"