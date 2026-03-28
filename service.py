from config.const import DIFFICULTY_DICT, PRIORITY_DICT
from database.model import Task


def create_answer_message(tasks: list[Task]) -> str:
    result = "<b>Активные привычки</b>\n"
    for task in tasks:
        result += f"{PRIORITY_DICT[task.priority]} {task.title} - {task.created_at} {DIFFICULTY_DICT[task.difficulty]}\n"
    result += "\n\nУровень сложности:\n"
    for key, value in DIFFICULTY_DICT.items():
        result += f"{key} - {value}\n"

    result += "\n\nПриоритет:\n"
    for key, value in PRIORITY_DICT.items():
        result += f"{key} - {value}\n"
    return result
