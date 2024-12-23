from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart


router = Router()


# This handler receives messages with `/start` command
@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(
        f"Вас приветствует"
    )
