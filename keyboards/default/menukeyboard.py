from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Kurslar"),
        ],
        [
            KeyboardButton(text="Ro'yxatdan o'tish"),
        ],
    ],
    resize_keyboard=True
)
