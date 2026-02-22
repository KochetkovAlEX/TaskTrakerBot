from task_difficulties import TaskDifficulty
from task_priority import TaskPriority

# ----- Dicts for notification message -----

PRIORITY_DICT: dict[str, str] = {
    TaskPriority.LOW.value: "⏹️",
    TaskPriority.MEDIUM.value: "🔼",
    TaskPriority.HIGHT.value: "⏫",
}


DIFICULTY_DICT: dict[str, str] = {
    TaskDifficulty.EASY.value: "🟢",
    TaskDifficulty.MEDIUM.value: "🟠",
    TaskDifficulty.HARD.value: "🔴",
    TaskDifficulty.EXPERT.value: "🟣",
}
