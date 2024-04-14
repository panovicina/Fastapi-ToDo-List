from typing import List, Optional

from sqlalchemy import Boolean, ForeignKey, String, Text
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
    relationship,
)


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(30), nullable=False)
    password: Mapped[str] = mapped_column(String(30), nullable=False)
    todo_lists: Mapped[List["TODOList"]] = relationship(
        back_populates="user", cascade="all, delete-orphan"
    )


class TODOList(Base):
    __tablename__ = "todo_lists"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30), nullable=False)
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship(back_populates="todo_lists")
    tasks: Mapped[List["Tasks"]] = relationship(
        back_populates="list", cascade="all, delete-orphan"
    )


class Tasks(Base):
    __tablename__ = "tasks"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    is_done: Mapped[bool] = mapped_column(Boolean, default=False)
    list_id: Mapped[int] = mapped_column(ForeignKey("todo_lists.id"))
    list: Mapped["TODOList"] = relationship(back_populates="tasks")
