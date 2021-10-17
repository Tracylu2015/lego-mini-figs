from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from miniFig_app import db
from sqlalchemy.orm import relationship

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    email = db.Column(db.String(255), index=True, unique=True)
    password = db.Column(db.String(60)) 
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.current_timestamp())
    cart = relationship("Cart")
    sell_fig = relationship("Sell_fig")
    transaction = relationship("Transaction")

    def __repr__(self):
        return '<User {}>'.format(self.__dict__)
