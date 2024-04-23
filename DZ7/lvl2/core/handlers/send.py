from aiogram import Bot, Dispatcher
from aiogram.types import Message, FSInputFile

from DZ7.lvl2.core.filters.what_is_file import SendPhoto, SendDocument
from DZ7.lvl2.core.filters.get_file import get_file


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


def register_handler(dp: Dispatcher):
    dp.message.register(send_photo, SendPhoto())
    dp.message.register(send_document, SendDocument())
