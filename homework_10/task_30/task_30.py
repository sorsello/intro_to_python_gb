import telebot
from telebot import types
from datetime import datetime

from homework_10.task_30.logger_service import log_activity

API_TOKEN = "5884697253:AAHA4GPlet2QMSNeg6JRf7WgddtSjVdN2W0"
bot = telebot.TeleBot(API_TOKEN)

app_data = {"num1": 0, "num2": 0, "separator": "|", "timeformat": datetime.now().strftime('%D %H:%M')}

@bot.message_handler(commands=["start"])
def bot_start(message):
    bot.send_message(message.chat.id, "Let's go.")
    initiate_calc(message)

@bot.message_handler(commands=["button"])
def initiate_calc(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_whole = types.KeyboardButton("Whole Numbers")
    button_complex = types.KeyboardButton("Complex Numbers")
    markup.add(button_whole)
    markup.add(button_complex)
    bot.send_message(message.chat.id, "Select the calculator mode", reply_markup=markup)

@bot.message_handler(content_types=["text"])
def enter_numbers(message):
    if message.text == "Whole Numbers":
        bot.send_message(message.chat.id, "Enter two numbers separated by a space")
        log_activity(message, app_data)
        bot.register_next_step_handler(message, capture_user_whole_numbers)
    elif message.text == "Complex Numbers":
        bot.send_message(message.chat.id, "Enter two complex numbers separated by a space. Like 1+3j 2+4j")
        log_activity(message, app_data)
        bot.register_next_step_handler(message, capture_user_complex_numbers)

def capture_user_whole_numbers(message):
    log_activity(message, app_data)
    numbers = message.text
    app_data["num1"] = int(numbers.split()[0])
    app_data["num2"] = int(numbers.split()[1])
    catpure_operator_button_whole(message)

def capture_user_complex_numbers(message):
    log_activity(message, app_data)
    numbers = message.text
    app_data["num1"] = complex(numbers.split()[0])
    app_data["num2"] = complex(numbers.split()[1])
    capture_operator_button_complex(message)

def catpure_operator_button_whole(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton("+")
    but2 = types.KeyboardButton("-")
    but3 = types.KeyboardButton("*")
    but4 = types.KeyboardButton("/")
    but5 = types.KeyboardButton("%")
    but6 = types.KeyboardButton("//")
    markup.add(but1)
    markup.add(but2)
    markup.add(but3)
    markup.add(but4)
    markup.add(but5)
    markup.add(but6)
    bot.send_message(message.chat.id, "Select an operator", reply_markup=markup)
    bot.register_next_step_handler(message, perform_calculation)

def capture_operator_button_complex(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton("+")
    but2 = types.KeyboardButton("-")
    but3 = types.KeyboardButton("*")
    but4 = types.KeyboardButton("/")
    markup.add(but1)
    markup.add(but2)
    markup.add(but3)
    markup.add(but4)
    bot.send_message(message.chat.id, "Select an operator", reply_markup=markup)
    bot.register_next_step_handler(message, perform_calculation)

@bot.message_handler(content_types=["text"])
def perform_calculation(message):
    log_activity(message,app_data)
    result = 0
    if message.text == "+":
        result = app_data["num1"] + app_data["num2"]
        bot.send_message(message.chat.id, f'{app_data["num1"]} + {app_data["num2"]} = {result}')
    elif message.text == "-":
        result = app_data["num1"] - app_data["num2"]
        bot.send_message(message.chat.id, f'{app_data["num1"]} - {app_data["num2"]} = {result}')
    elif message.text == "*":
        result = app_data["num1"] * app_data["num2"]
        bot.send_message(message.chat.id, f'{app_data["num1"]} * {app_data["num2"]} = {result}')
    elif message.text == "/":
        result = app_data["num1"] / app_data["num2"]
        bot.send_message(message.chat.id, f'{app_data["num1"]} / {app_data["num2"]} = {result}')
    elif message.text == "%":
        result = app_data["num1"] % app_data["num2"]
        bot.send_message(message.chat.id, f'{app_data["num1"]} % {app_data["num2"]} = {result}')
    elif message.text == "//":
        result = app_data["num1"] // app_data["num2"]
        bot.send_message(message.chat.id, f'{app_data["num1"]} // {app_data["num2"]} = {result}')
    initiate_calc(message)

bot.infinity_polling()