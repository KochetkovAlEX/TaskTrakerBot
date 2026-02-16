from datetime import datetime

from sqlalchemy import BigInteger, DateTime, ForeignKey, String, func
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

engine = create_async_engine(url="sqlite+aiosqlite:///db.sqlite3", echo=True)

async_session = async_sessionmaker(engine)


class Base(
    AsyncAttrs, DeclarativeBase
):  # Асинхронная сессия и декларативный стиль для описания таблиц, колонок и отношений. Это родительский класс, этот класс нужен всегда
    pass


class User(Base):
    """Модель пользователя"""

    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id: Mapped[int] = mapped_column(BigInteger)
    notion_time: Mapped[str] = mapped_column(String, default="20:00")
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())


class Task(Base):
    """Модель отслеживаемых задач"""

    __tablename__ = "tasks"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String)
    description: Mapped[str] = mapped_column(String)
    difficulty: Mapped[str] = mapped_column(String)
    priority: Mapped[str] = mapped_column(String)
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())


class CompletedTask(Base):
    """Модель завершённых задач"""

    __tablename__ = "completed_task"
    id: Mapped[int] = mapped_column(primary_key=True)
    task_id: Mapped[int] = mapped_column(ForeignKey("tasks.id"))
    completed_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
