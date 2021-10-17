from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship

from sqlalchemy.sql import func
from miniFig_app import db

class Figure(db.Model):
    __tablename__ = "figures"

    id = db.Column(db.String(255), primary_key=True)
    name = db.Column(db.String(255))
    year = db.Column(db.Integer)
    theme = db.Column(db.String(255))
    img_url=db.Column(db.String(255))
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.current_timestamp())
    sell_fig = relationship("Sell_fig")

    def __repr__(self):
        return '<Figure {}>'.format(self.__dict__)
