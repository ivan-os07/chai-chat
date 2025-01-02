from time import sleep

from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart
import requests

from keyboards.inline import start_kb, can_kb

router = Router()


# This handler receives messages with `/start` command
@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
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


# Пример как будет посылаться запрос к беку
@router.message(F.text == "/test")
async def test(message: Message):
    # Ваш JWT токен
    jwt_token = "eyJhbGJ9.eyJzdWIiOiJ0ZXN0IiwianRpIjoiYTlmOTNmM2QtMDJmZC00NDhhLTkwMDctODlmYjk1ZjIxYWY3IiwidHlwZSI6ImFjY2VzcyIsImZyZXNoIjpmYWxzZSwiY3NyZiI6IiIsImlhdCI6MTczNTY1ODMyNSwiZXhwIjoxNzM1NjU5MjI1LjMwMzY3Nn0.QeBU_8oHGAaPkvBt6cF6PO_u3pUGvO_jOXVF3U5ZbLU"

    # URL, к которому вы хотите отправить запрос
    url = "http://127.0.0.1:8000/api/v1/protected/"

    # Заголовки запроса
    headers = {
        "Authorization": f"Bearer {jwt_token}",
    }

    # Пример GET запроса
    response = requests.get(url, headers=headers)

    await message.answer(f"{response.json()}")
