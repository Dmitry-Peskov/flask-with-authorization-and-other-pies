from flask import Blueprint, render_template


registration = Blueprint("registration", __name__, template_folder="templates", static_folder="static")
auth = Blueprint("auth", __name__, template_folder="templates", static_folder="static")


@registration.route("/", methods=["GET"])
def registration_get():
    return render_template("registration.html", title="Регистрация")


@auth.route("/", methods=["GET"])
def auth_get():
    return render_template("auth.html", title="Авторизация")
