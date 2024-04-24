from aiogram import Bot, Dispatcher
from aiogram.types import Message, FSInputFile
from aiogram.filters import Command

from DZ7.lvl2.core.filters.what_is_file import SendPhoto, SendDocument
from DZ7.lvl2.core.filters.get_file import get_file, get_all_files


async def send_photo(message: Message, bot: Bot):
    path = 'core/filters/files/{}.jpg'.format(message.text)
    await bot.send_photo(
        chat_id=message.chat.id,
        photo=FSInputFile(path=path)
    )


async def send_document(message: Message, bot: Bot):
    path = 'core/filters/files/{}'.format(get_file(message.text))
    await bot.send_document(
        chat_id=message.chat.id,
        document=FSInputFile(path=path)
    )


async def send_all_file_names(message: Message, bot: Bot):
    names = ', '.join(get_all_files())
    await message.answer(names)


def register_handler(dp: Dispatcher):
    dp.message.register(send_photo, SendPhoto())
    dp.message.register(send_document, SendDocument())
    dp.message.register(send_all_file_names, Command(commands=['all']))
