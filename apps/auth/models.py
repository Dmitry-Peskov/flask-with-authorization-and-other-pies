from __future__ import annotations

from datetime import datetime

from sqlalchemy import String, UniqueConstraint, Boolean, func, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import expression

from core import database


class User(database.Model):
    __tablename__ = "Users"

    email: Mapped[str] = mapped_column(
        String(100),
        primary_key=True,
        unique=True,
        index=True,
        nullable=False,
        comment="Корпоротивный email адрес пользователя по совместительству логин на портале"
    )
    fullname: Mapped[str] = mapped_column(
        String(150),
        nullable=False,
        comment="Полные ФИО пользователя"
    )
    hashed_password: Mapped[str] = mapped_column(
        String(300),
        nullable=False,
        comment="Хэш пароля пользователя"
    )
    active: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        server_default=expression.true(),
        comment="Отключен ли пользователь"
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        server_default=func.now(),
        comment="Дата и время создания пользователя"
    )

    __table_args__ = (UniqueConstraint("email", name="user_email_key"),)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.email=}, {self.fullname=}, {self.active=})"
