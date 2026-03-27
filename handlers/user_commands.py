from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from aiogram.enums.parse_mode import ParseMode
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
        "*Команды*"
        + "\n/add - *Добавить привычку*"
        + "\n/setup - *Изменить время оповещений*"
        + "\n/show - *Список привычек*"
        + "\n/update <название_привычки> - *Обновить привычку*"
        + "\n/delete <название_привычки> - *Удаление привычки*",
        parse_mode=ParseMode.MARKDOWN,
    )
