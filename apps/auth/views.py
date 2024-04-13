from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import login_user
from werkzeug.security import generate_password_hash, check_password_hash
from .forms import AuthForm, RegistrationForm
from .controler import create_user_from_db, get_user_by_email
from .userlogin import UserLogin
from core import login_manager


registration = Blueprint("registration", __name__, template_folder="templates", static_folder="static")
auth = Blueprint("auth", __name__, template_folder="templates", static_folder="static")


@login_manager.user_loader
def load_user(user_id: str):
    return UserLogin().from_db(user_id)


@registration.route("/", methods=["GET", "POST"])
def registry():
    form = RegistrationForm()
    if form.validate_on_submit():
        try:
            hashed_password = generate_password_hash(form.password.data)
            create_user_from_db(form.fullname.data, form.email.data, hashed_password)
            flash("Регистрация прошла успешно", "success")
            return redirect(url_for('registration'))
        except Exception:
            flash("При добавлении пользователя в БД произошла ошибка", "error")
    else:
        for t, e in form.errors.items():
            if t != "csrf_token":
                flash(*e, "error")
        return render_template("registration.html", title="Регистрация", form=form)


@auth.route("/", methods=["GET", "POST"])
def auth_get():
    form = AuthForm()
    if form.validate_on_submit():
        user = get_user_by_email(form.email.data)
        if user and check_password_hash(user.hashed_password, form.password.data):
            ulogin = UserLogin().create(user)
            login_user(ulogin)
            return redirect(url_for("index"))  # TODO реализовать корректную переадресацию на существующую страницу
        flash("Неверная пара логин/пароль", "error")
    return render_template("auth.html", title="Авторизация", form=form)
