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