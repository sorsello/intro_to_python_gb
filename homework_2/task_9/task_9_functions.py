def find_values_from_index_in_file(user_list: list[int]) -> list[int]:
    list_of_values_to_multiply: list[int] = []
    list_of_indexes_from_file: list[int] = []
    with open("file.txt") as read_file:
        lines = read_file.readlines()
        for index_from_line in lines:
            list_of_indexes_from_file.append(int(index_from_line))
            list_of_values_to_multiply.append(user_list[int(index_from_line)])
    print(f"Indexes from file.txt -> {list_of_indexes_from_file}")
    print(f"Values in indexes to multiply -> {list_of_values_to_multiply}")
    return list_of_values_to_multiply

def calculate_multiplication_of_list_elements(list_numbers: int) -> int:
    result_mult: int = 1
    for i in list_numbers:
        result_mult = result_mult * i
    return result_mult