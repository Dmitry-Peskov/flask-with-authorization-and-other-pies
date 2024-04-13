from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import login_required, current_user

from .controler import get_activities_id_and_value, write_active_to_db
from .forms import AddActivitiesForm

activities = Blueprint("activities", __name__, template_folder="templates", static_folder="static")


@activities.route("/", methods=["GET", "POST"])
@login_required
def activities_page():
    form = AddActivitiesForm()
    form.type.choices = get_activities_id_and_value()
    if form.validate_on_submit():
        try:
            write_active_to_db(current_user.get_id(), form.type.data, form.duration.data, form.url.data, form.description.data)
            flash("Активность добавлена", "success")
            return redirect(url_for('activities.activities_page'))
        except Exception as _:
            flash("Возникла ошибка при добавлении записи в БД", "error")
    else:
        for t, e in form.errors.items():
            if t != "csrf_token":
                flash(*e, "error")
        return render_template("activities.html", title="Добавить активность", form=form)
