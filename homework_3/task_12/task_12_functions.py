def calculate_mult_of_mirror_elements_in_list(user_list: list[int]) -> list[int]:
    list_of_sums: list[int] = []

    if (len(user_list) % 2 == 0):
        for i in range(len(user_list) // 2):
            j = -(i) - 1
            list_of_sums.append(user_list[i] * user_list[j])
        return list_of_sums

    if (len(user_list) % 2 == 1):
        last_index: int = user_list.index(user_list[-1])
        middle_index: int = last_index // 2

        for i in range(middle_index + 1):
            if i != middle_index:
                j = -(i) - 1
                list_of_sums.append(user_list[i] * user_list[j])
            else:
                list_of_sums.append(user_list[middle_index] * user_list[middle_index])
        return list_of_sums