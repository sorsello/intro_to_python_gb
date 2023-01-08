# Задайте список из вещественных чисел.
# Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
#
# Пример:
#
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

from common.console_helpers import capture_user_input_list_of_float
from homework_3.task_13.task_13_functions import extract_decimal_parts_from_list_of_floats, \
    determine_difference_between_max_and_min_decimal_parts

your_list: list[float] = capture_user_input_list_of_float()
list_with_decimal_parts: list[float] = extract_decimal_parts_from_list_of_floats(your_list)
print(f"List with decimal parts only -> {list_with_decimal_parts}")
determine_difference_between_max_and_min_decimal_parts(list_with_decimal_parts)