from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

test_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text=f'Да', callback_data=f'yes'),
        ],
        [
            InlineKeyboardButton(text='Нет', callback_data=f"no"),
        ]
    ]
)
