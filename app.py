from aiogram import executor
from loader import bot, dp
import handlers, filters
from config import ADMIN
import asyncio
import data.db as db
import datetime


async def on_shutdown(dp):
    await bot.send_message(chat_id=ADMIN, text="Бот окончил свою работу")
    await bot.close()

async def send_to_admin(dp):
    await bot.send_message(chat_id=ADMIN, text="Бот запущен")


if __name__ == '__main__':
    
    

    #dp.loop.create_task(example())
    executor.start_polling(dp, on_startup=send_to_admin, on_shutdown=on_shutdown)