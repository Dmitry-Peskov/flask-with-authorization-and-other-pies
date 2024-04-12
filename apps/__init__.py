__all__ = [
    "auth_route",
    "auth_models",
    "registration_route"
]

from apps.auth.views import auth as auth_route
from apps.auth.views import registration as registration_route
from apps.auth import models as auth_models
