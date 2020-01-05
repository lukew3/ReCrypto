from datetime import datetime
from recrypto import db
from recrypto import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(30), unique=False, nullable=False)
    password = db.Column(db.String(50), unique=False, nullable=False)
    #profilePicture = db.Column(db.String(20), unique=False, nullable=False, default="default.jpg")

    def __repr__(self):
        return f"User('{self.username}', '{self.email}' )"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), unique=False, nullable=False)
    description = db.Column(db.String(1000), unique=False, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    #photo = db.Column(db.String(100), nullable=False, unique=False)
    #author =
    #photo =

    def __repr__(self):
        return f"Post('{self.title}', '{self.description}')"
