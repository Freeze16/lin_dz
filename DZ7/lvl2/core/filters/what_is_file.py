import os

from aiogram.filters import BaseFilter
from aiogram.types import Message

PATH = 'core/filters/files/'


class SendPhoto(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        try:
            return message.text + '.jpg' in os.listdir(PATH)
        except:
            return False


class SendDocument(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        documents = [''.join(document.split('.')[:-1]) for document in os.listdir(PATH) if document.split('.')[-1] != 'jpg']
        try:
            return message.text in documents
        except:
            return False
