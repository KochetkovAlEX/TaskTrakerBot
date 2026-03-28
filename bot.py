import asyncio
import os

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.storage.memory import MemoryStorage
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from dotenv import load_dotenv

from admin_router import commands
from handlers import callback, habits, user_commands

load_dotenv()
TOKEN = os.getenv("TOKEN")

dp = Dispatcher(storage=MemoryStorage())
job_store = {"default": SQLAlchemyJobStore("sqlite+aiosqlite:///db.sqlite3")}
scheduler = AsyncIOScheduler(job_store=job_store)


async def setup(bot: Bot) -> None:
    if not scheduler.running:
        scheduler.start()
    print("Scheduler start working")


async def main() -> None:
    """Функция запуска основной программы"""
    bot = Bot(
        token=TOKEN,
        default=DefaultBotProperties(parse_mode="MarkdownV2"),
    )
    # запуск функции при запуске
    dp.startup.register(setup)

    dp.include_routers(
        commands.admin, habits.router, user_commands.router, callback.router
    )
    # сообщения, которые были отправлены боту, когда он был выключен, при включении будут игнорироваться
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    # logging.basicConfig(level=logging.INFO)
    try:
        print("bot start working")
        asyncio.run(main())
    except KeyboardInterrupt:
        print("bot stop working")
