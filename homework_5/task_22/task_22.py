# Создайте программу для игры в ""Крестики-нолики"".
# Игра реализуется в терминале, игроки ходят поочередно,
# необходимо вывести карту
# (как удобнее, можно например в виде списка, внутри которого будут 3 списка по 3 элемента,
# каждый из которого обозначает соответсвующие клетки от 1 до 9),
# сделать проверку не занята ли клетка, на которую мы хотим поставить крестик или нолик,
# и проверку на победу (стоят ли крестики или нолик в ряд по диагонали, вертикали, горизонтали)

from homework_5.task_22.task_22_functions import check_if_game_is_completed, display_current_board, turn_put_symbol, \
    alternate_player_turns

line_1: list[str] = ["-", "-", "-"]
line_2: list[str] = ["-", "-", "-"]
line_3: list[str] = ["-", "-", "-"]

dict_game_global_values = {"is_game_finished": False, "is_invalid_turn": False, "current_player": "Player 1" }

display_current_board(line_1, line_2, line_3)
check_if_game_is_completed(line_1, line_2, line_3, dict_game_global_values)

print(f"{dict_game_global_values['current_player']}'s turn now.")
while not dict_game_global_values["is_game_finished"]:
    dict_game_global_values["is_game_finished"] = turn_put_symbol(line_1, line_2, line_3, dict_game_global_values)
    if dict_game_global_values["is_invalid_turn"]:
        pass
    else:
        current_player = alternate_player_turns(dict_game_global_values)





