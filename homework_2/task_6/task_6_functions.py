def calc_numbers_from_user_input_float(user_input_float: float) -> int:
    final_result: int = 0

    for item_number in str(user_input_float):
        if item_number == ".":
            continue
        final_result = final_result + int(item_number)

    return final_result

def display_final_result(user_input_float:float, final_result: int):
    print(f'{user_input_float} -> {final_result}')
