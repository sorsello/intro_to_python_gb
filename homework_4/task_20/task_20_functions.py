from collections import Counter
from operator import itemgetter

from common.console_helpers import capture_user_input_number
from homework_4.task_19.task_19_functions import generate_list_of_random_numbers, generate_math_stuff_with_pow, \
    generate_file_with_answer


def read_file_with_equation(file_name: str) -> str:
    file = open(file_name, "r")
    equation_in_file: str = file.readline()
    print(f"File {file_name} -> equation: {equation_in_file}")
    print("----")
    return equation_in_file

def convert_equation_to_dict(user_equation: str) -> dict[str:str]:
    dict_1: dict[str:int] = {}
    result: str = user_equation.removesuffix(" = 0")
    split_result: list[str] = result.split(" + ")
    list_of_split_results: list[list[str]] = []
    for i in range(len(split_result)):
        split_value_two_stars: list[str] = split_result[i].split("*x")
        list_of_split_results.append(split_value_two_stars)

    for i in range(len(list_of_split_results)):
        try:
            dict_1[list_of_split_results[i][1]] = int(list_of_split_results[i][0])
        except IndexError:
            dict_1["no-x"] = int(list_of_split_results[i][0])

    return dict_1

def combine_dicts(user_dict1: dict[str,int], user_dict2: dict[str, int]) -> dict[str, int]:
    combined_dicts: Counter = Counter(user_dict1) + Counter(user_dict2)
    return dict(combined_dicts)

def convert_dict_to_equation(user_dict: dict[str, int]) -> str:
    list_of_split_equation: list[list[str]] = []

    no_stars_dict: dict[str,int] = { k.replace('**', ''): v for k, v in user_dict.items() }
    value_one_x = no_stars_dict[""]
    no_stars_dict.pop("")
    value_no_x = no_stars_dict["no-x"]
    no_stars_dict.pop("no-x")

    for x in no_stars_dict.keys():
        list_of_split_equation.append([x, str(no_stars_dict[x])])

    sorted_list_of_split_equation = sorted(list_of_split_equation, key=itemgetter(0), reverse=True)
    for i in range(len(sorted_list_of_split_equation)):
        temp_value: str = sorted_list_of_split_equation[i][0]
        sorted_list_of_split_equation[i][0] = sorted_list_of_split_equation[i][1]
        sorted_list_of_split_equation[i][1] = "**" + temp_value

    sorted_list_of_split_equation.append([str(value_one_x), ""])
    sorted_list_of_split_equation.append([str(value_no_x), "no-x"])

    joined_equation_list: list[str] = []
    for i in range(len(sorted_list_of_split_equation)):
        joined_equation_item = "*x".join(sorted_list_of_split_equation[i])
        joined_equation_list.append(joined_equation_item)

    joined_with_x_equation: str = " + ".join(joined_equation_list)
    without_no_x_joined_equation: str = joined_with_x_equation.replace("*xno-x", "")
    final_joined_equation: str = without_no_x_joined_equation + " = 0"
    return final_joined_equation

def generate_equation_in_file_then_read_file(file_name: str) -> str:
    my_user_input: int = capture_user_input_number("Please enter a number that will be uses as a base for pow: ")

    list_random_numbers: list[int] = generate_list_of_random_numbers(my_user_input)
    final_equation = generate_math_stuff_with_pow(list_random_numbers)
    print(final_equation)

    generate_file_with_answer(final_equation, file_name)
    generated_equation_from_file: str = read_file_with_equation(file_name)
    return generated_equation_from_file