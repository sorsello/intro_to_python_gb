from homework_7.task_27.console_command_service import exit_program, print_lines_logic_break
from homework_7.task_27.export_service import display_data_from_file, display_only_first_and_last_name_from_file
from homework_7.task_27.file_service import append_new_entry_to_file, sort_entries_by_id, sort_entries_by_name, \
    create_file_if_does_not_exist
from homework_7.task_27.import_service import create_new_entry

def enter_file_name() -> str:
    user_file_name: str = input("Please enter a file name to work with: ")
    create_file_if_does_not_exist(user_file_name)
    print(f"Working with {user_file_name}")
    print_lines_logic_break()
    return user_file_name

def run_the_application(action_number:int, file_name: str) -> None:
    if action_number == 1:
        user_entry: str = create_new_entry(file_name)
        append_new_entry_to_file(file_name, user_entry)
    elif action_number == 2:
        display_data_from_file(file_name)
    elif action_number == 3:
        display_only_first_and_last_name_from_file(file_name)
    elif action_number == 4:
        sort_entries_by_id(file_name)
    elif action_number == 5:
        sort_entries_by_name(file_name)
    elif action_number == 6:
        exit_program()

