from aiogram import Bot, Dispatcher
from aiogram.types import Message


async def bot_start(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id, 'Hello!')


def register_handler(dp: Dispatcher):
    dp.message.register(bot_start)
