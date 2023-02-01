from common.console_helpers import capture_user_input_number

def create_new_entry(user_file_name: str) -> str:
    system_generated_id: int = capture_user_input_number("Please enter an id (if '0' is entered, the id will be incremented automatically based on the last entry): ")
    if system_generated_id == 0:
        system_generated_id = (generate_id(user_file_name))
    user_entry_name: str = input("Please enter a name: ")
    user_entry_last_name: str = input("Please enter a last name: ")
    user_entry_phone_number: str = input("Please enter a phone number: ")
    user_entry_comment: str = input("Please enter a comment: ")
    combined_entry: str = f"{system_generated_id},{user_entry_name},{user_entry_last_name},{user_entry_phone_number},{user_entry_comment}"
    return combined_entry
def generate_id(file_name: str) -> int:
    try:
        file = open(file_name, "r", encoding="utf8")
        last_id:int = get_the_last_entry_id(file)
        return last_id + 1
    except FileNotFoundError:
        return 1

def get_the_last_entry_id(user_file) -> int:
    file_lines: list[str] = user_file.readlines()
    last_entry: str = file_lines[-1]
    last_entry_id = last_entry.split(",")[0]
    return int(last_entry_id)

