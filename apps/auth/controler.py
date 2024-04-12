from .models import User
from core import database


def create_user_from_db(fullname: str, email: str, hashed_password: str):
    """Добавить нового пользователя в БД"""
    user = User(fullname=fullname, email=email, hashed_password=hashed_password)
    database.session.add(user)
    database.session.commit()


def get_user_by_email(email: str) -> User:
    """Получить пользователя из БД по email"""
    return User.query.get(email)

