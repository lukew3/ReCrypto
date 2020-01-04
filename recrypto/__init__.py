import os
from flask import Flask, session, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
UPLOAD_FOLDER = '/media'
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['UPLOAD_FOLDER'] = 'userPhotos'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024 #restricts max file size to 16mb
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from recrypto import routes
