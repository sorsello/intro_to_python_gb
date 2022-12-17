# Task 2
# Напишите программу для
# проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z
# для всех значений предикат.
from homework_1.task_2.task2_functions import *

x: int = 0
y: int = 0
z: int = 0

result_list: list[int] = [x, y, z]

iterations: int = 2 ** len(result_list)

for item in range(iterations):
    set_one_to_the_second_half_values(item, iterations, result_list)
    set_one_to_every_two_values(item, result_list)
    set_one_to_every_second_value(item, result_list)

    final_result:bool = determine_true_or_false(result_list)
    print(f"{result_list} -> ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z => {final_result}")
