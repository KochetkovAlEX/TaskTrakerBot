import asyncio
import logging
import os

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from dotenv import load_dotenv

from routers import habbit_router

load_dotenv()
TOKEN = os.getenv("TOKEN")

dp = Dispatcher()


@dp.message(CommandStart())
async def greeting(message: Message) -> None:
    """Функция для приветствия"""
    await message.answer(f"Hello, {message.from_user.first_name}")


async def main() -> None:
    """Функция запуска основной программы"""
    bot = Bot(
        token=TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )

    dp.include_router(habbit_router.router)
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
