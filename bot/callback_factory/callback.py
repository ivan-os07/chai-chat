from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext

from .main_callback import MainCb
from keyboards.inline import planning_kb, ai_psych_tools_kb
from fsm.horoscope import HoroscopeStates, test_znakiZodiaka
from service.ai_req import get_horoscope

router = Router()


@router.callback_query(
    MainCb.filter(F.first_action == "page-1" and F.last_action == "planning_tools")
)
async def test(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.answer(
        f"Инструменты для планирования", reply_markup=planning_kb
    )


@router.callback_query(
    MainCb.filter(F.first_action == "page-1" and F.last_action == "ai_psych_tools")
)
async def test(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.answer(f"AI Психология", reply_markup=ai_psych_tools_kb)


@router.callback_query(
    MainCb.filter(F.first_action == "page-1" and F.last_action == "game_func")
)
async def test(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.answer(f"Развлекательные функции")


@router.callback_query(
    MainCb.filter(F.first_action == "page-1" and F.last_action == "horoscope")
)
async def horoscope(callback: types.CallbackQuery, state: FSMContext):
    await callback.answer()
    await callback.message.answer(f"Введите ваш знак зодиака")
    await state.set_state(HoroscopeStates.waiting_for_zodiac)


@router.message(HoroscopeStates.waiting_for_zodiac)
async def process_zodiac(message: types.Message, state: FSMContext):
    zodiac_sign = message.text.lower()
    if await test_znakiZodiaka(zodiac_sign):
        await state.update_data(zodiac_sign=zodiac_sign)
        
        msg = await get_horoscope(zodiac_sign)
        await message.answer(msg)

        # Сброс состояния
        await state.clear()
    else:
        await message.answer("Неверный ввод. Пожалуйста, введите знак зодиака.")
