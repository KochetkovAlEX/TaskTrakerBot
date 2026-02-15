from datetime import datetime

from sqlalchemy import BigInteger, Boolean, DateTime, ForeignKey, String, func
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

engine = create_async_engine(url="sqlite+aiosqlite:///db.sqlite3", echo=True)

async_session = async_sessionmaker(engine)


class Base(
    AsyncAttrs, DeclarativeBase
):  # Асинхронная сессия и декларативный стиль для описания таблиц, колонок и отношений. Это родительский класс, этот класс нужен всегда
    pass


class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id: Mapped[int] = mapped_column(BigInteger)
    notion_time: Mapped[str] = mapped_column(String, default="20:00")
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())


class Task(Base):
    __tablename__ = "tasks"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String)
    description: Mapped[str] = mapped_column(String)
    level: Mapped[str] = mapped_column(String)
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())


class CompletedTask(Base):
    __tablename__ = "completed_task"
    id: Mapped[int] = mapped_column(primary_key=True)
    task_id: Mapped[int] = mapped_column(ForeignKey("tasks.id"))


# async def async_main():
#     async with engine.begin() as conn:
#         await conn.run_sync(Base.metadata.create_all)
