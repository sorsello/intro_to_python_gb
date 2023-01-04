# Напишите программу,
# которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N.
#
# Пример:
#
# пусть N = 4,
# тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

from common.console_helpers import capture_user_input_number
from homework_2.task_7.task_7_functions import check_user_input_greater_than_zero, generate_list_of_factorials

user_input: int = capture_user_input_number("Enter a number: ")

check_user_input_greater_than_zero(user_input)

result: list[int] = generate_list_of_factorials(user_input)

print(f'N = {user_input} -> {result}')
