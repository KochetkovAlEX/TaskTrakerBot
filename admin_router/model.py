import os

from aiogram.filters import Filter
from aiogram.types import Message
from dotenv import load_dotenv

load_dotenv()
ADMIN_ID = int(os.getenv("ADMIN", "0"))


class Admin(Filter):
    """Класс администратора"""

    def __init__(self) -> None:
        """Метод инициализации класса"""
        self.admin_id = ADMIN_ID

    async def __call__(self, message: Message) -> bool:
        """Метод проверки пользователя на наличие прав администратора"""
        return message.from_user.id == self.admin_id
