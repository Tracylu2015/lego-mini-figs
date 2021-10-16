from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from miniFig_app import db

class Transaction(db.Model):
    __tablename__ = "transactions"

    id = db.Column(db.Integer, primary_key=True)

    # parent_id = Column(Integer, ForeignKey('parent.id'))
    user_id = db.Column(db.Integer, ForeignKey('user.id'))
    purchased_items = relationship("Purchased_items")

    def __repr__(self):
        return '<Transaction {}>'.format(self.__dict__)