import os

from aiogram.filters import Filter
from aiogram.types import Message
from dotenv import load_dotenv

load_dotenv()
ADMIN_ID = int(os.getenv("ADMIN", "0"))


class Admin(Filter):
    def __init__(self) -> None:
        self.admin_id = ADMIN_ID

    async def __call__(self, message: Message) -> bool:
        return message.from_user.id == self.admin_id
