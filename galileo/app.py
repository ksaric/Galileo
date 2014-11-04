# -*- coding: utf-8 -*-
import os

import flask
from flask.ext.httpauth import HTTPBasicAuth
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.restless import APIManager

# Create the Flask application and the Flask-SQLAlchemy object.
app = flask.Flask(__name__, static_url_path='/static')
app.config.from_object('config')

db = SQLAlchemy(app)
auth = HTTPBasicAuth()
manager = APIManager(app, flask_sqlalchemy_db=db)

# Upload
# nmap_data = UploadSet('nmap', DATA)
# configure_uploads(app, (nmap_data,))

from galileo.views import mod as galileoModule

app.register_blueprint(galileoModule)

