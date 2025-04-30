import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot import types
import telebot
from parser import *
from db import *

bot = telebot.TeleBot('7833937382:AAEY_5GgGZRGWNCvvPWjcgFB48KygWHXhgs')
ADMIN = ''

zodiac_signs = {
    '♈️ Овен': 'aries',
    '♉ Телец': 'taurus',
    '♊ Близнецы': 'gemini',
    '♋️ Рак': 'cancer',
    '♌ Лев': 'leo',
    '♍ Дева': 'virgo',
    '♎ Весы': 'libra',
    '♏ Скорпион': 'scorpio',
    '♐ Стрелец': 'sagittarius',
    '♑ Козерог': 'capricorn',
    '♒ Водолей': 'aquarius',
    '♓ Рыбы': 'pisces'
}


@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)  # Здесь изменено значение параметра
    col1, col2 = [], []
    for sign in zodiac_signs:
        if len(col1) < 6:
            col1.append(sign)
        else:
            col2.append(sign)
    markup.add(*col1)
    markup.add(*col2)
    wlcmmsg = '<b>👋 Привет '  + message.from_user.first_name  + '</b>' + '\n\n⚛️ Выберите Ваш знак зодиака'
    bot.send_message(message.from_user.id, text=wlcmmsg, reply_markup=markup, parse_mode="html", disable_web_page_preview=True)
    tgidregister(message.from_user.id)

@bot.message_handler(content_types=['text'])
def process_step(message):
    sign = zodiac_signs.get(message.text)
    if sign:
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(*[InlineKeyboardButton(text=period, callback_data=f'{sign}|{period}') for period in ['вчера', 'сегодня', 'завтра', 'неделя', 'месяц', 'год']])
        bot.send_message(message.from_user.id, f'Получить гороскоп {message.text} на:', reply_markup=keyboard, parse_mode="html")

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    el = call.data.split("|")
    period_text = {
        'вчера': 'yesterday',
        'сегодня': 'today',
        'завтра': 'tomorrow',
        'неделя': 'week',
        'месяц': 'month',
        'год': 'year'
    }
    bot.send_message(call.message.chat.id, getHoro(el[0], period_text[el[1]]), parse_mode="html", disable_web_page_preview=True)

bot.polling(none_stop=True, interval=0)