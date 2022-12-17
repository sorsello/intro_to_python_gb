# Напишите программу,
# которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.
#
# Пример:
#
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21
import math

from common.console_helpers import capture_user_input_number
from homework_1.task_5.task_5_functions import *

a_x: int = capture_user_input_number("For A enter coordinate X: ")
a_y: int = capture_user_input_number("For A enter coordinate Y: ")
b_x: int = capture_user_input_number("For B enter coordinate X: ")
b_y: int = capture_user_input_number("For B enter coordinate Y: ")

user_coordinates: tuple[int,int,int,int] = (a_x, a_y, b_x, b_y)
result: float = calc_distance_between_coord(user_coordinates)

display_final_result(user_coordinates, result)