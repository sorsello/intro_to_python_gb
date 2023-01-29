# Задача 30:  Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
# Ввод: 7 2 5
# Вывод: 7 9 11 13 15

from common.console_helpers import capture_user_input_number

user_initial_num: int = capture_user_input_number("Set a starting number: ")
user_progression_step: int = capture_user_input_number("Set a progression step: ")
user_number_of_elems: int = capture_user_input_number("Set a number of elements: ")

final_list: list[int] = []

for x in range(user_number_of_elems):
    calc_formula = lambda iteration: user_initial_num + (iteration * user_progression_step)
    final_list.append(calc_formula(x))

print(final_list)