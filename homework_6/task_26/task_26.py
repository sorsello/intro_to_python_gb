# Задача 32:  Напишите программу,
# которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

from common.console_helpers import capture_user_input_number
from homework_6.task_26.task_26_functions import to_the_power_of

user_input_number: int = capture_user_input_number("Set a number: ")
user_input_power_of: int = capture_user_input_number("Set to the power of number: ")

result: int = to_the_power_of(3,5)
print(result)