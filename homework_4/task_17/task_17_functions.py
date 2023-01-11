import math

def prime_factor_numbers(user_input) -> list[int]:
    list_of_prime_factor: list[int] = []

    while user_input % 2 == 0:
        list_of_prime_factor.append(2)
        user_input = user_input / 2

    for i in range(3, int(math.sqrt(user_input)) + 1, 2):
        while (user_input % i == 0):
            list_of_prime_factor.append(i)
            user_input = user_input / i

    if user_input > 2:
        list_of_prime_factor.append(user_input)

    return list_of_prime_factor