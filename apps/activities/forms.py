from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField, URLField, IntegerField, TextAreaField
from wtforms.validators import DataRequired, NumberRange, URL
from .controler import get_activities_id_and_value


class AddActivitiesForm(FlaskForm):
    type = SelectField(
        "Тип работ: ",
        choices=None,
        validators=[DataRequired("Необходимо выбрать тип проделанной работы")]
    )
    duration = IntegerField(
        "Затрачено минут: ",
        validators=[
            NumberRange(min=1, max=90, message='Время должно быть в диапазоне 1-90 минут'),
            DataRequired("Необходимо указать затраченное время")
        ]
    )
    url = URLField(
        "Ссылка: ",
        validators=[
            URL(message="Введённое значение не являеться корректной ссылкой"),
        ]
    )
    description = TextAreaField(
        "Описание: ",
        validators=[DataRequired("Поле Описание, обязательно для заполнения")]
    )
    submit = SubmitField("Зафиксировать")
