# Задайте список из n чисел последовательности
# $(1+\frac 1 n)^n$
# и выведите на экран их сумму.
#
# Пример:
#
# Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44}
import math

from common.console_helpers import capture_user_input_number
from homework_2.task_8.task_8_functions import generate_list_in_line_with_formula, calculate_sum_of_list_elements, \
    display_combined_results

user_input: int = capture_user_input_number("Enter a number: ")
resulting_list: list[int] = generate_list_in_line_with_formula(user_input)
resulting_sum: int = calculate_sum_of_list_elements(resulting_list)
display_combined_results(user_input, resulting_list)
print(f"Sum = {resulting_sum}")