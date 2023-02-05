def init_game(initial_num: int, game_data_dict):
    game_data_dict["amount_of_sweets"] = initial_num
    game_data_dict["bot_sweets"] = 0
    game_data_dict["bot_sweets"] = 0
    game_data_dict["game_finished"] = False
    game_data_dict["winner"] = ""

def display_current_number_of_sweets(bot, message, game_data_dict):
    bot.send_message(message.chat.id, f"Количество конфет - {game_data_dict['amount_of_sweets']}")

def check_if_game_is_finished(bot, message, game_data_dict, you_const, bot_const):
    if game_data_dict["amount_of_sweets"] == 0:
        game_data_dict["game_finished"] = True
        #need to switch users as they are switched before take turn
        switch_users(game_data_dict, you_const, bot_const)
        game_data_dict["winner"] = game_data_dict["current_user"]
        bot.send_message(message.chat.id, f"{game_data_dict['current_user']} выйграл! Игра завершена.")
        bot.send_message(message.chat.id, f"#####\nЧтобы начать игру заново, отправьте /start\n#####")

def switch_users(game_data_dict, you_const, bot_const):
    if game_data_dict['current_user'] == you_const:
        game_data_dict['current_user'] = bot_const
    else:
        game_data_dict['current_user'] = you_const