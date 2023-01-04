import math

def generate_list_in_line_with_formula(user_input_number: int) -> list[int]:
    result_list: list[int] = []
    for i in range(1, user_input_number + 1):
        temp_result: int = round(math.pow((1 + 1 / i), i), 2)
        result_list.append(temp_result)
    return result_list

def calculate_sum_of_list_elements(list_numbers: int) -> int:
    result_sum: int = 0
    for i in list_numbers:
        result_sum = result_sum + i
    return result_sum

def display_combined_results(user_input_number: int, result_list: list[int]) -> None:
    result_string: str = "{"
    for i in range(1, user_input_number + 1):
        result_string = f"{result_string} {i}: {result_list[i - 1]},"
    result_string = result_string.rstrip(",")
    result_string = result_string + " }"
    print(result_string)