# -*- coding: utf-8 -*-
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardButton, \
    InlineKeyboardMarkup, web_app_info
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher.filters.state import State, StatesGroup
from markups import *
from config import *
from mf import fill_contract_mf
from mr import fill_contract_mr
from xfiz import fill_contract_xf
from xur import fill_contract_xr
import convertapi

storage = MemoryStorage()
bot = Bot(token=bot_api_token)
dp = Dispatcher(bot, storage=storage)
prev_msgs = dict()
l = dict()
convertapi.api_secret = conv_api

class MFIZ(StatesGroup):
    msg1 = State()
    msg2 = State()
    msg3 = State()
    msg4 = State()
    msg5 = State()
    msg6 = State()
    msg7 = State()
    msg8 = State()
    msg9 = State()
    msg10 = State()
    msg11 = State()
    msg12 = State()
    msg13 = State()
    msg14 = State()
    msg15 = State()
    msg16 = State()
    msg17 = State()
    msg18 = State()
    msg19 = State()
    msg20 = State()
    msg21 = State()
    msg22 = State()
    msg23 = State()
    msg24 = State()
    msg25 = State()
    msg26 = State()
    msg27 = State()
    msg28 = State()
    msg29 = State()
    msg30 = State()

async def on_startup(_):
    print('bot is working')

@dp.message_handler(commands=['start'])
async def start(msg: types.Message):
    await bot.send_message(msg.from_user.id, f"Здравствуйте, {msg.from_user.username}. Выберите документ", reply_markup=chs_mrkp)

@dp.callback_query_handler(text = 'mutual_fiz')
async def mfiz(clb: types.CallbackQuery):
    await MFIZ.msg1.set()
    l[clb.from_user.id] = 1
    await bot.send_message(clb.from_user.id, f"Хорошо, теперь запоните форму. Для начала заполнения введите 'ок'")

@dp.callback_query_handler(text = 'mutual_ur')
async def mfiz(clb: types.CallbackQuery):
    await MFIZ.msg1.set()
    l[clb.from_user.id] = 2
    await bot.send_message(clb.from_user.id, f"Хорошо, теперь запоните форму. Для начала заполнения введите 'ок'")

@dp.callback_query_handler(text = 'x1fiz')
async def mfiz(clb: types.CallbackQuery):
    await MFIZ.msg1.set()
    l[clb.from_user.id] = 3
    await bot.send_message(clb.from_user.id, f"Хорошо, теперь запоните форму. Для начала заполнения введите 'ок'")

@dp.callback_query_handler(text = 'x1ur')
async def mfiz(clb: types.CallbackQuery):
    await MFIZ.msg1.set()
    l[clb.from_user.id] = 4
    await bot.send_message(clb.from_user.id, f"Хорошо, теперь запоните форму. Для начала заполнения введите 'ок'")

@dp.callback_query_handler(text = 'Yearfiz')
async def mfiz(clb: types.CallbackQuery):
    await MFIZ.msg1.set()
    l[clb.from_user.id] = 5
    await bot.send_message(clb.from_user.id, f"Хорошо, теперь запоните форму. Для начала заполнения введите 'ок'")

@dp.callback_query_handler(text = 'Yearur')
async def mfiz(clb: types.CallbackQuery):
    await MFIZ.msg1.set()
    l[clb.from_user.id] = 6
    await bot.send_message(clb.from_user.id, f"Хорошо, теперь запоните форму. Для начала заполнения введите 'ок'")



@dp.message_handler(state=MFIZ.msg1)
async def answer_q1(message: types.Message, state: FSMContext):
    answer = message.text
    await message.answer(f"Номер договора:")
    await MFIZ.next()

@dp.message_handler(state=MFIZ.msg2)
async def answer_q1(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(answer1=answer)
    await message.answer("ТОО вашей компании:")
    await MFIZ.next()

@dp.message_handler(state=MFIZ.msg3)
async def answer_q1(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(answer2=answer)
    await message.answer(f"БИН вашей компании:")
    await MFIZ.next()

@dp.message_handler(state=MFIZ.msg4)
async def answer_q1(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(answer3=answer)
    await message.answer("директор вашей компании в Р.П.:")
    await MFIZ.next()

@dp.message_handler(state=MFIZ.msg5)
async def answer_q1(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(answer4=answer)
    await message.answer(f"основание:")
    await MFIZ.next()

@dp.message_handler(state=MFIZ.msg6)
async def answer_q1(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(answer5=answer)
    await message.answer("ФИО физ лица:")
    await MFIZ.next()

@dp.message_handler(state=MFIZ.msg7)
async def answer_q1(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(answer6=answer)
    await message.answer(f"ИИН:")
    await MFIZ.next()

@dp.message_handler(state=MFIZ.msg8)
async def answer_q1(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(answer7=answer)
    await message.answer("УН:")
    await MFIZ.next()

@dp.message_handler(state=MFIZ.msg9)
async def answer_q1(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(answer8=answer)
    await message.answer(f"От ... выдан ...")
    await MFIZ.next()

@dp.message_handler(state=MFIZ.msg10)
async def answer_q1(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(answer9=answer)
    await message.answer(f"Адрес исп:")
    await MFIZ.next()

@dp.message_handler(state=MFIZ.msg11)
async def answer_q1(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(answer10=answer)
    await message.answer(f"E-mail исп:")
    await MFIZ.next()

@dp.message_handler(state=MFIZ.msg12)
async def answer_q1(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(answer11=answer)
    await message.answer("Тел исп:")
    await MFIZ.next()

@dp.message_handler(state=MFIZ.msg13)
async def answer_q1(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(answer12=answer)
    await message.answer(f"IBAN исп:")
    await MFIZ.next()

@dp.message_handler(state=MFIZ.msg14)
async def answer_q1(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(answer13=answer)
    await message.answer(f"В АО исп:")
    await MFIZ.next()

@dp.message_handler(state=MFIZ.msg15)
async def answer_q1(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(answer14=answer)
    await message.answer(f"Бик исп:")
    await MFIZ.next()

@dp.message_handler(state=MFIZ.msg16)
async def answer_q1(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(answer15=answer)
    await message.answer(f"Адрес зак:")
    await MFIZ.next()

@dp.message_handler(state=MFIZ.msg17)
async def answer_q1(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(answer16=answer)
    await message.answer(f"E-mail зак:")
    await MFIZ.next()

@dp.message_handler(state=MFIZ.msg18)
async def answer_q1(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(answer17=answer)
    await message.answer("Тел зак:")
    await MFIZ.next()

@dp.message_handler(state=MFIZ.msg19)
async def answer_q1(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(answer18=answer)
    await message.answer(f"IBAN зак:")
    await MFIZ.next()

@dp.message_handler(state=MFIZ.msg20)
async def answer_q1(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(answer19=answer)
    await message.answer(f"В АО зак:")
    await MFIZ.next()

@dp.message_handler(state=MFIZ.msg21)
async def answer_q1(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(answer20=answer)
    await message.answer(f"Бик зак:")
    await MFIZ.next()

@dp.message_handler(state=MFIZ.msg22)
async def answer_q1(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(answer21=answer)
    await message.answer("Место оказания услуг:")
    await MFIZ.next()

@dp.message_handler(state=MFIZ.msg23)
async def answer_q1(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(answer22=answer)
    await message.answer(f"Действительно в течение:")
    await MFIZ.next()

@dp.message_handler(state=MFIZ.msg24)
async def answer_q1(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(answer23=answer)
    await message.answer("Теперь введите список услуг 1 сообщением так, что каждая слеедующая услуга будет начинаться с следующей строки")
    await MFIZ.next()

@dp.message_handler(state=MFIZ.msg25)
async def answer_q1(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(answer24=answer)
    await message.answer("директор вашей компании в И.П.:")
    await MFIZ.next()

@dp.message_handler(state=MFIZ.msg26)
async def answer_q1(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(answer25=answer)
    await message.answer("директор компании заказчика в Р.П.:")
    await MFIZ.next()

@dp.message_handler(state=MFIZ.msg27)
async def answer_q1(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(answer26=answer)
    await message.answer("директор компании заказчика в И.П.:")
    await MFIZ.next()

@dp.message_handler(state=MFIZ.msg28)
async def answer_q1(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(answer27=answer)
    await message.answer("ТОО компании заказчика:")
    await MFIZ.next()

@dp.message_handler(state=MFIZ.msg29)
async def answer_q1(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(answer28=answer)
    await message.answer("БИН компании заказчика:")
    await MFIZ.next()

@dp.message_handler(state=MFIZ.msg30)
async def answer_q26(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(answer29=answer)
    data = await state.get_data()
    a = [data[f"answer{i}"] for i in range(1, 29)]
    a.append(answer)
    await state.finish()
    await message.answer("Все сообщения были введены!")
    uid = message.from_user.id
    if (l[message.from_user.id] == 1):
        fill_contract_mf(uid, a)
    if (l[message.from_user.id] == 2):
        fill_contract_mr(uid, a)
    if (l[message.from_user.id] == 3):
        fill_contract_xf(uid, a, 1)
    if (l[message.from_user.id] == 4):
        fill_contract_xr(uid, a, 1)
    if (l[message.from_user.id] == 5):
        fill_contract_xf(uid, a, 2)
    if (l[message.from_user.id] == 6):
        fill_contract_xr(uid, a, 2)
    convertapi.convert('pdf', {
        'File': f'docx/{uid}.docx'
    }, from_format='docx').save_files('pdf/')
    with open(f'docx/{uid}.docx', 'rb') as file:
        await bot.send_document(uid, file)
    with open(f'pdf/{uid}.pdf', 'rb') as file:
        await bot.send_document(uid, file)




executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
