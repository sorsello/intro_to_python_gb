# сделать бота для игры с конфетами между человеком и телеграмм ботом

import random
import telebot

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

def init_game():
    game_data["amount_of_sweets"] = inital_num_of_sweets
    game_data["bot_sweets"] = 0
    game_data["bot_sweets"] = 0
    game_data["game_finished"] = False
    game_data["winner"] = ""

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
    init_game()
    game_data['turn'] = 1
    take_turn(message)

def display_current_number_of_sweets(message):
    bot.send_message(message.chat.id, f"Количество конфет - {game_data['amount_of_sweets']}")

def switch_users():
    if game_data['current_user'] == you:
        game_data['current_user'] = smart_bot
    else:
        game_data['current_user'] = you

def take_turn(message):
    if game_data["game_finished"] == True:
        return
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
        check_if_game_is_finished(message)
        take_turn(message)

def bot_determine_num_of_sweets_to_take() -> int:
    if game_data["amount_of_sweets"] <= 28:
        bot_take_sweets = game_data["amount_of_sweets"]
    else:
        bot_take_sweets = (random.randint(1, 28))
    return bot_take_sweets


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
        check_if_game_is_finished(message)
        take_turn(message)

def check_if_game_is_finished(message):
    if game_data["amount_of_sweets"] == 0:
        game_data["game_finished"] = True
        #need to switch users as they are switched before take turn
        switch_users()
        game_data["winner"] = game_data["current_user"]
        bot.send_message(message.chat.id, f"{game_data['current_user']} выйграл! Игра завершена.")
        bot.send_message(message.chat.id, f"#####\nЧтобы начать игру заново, отправьте /start\n#####")

bot.infinity_polling()