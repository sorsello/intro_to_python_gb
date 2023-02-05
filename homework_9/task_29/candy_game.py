# сделать бота для игры с конфетами между человеком и телеграмм ботом

import random
import telebot

from homework_9.task_29.bot_turn_service import bot_take_turn
from homework_9.task_29.controller import run_game
from homework_9.task_29.game_state_service import check_if_game_is_finished

token: str = "YOUR_TOKEN"

bot = telebot.TeleBot(token)

you: str = "'😀 игрок'"
smart_bot: str = "'🤖 бот'"
inital_num_of_sweets: int = 221

game_data = {"turn": 0,
             "current_user": "",
             "amount_of_sweets": 0,
             "bot_sweets": 0,
             "game_finished": False,
             "winner": ""}

@bot.message_handler(commands = ["start"])
def start(message):
    bot.send_message(message.chat.id, "----- Начать игру 'Конфеты' -----")
    bot.send_message(message.chat.id, f"На столе лежит {inital_num_of_sweets} конфет. " 
                                      f"Играют бот и игрок, делая ход друг после друга. "
                                      f"Первый ход определяется жеребьёвкой. "
                                      f"За один ход можно забрать не более чем 28 конфет. "
                                      f"Все конфеты оппонента достаются сделавшему последний ход. ")
    bot.send_message(message.chat.id, "/whoisfirst чтобы определить кто ходит первый - Вы или бот.")

@bot.message_handler(commands= ["whoisfirst"])
def button(message):
    rand_num = (random.randint(0, 1))
    if rand_num == 0:
        game_data["current_user"] = you
    else:
        game_data["current_user"] = smart_bot
    run_game(bot, inital_num_of_sweets, game_data, message, you, bot)

@bot.message_handler(content_types=["text"], )
def user_turn(message):
    if int(message.text) > game_data["amount_of_sweets"]:
        bot.send_message(message.chat.id, f"Нельзя взять больше конфет {message.text}, чем осталось {game_data['amount_of_sweets']}")
        bot.send_message(message.chat.id, f"Возьмите {game_data['amount_of_sweets']} и Вы выиграйте эту игру!")
    elif int(message.text) < 1 or int(message.text) > 28:
        bot.send_message(message.chat.id, f"Неверное кол-во конфет {message.text} - должно быть от 1 до 28")
    else:

        bot.send_message(message.chat.id,
                         f"{game_data['current_user']} забрал {message.text} конфет -> осталось конфет: {int(game_data['amount_of_sweets']) - int(message.text)}")
        game_data['amount_of_sweets'] = int(game_data['amount_of_sweets']) - int(message.text)
        game_data['current_user'] = smart_bot
        game_data['turn'] = int(game_data['turn']) + 1
        check_if_game_is_finished(bot, message, game_data, you, smart_bot)
        bot_take_turn(bot, message, game_data, you, smart_bot)

bot.infinity_polling()