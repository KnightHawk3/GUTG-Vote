from flask.ext.login import LoginManager
from flask.ext.mongoengine import MongoEngine


db = MongoEngine()
login = LoginManager()