import asyncio
import logging
import os

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from dotenv import load_dotenv

from admin_router import commands
from handlers import habits, user_commands

load_dotenv()
TOKEN = os.getenv("TOKEN")

dp = Dispatcher()


async def main() -> None:
    """Функция запуска основной программы"""
    bot = Bot(
        token=TOKEN,
        default=DefaultBotProperties(parse_mode="MarkdownV2"),
    )

    dp.include_routers(commands.admin, habits.router, user_commands.router)
    # сообщения, которые были отправлены боту, когда он был выключен, при включении будут игнорироваться
    await bot.delete_webhook(drop_pending_updates=True)
    # запуск бота
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        print("bot start working")
        asyncio.run(main())
    except KeyboardInterrupt as e:
        print("bot stop working")
