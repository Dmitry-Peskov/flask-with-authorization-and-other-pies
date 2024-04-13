from .models import Activity, WorkDone
from core import database


def get_activities_id_and_value() -> list[tuple[int, str]]:
    result = []
    activities = Activity.query.all()
    for act in activities:
        act_tuple = (act.id, act.name)
        result.append(act_tuple)
    return result


def write_active_to_db(user_email: str, activity_type: int, duration: int, url_in: str | None, description: str):
    act = WorkDone(
        user_email=user_email,
        activity_id=int(activity_type),
        duration_in_minutes=int(duration),
        url=None if url_in is None or url_in == "" else url_in,
        description=description
        )
    database.session.add(act)
    database.session.commit()
