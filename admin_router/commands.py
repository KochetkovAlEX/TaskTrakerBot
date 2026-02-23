from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from database import crud
from handlers import user_commands

from .model import Admin

admin = Router()


@admin.message(Admin(), Command("help"))
async def admin_help(message: Message) -> None:
    """Функция вызова списка команд администратора. Только для админов"""
    await user_commands.show_help_message(message)
    await message.answer(
        "<b>Admin Commands</b>\n/reload - <b>Drop and Create Database</b>",
        parse_mode="HTML",
    )


@admin.message(Admin(), Command("reload"))
async def admin_reload_database(message: Message) -> None:
    """Функция пересоздания базы данных"""
    await crud.reload_database()
    await message.answer(
        "<b>Database reloaded and recreated</b>",
        parse_mode="HTML"
    )
