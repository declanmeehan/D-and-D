from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, Email, Length, EqualTo

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[Required()])
    password = PasswordField("Password", validators=[Required()])
    remember_me = BooleanField("Stay logged in")
    submit = SubmitField("Log In")