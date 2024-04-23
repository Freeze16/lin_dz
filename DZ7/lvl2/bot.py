import asyncio

from aiogram import Bot, Dispatcher

import admin
from core.handlers import base
from core.handlers import save
from core.handlers import send
from core.config import load_config

config = load_config()


def register_all_handlers(dp: Dispatcher):
    admin.register_handler(dp)
    save.register_handler(dp)
    send.register_handler(dp)
    base.register_handler(dp)


async def main():
    bot = Bot(token=config.token)
    dp = Dispatcher()

    register_all_handlers(dp)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(main())
