# Реализуйте алгоритм перемешивания списка.

from copy import deepcopy
from random import randint

original_list_of_nums = [6, 5, 4, 3, 2, 1, 0]
def shuffle_list_fisher_yates(user_list):
  temp_list = deepcopy(user_list)
  m = len(temp_list)
  while (m):
    m = m - 1
    i = randint(0, m)
    temp_list[m], temp_list[i] = temp_list[i], temp_list[m]
  return temp_list

print(f"Original list -> {original_list_of_nums}")
print(f"Shuffled list -> {shuffle_list_fisher_yates(original_list_of_nums)}")