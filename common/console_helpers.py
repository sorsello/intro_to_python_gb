def exit_program_with_error_message(error_message: str):
    print(error_message)
    print("The program will exit now.")
    exit()

def capture_user_input_number(user_input_msg: str) -> int:
    user_input = input(user_input_msg)
    try:
        user_input_int: int = int(user_input)
        return user_input_int
    except ValueError:
        exit_program_with_error_message("The input must be a number.")

def capture_user_input_number_float(user_input_msg: str) -> float:
    user_input = input(user_input_msg)
    try:
        user_input_int: float = float(user_input)
        return user_input_int
    except ValueError:
        exit_program_with_error_message("The input must be a number or a float.")

def capture_user_input_list_of_int() -> list[int]:
    try:
        user_list: list[int] = []
        list_length: int = int(input("Set how many elements your list will have: "))
        for i in range(list_length):
            user_element: int = int(input(f"Please set int value for the {i} element in the list: "))
            user_list.append(user_element)

        print(f"Your list is -> {user_list}")
        return user_list
    except ValueError:
        exit_program_with_error_message("The input must be a number.")