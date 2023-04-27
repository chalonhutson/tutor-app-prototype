from flask import Blueprint, render_template

from .forms import LoginForm

home = Blueprint("home", __name__)

@home.route("/")
def homepage():
    return render_template("homepage.html")

@home.route("/login")
def login():
    form = LoginForm()
    return render_template("login.html", form=form)

@home.route("/contact-us")
def contact_us():
    return render_template("contact-us.html")

@home.route("/who-we-are")
def who_we_are():
    return render_template("who-we-are.html")

@home.route("/what-we-do")
def what_we_do():
    return render_template("what-we-do.html")