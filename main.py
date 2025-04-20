import telebot

bot = telebot.TeleBot('8092057466:AAEvaTKlJRa7rKExCnXROLvZ77Tz4exEO5s')

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

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
  if message.text == "Привет" or message.text == "привет":
      bot.send_message(message.from_user.id, "Привет, сейчас я расскажу тебе гороскоп на сегодня.")
  elif message.text == "/help":
      bot.send_message(message.from_user.id, "Напиши Привет/привет")
  else:
      bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")

bot.polling(none_stop=True, interval=0)