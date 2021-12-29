import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or "lengthy-password"
    SQLALCHEMY_DATABASE_URI = "postgresql://tosh:flask-practice@localhost:5432/flask-practice"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
