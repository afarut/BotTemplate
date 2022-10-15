from aiogram.types import Message
from loader import dp


@dp.message_handler()
async def text_msg(message: Message):
    s = message.text
    await message.answer(s) 