# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import time
import telebot
from telebot import types

bot = telebot.TeleBot("5412013624:AAE69GMfVYNYr27igZtBzzWb560GpuShsYM")


@bot.message_handler(commands=["start"])
def inline(message):
        markup =types.InlineKeyboardMarkup()
        itm = types.InlineKeyboardButton(text="3я категория", url="https://t.me/kategory_3_bot")
        markup.add(itm)
        bot.send_message(message.chat.id, "Выберите категорию из списка",
                         reply_markup=markup)


if __name__ == '__main__':
    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as e:
            time.sleep(3)
            print(e)