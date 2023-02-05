import random
from homework_9.task_29.game_state_service import display_current_number_of_sweets, check_if_game_is_finished

def bot_take_turn(bot, message, game_data_dict, you_const, bot_const):
    if game_data_dict["game_finished"] == True:
        return
    bot.send_message(message.chat.id, f"-----\nХод {game_data_dict['turn']} - {game_data_dict['current_user']}")
    display_current_number_of_sweets(bot, message, game_data_dict)
    if game_data_dict['current_user'] == you_const:
        bot.send_message(message.chat.id, f"{game_data_dict['current_user']} - Сколько конфет забрать? (1-28)")
    else:
        bot_turn_sweets = bot_determine_num_of_sweets_to_take(game_data_dict)
        game_data_dict["bot_sweets"] = bot_turn_sweets
        bot.send_message(message.chat.id,
     f"{game_data_dict['current_user']} забрал {bot_turn_sweets} конфет -> осталось конфет: {int(game_data_dict['amount_of_sweets']) - int(game_data_dict['bot_sweets'])}")
        game_data_dict['amount_of_sweets'] = int(game_data_dict['amount_of_sweets']) - int(game_data_dict['bot_sweets'])
        game_data_dict['current_user'] = you_const
        game_data_dict['turn'] = int(game_data_dict['turn']) + 1
        check_if_game_is_finished(bot, message, game_data_dict, you_const, bot_const)
        bot_take_turn(bot, message, game_data_dict, you_const, bot_const)

def bot_determine_num_of_sweets_to_take(game_data_dict) -> int:
    if game_data_dict["amount_of_sweets"] <= 28:
        bot_take_sweets = game_data_dict["amount_of_sweets"]
    else:
        bot_take_sweets = (random.randint(1, 28))
    return bot_take_sweets