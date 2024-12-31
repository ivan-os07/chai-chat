from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart
import requests

router = Router()


# This handler receives messages with `/start` command
@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Вас приветствует")

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

    await message.answer(f'{response.json()}')
