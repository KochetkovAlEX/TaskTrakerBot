from datetime import datetime
from functools import wraps
from zoneinfo import ZoneInfo

import aiofiles

moscow = ZoneInfo("Europe/Moscow")


def logger_function(func):
    """
    Декоратор для логгирования функций. Все логи сохраняются в log.txt
    """

    @wraps(func)
    async def wrapper(*args, **kwargs):
        print(111)
        try:
            result = await func(*args, **kwargs)
            async with aiofiles.open("log.txt", "a", encoding="utf-8") as f:
                await f.write(
                    f"{datetime.now(moscow).strftime('%Y-%m-%d %H:%M:%S')} - {func.__name__} - {repr(result)}\n"
                )

            return result
        except Exception as e:
            async with aiofiles.open("log.txt", "a", encoding="utf-8") as f:
                await f.write(
                    f"{datetime.now(moscow).strftime('%Y-%m-%d %H:%M:%S')} - {func.__name__} - {str(e)}\n"
                )
            raise  # переброс на другие исключения

    return wrapper
