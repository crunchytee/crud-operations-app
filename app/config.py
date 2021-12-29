import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv()

class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or "lengthy-password"
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FLASK_APP = os.environ.get("FLASK_APP")
