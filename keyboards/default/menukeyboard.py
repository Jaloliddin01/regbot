from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Kurslar 💻"),
        ],
        [
            KeyboardButton(text="Ro'yxatdan o'tish 📋"),
        ],
        [
            KeyboardButton(text="Biz haqimizda 👨🏻‍💻"),
        ]
    ],
    resize_keyboard=True
)

