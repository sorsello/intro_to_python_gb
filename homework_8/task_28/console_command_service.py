from common.console_helpers import capture_user_input_number


def display_available_options() -> None:
    print("The following actions are available:\n"
          "1 - Add a new student\n"
          "2 - Add a subject to all students\n"
          "3 - Add a subject grade to a student\n"
          "4 - Show all students (First Last names)\n"
          "5 - Show all grades for a student\n"
          "6 - Exit the program.")

def capture_user_action_number() -> int:
    action_number: int = capture_user_input_number("Please enter Action Number and press Enter: ")
    while action_number < 1 or action_number > 6:
        action_number: int = capture_user_input_number("Please enter Action Number (1 - 6) and press Enter: ")
        print_lines_logic_break()
    return action_number

def exit_program() -> None:
    print("'6' has been selected. The program will close now.")
    print_lines_logic_break()
    exit()

def print_lines_logic_break() -> None:
    print("----")