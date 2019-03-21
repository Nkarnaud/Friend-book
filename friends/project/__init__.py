# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 21:16:09 2019

@author: nkeumo
"""


import os
import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt

# instantiate the extensions
db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()



def create_app(script_info=None):

    # instantiate the app
    app = Flask(__name__)

    # enable CORS
    CORS(app)

    # set config
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)
    os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

    app.config['SECRET_KEY'] = "development key"


    # set up extensions
    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)

    # register endpoints 
    from project.api.friendsbook import friends_blueprint
    app.register_blueprint(friends_blueprint)
    # shell context for flask cli
    app.shell_context_processor({'app': app, 'db': db})

    return app