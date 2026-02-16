from .model import Base, engine


# ----- core database functions -----
async def reload_database() -> None:
    """Функция перезагрузки базы данных. Сначала полностью удаляет её, а потом создаёт заново"""
    async with engine.begin() as con:
        await con.run_sync(Base.metadata.drop_all)
        await con.run_sync(Base.metadata.create_all)


# ----- CRUD -----
async def add_task(
    title: str, descriprion: str, difficulty: str, priority: str
) -> None:
    """Функция добавления отслеживаемой задачи задачи"""
    pass


async def complete_task(task_id: int) -> None:
    """Функция, переводящая задачу из 'активных' в 'выполненные'"""
    pass


async def update_task(task_id: int) -> None:
    """Функция обновления данных задачи"""
    pass


async def delete_task(task_id: int) -> None:
    """Функция удаления задачи (не переводит в статус завершённых)"""
    pass


# ----- user model -----
async def change_notion_time(user_id: int) -> None:
    """Функция изменения времени рассылки по id пользователя"""
    pass
