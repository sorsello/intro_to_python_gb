def determine_elements_in_odd_indexes_and_sum_them(user_list: list[int]) -> None:
    list_with_values_from_odd_indexes: list[0] = []
    final_result: int = 0

    for i in range(len(user_list)):
        if (i % 2 == 1):
            list_with_values_from_odd_indexes.append(user_list[i])
            final_result += user_list[i]

    print(f"Elements from odd indexes -> {list_with_values_from_odd_indexes}")
    print(f"Sum -> {final_result}")