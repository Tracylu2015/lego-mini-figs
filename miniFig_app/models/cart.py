from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from miniFig_app import db
from sqlalchemy.orm import relationship
from miniFig_app.models.sell_fig import Sell_fig


class Cart(db.Model):
    __tablename__ = "carts"

    id = db.Column(db.Integer, primary_key=True)
    fig_quantity = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    sell_fig_id = db.Column(db.Integer, db.ForeignKey('sell_figs.id'))

    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.current_timestamp())
    sell_fig=relationship("Sell_fig", back_populates="cart")

    def __repr__(self):
        return '<Cart {}>'.format(self.__dict__)


    @classmethod
    def add_to_cart(cls,form, user_id, figure_id): # when click add item, data should be inserted into cart table
        cart = Cart()
        cart.fig_quantity = form.fig_quantity.data
        cart.user_id = user_id
        cart.sell_fig_id = figure_id
        db.session.add(cart)

    @classmethod
    def pay_all_items(cls,cart): # cart html show all the items added to cart and check whether to pay
        cart_items = Cart.query.filter(Cart.id == cart).all()
        print(cart_items)
        return cart_items
    