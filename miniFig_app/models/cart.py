from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from miniFig_app import db

class Cart(db.Model):
    __tablename__ = "carts"

    id = db.Column(db.Integer, primary_key=True)
    fig_quantity = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    sell_fig_id = db.Column(db.Integer, db.ForeignKey('sell_figs.id'))

    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.current_timestamp())

    def __repr__(self):
        return '<Cart {}>'.format(self.__dict__)