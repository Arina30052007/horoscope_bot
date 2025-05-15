from telebot.types import InlineKeyboardButton
from telebot import types
import telebot
from parser import *
from bd import *
from requests import get

bot = telebot.TeleBot('8101490115:AAGWSt8km_gWTmrYNp1UqXbU3RXmotbQwp8')
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
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True,
                                       one_time_keyboard=False)  # Здесь изменено значение параметра
    col1, col2 = [], []
    for sign in zodiac_signs:
        if len(col1) < 6:
            col1.append(sign)
        else:
            col2.append(sign)
    markup.add(*col1)
    markup.add(*col2)
    wlcmmsg = '<b>👋 Привет ' + message.from_user.first_name + '</b>' + '\n\n⚛️ Выберите Ваш знак зодиака'
    bot.send_message(message.from_user.id, text=wlcmmsg, reply_markup=markup, parse_mode="html",
                     disable_web_page_preview=True)

@bot.message_handler(commands=['help'])
def send_welcome(message):
    wlcmmsg = '🤔 Не знаешь свой знак зодиака? '  +  '\n\nТогда просто введи свой день рождения в виде "день.месяц"'
    bot.send_message(message.from_user.id, text=wlcmmsg)



@bot.message_handler(content_types=['text'])
def process_step(message):
    k = a = message.text
    a = a.split('.')
    if len(a) == 2:
        a = [int(i) for i in a]
        if ((a[0] in [21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31] and a[1] == 3) or
                (a[0] in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20] and a[1] == 4)):
            bot.reply_to(message, 'Вы ♈️ Овен')
        elif ((a[0] in [21, 22, 23, 24, 25, 26, 27, 28, 29, 30] and a[1] == 4) or
              (a[0] in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20] and a[1] == 5)):
            bot.reply_to(message, 'Вы ♉ Телец')
        elif ((a[0] in [21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31] and a[1] == 5) or
              (a[0] in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21] and a[1] == 6)):
            bot.reply_to(message, 'Вы ♊ Близнецы')
        elif ((a[0] in [22, 23, 24, 25, 26, 27, 28, 29, 30] and a[1] == 6) or
              (a[0] in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22] and a[1] == 7)):
            bot.reply_to(message, 'Вы ♋️ Рак')
        elif ((a[0] in [23, 24, 25, 26, 27, 28, 29, 30, 31] and a[1] == 7) or
              (a[0] in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23] and a[1] == 8)):
            bot.reply_to(message, 'Вы ♌ Лев')
        elif ((a[0] in [24, 25, 26, 27, 28, 29, 30, 31] and a[1] == 8) or
              (a[0] in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23] and a[1] == 9)):
            bot.reply_to(message, 'Вы ♍ Дева')
        elif ((a[0] in [24, 25, 26, 27, 28, 29, 30] and a[1] == 9) or
              (a[0] in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23] and a[1] == 10)):
            bot.reply_to(message, 'Вы ♎ Весы')
        elif ((a[0] in [24, 25, 26, 27, 28, 29, 30, 31] and a[1] == 10) or
              (a[0] in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22] and a[1] == 11)):
            bot.reply_to(message, 'Вы ♏ Скорпион')
        elif ((a[0] in [23, 24, 25, 26, 27, 28, 29, 30] and a[1] == 11) or
              (a[0] in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21] and a[1] == 12)):
            bot.reply_to(message, 'Вы ♐ Стрелец')
        elif ((a[0] in [22, 23, 24, 25, 26, 27, 28, 29, 30, 31] and a[1] == 12) or
              (a[0] in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20] and a[1] == 1)):
            bot.reply_to(message, 'Вы ♑ Козерог')
        elif ((a[0] in [21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31] and a[1] == 1) or
              (a[0] in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20] and a[1] == 2)):
            bot.reply_to(message, 'Вы ♒ Водолей')
        elif ((a[0] in [21, 22, 23, 24, 25, 26, 27, 28, 29] and a[1] == 2) or
              (a[0] in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20] and a[1] == 3)):
            bot.reply_to(message, 'Вы ♓ Рыбы')

    else:
        sign = zodiac_signs.get(message.text)
        if sign:
            ph = {
                '♈️ Овен': 'https://cdn.fishki.net/upload/post/2019/08/20/3063203/tn/oven.jpg',
                '♉ Телец': 'https://cdn.fishki.net/upload/post/2019/08/20/3063203/tn/telec.jpg',
                '♊ Близнецы': 'https://cdn.fishki.net/upload/post/2019/08/20/3063203/tn/bliznecy.jpg',
                '♋️ Рак': 'https://cdn.fishki.net/upload/post/2019/08/20/3063203/tn/rak.jpg',
                '♌ Лев': 'https://cdn.fishki.net/upload/post/2019/08/20/3063203/tn/lev.jpg',
                '♍ Дева': 'https://cdn.fishki.net/upload/post/2019/08/20/3063203/tn/deva.jpg',
                '♎ Весы': 'https://cdn.fishki.net/upload/post/2019/08/20/3063203/tn/vesy.jpg',
                '♏ Скорпион': 'https://cdn.fishki.net/upload/post/2019/08/20/3063203/tn/skorpion.jpg',
                '♐ Стрелец': 'https://cdn.fishki.net/upload/post/2019/08/20/3063203/tn/strelec.jpg',
                '♑ Козерог': 'https://cdn.fishki.net/upload/post/2019/08/20/3063203/tn/kozerog.jpg',
                '♒ Водолей': 'https://cdn.fishki.net/upload/post/2019/08/20/3063203/tn/vodolej.jpg',
                '♓ Рыбы': 'https://cdn.fishki.net/upload/post/2019/08/20/3063203/tn/ryby.jpg'
            }
            tgidregister(message.from_user.id, message.from_user.first_name, sign)
            keyboard = types.InlineKeyboardMarkup()
            keyboard.add(*[InlineKeyboardButton(text=period, callback_data=f'{sign}|{period}') for period in
                           ['вчера', 'сегодня', 'завтра', 'неделя', 'месяц', 'год']])
            bot.send_photo(message.from_user.id, get(ph[message.text]).content)
            bot.send_message(message.from_user.id, f'Получить гороскоп {message.text} на:', reply_markup=keyboard,
                             parse_mode="html")


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
    bot.send_message(call.message.chat.id, getHoro(el[0], period_text[el[1]]), parse_mode="html",
                     disable_web_page_preview=True)




bot.polling(none_stop=True, interval=0)
