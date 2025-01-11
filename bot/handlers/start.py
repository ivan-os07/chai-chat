from time import sleep

from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart

from keyboards.inline import start_kb, can_kb
from database.database import create_user, async_session


router = Router()


# This handler receives messages with `/start` command
@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    async with async_session() as session:

        await create_user(
            session,
            telegram_id=message.from_user.id,
            first_name=message.from_user.first_name,
            last_name=message.from_user.last_name,
        )

    await message.answer(
        f"Привет, <b>{message.from_user.full_name}</b>👋🏻\n<b>Я многофункциональный</b> AI ассистент",
        reply_markup=start_kb,
    )

    await message.answer(
        f"<i>Если у вас возникли <b>вопросы</b> или <b>предложения</b>, обратитесь к разработчику</i> @iChizh007 ✍️"
    )

    sleep(1)
    await message.answer(
        f"<i>Я могу</i>:\n<b>Инструменты для планирования:</b>\nМожешь записать свои задачи и события\n<b>AI Психология:</b>\nРасскажи, что ты чувствуешь. Я проконсультирую тебя в вопросе ментального здоровья и дам заряд мотивации\n<b>Развлекательные функции:</b>\nДа, у меня есть и игры",
        reply_markup=can_kb,
    )
