from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from keyboards.inline import inline_difficulty_buttons
from states.task import TaskState

router = Router()


# @router.message(Command("add"))
# async def add_habbit(message: Message, command: Command) -> None:
#     if command.args:
#         await message.answer(f"{command.args}")

#     else:
#         await message.answer("Пожалуйста, напишите привычку для отслеживания")


@router.message(Command("setup"))
async def setup_notion_time(message: Message) -> None:
    pass


@router.message(Command("add"))
async def add_habbit(message: Message, state: FSMContext) -> None:
    await state.set_state(TaskState.title)
    await message.answer("Напишите название привычки")


@router.message(TaskState.title)
async def add_difficult_after_title(message: Message, state: FSMContext) -> None:
    await state.update_data(title=message.text)
    await state.set_state(TaskState.difficulty)
    await message.answer("Выберите сложность", reply_markup=inline_difficulty_buttons)
