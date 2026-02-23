from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from database.crud import add_task
from keyboards.inline import inline_priority_buttons
from states.task import TaskState

router = Router()


@router.callback_query(F.data == "button_cancel")
async def cancel_function(callback: CallbackQuery, state: FSMContext) -> None:
    """Функция для очистки состояния"""
    await callback.answer()
    await callback.message.answer("Отмена добавления задачи")
    await state.clear()


@router.callback_query(F.data.contains("level_"))
async def set_difficulty(callback: CallbackQuery, state: FSMContext) -> None:
    """Функция для выбора уровня сложности привычки"""
    await state.update_data(difficulty=callback.data.split("_")[1])
    await state.set_state(TaskState.priority)
    await callback.message.answer(
        "Выберите приоритет", reply_markup=inline_priority_buttons
    )


@router.callback_query(F.data.contains("priority_"))
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
