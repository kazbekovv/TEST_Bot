import logging
from config import dp, bot
from aiogram.utils import executor
from handlers import commands, FSM_products, FSM_zakazy
from db import db_main
from aiogram import types
from config import admin


async def on_startup(_):
    for i in admin:
        await bot.send_message(chat_id=i, text='Бот включен!')
        await db_main.sql_create()

async def on_shutdown(_):
    for i in admin:
        await bot.send_message(chat_id=i, text='Бот выключен!')

commands.register_commands(dp)
FSM_products.products_fsm(dp)
FSM_zakazy.zakazy_fsm(dp)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup,
                           on_shutdown=on_shutdown)