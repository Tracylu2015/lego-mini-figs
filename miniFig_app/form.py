from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from wtforms import *
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from miniFig_app import app
from miniFig_app import User
from miniFig_app import Figure

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')


class PostSellFigForm(FlaskForm):
    # image = FileField('Upload Image', validators=[FileRequired()])
    
    fig_id= StringField('Minifig ID', validators=[DataRequired()])
    fig_name = StringField('Minifig Name', validators=[DataRequired()])
    # fig_theme = StringField('Minifig Theme', validators=[DataRequired()])
    # fig_year = SelectField(
    #     "Minifig Year",
    #     [DataRequired()],
    #     choices=list(range(2021, 1974, -1)),
    # )
    fig_quantity = IntegerField('Minifig Quantities', validators=[DataRequired()])
    fig_price = DecimalField('Set Your Price', validators=[DataRequired()])
    submit = SubmitField('Post to Sell')

    def validate_fig_id(self, fig_id):
        fig = Figure.query.filter_by(id=fig_id.data).first()
        if not fig:
            raise ValidationError('Minifigure Id is not exist, please check and input again!')

class UserUpdateForm(FlaskForm):
    username = StringField('Username')
    email = StringField('Email', validators=[DataRequired(), Email()])
    # password = PasswordField('Password', validators=[DataRequired()])
    # password2 = PasswordField(
    #     'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Update')


    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')