import random

def generate_list_of_random_numbers(user_input: int) -> list[int]:
    list_of_random_numbers: list[int] = []

    for i in range(user_input + 1):
        random_number:int = random.randint(0, 100)
        if random_number == 0:
            print("Randomly generated number was 0. The program will exit now.")
            exit()
        list_of_random_numbers.append(random.randint(0, 100))

    return list_of_random_numbers

def generate_math_stuff_with_pow(list_of_random_numbers: list[int]) -> str:

    final_result: str = ""

    for i in range(len(list_of_random_numbers)):
        # need decrease_i to be dynamic
        decrease_i = len(list_of_random_numbers) - i - 1
        x_value: str
        if decrease_i == 0:
            x_value = ""
            decrease_i = ""
        elif decrease_i == 1:
            x_value = "*x"
        else:
            x_value = "*x**"
        final_result = final_result + f"{list_of_random_numbers[i]}{x_value}{decrease_i} + "

    final_result_stripped: str = final_result.strip(" ").strip("+").rstrip(" ")
    final_result_stripped += " = 0"
    return final_result_stripped

def generate_file_with_answer(answer: str) -> None:
    file_name: str = "task_19_answer.txt"
    file = open(file_name, "w")
    file.write(answer)
    print(f"File {file_name} has been created.")