import os
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.future import select

from .models import Base, User

# Получаем путь к корневому каталогу проекта
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Формируем путь к файлу базы данных в корневом каталоге
DATABASE_PATH = os.path.join(ROOT_DIR, "database.db")

# Создаем URL для SQLAlchemy
DATABASE_URL = f"sqlite+aiosqlite:///{DATABASE_PATH}"

engine = create_async_engine(DATABASE_URL, echo=True)
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def create_user(
    db: AsyncSession, telegram_id: int, first_name: str, last_name: str
):
    # Проверяем, существует ли пользователь с таким именем
    result = await db.execute(select(User).filter(User.telegram_id == telegram_id))
    existing_user = result.scalars().first()

    if existing_user:
        #print(f"Пользователь с именем '{first_name} {last_name}' уже существует.")
        return None  # Возвращаем None или можно выбросить исключение

    # Если пользователя нет, добавляем нового
    new_user = User(telegram_id=telegram_id, first_name=first_name, last_name=last_name)
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return new_user
