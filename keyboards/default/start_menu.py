from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_keyboard = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text='Кнопка 1'),
        ],

    ],
    resize_keyboard=True)
