from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

keyboard = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text='Отправить фото 🖼'
        ),
        KeyboardButton(
            text='Отправить документ 📄'
        )
    ],
    [
        KeyboardButton(
            text='Найти файл 💾'
        )
    ]
], resize_keyboard=True)
