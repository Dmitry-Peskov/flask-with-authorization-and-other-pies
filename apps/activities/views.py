from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import login_user, login_required
from .forms import AddActivitiesForm
from .controler import get_activities_id_and_value

activities = Blueprint("activities", __name__, template_folder="templates", static_folder="static")


@activities.route("/", methods=["GET", "POST"])
@login_required
def activities_page():
    form = AddActivitiesForm()
    form.type.choices = get_activities_id_and_value()
    if form.validate_on_submit():
        pass
    else:
        return render_template("activities.html", title="Добавить активность", form=form)
