from aiogram import Bot, Dispatcher
from bot import config

from core.utils.commands import set_commands


async def start_bot(bot: Bot):
    await set_commands(bot)
    await bot.send_message(config.admin, 'Бот запущен!')


async def stop_bot(bot: Bot):
    await bot.send_message(config.admin, 'Бот остоновлен!')


def register_handler(dp: Dispatcher):
    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)
