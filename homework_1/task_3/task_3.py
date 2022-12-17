# Напишите программу,
# которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0
# и выдаёт номер четверти плоскости,
# в которой находится эта точка (или на какой оси она находится).
#
# Пример:
#
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3
from common.console_helpers import capture_user_input_number
from homework_1.task_3.task_3_functions import *

x: int = capture_user_input_number("Enter coordinate X: ")
y: int = capture_user_input_number("Enter coordinate Y: ")

check_x_and_y_are_not_zero(x, y)

dimension_result: int = determine_coordinates_dimension(x, y)

display_final_result(x, y, dimension_result)