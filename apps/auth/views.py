from flask import Blueprint, render_template, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from .forms import AuthForm, RegistrationForm
from .controler import create_user_from_db


registration = Blueprint("registration", __name__, template_folder="templates", static_folder="static")
auth = Blueprint("auth", __name__, template_folder="templates", static_folder="static")


@registration.route("/", methods=["GET", "POST"])
def registry():
    form = RegistrationForm()
    if form.validate_on_submit():
        try:
            hashed_password = generate_password_hash(form.password.data)
            create_user_from_db(form.fullname.data, form.email.data, hashed_password)
            flash("Регистрация прошла успешно", "info")
        except Exception:
            flash("При добавлении пользователя в БД произошла ошибка", "error")
    return render_template("registration.html", title="Регистрация", form=form)


@auth.route("/", methods=["GET", "POST"])
def auth_get():
    if request.method == "GET":
        form = AuthForm()
        return render_template("auth.html", title="Авторизация", form=form)
