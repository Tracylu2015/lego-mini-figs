from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from miniFig_app import db
from sqlalchemy.orm import relationship
from miniFig_app.models.figure import Figure


class Sell_fig(db.Model):
    __tablename__ = "sell_figs"

    id = db.Column(db.Integer, primary_key=True)
    sell_price = db.Column(db.Float)
    quantity = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    figure_id = db.Column(db.String(255), db.ForeignKey('figures.id'))
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.current_timestamp())
    purchased_item = relationship("Purchased_item")
    figure = relationship("Figure", back_populates="sell_fig")

    def __repr__(self):
        return '<Sell_fig {}>'.format(self.__dict__)

    @classmethod
    def display_all_by_user_id(cls,user_id):
        display_sell_figs = Sell_fig.query.filter(Sell_fig.user_id == user_id).all()
        return display_sell_figs

    @classmethod
    def delete_item(cls,id):
        Sell_fig.query.filter(Sell_fig.id == id).delete()
        db.session.commit()

    @classmethod
    def edit_item(cls, form, id):
        Sell_fig.query.filter(Sell_fig.id == id).update(
            dict(quantity=form.quantity.data, sell_price=form.sell_price.data)
        )
        db.session.commit()

    @classmethod
    def get_item(cls,id):
        return Sell_fig.query.filter(Sell_fig.id == id).one()

    @classmethod
    def get_all_sellInfo_by_fig_id(cls,id):
        sellInfo = Sell_fig.query.filter(Sell_fig.figure_id == id).all()
        return sellInfo 
        
    