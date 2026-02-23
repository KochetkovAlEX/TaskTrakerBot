from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

from database.crud import create_user

router = Router()


@router.message(CommandStart())
async def greeting(message: Message) -> None:
    """Функция для приветствия"""
    await create_user(message.from_user.id)
    await message.answer(f"Hello, {message.from_user.first_name}")


@router.message(Command("help"))
async def show_help_message(message: Message) -> None:
    """Функция для показа списка команд"""
    await message.answer(
        "<b>Commands</b>\n/add - <b>Добавить привычку</b>\n"
        + "/setup - <b>Изменить время оповещений</b>"
        + "\n/show_habbits - <b>Список привычек</b>",
        parse_mode="HTML",
    )
