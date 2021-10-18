from flask import render_template, flash, redirect,url_for
from miniFig_app import app, db
from miniFig_app.form import LoginForm, RegistrationForm, PostSellFigForm
from flask_login import current_user,login_user,logout_user,login_required
from flask_bcrypt import Bcrypt
from miniFig_app.models.user import User 

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
        db.session.add(user)
        db.session.commit()
        login_user(user)
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('index'))
    return render_template('register.html', title='Register', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/user_account')
def user_profile():
    return render_template('user_profile.html')

@app.route('/sell_fig', methods=['GET', 'POST'])
def sell_fig():
    form = PostSellFigForm()
    #need to add validator
    return render_template('sell_fig.html', title='Post to Sell', form = form)

