from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from database.crud import add_task, update_task
from keyboards.inline import inline_difficulty_buttons, inline_priority_buttons
from states.task import TaskState, UpdateTaskState

router = Router()


# ==== Create Task ====
@router.callback_query(F.data == "button_cancel")
async def cancel_function(callback: CallbackQuery, state: FSMContext) -> None:
    """Функция для очистки состояния"""
    await callback.answer()
    await callback.message.answer("Отмена добавления задачи")
    await state.clear()


@router.callback_query(F.data.contains("level_"), TaskState.difficulty)
async def set_difficulty(callback: CallbackQuery, state: FSMContext) -> None:
    """Функция для выбора уровня сложности привычки"""
    await state.update_data(difficulty=callback.data.split("_")[1])
    await state.set_state(TaskState.priority)
    await callback.message.answer(
        "Выберите приоритет", reply_markup=inline_priority_buttons
    )


@router.callback_query(F.data.contains("priority_"),  TaskState.priority)
async def set_priority(callback: CallbackQuery, state: FSMContext) -> None:
    """Функция для выбора приоритета привычки"""
    await state.update_data(priority=callback.data.split("_")[1])
    data = await state.get_data()
    await add_task(
        data["title"].capitalize(),
        data["difficulty"].capitalize(),
        data["priority"].capitalize(),
        callback.from_user.id,
    )
    await state.clear()
    await callback.message.answer("Привычка добавлена")


# ==== Update Task ====
@router.callback_query(F.data == "level_update")
async def update_difficulty_handler(callback: CallbackQuery, state: FSMContext) -> None:
    """Функция подготовки обновления сложности задачи"""
    await callback.answer()
    await state.set_state(UpdateTaskState.difficulty)
    await callback.message.answer(
        "Выберите новую сложность",
        reply_markup=inline_difficulty_buttons,
    )


@router.callback_query(F.data.contains("level_"), UpdateTaskState.difficulty)
async def confirm_difficulty_update(callback: CallbackQuery, state: FSMContext) -> None:
    """Функция обновления сложности задачи"""
    difficulty = callback.data.split("_")[1]
    data = await state.get_data()
    await update_task(data["task_id"], difficulty=difficulty.capitalize())
    await callback.answer()
    await callback.message.answer("Сложность обновлена ✅")
    await state.clear()


@router.callback_query(F.data == "priority_update")
async def update_priority_handler(callback: CallbackQuery, state: FSMContext) -> None:
    """Функция подготовки обновления сложности задачи"""
    await callback.answer()
    await state.set_state(UpdateTaskState.priority)
    await callback.message.answer(
        "Выберите новый приоритет",
        reply_markup=inline_priority_buttons,
    )


@router.callback_query(F.data.contains("priority_"), UpdateTaskState.priority)
async def confirm_priority_update(callback: CallbackQuery, state: FSMContext) -> None:
    """Функция обновления приоритета задачи"""
    priority = callback.data.split("_")[1]
    data = await state.get_data()
    await update_task(data["task_id"], priority=priority.capitalize())
    await callback.answer()
    await callback.message.answer("Приоритет обновлён ✅")
    await state.clear()


@router.callback_query(F.data == "title_update")
async def update_title_handler(callback: CallbackQuery, state: FSMContext) -> None:
    """Функция подготовки обновления сложности задачи"""
    await callback.answer()
    await state.set_state(UpdateTaskState.title)
    await callback.message.answer("Напишите новое название")


@router.message(UpdateTaskState.title)
async def confirm_update_title(message: Message, state: FSMContext) -> None:
    data = await state.get_data()
    await update_task(data["task_id"], title=message.text.capitalize())
    await message.answer("Название обновлено ✅")
    await state.clear()
