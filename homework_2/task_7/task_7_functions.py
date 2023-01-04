from common.console_helpers import exit_program_with_error_message


def check_user_input_greater_than_zero(user_input_number: int):
    if user_input_number >= 0:
        pass
    else:
        exit_program_with_error_message(f"The number must be greater than or equal to 0. Your number {user_input_number} is less than zero.")

def generate_list_of_factorials(user_input_number: int) -> list[int]:
    result_list: list[int] = []

    factorial_number: int = 1
    if user_input_number == 0:
        print("The factorial of 0 is 1")
        result_list.append(factorial_number)
    else:
        for x in range(1, user_input_number + 1):
            factorial_number = factorial_number * x
            result_list.append(factorial_number)

    return result_list