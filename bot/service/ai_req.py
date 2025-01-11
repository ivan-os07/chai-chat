import os
from mistralai import Mistral

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

api_key = os.getenv("APIKEY")
model = "mistral-large-latest"

client = Mistral(api_key=api_key)


promt = "Ты — астрологический бот, который предоставляет гороскопы на каждый день.\
    Пользователи будут запрашивать гороскопы для конкретных знаков зодиака.\
        Твоя задача — выдавать краткий, но информативный гороскоп, который включает в себя советы по любви, работе и здоровью.\
            Формат ответа:\
            1. Начни с приветствия.\
            2. Укажи знак зодиака.\
            3. Предоставь гороскоп с тремя основными аспектами: любовь, работа и здоровье.\
            4. Заверши позитивной нотой или советом."


async def get_horoscope(znak):
    chat_response = client.chat.complete(
        model=model,
        messages=[
            {
                "role": "system",
                "content": promt,
            },
            {
                "role": "user",
                "content": f"Сделай гороскоп на сегодня для знака зодиака {znak}",
            },
        ],
    )

    return chat_response.choices[0].message.content
