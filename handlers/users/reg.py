from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from data.config import ADMINS
from loader import dp
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
import logging

class Form(StatesGroup):
    name = State()
    surname = State()
    phone = State()
    description = State()

data = {}

@dp.message_handler(text="Ro'yxatdan o'tish 📋")
async def register(message: types.Message):
    await message.answer(f"Ro'yxatdan o'tish uchun ma'lumotlarni kiriting:")
    await Form.name.set()
    await message.answer(f"👤Ismingiz:")

@dp.message_handler(state=Form.name)
async def name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    data['name'] = message.text
    await message.answer(f"👤Familiyangiz:")
    await Form.next()

@dp.message_handler(state=Form.surname)
async def surname(message: types.Message, state: FSMContext):
    await state.update_data(surname=message.text)
    data['surname'] = message.text
    await message.answer(f"📱Telefon raqamingiz (99 000 00 00):")
    await Form.next()

@dp.message_handler(state=Form.phone)
async def phone(message: types.Message, state: FSMContext):
    await state.update_data(phone=message.text)
    data['phone'] = message.text
    await message.answer(f"📝Dasturlashni bilish darajangiz haqida qisqacha ma'lumot:")
    await Form.next()

@dp.message_handler(state=Form.description)
async def description(message: types.Message, state: FSMContext):
    await state.update_data(description=message.text)
    data['description'] = message.text
    await message.answer(f"Ma'lumotlar muvaffaqiyatli saqlandi! Tez orada siz bilan bog'lanamiz")
    await state.finish()

    try:
        await dp.bot.send_message(ADMINS[0], f"Ro'yxatdan o'tgan foydalanuvchi: \nIsmi : {data['name']}\nFamiliyasi: {data['surname']}\nTelefon raqami: {data['phone']}\nQisqa izoh: {data['description']}")
    except Exception as err:
        logging.exception(err)

    

    

    
