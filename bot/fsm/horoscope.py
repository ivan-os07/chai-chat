from aiogram.fsm.state import State, StatesGroup


class HoroscopeStates(StatesGroup):
    waiting_for_zodiac = State()


znakiZodiaka = [
    "овен",
    "телец",
    "близнецы",
    "рак",
    "лев",
    "дева",
    "весы",
    "скорпион",
    "стрелец",
    "козерог",
    "водолей",
    "рыбы",
]


async def test_znakiZodiaka(znak: str):
    znak = " ".join(znak.strip().lower().split())
    # print(znak)
    if znak not in znakiZodiaka:
        return False
    return True
