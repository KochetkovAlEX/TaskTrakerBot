from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import CallbackQuery, Message

from config import task_difficulties, task_priority
from keyboards.inline import inline_priority_buttons
from states.task import TaskState

router = Router()


@router.callback_query(F.data == "button_cancel")
async def cancel_function(callback: CallbackQuery, state: FSMContext) -> None:
    await callback.answer()
    await callback.message.answer("Отмена добавления задачи")
    await state.clear()


@router.callback_query(F.data.contains("level_"))
async def set_difficulty(callback: CallbackQuery, state: FSMContext) -> None:
    await state.update_data(difficulty=callback.data.split("_")[1])
    await state.set_state(TaskState.priority)
    await callback.message.answer(
        "Выберите приоритет", reply_markup=inline_priority_buttons
    )


@router.callback_query(F.data.contains("priority_"))
async def set_priority(callback: CallbackQuery, state: FSMContext) -> None:
    await state.update_data(priority=callback.data.split("_")[1])
    data = await state.get_data()
    print(data)
    await state.clear()
