from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from database.crud import get_tasks
from keyboards.inline import inline_difficulty_buttons
from service import create_anser_message
from states.task import TaskState

router = Router()


# @router.message(Command("add"))
# async def add_habbit(message: Message, command: Command) -> None:
#     if command.args:
#         await message.answer(f"{command.args}")


@router.message(Command("setup"))
async def setup_notion_time(message: Message) -> None:
    """Функция для изменения времени оповещения"""
    pass


@router.message(Command("add"))
async def add_habbit(message: Message, state: FSMContext) -> None:
    """Функция добавления задачи"""
    await state.set_state(TaskState.title)
    await message.answer("Напишите название привычки")


@router.message(TaskState.title)
async def add_difficult_level(message: Message, state: FSMContext) -> None:
    """Функция для ввода названия привычки"""
    await state.update_data(title=message.text)
    await state.set_state(TaskState.difficulty)
    await message.answer(
        "Выберите сложность",
        reply_markup=inline_difficulty_buttons,
    )


@router.message(Command("show_habbits"))
async def show_active_tasks(message: Message) -> None:
    """Функция вывода списка отслеживаемых привычек"""
    tasks = await get_tasks(message.from_user.id)
    if not tasks:
        message.answer(
            "Список задач пуст\n Вы можете добавить задачу, написав `/add`",
            parse_mode="HTML",
        )

    tasks_message = create_anser_message(tasks)
    await message.answer(tasks_message, parse_mode="HTML")


@router.message(Command("update_task"))
async def update_active_task(message: Message) -> None:
    pass


@router.message(Comand("delete_task"))
async def delete_active_task(message: Message) -> None:
    pass
