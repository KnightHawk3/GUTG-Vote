#! ../env/bin/python
# -*- coding: utf-8 -*-

__author__ = 'Melody Kelly'
__email__ = 'melody@melody.blue'
__version__ = '0.0.1'

from flask import Flask
from GUTG_Vote.views import main
from GUTG_Vote.extensions import db, login            
from GUTG_Vote.utilities import sync_mongo_with_spreadsheet

'''
@login.user_loader
def load_user(username):  
    u = current_app.config['USERS_COLLECTION'].find_one({"_id": username})
    if not u:
        return None
    return User(u['_id'])
    '''


def create_app(config='GUTG_Vote.settings.DevConfig'):
    app = Flask(__name__)
    if config is not None:
        app.config.from_object(config)
    app.register_blueprint(main)
    db.init_app(app)
    #app.session_interface = MongoEngineSessionInterface(db)
    login.init_app(app)
    sync_mongo_with_spreadsheet()
    return app