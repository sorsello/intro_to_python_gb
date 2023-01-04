# Напишите программу,
# которая принимает на вход вещественное число
# и показывает сумму его цифр.
#
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

from common.console_helpers import capture_user_input_number_float
from homework_2.task_6.task_6_functions import calc_numbers_from_user_input_float, display_final_result

user_input: float = capture_user_input_number_float("Enter a number or a float: ")
result: int = calc_numbers_from_user_input_float(user_input)

display_final_result(user_input, result)