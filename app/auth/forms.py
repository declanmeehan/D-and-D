from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, Email, Length, EqualTo
from ..models import User

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[Required(), Email(), Length(1, 64)])
    password = PasswordField("Password", validators=[Required()])
    remember_me = BooleanField("Stay logged in")
    submit = SubmitField("Log In")

class RegistrationForm(FlaskForm):
    email = StringField("Email", validators=[Required(), Email(), Length(1, 64)])
    username = StringField("User name", validators=[Required(), Length(1, 64)])
    password = PasswordField("Password", validators=[
        Required(), EqualTo("password2", message="Passwords must match")
    ])
    password2 = PasswordField("Confirm password", validators=[Required()])

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise AttributeError("Email already registered.")
    
    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise AttributeError("Username already in use.")