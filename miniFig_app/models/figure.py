from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.ext.declarative import declarative_base
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


    @classmethod
    def browse_all(cls):
        browse_figs = Figure.query.limit(100).all() #select * 
        return browse_figs
    # session_browse.close()

    @classmethod
    def browse_all_by_year(cls,year):
        browse_figs = Figure.query.filter(Figure.year == year).limit(30).all()
        return browse_figs

    @classmethod
    def browse_all_by_theme(cls,theme):
        browse_figs = Figure.query.filter(Figure.theme == theme).limit(30).all()
        print(browse_figs)#select * by theme
        return browse_figs

    @classmethod
    def get_one_by_fig_id(cls,id):
        return Figure.query.filter(Figure.id == id).one()


