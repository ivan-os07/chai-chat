from aiogram import Router, F, types

from .main_callback import MainCb
from keyboards.inline import planning_kb, ai_psych_tools_kb

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
async def test(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.answer(f"Гороскоп")
