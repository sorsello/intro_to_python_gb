# Задайте список из N элементов,
# заполненных числами из промежутка [-N, N].
#
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

from common.console_helpers import capture_user_input_number
from homework_2.task_9.task_9_functions import find_values_from_index_in_file, calculate_multiplication_of_list_elements

user_input: int = capture_user_input_number("Enter a number: ")
generated_list: list[int] = list(range(-user_input, user_input))
print(generated_list)
list_of_values_from_indexes: list[int] = find_values_from_index_in_file(generated_list)
multiplication_result: int = calculate_multiplication_of_list_elements(list_of_values_from_indexes)
print(f"Multiplication result of values in indexes = {multiplication_result}")