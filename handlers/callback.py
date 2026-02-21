from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import CallbackQuery, Message

from config import task_difficulties, task_priority


class TaskForm(StatesGroup):
    title: State = State()
    description: State = State()
    difficulty: State = State()
    priority: State = State()


router = Router()


@router.callback_query(F.data == "button_cancel")
async def cancel_function(callback: CallbackQuery) -> None:
    await callback.answer()
    await callback.message.answer("Вы нажали назад")


@router.callback_query()
@router.callback_query(F.data.contains("level_"))
async def f():
    pass
