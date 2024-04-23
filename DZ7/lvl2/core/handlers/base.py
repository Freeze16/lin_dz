from aiogram import F
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart

from DZ7.lvl2.core.keyboards.base_keyboard import keyboard


async def bot_start(message: Message, bot: Bot):
    with open('core/introduction.txt', 'r') as introduction:
        text = introduction.read()

    await message.answer(text, reply_markup=keyboard)


async def wait_photo(message: Message, bot: Bot):
    await message.answer('Отправьте вашу картинку, вместе с её названием в одном сообщении')


async def wait_file(message: Message, bot: Bot):
    await message.answer('Отправьте ваш текстовый документ, вместе с его названием в одном сообщении')


async def wait_sending(message: Message, bot: Bot):
    await message.answer('Введите имя интересуемого файла')


async def fail(message: Message, bot: Bot):
    await message.answer('Ничего не найдено :(')


def register_handler(dp: Dispatcher):
    dp.message.register(bot_start, CommandStart())
    dp.message.register(wait_photo, F.text == 'Отправить фото 🖼')
    dp.message.register(wait_file, F.text == 'Отправить документ 📄')
    dp.message.register(wait_sending, F.text == 'Найти файл 💾')
    dp.message.register(fail)
