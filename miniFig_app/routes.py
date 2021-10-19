from flask import render_template, flash, redirect, url_for, request
from miniFig_app import app, db
from miniFig_app.form import LoginForm, RegistrationForm, PostSellFigForm, UserUpdateForm, SellItemUpdateForm
from flask_login import current_user, login_user, logout_user, login_required
from flask_bcrypt import Bcrypt
from miniFig_app.models.user import User
from miniFig_app.models.figure import Figure
from miniFig_app.models.sell_fig import Sell_fig

bcrypt = Bcrypt(app)

# @app.route('/add_to_cart')
# @login_required
# def index():
#     return render_template('index.html')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.email.data, form.remember_me.data))
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not bcrypt.check_password_hash(user.password, form.password.data):
            flash('Invalid email or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(bcrypt.generate_password_hash(form.password.data))
        db.session.add(user)  # MySQL insert query
        db.session.commit()
        login_user(user)
        return redirect(url_for('index'))
    return render_template('register.html', title='Register', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/user_account')
def user_profile():
    user_id = current_user.get_id()
    sell_figs = Sell_fig.display_all_by_user_id(user_id)
    return render_template('user_profile.html', sell_figs=sell_figs)


@app.route('/sell_fig', methods=['GET', 'POST'])
def sell_fig():
    form = PostSellFigForm()
    if form.validate_on_submit():
        sell_fig = Sell_fig(quantity=form.fig_quantity.data, sell_price=form.fig_price.data,figure_id=form.fig_id.data, user_id=int(current_user.get_id()))
        db.session.add(sell_fig)
        db.session.commit()
        return redirect(url_for('user_profile'))
    return render_template('sell_fig.html', title='Post to Sell', form=form)


@app.route('/browse_fig')
def browse_all():
    # query data and pass to the html
    data = Figure.browse_all()
    return render_template('browse_all.html', data=data)


@app.route('/browse_fig/year/<year>')
def browse_all_by_year(year=2021):
    data = Figure.browse_all_by_year(year)
    return render_template('year.html', data=data)


@app.route('/browse_fig/theme/<theme>')
def browse_all_by_theme(theme="General"):
    themes = Figure.browse_all_by_theme(theme)
    all_themes = ["General", "Basic Set", "Disney Princess","Duplo", "Super Heros", "City", "Star Wars", "Harry Potter"]
    return render_template('theme.html', themes=themes, all_themes=all_themes)

# @app.route('/user_account/edit/<id>')
# def update_info(id):

#     return render_template('user_profile.html')

@app.route('/user_account/edit', methods=['GET', 'POST'])
def edit_user():
    form = UserUpdateForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data
        User.update_info(form, current_user.get_id())
        return redirect(url_for('user_profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    return render_template('user_edit.html', title='Edit Information', form=form)

@app.route('/sell_fig/delete/<id>')
def delete_sell_fig(id):
    Sell_fig.delete_item(id)
    return redirect(url_for('user_profile'))

@app.route('/sell_fig/edit/<id>', methods=['GET', 'POST'])
def edit_sell_fig(id):
    form = SellItemUpdateForm()
    if form.validate_on_submit():
        Sell_fig.edit_item(form, id)
        return redirect(url_for('user_profile'))
    elif request.method == 'GET':
        item = Sell_fig.get_item(id)
        form.sell_price.data = item.sell_price
        form.quantity.data = item.quantity
    return render_template('sell_edit.html', title='Edit Sell Item', form=form)
