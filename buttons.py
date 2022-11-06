from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton


btn_start = [
    InlineKeyboardButton('Меню', callback_data='Menu'),
    InlineKeyboardButton('Заказ', callback_data='zakaz')
    ]
inline_kb1 = InlineKeyboardMarkup(row_width=2).add(*btn_start)

btn_order = [
    InlineKeyboardButton('Шаверма из собачатины', callback_data='zak_1'),
    InlineKeyboardButton('-', callback_data='zak_-1'),
    InlineKeyboardButton('Таук из крысятины', callback_data='zak_2'),
    InlineKeyboardButton('-', callback_data='zak_-2'),
    InlineKeyboardButton('Каша из топора', callback_data='zak_3'),
    InlineKeyboardButton('-', callback_data='zak_-3'),
]
inline_kb_order = InlineKeyboardMarkup(row_width=2).add(*btn_order)