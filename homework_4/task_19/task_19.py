# Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена
# и записать в файл многочлен степени k.

from common.console_helpers import capture_user_input_number
from homework_4.task_19.task_19_functions import generate_list_of_random_numbers, generate_math_stuff_with_pow, \
    generate_file_with_answer

my_user_input: int = capture_user_input_number("Please enter a number that will be uses as a base for pow: ")

list_random_numbers: list[int] = generate_list_of_random_numbers(my_user_input)
final_equation = generate_math_stuff_with_pow(list_random_numbers)
print(final_equation)

generate_file_with_answer(final_equation)