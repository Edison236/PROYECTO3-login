from databases.db import db
from flask_login import UserMixin

class User(db.Model, UserMixin):

    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    is_admin = db.Column(db.Boolean, nullable=False, default=False)

    def __init__(self,id,username,password) -> None:
        self.id = id
        self.username = username
        self.password = password

        