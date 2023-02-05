import datetime
import telebot
from telebot import types

bot = telebot.TeleBot("6146443023:AAFU7aiE8iwTpdHWqrb-AGoLU7g1hnRA6WQ")

# @bot.message_handler(commands = ["start"])
# def start(message):
#     bot.send_message(message.chat.id, "напиши фамилию и имя на одной строке")
#     bot.register_next_step_handler(message, sentence)

@bot.message_handler(commands = ["start"])
def start(message):
    bot.send_message(message.chat.id, "напиши клавиатура")

@bot.message_handler(content_types=["text"])
def button(message):
    if message.text == "клавиатура":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        but1 = types.KeyboardButton("сделать предложение")
        but2 = types.KeyboardButton("узнать время")
        markup.add(but1)
        markup.add(but2)
        bot.send_message(message.chat.id, "выбери ниже", reply_markup=markup)
    elif message.text == "сделать предложение":
        bot.send_message(message.chat.id, "введи имя фамилию")
        bot.register_next_step_handler(message, sentence)
    elif message.text == "узнать время":
        bot.send_message(message.chat.id, f"текущее время - {datetime.datetime.now()}")

# @bot.message_handler(content_types="text")
# def controller(message):



def sentence(message):
    text = message.text
    surname = text.split()[0]
    name = text.split()[1]
    bot.send_message(message.chat.id, f"Вас зовут - {name}, фамилия - {surname}")

bot.infinity_polling()