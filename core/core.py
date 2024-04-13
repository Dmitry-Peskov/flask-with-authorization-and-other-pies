from flask_alembic import Alembic
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from sqlalchemy.orm import DeclarativeBase


class BaseModel(DeclarativeBase):
    pass


database = SQLAlchemy(model_class=BaseModel)
migrations = Alembic()
login_manager = LoginManager()
login_manager.login_view = "auth.auth_get"
login_manager.login_message = u"Авторизуйтесь в системе, чтобы продолжить"
login_manager.login_message_category = "info"
