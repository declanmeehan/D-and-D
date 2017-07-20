from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import Required, Email, Length, EqualTo

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[Required()])
    password = PasswordField("Password", validators=[Required()])

    def validate_password(self, field):
        