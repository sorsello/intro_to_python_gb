from common.console_helpers import capture_user_input_number


def display_available_options() -> None:
    print("The following actions are available:\n"
          "0 - Set another file name\n"
          "1 - Add a new entry\n"
          "2 - Display all available entries (full)\n"
          "3 - Display all available entries (first and last names)\n"
          "4 - Sort entries by ID\n"
          "5 - Sort entries by Name\n"
          "6 - Exit the program.")

def capture_user_action_number() -> int:
    action_number: int = capture_user_input_number("Please enter Action Number and press Enter: ")
    print_lines_logic_break()
    while action_number < 0 or action_number > 6:
        action_number: int = capture_user_input_number("Please enter Action Number (0 - 6) and press Enter: ")
        print_lines_logic_break()
    return action_number

def exit_program() -> None:
    print("'6' has been selected. The program will close now.")
    print_lines_logic_break()
    exit()

def print_lines_logic_break() -> None:
    print("----")