from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config.task_difficulties import TaskDifficulty
from config.task_priority import TaskPriority

# ----- inline buttons for creating task -----
inline_difficulty_buttons = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text=f"{TaskDifficulty.EASY.value}",
                callback_data="level_" + f"{TaskDifficulty.EASY.value}",
            ),
            InlineKeyboardButton(
                text=f"{TaskDifficulty.MEDIUM.value}",
                callback_data="level_" + f"{TaskDifficulty.MEDIUM.value}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"{TaskDifficulty.HARD.value}",
                callback_data="level_" + f"{TaskDifficulty.HARD.value}",
            ),
            InlineKeyboardButton(
                text=f"{TaskDifficulty.EXPERT.value}",
                callback_data="level_" + f"{TaskDifficulty.EXPERT.value}",
            ),
        ],
        [InlineKeyboardButton(text="Отмена", callback_data="button_cancel")],
    ]
)


inline_priority_buttons = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text=f"{TaskPriority.LOW.value}",
                callback_data="priority_" + f"{TaskPriority.LOW.value}",
            ),
            InlineKeyboardButton(
                text=f"{TaskDifficulty.MEDIUM.value}",
                callback_data="priority_" + f"{TaskPriority.MEDIUM.value}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"{TaskDifficulty.HARD.value}",
                callback_data="priority_" + f"{TaskPriority.HIGHT.value}",
            )
        ],
        [InlineKeyboardButton(text="Отмена", callback_data="button_cancel")],
    ]
)


# ----- buttons for updating task -----
# ON FUTURE
"""inline_update_buttons = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Название",
                callback_data="title_update",
            ),
        ],
        [
            InlineKeyboardButton(
                text="Приоритет",
                callback_data="priority_update",
            )
        ],
        [
            InlineKeyboardButton(
                text="Сложность",
                callback_data="level_update"
            )
        ],
        [
            InlineKeyboardButton(text="Отмена", callback_data="button_cancel")
        ],
    ]
)"""
