from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from miniFig_app import db

class Purchased_item(db.Model):
    __tablename__ = "purchased_items"

    id = db.Column(db.Integer, primary_key=True)

    # parent_id = Column(Integer, ForeignKey('parent.id'))
    sell_fig_id = db.Column(db.Integer, ForeignKey('sell_fig.id'))
    transaction_id = db.Column(db.Integer, ForeignKey('transaction.id'))


    def __repr__(self):
        return '<Purchased_item {}>'.format(self.__dict__)