from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_commands(bot: Bot):
    commands = [
        BotCommand(
            command='start',
            description='Описание бота'
        ),
        BotCommand(
            command='example',
            description='Пример работы'
        ),
        BotCommand(
            command='all',
            description='Вывести все названия файлов'
        )
    ]

    await bot.set_my_commands(commands, BotCommandScopeDefault())
