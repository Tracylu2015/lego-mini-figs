from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from miniFig_app import db

class Cart(db.Model):
    __tablename__ = "carts"

    id = db.Column(db.Integer, primary_key=True)
    fig_quantity = db.Column(db.Integer)
    # parent_id = Column(Integer, ForeignKey('parent.id'))
    user_id = db.Column(db.Integer, ForeignKey('user.id'))
    sell_fig_id = db.Column(db.Integer, ForeignKey('sell_fig.id'))

    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.current_timestamp())

    def __repr__(self):
        return '<Cart {}>'.format(self.__dict__)