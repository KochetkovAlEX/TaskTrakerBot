from .model import Base, engine


async def reload_database() -> None:
    async with engine.begin() as con:
        await con.run_sync(Base.metadata.drop_all)
        await con.run_sync(Base.metadata.create_all)
