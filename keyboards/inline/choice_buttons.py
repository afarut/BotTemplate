from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def example_btns(url):
    keyboard = InlineKeyboardMarkup()
    btn1 = InlineKeyboardButton('Example url', url=url)
    btn2 = InlineKeyboardButton('Example button', callback_data=f"example")
    keyboard.row(btn1)
    keyboard.row(btn2)
    return keyboard