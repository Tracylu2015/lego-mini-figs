from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from miniFig_app import db

class Sell_fig(db.Model):
    __tablename__ = "sell_figs"

    id = db.Column(db.Integer, primary_key=True)
    sell_price = db.Column(db.Float)
    quantity = db.Column(db.Integer)
    # parent_id = Column(Integer, ForeignKey('parent.id'))
    user_id = db.Column(db.Integer, ForeignKey('user.id'))
    figure_id = db.Column(db.Integer, ForeignKey('figure.id'))
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.current_timestamp())
    purchased_items = relationship("Purchased_items")

    def __repr__(self):
        return '<Sell_fig {}>'.format(self.__dict__)