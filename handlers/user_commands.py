from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

from keyboards import inline

router = Router()


@router.message(CommandStart())
async def greeting(message: Message) -> None:
    """Функция для приветствия"""
    await message.answer(f"Hello, {message.from_user.first_name}")


@router.message(Command("help"))
async def show_help_message(message: Message) -> None:
    await message.answer(
        "**Commands**\n/add \- **Добавить привычку** \n/setup \- **Изменить время оповещений**\n",
        parse_mode="MarkdownV2",
    )


@router.message(Command("test"))
async def test_function(message: Message) -> None:
    await message.answer("Кнопки", reply_markup=inline.inline_difficulty_buttons)

    await message.edit_text(
        "новый текст", reply_markup=inline.inline_difficulty_buttons
    )
