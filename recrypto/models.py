from recrypto import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(30), unique=False, nullable=False)
    password = db.Column(db.String(50), unique=False, nullable=False)
    #profilePicture = db.Column(db.String(20), unique=False, nullable=False, default="default.jpg")

    def __repr__(self):
        return f"User('{self.username}', '{self.email}' )"
