from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.menukeyboard import menu
from data.config import ADMINS
from loader import dp
import logging

data = {}

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!")
    await message.answer(f"Iltimos ismingizni kiriting:")
    data['name'] = message.text
    await surname()

@dp.message_handler()
async def surname(message: types.Message):
    await message.answer(f"Iltimos familiyangizni kiriting:")
    data['surname'] = message.text
    await phone_number()

@dp.message_handler()
async def phone_number(message: types.Message):
    await message.answer(f"Iltimos telefon raqamingizni kiriting:")
    # data['phone_number'] = message.text
    await description()

@dp.message_handler()
async def description(message: types.Message):
    await message.answer(f"Iltimos nimalar bilishingiz haqida qisqacha yozing:")
    data['description'] = message.text
    await message.answer(f"Ma'lumotlarni tekshiring")
    await message.answer(f"{data['name']}, {data['surname']}, {data['phone_number']}, {data['description']}")
    await message.answer(f"Ma'lumotlaringiz qabul qilindi!")
    await message.answer(f"Tez orada siz bilan bog'lanamiz!")
    for admin in ADMINS:
        try:
            await dp.bot.send_message(admin, f"{data['name']}, {data['surname']}, {data['phone_number']}, {data['description']}")

        except Exception as err:
            logging.exception(err)


