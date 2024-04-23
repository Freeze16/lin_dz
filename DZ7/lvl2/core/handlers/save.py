from aiogram import F
from aiogram import Bot, Dispatcher
from aiogram.types import Message


async def get_photo(message: Message, bot: Bot):
    await message.answer(f'Ваша картинка сохранена под названием: {message.caption}')
    photo = await bot.get_file(message.photo[-1].file_id)
    await bot.download_file(photo.file_path, 'core/filters/files/{}.jpg'.format(message.caption))


async def get_document(message: Message, bot: Bot):
    await message.answer(f'Ваш файл сохранён под названием: {message.caption}')
    document = await bot.get_file(message.document.file_id)
    extension = message.document.file_name.split('.')[-1]
    await bot.download_file(document.file_path, 'core/filters/files/{}.{}'.format(message.caption, extension))


def register_handler(dp: Dispatcher):
    dp.message.register(get_photo, F.photo)
    dp.message.register(get_document, F.document)
