from sqlalchemy import BigInteger, ForeignKey, String
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
    tg_id = mapped_column(BigInteger)


class Task(Base):
    __tablename__ = "tasks"
    id: Mapped[int] = mapped_column(primary_key=True)


async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
