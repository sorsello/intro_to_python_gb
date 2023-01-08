# Задайте список из нескольких чисел.
# Напишите программу,
# которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.
#
# Пример:
#
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from common.console_helpers import capture_user_input_list_of_int
from homework_3.task_11.task_11_functions import determine_elements_in_odd_indexes_and_sum_them

your_list: list[int] = capture_user_input_list_of_int()
determine_elements_in_odd_indexes_and_sum_them(your_list)