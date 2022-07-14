from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.inline.test_inline import test_keyboard
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(text=f"Привет, {message.from_user.full_name}!",
                         reply_markup=test_keyboard)
