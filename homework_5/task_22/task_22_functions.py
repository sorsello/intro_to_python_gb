def display_current_board(list_1, list_2, list_3) -> None:
    print(f"|{list_1[0]} {list_1[1]} {list_1[2]}|")
    print(f"|{list_2[0]} {list_2[1]} {list_2[2]}|")
    print(f"|{list_3[0]} {list_3[1]} {list_3[2]}|")

def check_if_game_is_completed(list_1, list_2, list_3, global_dict) -> bool:

    global_dict["is_game_finished"] = False

    if list_1[0] == list_1[1] == list_1[2] == "X":
        global_dict["is_game_finished"] = True
    elif list_2[0] == list_2[1] == list_2[2] == "X":
        global_dict["is_game_finished"] = True
    elif list_3[0] == list_3[1] == list_3[2] == "X":
        global_dict["is_game_finished"] = True
    elif list_1[0] == list_2[0] == list_3[0] == "X":
        global_dict["is_game_finished"] = True
    elif list_1[1] == list_2[1] == list_3[1] == "X":
        global_dict["is_game_finished"] = True
    elif list_1[2] == list_2[2] == list_3[2] == "X":
        global_dict["is_game_finished"] = True
    elif list_1[0] == list_2[1] == list_3[2] == "X":
        global_dict["is_game_finished"] = True
    elif list_1[2] == list_2[1] == list_3[0] == "X":
        global_dict["is_game_finished"] = True

    if list_1[0] == list_1[1] == list_1[2] == "O":
        global_dict["is_game_finished"] = True
    elif list_2[0] == list_2[1] == list_2[2] == "O":
        global_dict["is_game_finished"] = True
    elif list_3[0] == list_3[1] == list_3[2] == "O":
        global_dict["is_game_finished"] = True
    elif list_1[0] == list_2[0] == list_3[0] == "O":
        global_dict["is_game_finished"] = True
    elif list_1[1] == list_2[1] == list_3[1] == "O":
        global_dict["is_game_finished"] = True
    elif list_1[2] == list_2[2] == list_3[2] == "O":
        global_dict["is_game_finished"] = True
    elif list_1[0] == list_2[1] == list_3[2] == "O":
        global_dict["is_game_finished"] = True
    elif list_1[2] == list_2[1] == list_3[0] == "O":
        global_dict["is_game_finished"] = True

    if global_dict["is_game_finished"] == False and "-" not in list_1 and "-" not in list_2 and "-" not in list_3:
        print("It's a draw. Nobody won.")
        global_dict["is_game_finished"] = True
        return global_dict["is_game_finished"]
    elif global_dict["is_game_finished"]:
        print(f"Game Completed - {global_dict['current_player']} won!")
        global_dict["is_game_finished"] = True
        return global_dict["is_game_finished"]
    else:
        return global_dict["is_game_finished"]

def turn_put_symbol(list_1, list_2, list_3, global_dict) -> bool:

    if global_dict["current_player"] == "Player 1":
        symbol_mark: str = "X"
    else:
        symbol_mark: str = "O"
    user_line: int = int(input(f"Select the line (1,2,3) to put {symbol_mark}: "))
    user_column: int = int(input(f"Select the column (1,2,3) to put {symbol_mark}: "))

    if (user_line > 3 or user_line < 1):
        global_dict["is_invalid_turn"] = True
        print(f"Allowed Values for line are 1,2,3. You have entered line - {user_line}")
        return False
    elif (user_column > 3 or user_column < 1):
        global_dict["is_invalid_turn"] = True
        print(f"Allowed Values for column are 1,2,3. You have entered column - {user_column}")
        return False
    else:
        if user_line == 1:
            if list_1[user_column - 1] == "-":
                list_1[user_column - 1] = symbol_mark
                global_dict["is_invalid_turn"] = False
            else:
                global_dict["is_invalid_turn"] = True
                print(f"You cannot put {symbol_mark} here. It already has the value - {list_1[user_column - 1]}")
        elif user_line == 2:
            if list_2[user_column - 1] == "-":
                list_2[user_column - 1] = symbol_mark
                global_dict["is_invalid_turn"] = False
            else:
                global_dict["is_invalid_turn"] = True
                print(f"You cannot put {symbol_mark} here. It already has the value - {list_2[user_column - 1]}")
        elif user_line == 3:
            if list_3[user_column - 1] == "-":
                list_3[user_column - 1] = symbol_mark
                global_dict["is_invalid_turn"] = False
            else:
                global_dict["is_invalid_turn"] = True
                print(f"You cannot put {symbol_mark} here. It already has the value - {list_2[user_column - 1]}")

        display_current_board(list_1, list_2, list_3)
        return check_if_game_is_completed(list_1, list_2, list_3, global_dict)

def alternate_player_turns(global_dict) -> str:
    if global_dict["is_game_finished"]:
        pass
    else:
        if global_dict["current_player"] == "Player 1":
            global_dict["current_player"] = "Player 2"
            print("---")
            print(f"{global_dict['current_player']}'s turn now.")
            return global_dict["current_player"]
        else:
            global_dict["current_player"] = "Player 1"
            print("---")
            print(f"{global_dict['current_player']}'s turn now.")
            return global_dict["current_player"]
