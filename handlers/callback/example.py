from loader import dp
from aiogram.types import CallbackQuery


@dp.callback_query_handler(lambda call: "example" in call.data)
async def dislike(call: CallbackQuery):
    example = call.data