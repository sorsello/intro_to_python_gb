from homework_7.task_27.console_command_service import print_lines_logic_break

def display_data_from_file(file_name: str) -> None:
    file = open(file_name, "r", encoding="utf8")
    file_lines: list[str] = file.readlines()
    if len(file_lines) > 0:
        for x in file_lines:
            replaced_string: str = x.replace(",", " | ")
            print(replaced_string, end="")
        print_lines_logic_break()
    else:
        print(f"{file_name} is empty. Nothing to display.")
        print_lines_logic_break()

def display_only_first_and_last_name_from_file(file_name: str) -> None:
    file = open(file_name, "r", encoding="utf8")
    file_lines: list[str] = file.readlines()
    if len(file_lines) > 0:
        for x in file_lines:
            split_line: list[str] = x.split(",")
            first_last_name: str = f"{split_line[1]} {split_line[2]}"
            print(first_last_name)
        print_lines_logic_break()
    else:
        print(f"{file_name} is empty. Nothing to display.")
        print_lines_logic_break()