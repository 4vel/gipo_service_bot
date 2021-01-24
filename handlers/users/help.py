from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp
from utils.misc import rate_limit


@rate_limit(5, 'help')
@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = [
        'Список команд:',
        '/start - Запустить Gipo',
        '/help - Получить справку',
        '/calculate - Рассчитать ипотеку',
        # '/save - Сохранить расчет',
        # '/show - Показать сохраненные расчеты'
    ]
    await message.answer('\n'.join(text))
