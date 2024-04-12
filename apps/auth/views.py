from flask import Blueprint, render_template, request
from werkzeug.security import generate_password_hash, check_password_hash
from .forms import AuthForm, RegistrationForm


registration = Blueprint("registration", __name__, template_folder="templates", static_folder="static")
auth = Blueprint("auth", __name__, template_folder="templates", static_folder="static")


@registration.route("/", methods=["GET", "POST"])
def registry():
    if request.method == "GET":
        form = RegistrationForm()
        return render_template("registration.html", title="Регистрация", form=form)
    else:
        pass


@auth.route("/", methods=["GET", "POST"])
def auth_get():
    if request.method == "GET":
        form = AuthForm()
        return render_template("auth.html", title="Авторизация", form=form)
