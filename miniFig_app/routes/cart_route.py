from flask import render_template,redirect,url_for,request
from flask_login import current_user
from miniFig_app import app
from miniFig_app.models.sell_fig import Sell_fig
from miniFig_app.models.figure import Figure
from miniFig_app.models.cart import Cart
from miniFig_app.models.user import User
from miniFig_app.form import AddToCartForm

@app.route('/add_to_cart/<figure_id>', methods=['GET', 'POST'])
def add_to_cart(figure_id):
    form = AddToCartForm()
    user_id = current_user.get_id()
    if form.validate_on_submit():
        # Add item to cart
        sell_fig_id = form.sell_fig_id.data
        Cart.add_to_cart(form, user_id, sell_fig_id)
        return redirect(f'/display_minifig/{figure_id}')
    cart_items = Cart.get_all_items(user_id)
    return render_template("Add_to_cart.html",form=form,cart_items=cart_items)
