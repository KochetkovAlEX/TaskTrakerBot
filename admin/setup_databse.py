from aiogram import Router, F

from database.model import Base, engine

router = Router()


@router.message(F.text=)