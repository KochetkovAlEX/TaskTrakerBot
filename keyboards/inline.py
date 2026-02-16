from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config.task_difficulties import TaskDifficulty

inline_difficulty_buttons = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text=f"{TaskDifficulty.EASY.value}", callback_data="pass"
            ),
            InlineKeyboardButton(
                text=f"{TaskDifficulty.MEDIUM.value}", callback_data="pass"
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"{TaskDifficulty.HARD.value}", callback_data="pass"
            ),
            InlineKeyboardButton(
                text=f"{TaskDifficulty.EXPERT.value}", callback_data="pass"
            ),
        ],
        [InlineKeyboardButton(text="Назад", callback_data="pass")],
    ]
)
