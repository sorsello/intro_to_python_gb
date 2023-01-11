# Задайте последовательность чисел.
# Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности.

from common.console_helpers import capture_user_input_list_of_int

user_list: list[int] = capture_user_input_list_of_int()

final_list: list[int] = []

for elem in user_list:
    if(final_list.count(elem) > 0):
        continue
    else:
        final_list.append(elem)

print(f"List with unique elements and original order -> {final_list}")