from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from callback_factory.main_callback import MainCb

# start inline keyboard
start_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Github", url="https://github.com/ivan-os07"),
        ]
    ]
)

# start inline keyboard
can_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Инструменты для планирования❌",
                callback_data=MainCb.create(
                    first_action="page-1", last_action="planning_tools"
                ),
            ),
        ],
        [
            InlineKeyboardButton(
                text="AI Психология❌",
                callback_data=MainCb.create(
                    first_action="page-1", last_action="ai_psych_tools"
                ),
            ),
        ],
        [
            InlineKeyboardButton(
                text="Развлекательные функции❌",
                callback_data=MainCb.create(
                    first_action="page-1", last_action="game_func"
                ),
            ),
        ],
        [
            InlineKeyboardButton(
                text="Гороскоп✅",
                callback_data=MainCb.create(
                    first_action="page-1", last_action="horoscope"
                ),
            ),
        ],
    ]
)

planning_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Управление Задачами", callback_data="1"),
        ],
        [
            InlineKeyboardButton(text="Календарь событий", callback_data="1"),
        ],
    ]
)


ai_psych_tools_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Дай мотивацию", callback_data="1"),
            InlineKeyboardButton(text="Что чувствую", callback_data="1"),
        ],
    ]
)
