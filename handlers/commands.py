from aiogram import types, Dispatcher
from config import bot
import os
from aiogram.types import InputFile
import random


async def start_handler(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text='Привет')



async def info_handler(message: types.Message):
    await message.answer("Это тест Бот за 3 месяц\n"
                         "Казбеков Ислам, 44-2\n"
                         "Этот бот предназначен для управления продуктами и заказами.\n")


def register_commands(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=['start'])
    dp.register_message_handler(info_handler, commands=['info'])
