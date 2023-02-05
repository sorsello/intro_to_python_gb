from homework_9.task_29.bot_turn_service import bot_take_turn
from homework_9.task_29.game_state_service import init_game


def run_game(bot, initial_num, game_data_dict, message, you_const, bot_const):
    init_game(initial_num, game_data_dict)
    game_data_dict['turn'] = 1
    bot_take_turn(bot, message, game_data_dict, you_const, bot_const)