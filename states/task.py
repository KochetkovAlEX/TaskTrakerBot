from aiogram.fsm.state import State, StatesGroup


class TaskState(StatesGroup):
    """Класс состояния для обработки и сохранения формы"""

    title: State = State()
    difficulty: State = State()
    priority: State = State()


class UpdateTaskState(StatesGroup):
    """Класс состояния для обновления задачи"""

    title: State = State()
    difficulty: State = State()
    priority: State = State()
