def extract_decimal_parts_from_list_of_floats(user_list: list[float]) -> list[float]:
    new_list: list[float] = []
    for i in range(len(user_list)):
        decimal_part: float = round((user_list[i] / 1 - user_list[i] // 1), 2)
        if decimal_part == 0.0:
            continue
        else:
            new_list.append(decimal_part)
    return new_list

def determine_difference_between_max_and_min_decimal_parts(list_decimals: list[float]) -> None:
    min_decimal: float = min(list_decimals)
    print(f"Min value = {min_decimal}")
    max_decimal: float = max(list_decimals)
    print(f"Max value = {max_decimal}")
    final_result: float = max_decimal - min_decimal
    print(f"Max - Min value = {final_result}")