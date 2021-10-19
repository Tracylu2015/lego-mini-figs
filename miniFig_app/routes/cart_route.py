from flask import render_template,redirect,url_for,request
from miniFig_app import app
from miniFig_app.models.sell_fig import Sell_fig
from miniFig_app.models.figure import Figure
from miniFig_app.models.cart import Cart
from miniFig_app.models.user import User
from miniFig_app.form import AddToCartForm

@app.route('/add_to_cart/<selfig_id>', methods=['GET', 'POST'])
def add_to_cart():
    form = AddToCartForm()
    user_id = User.current_user.get_id()
    cart = Cart.add_to_cart(form, user_id)
    if form.validate_on_submit():
        cart.fig_quantity= form.fig_quantity.data
        return redirect(url_for('display_minifig'))
    elif request.method == 'GET':
        form.fig_quantity.data = cart.fig_quantity
        cart_items = Cart.get_all_items(cart)
    return render_template("add_to_cart.html",form=form,cart_items=cart_items)



    
    