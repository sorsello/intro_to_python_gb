# Задача 31: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)
# Ввод:  [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# 5
# 15
# Вывод: [1, 9, 13, 14, 19]

user_min_number: int = 5
user_max_number: int = 15
user_list: list[int] = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
print(user_list)
enumerated_user_list = list(enumerate(user_list))
filtered_enumerated_result: list[int] = list(filter(lambda x: x[1] > user_min_number and x[1] < user_max_number, enumerated_user_list))
index_of_filtered_enumerated_result: list[int] = list(map(lambda x: x[0], filtered_enumerated_result))
print(index_of_filtered_enumerated_result)