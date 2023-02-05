import random

import telebot
from telebot import types

bot = telebot.TeleBot("6146443023:AAFU7aiE8iwTpdHWqrb-AGoLU7g1hnRA6WQ")

you: str = "игрок"
smart_bot: str = "бот"

game_data = {"turn": 0, "current_user": "", "amount_of_sweets": "", "bot_sweets": 0}


def init_game():
    game_data["amount_of_sweets"] = 60
    game_data["bot_sweets"] = 0
    game_data["bot_sweets"] = 0

@bot.message_handler(commands = ["start"])
def start(message):
    bot.send_message(message.chat.id, "Начать игру 'Конфеты'")
    bot.send_message(message.chat.id, "/whoisfirst чтобы определить кто ходит первый - Вы или бот.")

@bot.message_handler(commands= ["whoisfirst"])
def button(message):
    rand_num = (random.randint(0, 1))
    if rand_num == 0:
        current_user = you
    else:
        current_user = smart_bot
    init_game()
    game_data['turn'] = 1
    take_turn(message)

def display_current_number_of_sweets(message):
    bot.send_message(message.chat.id, f"Количество конфет - {game_data['amount_of_sweets']}")

def take_turn(message):
    bot.send_message(message.chat.id, f"-----\nХод {game_data['turn']} - {game_data['current_user']}")
    display_current_number_of_sweets(message)
    if game_data['current_user'] == you:
        bot.send_message(message.chat.id, f"{game_data['current_user']} - Сколько конфет забрать? (1-28)")

    else:
        bot_turn_sweets = bot_determine_num_of_sweets_to_take()
        game_data["bot_sweets"] = bot_turn_sweets
        bot.send_message(message.chat.id,
     f"{game_data['current_user']} забрал {bot_turn_sweets} конфет -> осталось конфет: {int(game_data['amount_of_sweets']) - int(game_data['bot_sweets'])}")
        game_data['amount_of_sweets'] = int(game_data['amount_of_sweets']) - int(game_data['bot_sweets'])
        game_data['current_user'] = you
        game_data['turn'] = int(game_data['turn']) + 1
        take_turn(message)

def bot_determine_num_of_sweets_to_take() -> int:
    bot_take_sweets = (random.randint(1, 28))
    return bot_take_sweets


@bot.message_handler(content_types=["text"], )
def button(message):
    if int(message.text) < 1 or int(message.text) > 28:
        bot.send_message(message.chat.id, f"Неверное кол-во конфет {message.text} - должно быть больше 0 и меньше 29")
        bot.send_message(message.chat.id, f"/taketurn")
    else:

        bot.send_message(message.chat.id,
                         f"{game_data['current_user']} забрал {message.text} конфет -> осталось конфет: {int(game_data['amount_of_sweets']) - int(message.text)}")
        game_data['amount_of_sweets'] = int(game_data['amount_of_sweets']) - int(message.text)
        game_data['current_user'] = smart_bot
        game_data["bot_sweets"] = int(game_data["bot_sweets"]) + 1
        take_turn(message)



bot.infinity_polling()