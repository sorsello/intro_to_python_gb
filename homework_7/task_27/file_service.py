from homework_7.task_27.console_command_service import print_lines_logic_break

def create_file_if_does_not_exist(file_name: str) -> None:
    try:
        file = open(file_name, "r", encoding="utf8")
        file.close()
    except FileNotFoundError:
        file = open(file_name, "a", encoding="utf8")
        file.close()
def append_new_entry_to_file(file_name: str, user_entry: str) -> None:
    file = open(file_name, "a", encoding="utf8")
    file.write(f"{user_entry}\n")
    file.close()
    print(f"'{user_entry}' has been added.")
    print_lines_logic_break()

def sort_entries_by_value(file_name: str, lambda_expression) -> None:
    file = open(file_name, "r", encoding="utf8")
    file_lines: list[str] = file.readlines()
    file.close()
    if len(file_lines) > 0:
        list_of_lists: list[list[str]] = []
        for x in file_lines:
            split_line: list[str] = x.split(",")
            list_of_lists.append(split_line)
        sorted_by_value: list[list[str]] = sorted(list_of_lists, key=lambda_expression)
        stringified_list: list[str] = []
        for item in sorted_by_value:
            string_from_list: str = ",".join(item)
            stringified_list.append(string_from_list)
        file = open(file_name, 'w', encoding="utf8")
        for item in stringified_list:
            file.write(item)
        file.close()
        print(f"Values in {file_name} has been sorted.")
        print_lines_logic_break()
    else:
        print(f"{file_name} is empty. Cannot sort anything.")
        print_lines_logic_break()

def sort_entries_by_id(file_name) -> None:
    sort_entries_by_value(file_name, lambda x: int(x[0]))

def sort_entries_by_name(file_name) -> None:
    sort_entries_by_value(file_name, lambda x: x[1])