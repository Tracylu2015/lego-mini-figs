from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, DecimalField
from wtforms.fields.simple import FileField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from miniFig_app import app
from miniFig_app import User


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

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')

class PostSellFigForm(FlaskForm):
    image = FileField('Upload Image', validators=[DataRequired()])
    fig_id= StringField('Minifig ID', validators=[DataRequired()])
    fig_name = StringField('Minifig Name', validators=[DataRequired()])
    fig_theme = StringField('Minifig Theme', validators=[DataRequired()])
    fig_year = IntegerField('Minifig Year', validators=[DataRequired()])
    fig_quantity = IntegerField('Minifig Quantities', validators=[DataRequired()])
    fig_price = DecimalField('Set Your Price', validators=[DataRequired()])
    submit = SubmitField('Post to Sell')