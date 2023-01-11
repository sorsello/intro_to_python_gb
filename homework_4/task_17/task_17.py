# Задайте натуральное число N.
#
# Напишите программу, которая составит список простых множителей числа N.

from common.console_helpers import capture_user_input_number
from homework_4.task_17.task_17_functions import prime_factor_numbers

user_input: int = capture_user_input_number("Enter a number: ")
result_list_of_prime_factors = prime_factor_numbers(user_input)
print(result_list_of_prime_factors)