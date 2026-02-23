from sqlalchemy import select, update

from .model import Base, Task, User, async_session, engine


# ----- core database functions -----
async def reload_database() -> None:
    """
    Функция перезагрузки базы данных
    Сначала полностью удаляет её, а потом создаёт заново
    """
    async with engine.begin() as con:
        await con.run_sync(Base.metadata.drop_all)
        await con.run_sync(Base.metadata.create_all)


# ----- CRUD -----
async def add_task(
        title: str,
        difficulty: str,
        priority: str,
        tg_id: int) -> None:
    """Функция добавления отслеживаемой задачи"""
    async with async_session() as session:
        task = await session.scalar(
            select(Task).where(
                Task.title == title,
                Task.difficulty == difficulty,
                Task.priority == priority,
                Task.user_id == tg_id,
            )
        )

        if not task:
            session.add(
                Task(
                    title=title,
                    difficulty=difficulty,
                    priority=priority,
                    user_id=tg_id
                )
            )
        await session.commit()


async def get_tasks(tg_id: int) -> list[Task]:
    """Функция для получения списка задач пользователя"""
    async with async_session() as session:
        tasks = await session.scalars(
            select(Task).where(Task.user_id == tg_id)
        )
        tasks_list = tasks.all()
        return list(tasks_list)


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
async def change_notification_time(tg_id: int) -> None:
    """Функция изменения времени рассылки по id пользователя"""
    pass


async def create_user(tg_id: int) -> None:
    """Функция добавления пользователя после нажатия '/start'"""
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))
        if not user:
            session.add(User(tg_id=tg_id))
        await session.commit()
