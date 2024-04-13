from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Email, Length, DataRequired


class RegistrationForm(FlaskForm):
    fullname = StringField(
        "ФИО: ",
        validators=[DataRequired("Поле ФИО не может быть пустым")]
    )
    email = StringField(
        "Email: ",
        validators=[
            Email("Не корректно заполнен Email адрес"),
            DataRequired("Поле Email не может быть пустым")
        ]
    )
    password = PasswordField(
        "Пароль: ",
        validators=[
            Length(min=8, max=12, message="Пароль должен иметь длинну от 8 до 12 символов"),
            DataRequired("Поле Пароль не может быть пустым")
        ]
    )
    submit = SubmitField("Регистрация")


class AuthForm(FlaskForm):
    email = StringField(
        "Email: ",
        validators=[
            Email("Не корректно заполнен Email адрес"),
            DataRequired("Поле Email не может быть пустым")
        ]
    )
    password = PasswordField(
        "Пароль: ",
        validators=[
            Length(min=8, max=12, message="Пароль должен иметь длинну от 8 до 12 символов"),
            DataRequired("Поле Пароль не может быть пустым")
        ]
    )
    submit = SubmitField("Вход")
