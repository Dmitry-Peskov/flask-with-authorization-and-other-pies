# встроенные пакеты
from __future__ import annotations
from datetime import datetime
from typing import List, Optional, TYPE_CHECKING
# сторонние зависимости
from sqlalchemy import String, UniqueConstraint, Boolean, func, DateTime, Integer, ForeignKey, SmallInteger
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import expression
# собственные зависимости
from core import database
if TYPE_CHECKING:
    from apps.auth.models import User


class Activity(database.Model):
    """
    Модель описывающая Типы активностей, которые может фиксировать пользователь.
    Подразумевается что на портале в списке доступных для выбора активностей будут
    только те, которые имеют состояние enabled=True.
    """
    __tablename__ = "Activities"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        unique=True,
        autoincrement=True,
        index=True,
        comment="ID записи, первичный ключ, автоинкремент"
    )
    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        unique=True,
        comment="Название активности"
    )
    enabled: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        server_default=expression.true(),
        comment="Состояние активности, доступна ли она для выбора на портале"
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        server_default=func.now(),
        comment="Дата и время создания активности"
    )
    # Устанавливаем связь с журналом зафиксированных пользователем работам
    # Один ко многим (может быть масса работ с конкретным типом, но у конкретной работы может быть только один тип)
    works_done: Mapped[List[WorkDone]] = relationship()

    # Добавляем ограничение, что в таблице может быть только одна активность с заданным именем
    __table_args__ = (
        UniqueConstraint("name", name="activity_name_key"),
    )

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.name=}, {self.id=}, {self.enabled=})"


class WorkDone(database.Model):
    """
    Модель описывающая совершенную Пользователем портала работу.
    Подразумевается, что авторизованный пользователь, заполнил форму на портале
    и информация из этой формы была сохранена в БД
    """
    __tablename__ = "WorksDone"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        unique=True,
        autoincrement=True,
        index=True,
        comment="ID записи, первичный ключ, автоинкремент"
    )
    # Устанавливаем связь с User по внешнему ключу email
    user_email: Mapped[str] = mapped_column(
        ForeignKey("Users.email"),
        nullable=False,
        comment="Корпоративный email Пользователя, зафиксировавшего данную активность"
    )
    user: Mapped[User] = relationship(back_populates="works_done")

    completed_in: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        server_default=func.now(),
        comment="Дата и время выполнения / фиксации работы на портале"
    )
    # Устанавливаем связь с Activity по внешнему ключу id
    activity_id: Mapped[int] = mapped_column(
        ForeignKey("Activities.id"),
        nullable=False,
        comment="ID типа совершенной / зафиксированной работы"
    )
    activity: Mapped[Activity] = relationship(back_populates="works_done")

    duration_in_minutes: Mapped[int] = mapped_column(
        SmallInteger,
        nullable=False,
        comment="Продолжительность зафиксированной работы в минутах"
    )
    url: Mapped[Optional[str]] = mapped_column(
        String(500),
        nullable=True,
        comment="Ссылка на задачу / материал в рамках которого велась работа (опционально, не обязательное поле)"
    )
    description: Mapped[str] = mapped_column(
        String,
        nullable=False,
        comment="Описание проделанной работы"
    )

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.user_email=}, {self.duration_in_minutes=}, {self.completed_in=})"
