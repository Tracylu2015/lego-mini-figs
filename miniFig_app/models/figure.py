from flask_sqlalchemy import SQLAlchemy
from app import db
from sqlalchemy.sql import func

class Figure(db.Model):
    # def __init__(self,data):
    #     self.id = data['id']
    #     self.name = data['name']
    #     self.year = data['year']
    #     self.theme = data['theme']
    #     self.img_url = data['img_url']
    #     self.created_at = data['created_at']
    #     self.updated_at = data['updated_at']

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), index=True, unique=True)
    year = db.Column(db.Integer)
    theme = db.Column(db.String(255))
    img_url=db.Column(db.String(255))
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, on_update=func.now())

    def __repr__(self):
        return '<Figure {}>'.format(self.__dict__)
