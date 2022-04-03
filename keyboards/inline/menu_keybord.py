from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData
from utils.db.db_menu import get_stage1
import logging

# Создаем CallbackData-объекты, которые будут нужны для работы с менюшкой
menu_cd = CallbackData("show_menu", "level", "state", "index", "rez")
# buy_item = CallbackData("buy", "item_id")


# С помощью этой функции будем формировать коллбек дату для каждого элемента меню, в зависимости от
# переданных параметров. Если Подкатегория, или айди товара не выбраны - они по умолчанию равны нулю
def make_callback_data(level, state="0", rez="0", index="0"):
    return menu_cd.new(level=level, state=state, rez=rez ,index=index)


# Создаем функцию, которая отдает
# клавиатуру с доступными stage
async def categories_keyboard(current_level, sql):
    markup = InlineKeyboardMarkup(row_width=2)
    logging.info('Function categories_keyboard')
    categories = get_stage1(sql)
    
    logging.info(f'Categories recived')
    for category in categories:
        # Текст на кнопке

        # Сформируем колбек дату, которая будет на кнопке.
        callback_data = make_callback_data(
            level=category[4],
            state=category[1],
            rez=category[2],
            index=category[-1])
        logging.info(f'Prepared callback_data for button. callback_data = {callback_data}')
        
        # Вставляем кнопку в клавиатуру
        markup.insert(InlineKeyboardButton(
            text=category[1],
            callback_data=callback_data))
        

    # Создаем Кнопку "Назад", в которой прописываем колбек дату
    if current_level != 0:
        markup.row(
            InlineKeyboardButton(
                text="Назад",
                callback_data=make_callback_data(level=0))
        )
    logging.info('Return markup')
    return markup