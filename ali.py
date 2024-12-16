from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
menu=ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Toshkent"),KeyboardButton(text="Xiva"),KeyboardButton(text="Xorazm")]
    ],
    resize_keyboard=True
)