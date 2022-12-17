# Task 4
# Напишите программу,
# которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).
from common.console_helpers import capture_user_input_number
from homework_1.task_4.task_4_functions import *

dimension: int = capture_user_input_number("Enter dimension (from 1 to 4): ")
check_user_input_dimension_allowed(dimension)
possible_ranges: tuple[str,str] = determine_x_and_y_ranges_by_dimension(dimension)
display_final_result(dimension, possible_ranges)