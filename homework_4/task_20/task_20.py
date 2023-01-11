# Даны два файла,
# в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

from homework_4.task_19.task_19_functions import generate_file_with_answer
from homework_4.task_20.task_20_functions import convert_equation_to_dict, combine_dicts, convert_dict_to_equation, \
    generate_equation_in_file_then_read_file, read_file_with_equation

user_equation_1: str = generate_equation_in_file_then_read_file("task_19_equation_1.txt")
user_equation_2: str = generate_equation_in_file_then_read_file("task_19_equation_2.txt")

result_dict1 = convert_equation_to_dict(user_equation_1)
result_dict2 = convert_equation_to_dict(user_equation_2)

combined_user_dicts: dict[str, int] = combine_dicts(result_dict1, result_dict2)

final_result: str = convert_dict_to_equation(combined_user_dicts)
print(f"final result -> {final_result}")

generate_file_with_answer(final_result, "task_20_final_answer.txt")
read_file_with_equation("task_20_final_answer.txt")