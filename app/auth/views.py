from flask import render_template, redirect, url_for, request
from flask_login import login_required, login_user, logout_user, current_user
from . import auth
from .. import db
from .forms import LoginForm, RegistrationForm
from ..models import User

@auth.route("/login")
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            return redirect(request.args.get("next") or url_for("main.index"))

    return render_template("auth/login.html", form=form)

@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))

@auth.route("/register")
def register_user():

    return render_template("auth/register_user.html")