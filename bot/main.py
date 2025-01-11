import os
import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.bot import DefaultBotProperties
from database.database import init_db

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
TOKEN = os.getenv("TOKEN")


from handlers.start import router
from callback_factory.callback import router as callback_router

ALLOWED_UPDATES = ["message", "callback_query"]


# Add this function to run the database initialization
async def ensure_db_created():
    await init_db()
    print("Database initialized successfully")


async def main() -> None:
    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    bot = Bot(TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    # Initialization database
    await ensure_db_created()

    dp = Dispatcher()
    dp.include_routers(router, callback_router)

    # To cut down on the flooding
    await bot.delete_webhook(drop_pending_updates=True)

    # And the run events dispatching
    await dp.start_polling(bot, allowed_updates=ALLOWED_UPDATES)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
