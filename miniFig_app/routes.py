from flask import render_template, flash, redirect,url_for
from miniFig_app import app
from miniFig_app.form import LoginForm
from miniFig_app.form import RegistrationForm
from miniFig_app import db
from flask_login import current_user,login_user,logout_user,login_required
from miniFig_app.models.user import User 

@app.route('/')
@app.route('/index')
@login_required
def index():
    pass
 
@app.route('/')
def mainroute():
    return render_template('index.html')



@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.email.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


