# Задайте число.
# Составьте список чисел Фибоначчи,
# в том числе для отрицательных индексов.
#
# Пример:
#
# - для k = 8 список будет выглядеть так:
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

from common.console_helpers import capture_user_input_number
from homework_3.task_15.task_15_functions import generate_positive_fibonacci_list, generate_negative_fibonacci_list

user_input: int = capture_user_input_number("Please enter N for Fibonacci sequence: ")
final_list: list[int]
pos_fibonacci_list: list[int] = generate_positive_fibonacci_list(user_input)
neg_fibonacci_list: list[int] = generate_negative_fibonacci_list(user_input)

print(f"Positive Fibonacci sequence -> {pos_fibonacci_list}")
print(f"Negative Fibonacci sequence -> {neg_fibonacci_list}")
pos_fibonacci_list.remove(0)
final_list: list[int] = neg_fibonacci_list + pos_fibonacci_list
print(f"Final result -> {final_list}")