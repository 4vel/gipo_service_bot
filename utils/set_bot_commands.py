from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand("start", "Запустить Gipo"),
        types.BotCommand("help", "Помощь"),
        types.BotCommand("calculate", "Рассчитать ипотеку"),
        # types.BotCommand("save", "Сохранить расчет"),
        # types.BotCommand("show", "Показать сохраненные расчеты"),

    ])

