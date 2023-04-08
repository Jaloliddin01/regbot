from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.menukeyboard import menu
from keyboards.default.menuCourses import menuCourses
from data.config import ADMINS

from loader import dp
import logging

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Botimizga xush kelibsiz {message.from_user.full_name}!")
    await message.answer(f"Codegeeks jamoasi sizga yordam berishdan xursand!", reply_markup=menu)  

@dp.message_handler(text="Kurslar 💻")
async def kurslar(message: types.Message):
    await message.answer("Bizning kurslar", reply_markup=menuCourses)

@dp.message_handler(text="Biz haqimizda 👨🏻‍💻")
async def biz_haqimizda(message: types.Message):
    await message.answer("Biz CodeGeeks jamoasi, sizga dasurlashni o'rganishda yordam beramiz")

@dp.message_handler(text="Ortga 🔙")
async def ortga(message: types.Message):
    await message.answer("Bosh sahifa", reply_markup=menu)

@dp.message_handler(text="Backend(Python)")
async def backend_python(message: types.Message):
    await message.answer("Backend(Python) kursi")

@dp.message_handler(text="Frontend(VueJS)")
async def frontend_vuejs(message: types.Message):
    await message.answer("Frontend(VueJS) kursi")

@dp.message_handler(text="Android(Kotlin)")   
async def android_kotlin(message: types.Message):
    await message.answer("Android(Kotlin) kursi")

@dp.message_handler(text="Telegram Bot(Python)")
async def telegram_bot_python(message: types.Message):
    await message.answer("Telegram Bot(Python) kursi")