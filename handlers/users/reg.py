from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from data.config import ADMINS
from loader import dp
import logging

@dp.message_handler(text="Ro'yxatdan o'tish 📋")
async def register(message: types.Message):
    await message.answer(f"Ro'yxatdan o'tish uchun ma'lumotlarni kiriting:")
    await message.answer(f"👤Ismingiz:")
    name = message.get_current
    await message.answer(f"👤Familiyangiz:")
    await message.get_current
    await message.answer(f"📱Telefon raqamingiz:")
    await message.get_current

    
