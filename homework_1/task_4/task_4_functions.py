from common.console_helpers import exit_program_with_error_message


def check_user_input_dimension_allowed(user_dimension: int):
    if (user_dimension > 0 and user_dimension <= 4):
        pass
    else:
        exit_program_with_error_message(f"Dimension must be greater than 0 and less than or equal to 4. Your input is {user_dimension}")

def determine_x_and_y_ranges_by_dimension(user_dimension:int) -> tuple[str,str]:
    possible_ranges: tuple[str,str]
    if (user_dimension == 1):
        possible_ranges = ("0 to ∞", "0 to ∞")
    elif (user_dimension == 2):
        possible_ranges = ("0 to -∞", "0 to ∞")
    elif (user_dimension == 3):
        possible_ranges = ("0 to -∞", "0 to -∞")
    elif (user_dimension == 4):
        possible_ranges = ("0 to -∞", "0 to ∞")
    return possible_ranges

def display_final_result(user_dimension: int, possible_ranges: tuple[str, str]):
    print(f"For dimension {user_dimension} the ranges are as follows: X from {possible_ranges[0]} ; Y from {possible_ranges[1]})")
