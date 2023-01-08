def generate_positive_fibonacci_list(number_of_seq: int) -> list[int]:
    n1 = 0
    n2 = 1
    count = -1
    result_fibonacci_list : list[int] = []
    while count < number_of_seq:
        result_fibonacci_list.append(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1
    return result_fibonacci_list

def generate_negative_fibonacci_list(number_of_seq: int) -> list[int]:
    n1 = 0
    n2 = 1
    count = -1
    result_fibonacci_list : list[int] = []
    while count < number_of_seq:
        if count % 2 == 1:
            result_fibonacci_list.append(-n1)
        else:
            result_fibonacci_list.append(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1
    result_fibonacci_list.reverse()
    return result_fibonacci_list