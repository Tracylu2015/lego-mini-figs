from flask_sqlalchemy import SQLAlchemy
from app import db
from sqlalchemy.sql import func

class User(db.Model):
    # def __init__(self,data):
    #     self.id = data['id']
    #     self.name = data['name']
    #     self.year = data['year']
    #     self.theme = data['theme']
    #     self.img_url = data['img_url']
    #     self.created_at = data['created_at']
    #     self.updated_at = data['updated_at']

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255), index=True, unique=True)
    last_name = db.Column(db.String(255), index=True, unique=True)
    email = db.Column(db.String(255))
    password = db.Column(db.String(60))
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, on_update=func.now())

    def __repr__(self):
        return '<User {}>'.format(self.__dict__)