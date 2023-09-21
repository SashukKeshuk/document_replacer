# -*- coding: utf-8 -*-
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup, web_app_info

mutual_fiz = InlineKeyboardButton('Возмоездное оказание услуг физ лицам', callback_data='mutual_fiz')
mutual_ur = InlineKeyboardButton('Возмоездное оказание услуг юр лицам', callback_data='mutual_ur')
x1fiz = InlineKeyboardButton('Разовая поставка физ лицам', callback_data='x1fiz')
x1ur = InlineKeyboardButton('Разовая поставка юр лицам', callback_data='x1ur')
Yearfiz = InlineKeyboardButton('Годовая поставка физ лицам', callback_data='Yearfiz')
Yearur = InlineKeyboardButton('Разовая поставка юр лицам', callback_data='Yearur')
chs_mrkp = InlineKeyboardMarkup()
chs_mrkp.add(mutual_fiz).add(mutual_ur).add(x1fiz).add(x1ur).add(Yearfiz).add(Yearur)