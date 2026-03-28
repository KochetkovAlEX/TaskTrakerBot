from aiogram import Router
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from config.const import DIFFICULTY_DICT, PRIORITY_DICT
from database.crud import get_task, get_tasks, delete_task
from keyboards.inline import inline_difficulty_buttons, inline_update_buttons
from service import create_answer_message
from states.task import TaskState

router = Router()


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


@router.message(Command("show"))
async def show_active_tasks(message: Message) -> None:
    """Функция вывода списка отслеживаемых привычек"""
    tasks = await get_tasks(message.from_user.id)
    if not tasks:
        await message.answer(
            "Список задач пуст\nВы можете добавить новую задачу, написав `/add`",
            parse_mode=ParseMode.MARKDOWN
        )
        return

    tasks_message = create_answer_message(tasks)
    await message.answer(tasks_message, parse_mode="HTML")


@router.message(Command("delete"))
async def delete_active_task(message: Message, command: Command) -> None:
    task_to_delete = command.args.capitalize()

    if not task_to_delete:
        await message.answer("Сообщение не должно быть пустым")
        return

    task = await get_task(message.from_user.id, task_to_delete)
    if not task:
        await message.answer("Такой задачи не существует")
        return

    await delete_task(task.id)
    await message.answer("Привычка успешно удалена ✅")


@router.message(Command("update"))
async def update_active_task(
        message: Message, command: Command, state: FSMContext
) -> None:
    if not command.args:
        await message.answer("Укажите название задачи")
        return

    task = await get_task(message.from_user.id, command.args.capitalize())

    if not task:
        await message.answer("Такой задачи нет")
        return

    await state.update_data(
        task_id=task.id,
        old_title=task.title,
        old_difficulty=task.difficulty,
        old_priority=task.priority,
        user_id=task.user_id,
    )

    await message.answer(
        f"Найдена задача: {PRIORITY_DICT[task.priority]} {task.title} {DIFFICULTY_DICT[task.difficulty]}",
        parse_mode="HTML",
    )

    await message.answer("Что вы хотите обновить?", reply_markup=inline_update_buttons)
