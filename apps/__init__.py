__all__ = [
    "auth_route",
    "auth_models"
]

from apps.auth.views import auth as auth_route
from apps.auth import models as auth_models
