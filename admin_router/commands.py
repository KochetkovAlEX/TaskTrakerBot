from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from database import crud
from handlers import user_commands

from .model import Admin

admin = Router()


@admin.message(Admin(), Command("help"))
async def admin_help(message: Message) -> None:
    await user_commands.show_help_message(message)
    await message.answer(
        "**Admin Commands**\n/reload \- **Drop and Create Database**",
        parse_mode="MarkdownV2",
    )


@admin.message(Admin(), Command("reload"))
async def admin_reload_database(message: Message) -> None:
    await crud.reload_database()
    await message.answer("Database reloaded and recreated")
