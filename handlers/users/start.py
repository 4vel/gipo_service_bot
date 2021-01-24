from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f'Привет, {message.from_user.full_name}!')
    await message.answer(f'Я Gipo 🤖! Могу помочь с расчетом платежей по ипотеке.🏠 ')
    await message.answer(f'Отправь команду calculate и введи исходные данные для расчета.')
    # await message.answer(f'Твой user_id {message.from_user.id}')


