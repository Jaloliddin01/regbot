from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menuCourses = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Backend(Python)"),
            KeyboardButton(text="Frontend(VueJS)"),
        ],
        [
            KeyboardButton(text="Android(Kotlin)"),
            KeyboardButton(text="Telegram Bot(Python)"),
        ],
        [
            KeyboardButton(text="Ortga 🔙"),
        ],
    ],
    resize_keyboard=True,
)

