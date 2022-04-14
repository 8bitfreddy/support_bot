from collections import UserString
from aiogram import types
from utils.db.db_menu import all_menu, all_users, menu3
from data.config import ADMINS
from aiogram.dispatcher.filters import Command
import logging
from loader import dp


@dp.message_handler(Command("admin"))
async def admin(message: types.Message):
    logging.info('Admin start') 
    admin = str(message.from_user.id)
    if admin in ADMINS:
        logging.info('Users list')
        await message.reply(f'''Нарекаю тебя АДМИНИСТРАТОР: {message.from_user.full_name}!''')
        all_usr=all_users()
        await message.answer('\n'.join(str(value) for value in all_usr))
        all_menu = menu3() 
        await message.answer(all_menu)
    else:
        logging.info(f'Кто-то нас раскрыл... {message.from_user.id}')
        await message.reply(f'''{message.from_user.full_name}, Вы не являетесь администратором бота!''')