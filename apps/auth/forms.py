from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Email, Length, DataRequired


class RegistrationForm(FlaskForm):
    fullname = StringField("ФИО: ", validators=[DataRequired()])
    email = StringField("Email: ", validators=[Email(), DataRequired()])
    password = PasswordField("Пароль: ", validators=[Length(min=8, max=12), DataRequired()])
    submit = SubmitField("Регистрация")


class AuthForm(FlaskForm):
    email = StringField("Email: ", validators=[Email(), DataRequired()])
    password = PasswordField("Пароль: ", validators=[Length(min=8, max=12), DataRequired()])
    submit = SubmitField("Вход")
