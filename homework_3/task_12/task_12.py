# Напишите программу,
# которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#
# Пример:
#
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

from common.console_helpers import capture_user_input_list_of_int
from homework_3.task_12.task_12_functions import calculate_mult_of_mirror_elements_in_list

your_list: list[int] = capture_user_input_list_of_int()
final_list: list[int] = calculate_mult_of_mirror_elements_in_list(your_list)
print(f"=> {final_list}")
