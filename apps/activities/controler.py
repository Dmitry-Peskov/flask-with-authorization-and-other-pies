from .models import Activity


def get_activities_id_and_value() -> list[tuple[int, str]]:
    result = []
    activities = Activity.query.all()
    for act in activities:
        act_tuple = (act.id, act.name)
        result.append(act_tuple)
    return result
