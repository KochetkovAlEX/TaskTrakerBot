from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup


class TaskState(StatesGroup):
    """Класс состояния для обработки и сохранения формы"""

    title: State = State()
    difficulty: State = State()
    priority: State = State()
