import asyncio

from aiogram import Bot, Dispatcher

import admin
from handlers import commands
from config import load_config

config = load_config()


def register_all_handlers(dp: Dispatcher):
    commands.register_handler(dp)
    admin.register_handler(dp)


async def main():
    bot = Bot(token=config.token)
    dp = Dispatcher()
    dp['config'] = config

    register_all_handlers(dp)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(main())
