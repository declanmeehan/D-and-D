from flask import render_template, redirect, url_for
from flask_login import login_required

@auth.route("/login")
def login():
    form = LoginForm()

    if form.validate_on_submit():
        

    return render_template("auth/login.html", form=form)