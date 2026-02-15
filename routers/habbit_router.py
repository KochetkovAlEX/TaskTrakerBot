from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router()


@router.message(Command("add"))
async def add_habbit(message: Message, command: Command) -> None:
    if command.args:
        await message.answer(f"{command.args}")

    else:
        await message.answer("Пожалуйста, напишите привычку для отслеживания")
