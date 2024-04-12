from flask_alembic import Alembic
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase


class BaseModel(DeclarativeBase):
    pass


database = SQLAlchemy(model_class=BaseModel)
migrations = Alembic()
