__all__ = [
    "auth_route",
    "auth_models",
    "registration_route",
    "activities_models"
]

from apps.auth.views import auth as auth_route
from apps.auth.views import registration as registration_route
from apps.auth import models as auth_models
from apps.activities import models as activities_models
from apps.activities.views import activities as activities_route
